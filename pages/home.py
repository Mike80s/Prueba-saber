import dash
from dash import html , dcc
import dash_bootstrap_components as dbc
from dash_labs.plugins import register_page


register_page(__name__, path="/")

from components.kpi.kpibadge import kpibadge
from components.maps.mapsample import mapsample


kpi1 = kpibadge('500k', 'Número de datos', 'DataIcfes')
kpi2 = kpibadge('81', 'Número de descriptores', 'Limpieza de datos')
kpi3 = kpibadge('5', 'Asignaturas revisadas ', 'DataIcfes')
kpi4 = kpibadge('32','Número de departamentos', 'Colombia')

mapa_ejemplo = mapsample('Mapa de ejemplo', 'id_mapa_ejemplo')

layout=  dbc.Container(
    [   dbc.Row([
               dbc.Col([
                   html.Img(src="data:image/jpeg;base64,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")
                ], xs=12, className='card')
        ]),
        dbc.Row([
            dbc.Col([
                kpi1.display()
            ], className='card'),
            dbc.Col([
                kpi2.display()
            ], className='card'),
            dbc.Col([
                kpi3.display()
            ], className='card'),
            dbc.Col([
                kpi4.display()
            ], className='card')
        ]),
        dbc.Row([
             dbc.Col([
                      html.Div([
                          html.H4(['Historia de la prueba saber 11']),
                          html.P('La prueba Saber 11 (ICFES) es una prueba escrita para estudiantes colombianos o extranjeros   que culminan el ciclo de educación media.'),
                          html.P( 'Se ha presentado anualmente o semestralmente durante  54 años desde su creación en 1968.'),
                          html.P('De otra parte en 1980, mediante el decreto 2343 de 1998 de 1996 se estípula su presentación obligatoria para el ingreso a cualquier programa de educación superior en Colombia.')
                         ])
            ], xs=12, className='card'),
        ]),
    ])