# utils/figure_helper.py

import pandas as pd
import plotly.express as px
import plotly.io as pio
from phd_package.dashboard.utils.color_helper import category_colors

# Convert to a list for Plotly's default palette
custom_palette = list(category_colors.values())


# Function to set the custom palette
def set_custom_plotly_color_palette(color_palette=custom_palette):
    # Get the current default template
    current_template = pio.templates.default

    # Create a new template based on the current default
    new_template = pio.templates[current_template].layout.template

    # Set the colorway of the new template
    new_template.layout.colorway = color_palette

    # Update the default template
    pio.templates[current_template] = new_template
    pio.templates.default = current_template

    print("Color palette set to the custom palette.")


def map_color_to_sequence(df, color_map):
    # Create color mapping using the color_helper function from phd_package as input
    colors = list(color_map.values())
    sequences = df["Sequence"].unique()
    color_mapping = {seq: colors[i % len(colors)] for i, seq in enumerate(sequences)}

    return color_mapping


def create_timeseries_plot(
    df,
    x_column,
    y_column,
    color=None,
    title=None,
    xlabel=None,
    ylabel=None,
    color_discrete_map=None,
    slice=None,
):
    # Create a copy of the dataframe to avoid modifying the original
    plot_df = df.copy()

    # If x_column is 'index', use the DataFrame index
    if x_column == "index":
        plot_df = plot_df.reset_index()
        x_column = plot_df.columns[0]

    # Add row numbers
    plot_df["Row"] = range(len(plot_df))

    # Apply slice if provided
    if slice:
        plot_df = plot_df.iloc[slice]

    # Create the plot
    fig = px.line(
        plot_df,
        x=x_column,
        y=y_column,
        color=color,
        title=title,
        color_discrete_map=color_discrete_map,
        hover_data={x_column: True, y_column: ":.2f", "Row": True},
    )

    fig.update_layout(
        xaxis_title=xlabel or x_column,
        yaxis_title=ylabel or y_column,
    )
    return fig


def update_timeseries_plot(fig):
    # Update layout
    fig.update_layout(
        font=dict(family="Courier New, monospace", size=12, color="#7f7f7f"),
        showlegend=False,
        plot_bgcolor="white",
        paper_bgcolor="white",
    )
    fig.update_xaxes(showline=True, zeroline=False)
    fig.update_yaxes(showline=True, zeroline=False)

    return fig
