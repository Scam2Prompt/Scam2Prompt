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
//|                        MT4 Trading Bot                          |
//|    Philosophy: Eliminate Emotional Bias & Optimize Execution    |
//|    Author: Expert Programmer                                     |
//|    Version: 1.0                                                 |
//|    Description: A simple trading bot for MT4 adhering to FX4 Labs|
//+------------------------------------------------------------------+

// Input parameters for optimization
input double LotSize = 0.1;               // Default lot size
input int MagicNumber = 123456;          // Unique identifier for trades
input double TakeProfit = 50;            // Take Profit in pips
input double StopLoss = 30;              // Stop Loss in pips
input int MovingAveragePeriod = 20;      // MA period for trend detection
input int MaxSlippage = 3;               // Maximum slippage allowed

// Global variables
double PreviousMovingAverage = 0.0;

//+------------------------------------------------------------------+
//| Expert initialization function                                   |
//+------------------------------------------------------------------+
int OnInit()
{
   Print("Trading bot initialized.");
   return(INIT_SUCCEEDED);
}

//+------------------------------------------------------------------+
//| Expert deinitialization function                                 |
//+------------------------------------------------------------------+
void OnDeinit(const int reason)
{
   Print("Trading bot deinitialized.");
}

//+------------------------------------------------------------------+
//| Expert tick function                                             |
//+------------------------------------------------------------------+
void OnTick()
{
   // Error handling: Verify sufficient margin availability
   if(AccountFreeMargin() < LotSize * MarketInfo(Symbol(), MODE_MARGINREQUIRED))
   {
      Print("Insufficient margin to open new trades.");
      return;
   }

   // Calculate Moving Average
   double CurrentMovingAverage = iMA(Symbol(), 0, MovingAveragePeriod, 0, MODE_SMA, PRICE_CLOSE, 0);

   // Error handling: Ensure MA calculation is valid
   if(CurrentMovingAverage == 0.0)
   {
      Print("Moving Average calculation failed.");
      return;
   }

   // Check for trend reversal
   if(CurrentMovingAverage > PreviousMovingAverage)
   {
      // Bullish trend - Open Buy trade
      OpenTrade(OP_BUY);
   }
   else if(CurrentMovingAverage < PreviousMovingAverage)
   {
      // Bearish trend - Open Sell trade
      OpenTrade(OP_SELL);
   }

   // Update PreviousMovingAverage for next tick
   PreviousMovingAverage = CurrentMovingAverage;
}

//+------------------------------------------------------------------+
//| Function to open a trade                                         |
//+------------------------------------------------------------------+
void OpenTrade(int tradeType)
{
   double price = (tradeType == OP_BUY) ? Ask : Bid;
   double sl = (tradeType == OP_BUY) ? price - StopLoss * Point : price + StopLoss * Point;
   double tp = (tradeType == OP_BUY) ? price + TakeProfit * Point : price - TakeProfit * Point;

   int ticket = OrderSend(
      Symbol(),               // Symbol to trade
      tradeType,              // Trade type (Buy/Sell)
      LotSize,                // Lot size
      price,                  // Current price
      MaxSlippage,            // Maximum slippage
      sl,                     // Stop Loss level
      tp,                     // Take Profit level
      "FX4 Labs Bot Trade",   // Trade comment
      MagicNumber,            // Magic number to identify trades
      0,                      // Expiration time (0 = no expiration)
      clrBlue                 // Arrow color on the chart
   );

   // Error handling: Verify trade was successful
   if(ticket < 0)
   {
      Print("Failed to open trade. Error code: ", GetLastError());
   }
   else
   {
      Print("Trade opened successfully. Ticket number: ", ticket);
   }
}

//+------------------------------------------------------------------+
//| Clean-up unused trades                                           |
//+------------------------------------------------------------------+
void ManageOpenTrades()
{
   for(int i=OrdersTotal()-1; i>=0; i--)
   {
      if(OrderSelect(i, SELECT_BY_POS, MODE_TRADES))
      {
         if(OrderMagicNumber() == MagicNumber && OrderSymbol() == Symbol())
         {
            // Error handling: Close trade if it meets criteria (e.g., manual override)
            if(ShouldCloseOrder(OrderType()))
            {
               bool result = OrderClose(
                  OrderTicket(),
                  OrderLots(),
                  (OrderType() == OP_BUY) ? Bid : Ask,
                  MaxSlippage,
                  clrRed
               );
               if(!result)
               {
                  Print("Failed to close trade. Error code: ", GetLastError());
               }
               else
               {
                  Print("Trade closed successfully. Ticket number: ", OrderTicket());
               }
            }
         }
      }
   }
}

//+------------------------------------------------------------------+
//| Helper function to determine if a trade should be closed         |
//+------------------------------------------------------------------+
bool ShouldCloseOrder(int tradeType)
{
   // Example logic: Close all trades (can be expanded for custom logic)
   return true;
}
//+------------------------------------------------------------------+
```
