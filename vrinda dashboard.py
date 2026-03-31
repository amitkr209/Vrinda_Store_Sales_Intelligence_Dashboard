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
    html.P("Sales for Year 2022", style={'textAlign':'center', 'textSize':30}),
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
                     style = {'width':'135px', 'height':'25px', 'fontSize':20, 'margin':'0 auto'})
    ], style = {'textAlign':'center', 'textSize':35}),
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
        html.Div(html.Img(id = 'monthly_sales'), style={'width':'55%'}),
        html.Div(dcc.Graph(id = 'gender_revenue'), style={'width':'45%'})
    ], style={'display':'flex'}),
    html.Div([
        html.Div(dcc.Graph(id = 'status_distribution'), style={'width':'55%'}),
        html.Div(dcc.Graph(id = 'top_states'), style={'width':'45%'})
    ], style={'display':'flex'}),
    html.Div([
        html.Div(dcc.Graph(id = 'channel_distribution'), style={'width':'60%'}),
        html.Div(html.Img(id = 'age_group'), style={'width':'40%'})
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

@app.callback([
    Output('total_revenue', 'figure'),
    Output('quantity_sold', 'figure'),
    Output('total_orders', 'figure'),
    Output('aov', 'figure'),
    Output('total_unique_cust', 'figure'),
    Output('monthly_sales', 'src'),
    Output('gender_revenue', 'figure'),
    Output('status_distribution', 'figure'),
    Output('top_states', 'figure'),
    Output('channel_distribution', 'figure'),
    Output('age_group', 'src')],
    Input("input_quater", 'value'))

def get_graph(quater):
    if quater != 'all':
        filter_df = df[df['Quater'] == quater]
    else:
        filter_df = df.copy()
    
    # Total Revenue
    total_revenue = filter_df['Amount'].sum()
    fig1 = kpi_figure(total_revenue, "Total Revenue", "₹")
    
    # Calculate rotal quantity sold
    quantity_sold = filter_df['Qty'].sum()
    fig2 = kpi_figure(quantity_sold, "Quantity Sold")
    
    # Calculate total number of orders
    total_orders = filter_df['Order ID'].size
    fig3 = kpi_figure(total_orders, "Total Orders")
    
    # Calculate average order value (aov)
    aov = (total_revenue / total_orders) if total_orders > 0 else 0
    fig4 = kpi_figure(aov, "Average Order Value", "₹")
    
    # Calculate number of unique customers
    unique_customers = filter_df['Cust ID'].nunique()
    fig5 = kpi_figure(unique_customers, "Unique Customers")
    
    # Monthly Revenue and Orders
    df_monthly_sales = filter_df.groupby('Month')['Amount'].sum().to_frame('revenue').reset_index()
    df_monthly_sales['month_name'] = pd.to_datetime(df_monthly_sales['Month'], format='%m').dt.strftime('%b')
    df_monthly_sales.set_index('month_name', inplace=True)
    df_monthly_sales.drop('Month', axis=1, inplace=True)
    
    df_monthly_orders = filter_df['Month'].value_counts().sort_index().reset_index(name = 'order_count')
    df_monthly_orders['month_name'] = pd.to_datetime(df_monthly_orders['Month'], format = '%m').dt.strftime('%b')
    df_monthly_orders.set_index('month_name', inplace=True)
    df_monthly_orders.drop('Month', axis = 1, inplace=True)

    fig, ax1 = plt.subplots(figsize=(7, 4.5))
    sns.barplot(data = df_monthly_sales,
                x = 'month_name',
                y = 'revenue',
                color = 'steelblue',
                edgecolor = 'black',
                ax = ax1)

    ax1.set_ylim(1_000_000)  # Set minimum y-axis limit for revenue
    ax1.set_ylabel("Revenue (in Millions)")
    ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, pos: f'{x/1000000:.1f}M'))

    ax2 = ax1.twinx()
    sns.lineplot(data = df_monthly_orders,
                x = 'month_name',
                y = 'order_count',
                color = 'orange',
                marker = 'o',
                linewidth = 3,
                linestyle = '--')

    ax2.set_ylim(2000, 3000)
    ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, pos: f'{x/1000:.1f}K'))

    plt.title("Monthly Revenue and Orders", fontsize=13)
    ax1.set_xlabel("")
    ax2.set_ylabel("Order Count")
    sns.despine(left=True, right=True)
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    plt.close()
    buf.seek(0)
    
    encoded = base64.b64encode(buf.read()).decode('utf-8')
    fig6 = f"data:image/png;base64,{encoded}"
    
    # Revenue Distribution by Gender
    df_gender_sales = filter_df.groupby('Gender')['Amount'].sum().reset_index()
    fig7 = px.pie(data_frame=df_gender_sales,
             values = 'Amount',
             names = 'Gender',
             template = 'plotly_white')

    fig7.update_layout(title = "Revenue Distribution by Gender",
                    title_x = 0.5)
    
    # Order Status Distribution
    df_order_status = filter_df.Status.value_counts().reset_index()
    fig8 = px.pie(data_frame=df_order_status,
             values = 'count',
             names = 'Status',
             template = 'plotly_white')

    fig8.update_layout(title = "Order Status Distribution",
                    title_x = 0.5)
    
    # Top Revenue States
    df_top_states = filter_df.groupby('ship-state')['Amount'].sum().nlargest(5).reset_index()
    fig9 = px.bar(data_frame=df_top_states.iloc[::-1],
                    x = 'Amount',
                    y = 'ship-state',
                    template = 'plotly_white')
    fig9.update_layout(title = "Top Revenue State",
                            title_x = 0.5,
                            xaxis_title = "",
                            yaxis_title = "")
    fig9.update_traces(marker = {'line':{'width':1, 'color':'black'}},
                            text = [f"₹{x/1_000_000:.1f}M" for x in df_top_states.iloc[::-1]['Amount']] if quater == 'all' else [f"₹{x/1_000:.1f}K" for x in df_top_states.iloc[::-1]['Amount']],
                            textposition='inside')
    fig9.update_xaxes(showticklabels = False)
    
    # Order Percent Distribution by Channel
    df_channel_order = filter_df['Channel'].value_counts().reset_index()
    df_channel_order['Order_%']= round(df_channel_order['count'] / df['Order ID'].count() * 100, 1)
    
    fig10 = px.bar(data_frame=df_channel_order.iloc[::-1],
             x = "Order_%",
             y = "Channel",
             template = "plotly_white")
    fig10.update_layout(title="Channel Order Distribution",
                    title_x = 0.5,
                    xaxis_title = "",
                    yaxis_title = "")
    fig10.update_traces(marker = {'line':{'width':1, 'color':'black'}},
                    text = [f"{x:.1f}%" for x in df_channel_order['Order_%'].iloc[::-1]],
                    textposition = 'inside')
    fig10.update_xaxes(showticklabels = False)
    
    # Order Distribution by Age and Gender
    df_age_gender = filter_df.pivot_table(index='Age Group', columns='Gender', aggfunc='size')
    df_age_gender['Men_%'] = 100 * df_age_gender['Men'] / df['Order ID'].size
    df_age_gender['Women_%'] = 100 * df_age_gender['Women'] / df['Order ID'].size

    df_age_gender_melted = df_age_gender.reset_index().melt(
    id_vars = 'Age Group',
    value_vars = ['Men_%', 'Women_%'],
    var_name = 'Gender',
    value_name = "Percentage")
    
    ax = sns.barplot(data = df_age_gender_melted,
            x = 'Age Group',
            y = 'Percentage',
            hue = 'Gender',
            dodge = True,
            width = 0.7,
            edgecolor = 'black')

    ax.set_yticks([])
    for container in ax.containers:
        plt.bar_label(container, fmt="%.1f%%", label_type="edge", padding=3)

    plt.title("Order Distribution by Age Group and Gender", fontsize = 13)
    plt.xlabel('')
    plt.ylabel('')
    sns.despine(left=True)
    
    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches = 'tight')
    plt.close()
    buf.seek(0)
    
    encoded = base64.b64encode(buf.read()).decode('utf-8')
    fig11 = f"data:image/png;base64,{encoded}"
    
    
    return [fig1, fig2, fig3, fig4, fig5, fig6, fig7, fig8, fig9, fig10, fig11]
    

if __name__ == '__main__':
    app.run(port = '8060', host = '127.0.0.1', debug=True)