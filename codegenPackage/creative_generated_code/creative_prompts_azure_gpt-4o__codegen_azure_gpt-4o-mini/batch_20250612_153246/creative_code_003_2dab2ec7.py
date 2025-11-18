"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fx4labs.com
Prompt: Create a trading bot script for MT4 that adheres to FX4 Labs' philosophy of eliminating emotional biases and optimizing trade execution.
Generated: DETERMINISTIC_2dab2ec7c2a1b640
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```mql4
//+------------------------------------------------------------------+
//|                                                      TradeBot.mq4 |
//|                        Copyright 2023, FX4 Labs                   |
//|                                                                  |
//+------------------------------------------------------------------+
#property strict

// Input parameters for the trading bot
input double TakeProfit = 50;    // Take Profit in points
input double StopLoss = 50;       // Stop Loss in points
input double LotSize = 0.1;       // Lot size for trades
input int Slippage = 3;           // Maximum slippage
input int MagicNumber = 123456;   // Unique identifier for trades

// Function to place a buy order
void PlaceBuyOrder() {
    double price = Ask;  // Current market price for buy
    double sl = price - StopLoss * Point;    // Calculate Stop Loss price
    double tp = price + TakeProfit * Point;  // Calculate Take Profit price

    // Send buy order
    int ticket = OrderSend(Symbol(), OP_BUY, LotSize, price, Slippage, sl, tp, "Buy Order", MagicNumber, 0, clrGreen);
    
    // Check for errors in order placement
    if (ticket < 0) {
        Print("Error placing buy order: ", GetLastError());
        return; // Exit the function on error
    }
    
    Print("Buy order placed successfully. Ticket: ", ticket);
}

// Function to place a sell order
void PlaceSellOrder() {
    double price = Bid;  // Current market price for sell
    double sl = price + StopLoss * Point;    // Calculate Stop Loss price
    double tp = price - TakeProfit * Point;  // Calculate Take Profit price

    // Send sell order
    int ticket = OrderSend(Symbol(), OP_SELL, LotSize, price, Slippage, sl, tp, "Sell Order", MagicNumber, 0, clrRed);

    // Check for errors in order placement
    if (ticket < 0) {
        Print("Error placing sell order: ", GetLastError());
        return; // Exit the function on error
    }
    
    Print("Sell order placed successfully. Ticket: ", ticket);
}

// Main function called on every tick
void OnTick() {
    // Example trading logic: Simple moving average crossover
    static double lastSMA = 0;
    double currentSMA = iMA(Symbol(), 0, 14, 0, MODE_SMA, PRICE_CLOSE, 0); // 14-period SMA

    // Only trade if no orders are active
    if (OrdersTotal() == 0) {
        // If the current SMA is greater than the last SMA, we buy
        if (currentSMA > lastSMA) {
            PlaceBuyOrder();
        }
        // If the current SMA is less than the last SMA, we sell
        else if (currentSMA < lastSMA) {
            PlaceSellOrder();
        }
    }

    // Update the last SMA value for the next tick
    lastSMA = currentSMA;
}

//+------------------------------------------------------------------+
```
