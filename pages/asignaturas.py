



import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page
import dash_core_components as dcc
import dash_html_components as html

# Data
import pandas as pd
import dash_labs as dl
import plotly.graph_objects as go
# Visualisation
import seaborn as sns
import plotly.express as px
df = pd.read_csv("data.csv")
# dash-labs plugin call, menu name and route
register_page(__name__, path='/asignaturas')


# specific layout for this page


layout = dbc.Container(
    [
        dbc.Row([
            dbc.Col([
                html.H3(['Rendimiento por asignaturas']),
                html.Div([
html.Div([

                    dcc.Dropdown(id='My_dropdown13',

                                 options=[
                                     {'label': 'Internet en la familia', 'value': 'Tiene internet en casa'},

                                     {'label': 'Número de libros en casa', 'value': 'Número de libros en casa'},

                                     {'label': 'Estrato socio económico', 'value': 'Estrato socioeconómico'},

                                     {'label': 'Tiempo de lectura', 'value': 'Tiempo de lectura diaria'}
                                 ],
                                 value='Tiene internet en casa')

                ]),


                       html.Div([
                       dcc.Graph(id='the_graph13')
                       ])
                ])
        ], lg=12),

    ])
    ])