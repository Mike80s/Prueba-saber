#libraries
import dash
import dash_labs as dl
import dash_bootstrap_components as dbc
import warnings
warnings.filterwarnings("ignore")

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc




# Data
import pandas as pd

# Visualisation
#import seaborn as sns
import plotly.express as px
#from callbacks import register_callbacks
import plotly.graph_objects as go

request_path_prefix = None


df = pd.read_csv("data.csv")


# Dash instance declaration
app = dash.Dash(__name__, plugins=[dl.plugins.pages], requests_pathname_prefix=request_path_prefix, external_stylesheets=[dbc.themes.FLATLY],)
server=app.server



#Top menu, items get from all pages registered with plugin.pages
navbar = dbc.NavbarSimple([

    dbc.NavItem(dbc.NavLink( "Fabián Ramos Hernández mframosh@unal.edu.co", href=request_path_prefix)),
    dbc.DropdownMenu(
        [
          dbc.DropdownMenuItem(page["name"], href=request_path_prefix or page["path"])
            for page in dash.page_registry.values()
            if page["module"] != "pages.not_found_404"
        ],
        nav=True,
        label="Opciones",
    ),
    #dbc.NavItem(dbc.NavLink("Nosotros", href=request_path_prefix )),
    ],
    brand="Análisis de la prueba saber 11 año 2020",
    color="primary",
    dark=True,
    className="mb-3",
)

#Main layout
app.layout = dbc.Container(
    [
        navbar,
        dl.plugins.page_container,
    ],
    className="dbc",
    fluid=True,
)

# Call to external function to register all callbacks
#register_callbacks(app)
@app.callback(
    Output(component_id='the_graph', component_property= 'figure'),
    Input(component_id='My_dropdown', component_property='value')
)
def the_graph(My_dropdown):
        df14=df[[My_dropdown,'Puntaje global']].groupby([My_dropdown]).mean()
        df14=df14.reset_index()
        #figure = px.bar(df14, x=My_dropdown, y='PUNT_GLOBAL')
        #figure1 = px.histogram(df, x=My_dropdown)
        figure=px.box(df, x=My_dropdown, y='Puntaje global')
        return   figure

@app.callback(
    Output(component_id='the_graph2', component_property= 'figure'),
    Input(component_id='My_dropdown', component_property='value')
)
def the_graph(My_dropdown):
    df15 = df.groupby(df[My_dropdown]).size()
    df15 = df15.reset_index()
    figure = px.pie(df15, values=0, names=My_dropdown, width=400, height=400)
    return   figure

@app.callback(
    Output(component_id='the_graph13', component_property= 'figure'),
    Input(component_id='My_dropdown13', component_property='value')
)
def the_graph(My_dropdown13):
    df35 = df[[My_dropdown13, 'PUNT_INGLES', 'PUNT_LECTURA_CRITICA', 'PUNT_MATEMATICAS', 'PUNT_C_NATURALES',
               'PUNT_SOCIALES_CIUDADANAS']].groupby([My_dropdown13]).mean()
    df35 = df35.reset_index()
    #figure=px.bar(df35,x=My_dropdown13,y='PUNT_MATEMATICAS')
    fig = go.Figure()
    fig.add_trace(go.Bar(x=df35[My_dropdown13],
                         y=df35['PUNT_INGLES'],
                         name='Inglés',
                         marker_color='rgb(180, 43, 40)'
                         ))
    fig.add_trace(go.Bar(x=df35[My_dropdown13],
                         y=df35['PUNT_LECTURA_CRITICA'],
                         name='Lectura crítica',
                         marker_color='rgb(110, 85, 180)'
                         ))
    fig.add_trace(go.Bar(x=df35[My_dropdown13],
                         y=df35['PUNT_MATEMATICAS'],
                         name='Matemáticas',
                         marker_color='rgb(110, 85, 109)'
                         ))
    fig.add_trace(go.Bar(x=df35[My_dropdown13],
                         y=df35['PUNT_C_NATURALES'],
                         name='Ciencias naturales',
                         marker_color='rgb(80, 148, 30)'
                         ))
    fig.add_trace(go.Bar(x=df35[My_dropdown13],
                         y=df35['PUNT_SOCIALES_CIUDADANAS'],
                         name='Ciencias sociales',
                         marker_color='rgb(80, 43, 89)'
                         ))

    fig.update_layout(
        #title='',
        xaxis_tickfont_size=14,
        yaxis=dict(
            title='Puntaje global',
            titlefont_size=16,
            tickfont_size=14,
        ),
        legend=dict(
            x=0,
            y=1.5,
            bgcolor='rgba(255, 255, 255, 0)',
            bordercolor='rgba(255, 255, 255, 0)'
        ),
        barmode='group',
        bargap=0.15,  # gap between bars of adjacent location coordinates.
        bargroupgap=0.1  # gap between bars of the same location coordinate.
    )
    return  fig




# This call will be used with Gunicorn server
server = app.server

# Testing server, don't use in production, host
if __name__ == "__main__":
    app.run_server(debug=False)