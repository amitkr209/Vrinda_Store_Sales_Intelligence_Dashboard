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
    html.H1("Vrinda Store Sales Dashboard", style={'fontSize':50, 'textAlign':'center', 'color':"#D8A720D8"})
])

if __name__ == '__main__':
    app.run(debug=True)