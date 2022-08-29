import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objects as go
import numpy as np
from dash import dash_table


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.SLATE])
server = app.server
app.config['suppress_callback_exceptions']= True
tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#5032d9',
    'color': 'white',
    #'padding': '6px'
}
tabs_styles = {
    'height': '75px',
    'width':'1850px',
    'align-items': 'center',
    'vertical-align' : 'bottom'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'fontWeight': 'bold',
    'background-color': 'rgba(0, 0, 0, 0)'

}
date_picker_style = {
    'background-color': 'rgba(0, 0, 0, 0)',
    'color': 'blue'
}
def drawFigure1():
    return  html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    id="graph",
                    responsive= 'auto',
                    animate=False
                )
            ])
        ),
    ])

def drawIndicator1():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    id = "Indicator1_Sales",
                )
            ])
        ),
    ])
def drawIndicator2():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    id = "Indicator2_Sales",
                )
            ])
        ),
    ])
def drawIndicator3():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    id = "Indicator3_Sales",
                )
            ])
        ),
    ])
def drawPie():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    id = "pie_segments",
                )
            ])
        ),
    ])
# Text field
def drawText():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                html.Div([
                    html.H2("Text"),
                ], style={'textAlign': 'center'})
            ])
        ),
    ])
def drawGroupedLine():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    id = "grouped_line_segments",
                )
            ])
        ),
    ])
def drawBoxPlot():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    id = "box_plot_segments",
                )
            ])
        ),
    ])
def drawBoxPlot1():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    id = "box_plot",
                )
            ])
        ),
    ])
def drawBarPlot():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    id = "bar_plot_segments",
                )
            ])
        ),
    ])
def drawBarPlot2():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    id = "bar_plot_barnds",
                )
            ])
        ),
    ])
def drawcomplet_lux():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    id = "ind_comple_lux",
                )
            ])
        ),
    ])
def drawcomplet_niche():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    id = "ind_comple_niche",
                )
            ])
        ),
    ])
def drawcomplet_mastige():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    id = "ind_comple_mastige",
                )
            ])
        ),
    ])
def drawcomplet_mass():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    id = "ind_comple_mass",
                )
            ])
        ),
    ])
def drawrich():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                dcc.Graph(
                    id = "rich_content",
                )
            ])
        ),
    ])
def drawtable():
    return html.Div([
        dbc.Card(
            dbc.CardBody([
                dash_table.DataTable(
                    data=df5.to_dict('records'),
                    columns=[{"name": i, "id": i} for i in df5.columns],
                    id = "table-multicol-sorting",
                    filter_action="native",
                    fixed_rows={'headers': True},
                    sort_action="native",
                    sort_mode="multi",
                    page_action= 'none',
                    style_table={'height': '450px', 'overflowY': 'scroll' },
                    style_data={'backgroundColor': 'rgba(0, 0, 0, 0)','color': '#5032d9', 'border': '1px solid blue'},
                    style_header={'backgroundColor': '#5032d9','color': 'white'},
                    style_cell={'textAlign': 'left', 'border': '1px white'},

                )
            ])
        ),
    ])
# Data
sales = pd.read_excel('sales_data1.xlsx')
df5 = sales.pivot_table(index = ['ASIN', 'Segment', 'Product Details', 'Price', 'Ratings', 'Review Count'], values = ['Sales'], aggfunc = np.sum)
df5.reset_index(inplace = True)
tab_1_layout = html.Div([
    dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    drawIndicator1()
                ], width=3),
                dbc.Col([
                    drawIndicator2()
                ], width=3),
                dbc.Col([
                    drawIndicator3()
                ], width=3),
            ], align='center', justify="center"),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    drawFigure1()
                ], width=6),
                dbc.Col([
                    drawPie()
                ], width=3),
            ], align='end', justify="center"),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    drawBoxPlot1()
                ], width=4),
                dbc.Col([
                    drawBarPlot2()
                ], width=5),
            ], align='end', justify="center"),
            html.Br(),
        ]), color = 'dark'
    )
])
tab_2_layout = html.Div([
    dbc.Card(
        dbc.CardBody([
            dbc.Row([
                dbc.Col([
                    drawGroupedLine()
                ], width=5),
                dbc.Col([
                    drawBoxPlot()
                ], width=4),
            ], align='center', justify="center"),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    drawBarPlot()
                ], width=3),
                dbc.Col([
                    drawtable()
                ], width=6),
            ], align='center', justify="center"),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    drawcomplet_lux()
                ], width=3),
                dbc.Col([
                    drawcomplet_niche()
                ], width=3),
                dbc.Col([
                    drawcomplet_mastige()
                ], width=3),
                ], align='center', justify="center"),
            dbc.Row([
                dbc.Col([
                    drawcomplet_mass()
                ], width=3),
                dbc.Col([
                    drawrich()
                ], width=6)
            ], align='center', justify="center"),
            html.Br(),
        ]),  color = 'dark'
    )
])
app.layout = html.Div([
    html.H1('Women Perfumes - Amazon.com', style={
        'textAlign': 'center'
}),
    html.Div([
            dcc.Tabs(id="tabs",
                     value='tab',
                     children = [
                         dcc.Tab(label="Category View",
                                 value='cat_tab',
                                 selected_style=tab_selected_style,
                                 style= tab_style),

                         dcc.Tab(label="Product View",
                                 value ='prod_tab',
                                 selected_style=tab_selected_style,
                                 style= tab_style)
                         ], style=tabs_styles, className='custom-tabs-container')
        ], style = {'width': '100%', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center'}),
    html.Div([
        html.Div([
            dcc.DatePickerRange(
                id = 'date_filter',
                start_date=sales['Time'].min(),
                end_date=sales['Time'].max(),
                min_date_allowed = sales['Time'].min(),
                max_date_allowed = sales['Time'].max(),
            ),
            ], style = {'width': '100%', 'display': 'flex', 'align-items': 'center', 'justify-content': 'center', 'vertical-align' : 'bottom', 'background-color': 'rgba(0, 0, 0, 0)', 'color':'blue'}),
        ]),
    html.Div(id='tabs-content'),
    ]
)

@app.callback(Output('tabs-content', 'children'),
             [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'cat_tab':
        return tab_1_layout
    elif tab == 'prod_tab':
        return tab_2_layout

@app.callback(
    Output('graph', 'figure'),
    Output('Indicator1_Sales', 'figure'),
    Output('Indicator2_Sales', 'figure'),
    Output('Indicator3_Sales', 'figure'),
    Output('box_plot', 'figure'),
    Output('bar_plot_barnds', 'figure'),
    Output('pie_segments', 'figure'),
    Input("date_filter", "start_date"),
    Input("date_filter", "end_date"),
)
def updateGraph1(start_date, end_date):

    df = sales.loc[pd.to_datetime(sales['Time']).between(pd.to_datetime(start_date), pd.to_datetime(end_date))]
    time_sales = df.pivot_table(values=['Sales', 'Revenue'], index=['Time'], aggfunc=np.sum)
    time_sales.reset_index(inplace=True)
    fig = px.line(time_sales, 'Time', 'Sales', title = "Sales units over time").update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)')

    Products = df['ASIN'].nunique()
    fig1 = go.Figure(go.Indicator(mode="number+delta", value=Products,
                                  number={'suffix': " Products in scope", "font":{"size":20}},
                                  title={"text": "<br><span style='font-size:5em;color:gray'>Ordered Units</span>"},
                                  domain={'row': 0, 'column': 0})
                     ).update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        height=150)

    Sales = df['Sales'].sum()
    fig2 = go.Figure(go.Indicator(mode="number+delta",value= Sales,
                                  number={'suffix': " Units Sold", "font":{"size":20}},
                                  title={"text": "<br><span style='font-size:5em;color:gray'>Ordered Units</span>"},
                                  domain={'row': 0, 'column': 0})
                     ).update_layout(
        template='plotly_dark',
        plot_bgcolor= 'rgba(0, 0, 0, 0)',
        paper_bgcolor= 'rgba(0, 0, 0, 0)',
        height=150)
    Revenue = df['Revenue'].sum()
    fig3 = go.Figure(go.Indicator(mode="number+delta", value=Revenue,
                                  number={'suffix': " $", "font":{"size":20}},
                                  title={"text": "<br><span style='font-size:5em;color:gray'>Revenue</span>"},
                                  domain={'row': 0, 'column': 0})
                     ).update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
        height=150)

    df2 =  df.pivot_table(index = ['Time', 'Holiday'], values = "Sales", aggfunc = np.sum)
    df2.reset_index(inplace=True)
    fig5 = px.box(df2, x="Holiday", y="Sales", title = "Sales (units) in common days and holiday").update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)')
    df3 = df.pivot_table(index=['Brand', 'Segment'], values='Sales', aggfunc=np.sum)
    df3.reset_index(inplace=True)
    dt = df3.sort_values(['Sales'], ascending=False).head(10).reset_index()
    fig6 = px.bar(dt, y='Sales', x='Brand', color = 'Segment',
                 title="Top 10 brands by Sales").update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)')
    date = df.pivot_table(index=['Segment'], values=['ASIN'], aggfunc=pd.Series.nunique)
    date.reset_index(inplace=True)
    fig4 = px.pie(date, values='ASIN', names='Segment', title = "Number of products in categories").update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)')
    return fig, fig1, fig2, fig3, fig5, fig6, fig4

@app.callback(
    Output('grouped_line_segments', 'figure'),
    Output('box_plot_segments', 'figure'),
    Output('bar_plot_segments', 'figure'),
    Output('ind_comple_lux', 'figure'),
    Output('ind_comple_niche', 'figure'),
    Output('ind_comple_mastige', 'figure'),
    Output('ind_comple_mass', 'figure'),
    Output('table-multicol-sorting', "data"),
    Output('rich_content', 'figure'),
    Input("date_filter", "start_date"),
    Input("date_filter", "end_date"),
)
def Update_Graph2(start_date, end_date):
    df = sales.loc[pd.to_datetime(sales['Time']).between(pd.to_datetime(start_date), pd.to_datetime(end_date))]
    time_sales = df.pivot_table(values=['Sales', 'Revenue'], index=['Time', 'Segment'], aggfunc=np.sum)
    time_sales.reset_index(inplace=True)
    fig5 = px.line(time_sales, x='Time', y='Sales', color='Segment', markers=False, title = "Sales (units) of products by category over time").update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)')
    fig6 = px.box(df, x="Segment", y="Price", title = "Prices of products by category").update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)')
    date1 = df.pivot_table(values=['Ratings', 'Review Count'], index=['Segment', 'ASIN'], aggfunc=np.mean)
    date1.reset_index(inplace=True)
    date1['Weighted_rating'] = date1['Ratings'] * date1['Review Count']
    date2 = date1.pivot_table(values=['Ratings', 'Review Count', 'Weighted_rating'], index=['Segment'],
                              aggfunc={"Ratings": np.mean, "Review Count": np.sum, "Weighted_rating": np.sum})
    date2['weigth_avg_rating'] = date2['Weighted_rating'] / date2['Review Count']
    date2.reset_index(inplace=True)
    fig7 = px.bar(date2, x='Segment', y='weigth_avg_rating', title = "Weighted Average Rating of categories").update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)')
    df['completeness'] = (df['description completeness'] + df['description completeness'] + df['bullet completeness'] + df['Images completeness']) / 4
    df3 = df.drop_duplicates('ASIN')
    df4 = df3.pivot_table(index=['Segment'], values=['completeness'], aggfunc=np.mean)
    df4.reset_index(inplace=True)
    mass_market = df4.loc[df4['Segment'] == 'mass market']['completeness'].values[0]
    lux = df4.loc[df4['Segment'] == 'lux']['completeness'].values[0]
    mastige = df4.loc[df4['Segment'] == 'mastige']['completeness'].values[0]
    niche = df4.loc[df4['Segment'] == 'niche']['completeness'].values[0]
    fig8 = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = lux * 100,
        number={'suffix': " %"},
        title = {'text': "Lux Content Completeness"},
        domain = {'x': [0, 1], 'y': [0, 1]}
    )).update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)')
    fig9 = go.Figure(go.Indicator(
        mode="gauge+number",
        value=niche * 100,
        number={'suffix': " %"},
        title={'text': "Niche Content Completeness"},
        domain={'x': [0, 1], 'y': [0, 1]}
    )).update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)')
    fig10 = go.Figure(go.Indicator(
        mode="gauge+number",
        value=mastige * 100,
        number={'suffix': " %"},
        title={'text': "Masstige Content Completeness"},
        domain={'x': [0, 1], 'y': [0, 1]}
    )).update_layout(
        title_font_size = 5,
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)')
    fig11 = go.Figure(go.Indicator(
        mode="gauge+number",
        value=mass_market * 100,
        number={'suffix': " %"},
        title={'text': "Mass market Content Completeness"},
        domain={'x': [0, 1], 'y': [0, 1]}
    )).update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)')
    df5 = df.pivot_table(index = ['ASIN', 'Segment', 'Product Details', 'Price', 'Ratings', 'Review Count'], values = ['Sales'], aggfunc = np.sum)
    df5.reset_index(inplace = True)
    data = df5.to_dict("records")

    df6 = df.drop_duplicates('ASIN')
    df7 = df6.pivot_table(index=['Segment'], values = 'Rich', aggfunc = np.mean)
    df7.reset_index(inplace = True)
    fig12 = px.bar(df7, x='Segment', y='Rich',
                  title="Share of products with Rich Content").update_layout(
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)')
    return fig5, fig6, fig7, fig8, fig9, fig10, fig11, data, fig12

if __name__ == '__main__':
    app.run_server(debug=True)
