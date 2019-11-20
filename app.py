import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

import pandas as pd

########### Define your variables
tabtitle='Dash Playground'

########### Load the data
df = pd.read_csv('https://ianrosewrites.com/1011010/days.csv')

pv = pd.pivot_table(df, index=['daynum'], columns=["daywk"], values=['yes'], fill_value=0)

trace1 = go.Bar(x=df['daynum'], y=df['yes'], name='Counted')
trace2 = go.Bar(x=df['daynum'], y=df['no'], name='Not Counted')

tracesu = go.Bar(x=pv.index, y=pv[('yes', 'Sun')], name='Sunday')
tracemo = go.Bar(x=pv.index, y=pv[('yes', 'Sun')], name='Monday')
tracetu = go.Bar(x=pv.index, y=pv[('yes', 'Sun')], name='Tuesday')
tracewe = go.Bar(x=pv.index, y=pv[('yes', 'Sun')], name='Wednesday')
traceth = go.Bar(x=pv.index, y=pv[('yes', 'Sun')], name='Thursday')
tracefr = go.Bar(x=pv.index, y=pv[('yes', 'Sun')], name='Friday')
tracesa = go.Bar(x=pv.index, y=pv[('yes', 'Sun')], name='Saturday')

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div([
    html.H1(children='Daily Logged Time'),
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['daywk'] == i]['daynum'],
                    y=df[df['daywk'] == i]['yes'],
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
    ), 
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [trace1, trace2],
            'layout':
            go.Layout(barmode='stack')
        }), 
    dcc.Graph(
        id='example-graph-2',
        figure={
            'data': [tracesu, tracemo, tracetu, tracewe, traceth, tracefr, tracesa],
            'layout':
            go.Layout(barmode='stack')
        })
])

if __name__ == '__main__':
    app.run_server()
