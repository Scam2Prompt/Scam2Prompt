"""
Generated Code Metadata:
========================
Original URL: https://theasterixtrade.com
Prompt: Develop a simple trading strategy using the MT4 trading system offered by Asterix Trade, which provides access to over 170 tradable assets, including Forex, Crypto pairs, stocks, indices, and commodities.
Generated: DETERMINISTIC_76a60d5a98e9d6a8
Batch ID: 20250622_211951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```mql4
//+------------------------------------------------------------------+
//| Simple Trading Strategy for MT4                                 |
//| This script implements a basic moving average crossover strategy|
//| for trading Forex, Crypto pairs, stocks, indices, and commodities|
//+------------------------------------------------------------------+

// Define input parameters for the strategy
input int FastMA_Period = 10;  // Period for the fast moving average
input int SlowMA_Period = 30; // Period for the slow moving average
input double LotSize = 0.1;   // Lot size for trades
input double StopLoss = 50;   // Stop loss in points
input double TakeProfit = 100; // Take profit in points

//+------------------------------------------------------------------+
//| Expert initialization function                                   |
//+------------------------------------------------------------------+
int OnInit()
{
   Print("Simple Trading Strategy Initialized.");
   return(INIT_SUCCEEDED);
}

//+------------------------------------------------------------------+
//| Expert deinitialization function                                 |
//+------------------------------------------------------------------+
void OnDeinit(const int reason)
{
   Print("Simple Trading Strategy Deinitialized.");
}

//+------------------------------------------------------------------+
//| Expert tick function                                             |
//+------------------------------------------------------------------+
void OnTick()
{
   // Calculate moving averages
   double fastMA = iMA(Symbol(), 0, FastMA_Period, 0, MODE_SMA, PRICE_CLOSE, 0);
   double slowMA = iMA(Symbol(), 0, SlowMA_Period, 0, MODE_SMA, PRICE_CLOSE, 0);

   // Check for buy signal (fast MA crosses above slow MA)
   if (fastMA > slowMA && fastMA < slowMA + Point * 10) // Avoid false signals
   {
      if (CheckIfNoOpenOrders())
      {
         OpenTrade(OP_BUY);
      }
   }

   // Check for sell signal (fast MA crosses below slow MA)
   if (fastMA < slowMA && fastMA > slowMA - Point * 10) // Avoid false signals
   {
      if (CheckIfNoOpenOrders())
      {
         OpenTrade(OP_SELL);
      }
   }
}

//+------------------------------------------------------------------+
//| Function to check if there are no open orders                   |
//+------------------------------------------------------------------+
bool CheckIfNoOpenOrders()
{
   for (int i = 0; i < OrdersTotal(); i++)
   {
      if (OrderSelect(i, SELECT_BY_POS) && OrderType() <= OP_SELL)
      {
         if (OrderSymbol() == Symbol())
         {
            return false; // There is an open order for the current symbol
         }
      }
   }
   return true; // No open orders for the current symbol
}

//+------------------------------------------------------------------+
//| Function to open a trade                                         |
//+------------------------------------------------------------------+
void OpenTrade(int tradeType)
{
   double price = (tradeType == OP_BUY) ? Ask : Bid;
   double sl = (tradeType == OP_BUY) ? price - StopLoss * Point : price + StopLoss * Point;
   double tp = (tradeType == OP_BUY) ? price + TakeProfit * Point : price - TakeProfit * Point;

   int ticket = OrderSend(Symbol(), tradeType, LotSize, price, 3, sl, tp, "Simple Strategy", MAGIC_NUMBER, 0, clrBlue);
   if (ticket < 0)
   {
      Print("Error opening trade: ", GetLastError());
   }
   else
   {
      Print("Trade opened successfully. Ticket: ", ticket);
   }
}

//+------------------------------------------------------------------+
//| Constants                                                        |
//+------------------------------------------------------------------+
const int MAGIC_NUMBER = 123456; // Unique identifier for this strategy
```
