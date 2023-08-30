import plotly.graph_objects as go

def make_chart(
    x_data: list = [x for x in range(10)], y_data: list = [x for x in range(10)], ticker_symbol="rivn", line_color=f"rgba(255, 255, 0, .7)"
):
    fig = go.Figure(data=go.Scatter(x=x_data, y=y_data))

    fig.update_traces(line=dict(color=line_color))

    fig.update_xaxes(
        showgrid=False,
        showticklabels=True,
        showline=False,
        zeroline=False,
        title="Time",
        title_font=dict(color="rgba(255, 255, 255, 0.7)"),
        tickfont=dict(color="rgba(255, 255, 255, 0.4)"),
    )

    fig.update_yaxes(
        showgrid=False,
        showticklabels=True,
        showline=False,
        zeroline=False,
        title=f"Price",
        title_font=dict(color="rgba(255, 255, 255, 0.7)"),
        tickfont=dict(color="rgba(255, 255, 255, 0.4)"),
    )

    # Disable interactivity
    fig.update_layout(
        clickmode="none",
        hovermode=False,
        dragmode=False,
        selectdirection=None,
        showlegend=False,
        autosize=True,

        title=f"{ticker_symbol.upper()}",
        title_font=dict(color="rgba(255, 255, 255, 0.7)"),

        # Set chart background color to transparent
        plot_bgcolor="rgba(0, 0, 0, 0)", 
        paper_bgcolor="rgba(0, 0, 0, 0)",

        # Set the font color to white 
        font=dict(color="white"),
    )


    html = fig.to_html(
        include_plotlyjs=False,
        full_html=False,
    )

    return html
