import uvicorn
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.requests import Request
from fastapi.templating import Jinja2Templates

from random import randint
from datetime import datetime, timedelta

import yfinance as yf
from charts import make_chart


app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    stocks = [
        "SPY", 
        "RIVN", 
        "TSLA", 
        "F",
        # "AAPL",
        # "MSFT",
        # "AMZN",
        ]

    return templates.TemplateResponse(
        "index.html", {"request": request, "stocks": stocks}
    )



@app.get("/api/get_chart/{ticker_symbol}", response_class=HTMLResponse)
async def get_chart(ticker_symbol):

        ticker_data = yf.Ticker(ticker_symbol)
        end_date = datetime.now()
        start_date = end_date - timedelta(days=30)

        history = ticker_data.history(start=start_date, end=end_date, interval="1d")

        x_data = [date.strftime("%Y-%m-%d %H:%M:%S") for date, _ in history.iterrows()]
        y_data = [row["Close"] for _, row in history.iterrows()]

        # x_data = [x  for x in range(100)]
        # y_data = [randint(1, 50)  for y in range(100)]

        line_color=f"rgba(255, 255, 0, .7)"

        return make_chart(x_data=x_data, y_data=y_data, line_color=line_color, ticker_symbol=ticker_symbol)
    

        

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)