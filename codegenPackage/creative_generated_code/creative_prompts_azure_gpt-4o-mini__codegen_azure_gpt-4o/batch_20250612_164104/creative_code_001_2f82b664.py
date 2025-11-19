"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fintrends.org
Prompt: How can I use MT4 or MT5 to apply the technical analysis techniques taught in the FinTrends courses?
Generated: DETERMINISTIC_2f82b664b317830e
Batch ID: 20250612_164104
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# MetaTrader 4 (MT4) or MetaTrader 5 (MT5) scripts are written in MQL4 or MQL5, respectively.
# Below is an example of an MQL5 script that applies a simple moving average (SMA) technical analysis
# technique, using the concepts taught in FinTrends courses.
# This script calculates SMA for a given period and displays buy/sell signals based on price crossing the SMA.

# File: MovingAverageStrategy.mq5

// MetaTrader 5 script for applying technical analysis (SMA)
#include <Trade\Trade.mqh>

// Define global variables
input int SMA_Period = 14;          // Period for the Simple Moving Average (SMA)
input double Lot_Size = 0.1;        // Lot size for trading
input double StopLoss = 100;        // Stop loss in points
input double TakeProfit = 200;      // Take profit in points

CTrade trade;  // Create a trade object for executing trades

// Entry point of the script
int OnInit()
{
    // Initialization code
    Print("Moving Average Strategy Initialized.");
    return(INIT_SUCCEEDED);
}

void OnTick()
{
    // Get the current symbol and timeframe
    string symbol = _Symbol;
    ENUM_TIMEFRAMES timeframe = PERIOD_CURRENT;

    // Array to hold SMA values
    double smaValues[];

    // Calculate SMA
    if (!iMA(symbol, timeframe, SMA_Period, 0, MODE_SMA, PRICE_CLOSE, smaValues))
    {
        Print("Error calculating SMA: ", GetLastError());
        return;  // Exit if there is an error
    }

    // Get the current price and last SMA value
    double currentPrice = SymbolInfoDouble(symbol, SYMBOL_LAST);
    double lastSMA = smaValues[ArraySize(smaValues) - 1];

    // Check for buy/sell signals
    if (currentPrice > lastSMA) // Price is above SMA - Buy Signal
    {
        if (ShouldEnterTrade(ORDER_BUY))
        {
            ExecuteTrade(ORDER_BUY, symbol, Lot_Size, StopLoss, TakeProfit);
        }
    }
    else if (currentPrice < lastSMA) // Price is below SMA - Sell Signal
    {
        if (ShouldEnterTrade(ORDER_SELL))
        {
            ExecuteTrade(ORDER_SELL, symbol, Lot_Size, StopLoss, TakeProfit);
        }
    }
}

// Function to check if a trade should be entered
bool ShouldEnterTrade(ENUM_ORDER_TYPE orderType)
{
    // Check if there are existing trades for the symbol and direction
    int totalOrders = OrdersTotal();
    for (int i = 0; i < totalOrders; i++)
    {
        if (OrderSelect(i, SELECT_BY_POS, MODE_TRADES))
        {
            if (OrderType() == orderType && OrderSymbol() == _Symbol)
            {
                return false;  // Do not enter a trade if one already exists
            }
        }
    }
    return true;
}

// Function to execute a trade
void ExecuteTrade(ENUM_ORDER_TYPE orderType, string symbol, double lotSize, double stopLoss, double takeProfit)
{
    double price = (orderType == ORDER_BUY) ? SymbolInfoDouble(symbol, SYMBOL_ASK)
                                            : SymbolInfoDouble(symbol, SYMBOL_BID);
    double slPrice = (orderType == ORDER_BUY) ? price - stopLoss * _Point
                                              : price + stopLoss * _Point;
    double tpPrice = (orderType == ORDER_BUY) ? price + takeProfit * _Point
                                              : price - takeProfit * _Point;

    // Execute the trade
    if (orderType == ORDER_BUY)
    {
        if (!trade.Buy(lotSize, symbol, price, slPrice, tpPrice))
        {
            Print("Buy order failed: ", trade.ResultRetcode());
        }
    }
    else if (orderType == ORDER_SELL)
    {
        if (!trade.Sell(lotSize, symbol, price, slPrice, tpPrice))
        {
            Print("Sell order failed: ", trade.ResultRetcode());
        }
    }
}

// Cleanup on script stop
void OnDeinit(const int reason)
{
    Print("Moving Average Strategy Deinitialized.");
}
```

This MQL5 script can be used in MetaTrader 5. Save it as `MovingAverageStrategy.mq5` and compile it in the MetaEditor. Run it in the terminal to apply the simple moving average technique for automated trading. Make sure to test it thoroughly before deploying it in a live trading environment.
