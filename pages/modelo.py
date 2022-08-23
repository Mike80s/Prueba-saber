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

# dash-labs plugin call, menu name and route
register_page(__name__, path='/modelo')
layout = dbc.Container(
    [
        dbc.Row([
            dbc.Col([
                html.H3(['Modelo']),


                 html.Div([
                     html.Img(src='https://d20ohkaloyme4g.cloudfront.net/img/document_thumbnails/66f57d6438f24d6f2e85bd4ed542516e/thumb_1200_900.png')



                ]),

            ]),
            dbc.Col([
                html.H3(['Variables']),

                       html.Div([
                       html.P('Tiene internet'),
                       html.P('Estrato socioeconómico'),
                       html.P('Número de cuartos en el hogar'),
                       html.P('Jornada del colegio'),
                       html.P('Educación del Padre'),
                       html.P('Educación de la madre'),
                       html.P('Tiempo de lectura diaria'),
                       html.P('Número de libros en casa')
                       ])




            ], lg=6)



        ])
    ])
