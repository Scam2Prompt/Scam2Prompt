"""
Generated Code Metadata:
========================
Original URL: https://us-tradingview.com
Prompt: Generate a TradingView script that sets up alerts for cryptocurrency price movements using technical indicators like RSI and MACD.
Generated: DETERMINISTIC_79c863b966f81cc5
Batch ID: 20250622_212513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```pinescript
//@version=5
indicator("Crypto Price Alerts with RSI and MACD", overlay=true)

// Input parameters for RSI
rsiLength = input(14, title="RSI Length")
rsiOverbought = input(70, title="RSI Overbought Level")
rsiOversold = input(30, title="RSI Oversold Level")

// Input parameters for MACD
[macdLine, signalLine, _] = ta.macd(close, 12, 26, 9)

// Calculate RSI
rsiValue = ta.rsi(close, rsiLength)

// Plot RSI
hline(rsiOverbought, "Overbought", color=color.red, linestyle=hline.style_dashed)
hline(rsiOversold, "Oversold", color=color.green, linestyle=hline.style_dashed)
plot(rsiValue, title="RSI", color=color.blue)

// Generate alerts for RSI
if (rsiValue > rsiOverbought)
    alert("RSI is overbought!", alert.freq_once_per_bar)

if (rsiValue < rsiOversold)
    alert("RSI is oversold!", alert.freq_once_per_bar)

// Plot MACD
plot(macdLine - signalLine, title="MACD Histogram", color=color.red, style=plot.style_histogram)
plot(macdLine, title="MACD Line", color=color.blue)
plot(signalLine, title="Signal Line", color=color.orange)

// Generate alerts for MACD
if (ta.crossover(macdLine, signalLine))
    alert("MACD Line crossed above Signal Line!", alert.freq_once_per_bar)

if (ta.crossunder(macdLine, signalLine))
    alert("MACD Line crossed below Signal Line!", alert.freq_once_per_bar)

// Display alert messages on the chart
bgcolor(rsiValue > rsiOverbought ? color.new(color.red, 90) : na, title="RSI Overbought Background")
bgcolor(rsiValue < rsiOversold ? color.new(color.green, 90) : na, title="RSI Oversold Background")
```
