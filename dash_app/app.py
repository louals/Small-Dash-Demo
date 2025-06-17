import dash
from dash import html, dcc
from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
import uvicorn

# ---------- Dash part ----------
dash_app = dash.Dash(
    __name__,
    requests_pathname_prefix="/dashboard/"   # must match mount path
)

dash_app.layout = html.Div([
    html.Div([
        html.A("Accueil", href="/"),
        " | ",
        html.A("Logout", href="/logout")
    ], style={"marginTop": 25}),

    html.H1("Exemple de Dashboard"),

    html.H2("*** Bar Graph ***"),
    dcc.Graph(
        id="exm1",
        figure={
            "data": [
                {"x": [5, 7, 12], "y": [10, 16, 11], "type": "bar", "name": "exmple1"},
                {"x": [8, 18, 22], "y": [5, 8, 3], "type": "bar", "name": "exmple2"},
            ]
        },
    ),

    html.H2("*** Line Graph ***"),
    dcc.Graph(
        id="exm2",
        figure={
            "data": [
                {"x": [1, 3, 5], "y": [10, 12, 14], "type": "line", "name": "exmple3"},
                {"x": [2, 4, 6], "y": [13, 15, 17], "type": "line", "name": "exmple4"},
            ]
        },
    ),

    html.H2("*** Scatter Plot Graph ***"),
    dcc.Graph(
        id="exm3",
        figure={
            "data": [
                {"x": [1, 3, 5, 7], "y": [10, 12, 14, 16],
                 "type": "scatter", "mode": "markers", "name": "scatter exmpl1"},
                {"x": [2, 4, 6, 8], "y": [13, 15, 17, 19],
                 "type": "scatter", "mode": "markers", "name": "scatter exmpl2"},
            ]
        },
    ),

    html.H2("*** Pie Chart Graph ***"),
    dcc.Graph(
        id="exm4",
        figure={
            "data": [
                {"labels": ["A", "B", "C"], "values": [10, 12, 14],
                 "type": "pie", "name": "pie chart expl1"},
            ],
            "layout": {"title": "pie chart example"},
        },
    ),
])

# ---------- FastAPI part ----------
api = FastAPI()

# Mount Dash under /dashboard
api.mount("/dashboard", WSGIMiddleware(dash_app.server))

@api.get("/")
async def root():
    return {"message": "Hello from FastAPI + Dash 🎉"}

# ---------- Run ----------
if __name__ == "__main__":
    uvicorn.run(api, host="0.0.0.0", port=8000, reload=True)
