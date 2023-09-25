# Import required libraries
import pandas as pd
import plotly.graph_objects as go
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output

# Read the airline data into the pandas dataframe
airline_data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv',
                            encoding = "ISO-8859-1",
                            dtype={'Div1Airport': str, 'Div1TailNum': str,
                                   'Div2Airport': str, 'Div2TailNum': str})

# Create a dash application layout
app = dash.Dash(__name__)

# Get the layout of the application and adjust it.
# Create an outer division using html.Div and add title to the dashboard using html.H1 component
# Add a html.Div and core input text component
# Finally, add graph component.
app.layout = html.Div(children=[html.H1(),
                                html.Div(["Input Year", dcc.Input(),],
                                style={}),
                                html.Br(),
                                html.Br(),
                                html.Div(),
                                ])


# add callback decorator
@app.callback(Output(),
              Input())
# Add computation to callback function and return graph
def get_graph(entered_year):
    # Select data based on the entered year
    df = airline_data[airline_data['Year'] == int(entered_year)]

    # Group the data by Month and compute the average over arrival delay time.
    line_data = df.groupby('Month')['ArrDelay'].mean().reset_index()

    #
    fig = go.Figure(data=None)
    fig.update_layout()

# Run the app
if __name__ == '__main__':
    app.run_server()