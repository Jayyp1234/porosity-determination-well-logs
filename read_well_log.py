import lasio
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Read the LAS file
logfile = lasio.read('Braun 2.las')

# Calculate porosity for limestone
# Limestone matrix density assumed = 2.65
# Fluid density = 1 g/cc assuming Water
matrix_density = 2.65
fluid_density = 1

# Calculate Density Porosity
logfile['DenRho'] = 100 * (matrix_density - logfile['RHOB']) / (matrix_density - fluid_density)

# Create a subplot grid
fig = make_subplots(
    rows=1,
    cols=3,
    shared_yaxes=True,
    subplot_titles=['Caliper Log', 'Density Log', 'Density Porosity'],
    horizontal_spacing=0.01
)

# Create traces for each curve/series
caliper = go.Scatter(x=logfile['CALI'], y=logfile['DEPT'], mode='lines', name='Caliper Log')
density = go.Scatter(x=logfile['RHOB'], y=logfile['DEPT'], mode='lines', name='Density Log')
porosity = go.Scatter(
    x=logfile['DenRho'], y=logfile['DEPT'], mode='lines', name='Density Porosity', fill='tozerox'
)

# Add traces to the subplot grid
fig.add_trace(caliper, row=1, col=1)
fig.add_trace(density, row=1, col=2)
fig.add_trace(porosity, row=1, col=3)

# Update layout
fig.update_layout(
    width=800,
    height=1000,
    template='plotly_white',
    title="Well Log Analysis",
    xaxis_title="Log Value",
    yaxis_title="Depth (ft)"
)

# Update X and Y axes properties
fig.update_xaxes(
    side='top',
    showline=True,
    linewidth=1,
    linecolor='black',
    mirror=True,
    gridcolor='grey'
)
fig.update_yaxes(
    showline=True,
    linewidth=1,
    linecolor='black',
    mirror=True,
    gridcolor='grey'
)

# Show the figure
fig.show()
