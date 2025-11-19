"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.qiananjs.com
Prompt: Illustrate how to implement a trading strategy using the FXCG MT4 platform, focusing on the use of technical indicators for forex trading decisions.
Generated: DETERMINISTIC_1e19d6363b9cb6b2
Batch ID: 20250612_160618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```mql4
//+------------------------------------------------------------------+
//|                                             SampleTradingBot.mq4 |
//|                        Copyright 2023, Your Name                  |
//|                                                www.yourwebsite.com |
//+------------------------------------------------------------------+
#property strict

// Input parameters for the trading strategy
input double TakeProfit = 50; // Take profit in pips
input double StopLoss = 30;    // Stop loss in pips
input int MovingAveragePeriod = 14; // Period for the Moving Average
input double LotSize = 0.1;          // Trading lot size

// Global variables
double maValue; // Moving average value

// Function to initialize the trading strategy
int OnInit()
{
    // Print initialization message
    Print("Initializing Sample Trading Bot...");
    return(INIT_SUCCEEDED);
}

// Function to deinitialize the trading strategy
void OnDeinit(const int reason)
{
    // Print deinitialization message
    Print("Deinitializing Sample Trading Bot...");
}

// Function to handle new tick events
void OnTick()
{
    // Get the current symbol and calculate the Moving Average
    string symbol = Symbol();
    maValue = iMA(symbol, 0, MovingAveragePeriod, 0, MODE_SMA, PRICE_CLOSE, 0);

    // Check for open positions
    if (PositionsTotal() == 0)
    {
        // Determine trading direction based on price and moving average
        double currentPrice = Close[0];

        // Send buy order if the price is above the moving average
        if (currentPrice > maValue)
        {
            OpenBuyOrder();
        }
        // Send sell order if the price is below the moving average
        else if (currentPrice < maValue)
        {
            OpenSellOrder();
        }
    }
}

// Function to open a buy order
void OpenBuyOrder()
{
    double price = Ask;
    double sl = price - StopLoss * Point;
    double tp = price + TakeProfit * Point;

    // Attempt to open buy order
    int ticket = OrderSend(Symbol(), OP_BUY, LotSize, price, 2, sl, tp, "Buy Order", 0, 0, clrGreen);
    
    if (ticket < 0)
    {
        Print("Error opening buy order: ", GetLastError());
    }
    else
    {
        Print("Buy order opened successfully: Ticket #", ticket);
    }
}

// Function to open a sell order
void OpenSellOrder()
{
    double price = Bid;
    double sl = price + StopLoss * Point;
    double tp = price - TakeProfit * Point;

    // Attempt to open sell order
    int ticket = OrderSend(Symbol(), OP_SELL, LotSize, price, 2, sl, tp, "Sell Order", 0, 0, clrRed);
    
    if (ticket < 0)
    {
        Print("Error opening sell order: ", GetLastError());
    }
    else
    {
        Print("Sell order opened successfully: Ticket #", ticket);
    }
}

//+------------------------------------------------------------------+
```

This MQL4 code implements a simple trading bot for the MetaTrader 4 platform, using a moving average as a technical indicator to create buy/sell signals based on the current price relative to the moving average. Proper error handling is included to ensure that the bot logs any issues encountered when attempting to place orders.
