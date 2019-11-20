import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

import pandas as pd

########### Define your variables
tabtitle='Dash Playground'

########### Load the data
# df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')
df = pd.read_csv('https://ianrosewrites.com/1011010/days.csv')

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                go.Scatter(
                    # x=df[df['continent'] == i]['gdp per capita'],
                    x=df[df['daywk'] == i]['daynum'],
                    # y=df[df['continent'] == i]['life expectancy'],
                    y=df[df['daywk'] == i]['yes'],
                    # text=df[df['continent'] == i]['country'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.daywk.unique()
            ],
            'layout': go.Layout(
                xaxis={'title': 'Day #'},
                yaxis={'title': 'Hours Logged'},
                margin={'l': 0, 'b': 0, 't': 0, 'r': 0},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server()
