#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Silent warnings
import warnings

warnings.filterwarnings("ignore")

import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

# Core


# Datacd
import pandas as pd

# Visualisation
import seaborn as sns
import plotly.express as px

# In[2]:


df = pd.read_csv("data.csv")

# In[3]:


#df = df.drop(df[df['ESTU_GENERO'] == '-'].index)
#fig0 = px.histogram(df['ESTU_GENERO'])
#fig0

# In[4]:


df.columns

# In[5]:


#fig = px.histogram(df, x='FAMI_TIENEINTERNET', color='ESTU_GENERO', histnorm='percent')
# fig.show()


# In[6]:


#df = df.drop(df[df['FAMI_TIENEINTERNET'] == '-'].index)
#df14 = df[['FAMI_TIENEINTERNET', 'PUNT_GLOBAL']].groupby(['FAMI_TIENEINTERNET']).mean()
#df14

# In[7]:


#type(df14)
#df14 = df14.reset_index()

# In[8]:


# df = px.data.tips()
# Here we use a column with categorical data

#fig = px.bar(df14, x='FAMI_TIENEINTERNET', y='PUNT_GLOBAL')

# In[ ]:


# In[ ]:


# In[ ]:


# In[9]:


fig0 = fig0.update_layout(barmode='stack', xaxis_type='category',
                          #title='<b></b><b>Análisis del puntaje global</b><br><i>Familia que cuenta con internet</i>',
                          # "",
                          #paper_bgcolor='rgb(206, 220, 227)',
                         # plot_bgcolor='rgb(206, 220, 227)',
                         # font=dict(
                              #family="Courier New, monospace",
                             # size=18,
                             # color="#000000"
                          #))

# In[ ]:


# In[ ]:


# In[ ]:


app = dash.Dash()
server = app.server

app.layout = html.Div([
    html.H1(children="Análisis de las pruebas Saber 11 año 2019"),
    html.Div(children="Primeros análisis"),
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig0)
])

if __name__ == '__main__':
    app.run_server(debug=False)