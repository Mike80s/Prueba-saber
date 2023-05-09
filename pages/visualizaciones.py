

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
# dash-labs plugin call, menu name and route
register_page(__name__, path='/visualizaciones')

# specific layout for this page

layout = dbc.Container(
    [
        dbc.Row([
            html.H3(['Visualizaciones según las variables del modelo']),
            html.P('En la parte izquierda se muestra un gráfico de cajas entre un descriptor y el puntaje global obtenido.En la parte derecha se genera un diagrama circular respecto a la frecuencia obtenida.'),
        dbc.Row([

            dbc.Col([
                html.H4(['Puntaje Global']),


                 html.Div([

                    dcc.Dropdown(id='My_dropdown',
                                 options=[
                                     {'label': 'Tiene internet en casa', 'value': 'Tiene internet en casa'},

                                     {'label': 'Número de libros en casa', 'value':'Número de libros en casa'},

                                     {'label': 'Estrato socioeconómico', 'value': 'Estrato socioeconómico'},

                                     {'label': 'Tiempo de lectura diaria', 'value': 'Tiempo de lectura diaria'}
                                 ],
                                 value='Tiene internet en casa'
                                  )

                ]),


                       html.Div([
                       dcc.Graph(id='the_graph')
                       ])




            ]),
            dbc.Col([
                html.H4(['Frecuencia']),

                       html.Div([
                       dcc.Graph(id='the_graph2')
                       ])




            ],lg=6)



        ])
    ])
        ])




