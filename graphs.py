import pandas as  pd 
import numpy as mp
import plotly.express as px 
import plotly.graph_objects as go

class Graphs:
    def __init__(self,df,geojson):
        self.df = df
        self.geojson = geojson
    
    def getCRPgraph(self):
        dm = self.df.drop_duplicates(subset='id', keep="first")
        fig = px.choropleth_mapbox(
            data_frame = dm,
            locations = 'id',
            geojson = self.geojson,
            color = ' PARTY ',
            labels = {' PARTY ' : 'Political Parties'},
            hover_name = ' AC NAME ',
            mapbox_style="carto-positron",
            hover_data = [' TOTAL '],
            opacity=0.5,
            center = {"lat": 18.866, "lon": 76.522},
            zoom=5.2
        )
        fig.update_layout(
            title_text = '2019 Maharashtra Assembly Elections',
            margin={"r":20,"t":50,"l":20,"b":20},
            height = 600,
            width = 800
        )
        return go.Figure(fig)

    def getConstituencyPieChart(self,constituency):
        dp = self.df.loc[self.df[' AC NAME '] == constituency]
        fig = px.pie(
            data_frame = dp,
            values = ' TOTAL ',
            names = ' PARTY ',
            title = 'NO OF VOTES BY EACH PARTY IN ' + constituency,
            hover_data = [' PARTY '], 
            labels={' TOTAL ':'Total number of votes'}
        )
        fig.update_layout(
            title_text = 'Performance of parties in a particular constituency',
            margin={"r":20,"t":50,"l":20,"b":20},
            height = 400,
            width = 600,
        )
        return fig

    def getPartyPerformance(self,partyname):
        dp = self.df.loc[self.df[' PARTY '] == partyname]
        fig = px.choropleth_mapbox(
            data_frame = dp,
            locations = 'id',
            geojson = self.geojson,
            color = ' TOTAL ',
            labels = {' TOTAL ' : 'Total no of Votes'},
            hover_data = [' TOTAL '],
            mapbox_style = 'carto-positron',
            opacity=0.5,
            center = {"lat": 18.866, "lon": 76.522},
            zoom=5
        )
        fig.update_geos(fitbounds = 'locations', visible = False)
        fig.update_layout(
            title_text = '2019 Maharashtra Assembly Elections ' + partyname + ' Performance',
            height = 400,
            width = 600,
            margin={"r":20,"t":50,"l":20,"b":20},
        )
        return fig
    


