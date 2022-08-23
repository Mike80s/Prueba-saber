import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page
import dash_core_components as dcc
import dash_html_components as html

# Data
import pandas as pd
import dash_labs as dl

# Visualisation
import seaborn as sns
import plotly.express as px
df = pd.read_csv("data.csv")
df14=df[['Departamento','Puntaje global']].groupby(['Departamento']).mean()
df14=df14.reset_index()
df14=df14.sort_values('Puntaje global')
fig = px.bar(df14, x='Departamento', y='Puntaje global')
# dash-labs plugin call, menu name and route
register_page(__name__, path='/departamentos')


layout = dbc.Container(
    [
        dbc.Row([
            dbc.Col([
                html.H3(['Puntaje global promedio por departamento']),
                html.Div([
                    dcc.Graph(id='life-exp-vs-gdp', figure=fig)
                ])
            ]),

            dbc.Row([
                html.H3(['Conflicto en Colombia']),
                       html.Div([
                       dcc.Graph(id='the_graph2')
                       ])




            ])



        ])
    ])
