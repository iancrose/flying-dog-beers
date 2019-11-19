import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

import pandas as pd

########### Define your variables
beers=['Chesapeake Stout', 'Snake Dog IPA', 'Imperial Porter', 'Double Dog IPA', 'FifthBeer']
ibu_values=[35, 60, 85, 75, 61]
abv_values=[5.4, 7.1, 9.2, 4.3, 4.8]
color1='lightblue'
color2='darkred'
mytitle='Beer Comparison'
tabtitle='beer!'
myheading='Some Beers'
label1='IBU'
label2='ABV'
githublink='https://github.com/austinlasseter/flying-dog-beers'
sourceurl='https://www.flyingdog.com/beers/'

########### Set up the chart
bitterness = go.Bar(
    x=beers,
    y=ibu_values,
    name=label1,
    marker={'color':color1}
)
alcohol = go.Bar(
    x=beers,
    y=abv_values,
    name=label2,
    marker={'color':color2}
)

beer_data = [bitterness, alcohol]
beer_layout = go.Layout(
    barmode='group',
    title = mytitle
)

beer_fig = go.Figure(data=beer_data, layout=beer_layout)

df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/'
    'c78bf172206ce24f77d6363a2d754b59/raw/'
    'c353e8ef842413cae56ae3920b8fd78468aa4cb2/'
    'usa-agricultural-exports-2011.csv')

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='flyingdog',
        figure=beer_fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A('Data Source', href=sourceurl),
    ]
)

layout = html.Div([
    html.H1("Food Product Exports in the United States", style={"textAlign": "center"}),
    html.Div([html.Div([dcc.Dropdown(id='product-selected1',
                                     options=[{'label': i.title(), 'value': i} for i in df.columns.values[2:]],
                                     value="poultry")], className="six columns",
                       style={"width": "40%", "float": "right"}),
              html.Div([dcc.Dropdown(id='product-selected2',
                                     options=[{'label': i.title(), 'value': i} for i in df.columns.values[2:]],
                                     value='beef')], className="six columns", style={"width": "40%", "float": "left"}),
              ], className="row", style={"padding": 50, "width": "60%", "margin-left": "auto", "margin-right": "auto"}),
    dcc.Graph(id='my-graph'),

    # dcc.Link('Go to Source Code', href='{}/code'.format(app_name))
], className="container")

if __name__ == '__main__':
    app.run_server()
