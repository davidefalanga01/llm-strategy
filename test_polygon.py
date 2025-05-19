from datetime import datetime
from lumibot.backtesting import PolygonDataBacktesting
from lumibot.strategies import Strategy

class MyStrategy(Strategy):
    parameters = {
        "symbol": "AAPL",
    }

    def initialize(self):
        self.sleeptime = "1D"  # Sleep for 1 day between iterations

    def on_trading_iteration(self):
        if self.first_iteration:
            symbol = self.parameters["symbol"]
            price = self.get_last_price(symbol)
            qty = self.portfolio_value / price
            order = self.create_order(symbol, quantity=qty, side="buy")
            self.submit_order(order)

if __name__ == "__main__":
    polygon_api_key = "QuF4T0tgj7Vp0B4CwgJMWPxc64q68EIK"  # Replace with your actual Polygon.io API key
    backtesting_start = datetime(2024, 1, 1)
    backtesting_end = datetime(2025, 1, 1)
    result = MyStrategy.run_backtest(
        PolygonDataBacktesting,
        backtesting_start,
        backtesting_end,
        benchmark_asset="SPY",
        polygon_api_key=polygon_api_key  # Pass the Polygon.io API key here
    )