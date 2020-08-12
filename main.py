import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import numpy as np
import json
from graphs import Graphs
import plotly.graph_objects as go

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('election_result_2019.csv')
geojson = json.load(open('maharashtra_assembly.json'))

dm = df.drop_duplicates(subset='id', keep="first")
fig = px.choropleth(
    data_frame = dm,
    locations = 'id',
    color = ' PARTY ',
    geojson = geojson, 
)
fig.update_geos(fitbounds = 'locations', visible = False)
fig.show()
app.layout = html.Div(children = [
    html.H1(children = "Hello World"),

    dcc.Graph(figure=fig)

])

app.run_server(debug=True)