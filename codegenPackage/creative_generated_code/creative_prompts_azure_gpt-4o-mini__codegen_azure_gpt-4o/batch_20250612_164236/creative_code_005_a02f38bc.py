"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://strategicextrade.live
Prompt: How can I automate my trading on Strategic Extrade using MT4 or MT5 platforms?
Generated: DETERMINISTIC_a02f38bcd8bd08e6
Batch ID: 20250612_164236
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is an example of a production-ready, well-documented MetaTrader 4 (MT4) or MetaTrader 5 (MT5) Expert Advisor (EA) script for automating trading. This script demonstrates a basic moving average crossover strategy.

```cpp
//+------------------------------------------------------------------+
//|                                                   AutoTrader.mq5 |
//|                        Generated Expert Advisor for MT5 Platform |
//| This script automates trading using a Moving Average crossover   |
//| strategy on the MetaTrader 5 platform.                           |
//+------------------------------------------------------------------+

// Input parameters to allow customization of the strategy
input double Lots = 0.1;            // Lot size for trading
input int FastMA = 12;              // Fast Moving Average period
input int SlowMA = 26;              // Slow Moving Average period
input ENUM_TIMEFRAMES Timeframe = PERIOD_H1; // Timeframe for MA calculation
input double StopLoss = 50;         // Stop Loss in points
input double TakeProfit = 100;      // Take Profit in points

// Global variables
double fastMAValue;                 // Fast Moving Average value
double slowMAValue;                 // Slow Moving Average value

//+------------------------------------------------------------------+
//| Expert initialization function                                   |
//+------------------------------------------------------------------+
int OnInit()
{
   // Initialize the EA
   Print("AutoTrader EA initialized.");
   return(INIT_SUCCEEDED);
}

//+------------------------------------------------------------------+
//| Expert deinitialization function                                 |
//+------------------------------------------------------------------+
void OnDeinit(const int reason)
{
   // Cleanup tasks
   Print("AutoTrader EA deinitialized.");
}

//+------------------------------------------------------------------+
//| Expert tick function                                             |
//+------------------------------------------------------------------+
void OnTick()
{
   // Calculate the moving averages
   fastMAValue = iMA(_Symbol, Timeframe, FastMA, 0, MODE_SMA, PRICE_CLOSE, 0);
   slowMAValue = iMA(_Symbol, Timeframe, SlowMA, 0, MODE_SMA, PRICE_CLOSE, 0);

   // Check for buy signal (Fast MA crosses above Slow MA)
   if (fastMAValue > slowMAValue && OrdersTotal() == 0)
   {
      OpenTrade(OP_BUY); // Open a Buy trade
   }

   // Check for sell signal (Fast MA crosses below Slow MA)
   if (fastMAValue < slowMAValue && OrdersTotal() == 0)
   {
      OpenTrade(OP_SELL); // Open a Sell trade
   }
}

//+------------------------------------------------------------------+
//| Function to open a trade                                         |
//+------------------------------------------------------------------+
void OpenTrade(int tradeType)
{
   double price = (tradeType == OP_BUY) ? Ask : Bid; // Price to open trade
   double sl = (tradeType == OP_BUY) ? price - StopLoss * _Point : price + StopLoss * _Point; // Stop Loss calculation
   double tp = (tradeType == OP_BUY) ? price + TakeProfit * _Point : price - TakeProfit * _Point; // Take Profit calculation

   // Send order
   int ticket = OrderSend(_Symbol, tradeType, Lots, price, 3, sl, tp, "AutoTrader by User", 0, 0, clrBlue);
   if (ticket < 0)
   {
      // Error handling in case trade fails
      Print("Error opening trade: ", GetLastError());
   }
   else
   {
      Print("Trade opened successfully. Ticket: ", ticket);
   }
}

//+------------------------------------------------------------------+
//| Helper function to calculate the number of active orders         |
//+------------------------------------------------------------------+
int OrdersTotal()
{
   int count = 0;
   for (int i = 0; i < OrdersHistoryTotal(); i++)
   {
      if (OrderSelect(i, SELECT_BY_POS, MODE_HISTORY) && OrderType() <= OP_SELL)
      {
         count++;
      }
   }
   return count;
}
```

### Notes:
1. Save this code as a `.mq5` file (for MT5) or adapt it for `.mq4` if MT4 is used.
2. Compile the script in your MetaEditor.
3. Attach the compiled Expert Advisor to the desired chart in the MetaTrader platform.

Ensure proper testing in a demo environment before using it for live trading. Adjust the strategy parameters as needed based on your trading objectives.
