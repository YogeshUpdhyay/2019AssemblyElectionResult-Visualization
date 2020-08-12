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
graph = Graphs(df,geojson)

app.layout = html.Div(children=[
    html.H1(
        children='2019 Assembly Election Analysis',
        style={
            'textAlign': 'center',
        }
    ),

    html.Div(style = {'float' : 'top' },children=[
        dcc.Graph(
            figure=graph.getCRPgraph(),   
            style={
                'float' : 'left',
                'width' : '70%',
            } 
        ),
        html.P(
            children='The following graph is the choropleth map of \'Mahrashtra\' showing the result of the 2019 Assembly Elections',
            style={
                'textAlign': 'left',
                'align' : 'left',
                'fontSize' : '20px',
                'float' : 'right',
                'width' : '30%',
                'marginTop' : 50,
                'marginBottom' : 410,
            }
        )  
    ]), 

    html.Div(style = {'float' : 'bottom'},children=[
        dcc.Graph(
            figure=graph.getConstituencyPieChart('Akkalkuwa '),    
            style = {
                'float' : 'left',
                'width' : '50%'
            }
        ),
        dcc.Graph(
            figure=graph.getPartyPerformance('BJP'), 
            style = {
                'float' : 'right',
                'width' : '50%'
            }   
        ),
           
    ]),

    html.Div(children = [
        html.H3(
            children='The following graph shows thr performance of various parties in a particular constituency',
            style={
                'float' : 'left',
                'width' : '50%',
            }
        ),
        html.H3(
            children='''This choropleth map shows the performance of a particular political party in the election ''',
            style={
                'float' : 'right',
                'width' : '50%',
            }
        )  
    ])

])

if __name__ == '__main__':
    app.run_server(debug=True)