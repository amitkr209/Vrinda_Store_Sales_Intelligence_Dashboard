# Vrinda Store Sales Dashboard

# Importing Libraries
import kagglehub
from kagglehub import KaggleDatasetAdapter

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=UserWarning)

import io
import base64
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, html, dcc, Input, Output

# Loading Dataset
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
        
file_path = "Vrinda Store Sales Data.csv"

df = kagglehub.load_dataset(
  KaggleDatasetAdapter.PANDAS,
  "amitkumar209/vrinda-store-sales-data",
  file_path,)

# Data Cleaning

# Fix Gender Values
df['Gender'] = df['Gender'].replace('M', 'Men')
df['Gender'] = df['Gender'].replace('W', 'Women')

# Fix Quantity Values
df['Qty'] = df['Qty'].replace('One', 1)
df['Qty'] = df['Qty'].replace('Two', 2)

# Convert Datatypes
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)
df['Qty'] = df['Qty'].astype('int')
df.columns = df.columns.str.strip()

# Extract month number from 'Date' column and store in new 'Month' column
df['Month'] = df['Date'].dt.month

# Categorize ages into groups: Senior, Young, Adult
df['Age Group'] = np.where(df['Age'] > 50, 'Senior',
                           np.where(df['Age'] < 30, 'Young', 'Adult'))

# Interactive Dashboard
app = Dash(__name__)

app.layout = html.Div(children=[
    html.H1("Vrinda Store Sales Dashboard", style={'textSize':50, 'textAlign':'center', 'color':'#D8A720D8'}),
    html.P("Sales for Year 2022", style={'textAlign':'center'}),
    html.Br(),
    html.Div([
        "Quater:",
        dcc.Dropdown(id="input_quater",
                     options = [{'label':'All', 'value':'all'},
                                {'label':'Jan-Mar', 'value':1},
                                {'label':'Apr-Jun', 'value':2},
                                {'label':'Jul-Sep', 'value':3},
                                {'label':'Oct-Dec', 'value':4}],
                     value = 'all',
                     clearable=False,
                     style = {'width':'120px', 'height':'25px', 'fontSize':25, 'margin':'0 auto'})
    ], style = {'textAlign':'center', 'textSize':25}),
    html.Br(),
    html.Div([
        dcc.Graph(id = "total_revenue",
                  config = {'displayModeBar':False},
                  style = {'width':'20%', 'height':'130px'}),
        dcc.Graph(id = "quantity_sold",
                  config = {'displayModeBar':False},
                  style = {'width':'20%', 'height':'130px'}),
        dcc.Graph(id = "total_orders",
                  config = {'displayModeBar':False},
                  style = {'width':'20%', 'height':'130px'}),
        dcc.Graph(id = "aov",
                  config = {'displayModeBar':False},
                  style = {'width':'20%', 'height':'130px'}),
        dcc.Graph(id = "total_unique_cust",
                  config = {'displayModeBar':False},
                  style = {'width':'20%', 'height':'130px'})
    ], style={'display':'flex'}),
    html.Br(),
    html.Div([
        html.Div(html.Img(id = 'monthly_sales'), style={'width':'50%'}),
        html.Div(dcc.Graph(id = 'gender_revenue'), style={'width':'50%'})
    ], style={'display':'flex'}),
    html.Div([
        html.Div(dcc.Graph(id = 'status_distribution'), style={'width':'50%'}),
        html.Div(dcc.Graph(id = 'top_states'), style={'width':'50%'})
    ], style={'display':'flex'}),
    html.Div([
        html.Div(dcc.Graph(id = 'channel_distribution'), style={'width':'50%'}),
        html.Div(dcc.Graph(id = 'age_group'), style={'width':'50%'})
    ], style={'display':'flex'}),
], style={'backgroundColor':'white'})

def kpi_figure(value, title, prefix=""):
    fig = go.Figure(
        go.Indicator(
            mode = "number",
            value = value,
            title = {'text':title, 'font':{'size':14}},
            number = {'prefix':prefix, 'font':{'size':28}},
            domain = {"x":[0, 1], "y":[0, 1]}))
    
    fig.update_layout(
        height = 120,
        margin = dict(t=30, b=8, l=8, r=8),
        paper_bgcolor = 'white')
    
    return fig

# @app.callback([
#     Output('total_revenue', 'figure'),
#     Output('quantity_sold', 'figure'),
#     Output('total_orders', 'figure'),
#     Output('aov', 'figure'),
#     Output('total_unique_cust', 'figure'),
#     Output('monthly_sales', 'src'),
#     Output('gender_revenue', 'figure'),
#     Output('status_distribution', 'figure'),
#     Output('top_states', 'figure'),
#     Output('channel_distribution', 'figure'),
#     Output('age_group', 'figure')],
#     Input("input_quater", 'value'))

# def get_graph(quater):
#     if quater != 'all':
#         filter_df = df[df['quater'] == quater]
#     else:
#         filter_df = df.copy()
    
#     # Total Revenue
#     total_revenue = filter_df['Amount'].sum()
#     fig1 = kpi_figure(total_revenue, "Total Revenue", "₹")
    
#     # Calculate rotal quantity sold
#     quantity_sold = df['Qty'].sum()
#     fig2 = kpi_figure(quantity_sold, "Quantity Sold")
    
    
    
#     return [fig1, fig2]
    

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = '8051', debug=True)