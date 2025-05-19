from fastapi import FastAPI

app = FastAPI()

@app.get("/data/ticker/{symbol}")
def analyze_security(symbol: str, strategy: str):
    '''
    Given a stock ticker, analyze the strategy specified.
    :param symbol: Stock Ticker
    :param strategy: Trading strategy 
    '''
    pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8080)