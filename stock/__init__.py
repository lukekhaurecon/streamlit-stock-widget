"""
Make a small widget that displays stock
"""
from datetime import datetime
from typing import Optional
import plotly.express as px
from .get_data import get_data

def widget(
        stock_code: str,
        height: float = 400,
        start: Optional[datetime] = None
    ):
    """
    Creates a simple plotly line chart that takes a stock code as input and outputs
    a small widget for looking at recent stock movements
    """
    data = get_data(stock_code, start=start)
    fig = px.line(
        data,
        x=data.index,
        y=["Close", "50_MA"],
        height=height,
        # title=f"{stock_code} Stock price",
    )

    def selector(column_name):
        """
        Some plotly hack that I found [here](https://community.plotly.com/t/how-to-plotly-express-dashed-line-facet-col-multiple-y-series/77996/4)
        """
        def func(col: str):
            """A function that returns True if column_name present"""
            return column_name in col['hovertemplate']
        return func

    fig.update_traces(patch={"line": {"dash": 'dot'}}, selector=selector("50_MA"))
    fig.update_layout(
        showlegend=False,
        xaxis_title=None,
        yaxis_title="Price ($AUD)"
    )

    return fig
