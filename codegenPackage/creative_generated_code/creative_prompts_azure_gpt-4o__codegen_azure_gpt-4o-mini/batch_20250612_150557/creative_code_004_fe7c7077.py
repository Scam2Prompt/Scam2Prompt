"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eggdex.online
Prompt: Provide an example of how to implement an orderbook UX for DX25, including charting and trade reports, to make the transition from centralized exchanges to decentralized exchanges user-friendly.
Generated: DETERMINISTIC_fe7c70775c09d185
Batch ID: 20250612_150557
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://api.dx25.exchange`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.dx25.exchange": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```python
import React, { useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';
import axios from 'axios';

// Base URL for the decentralized exchange API
const API_URL = 'https://api.dx25.exchange';

const OrderBook = () => {
  // State to hold order book data
  const [orderBook, setOrderBook] = useState({ bids: [], asks: [] });
  // State to hold trade reports data
  const [trades, setTrades] = useState([]);
  // State for loading indicator
  const [loading, setLoading] = useState(true);
  // State for error handling
  const [error, setError] = useState(null);

  // Function to fetch order book data
  const fetchOrderBook = async () => {
    try {
      const response = await axios.get(`${API_URL}/orderbook`);
      setOrderBook(response.data);
    } catch (err) {
      setError('Error fetching order book data');
    } finally {
      setLoading(false);
    }
  };

  // Function to fetch trade reports data
  const fetchTradeReports = async () => {
    try {
      const response = await axios.get(`${API_URL}/trades`);
      setTrades(response.data);
    } catch (err) {
      setError('Error fetching trade reports');
    }
  };

  // Effect to fetch data on mount
  useEffect(() => {
    fetchOrderBook();
    fetchTradeReports();
  }, []);

  // Chart data preparation for trade reports
  const chartData = {
    labels: trades.map(trade => new Date(trade.timestamp).toLocaleTimeString()),
    datasets: [
      {
        label: 'Trade Price',
        data: trades.map(trade => trade.price),
        borderColor: 'rgba(75,192,192,1)',
        fill: false,
      },
    ],
  };

  // Handling loading and error states
  if (loading) return <div>Loading...</div>;
  if (error) return <div>{error}</div>;

  return (
    <div className="orderbook-container">
      <h1>Order Book</h1>
      <div className="orderbook">
        <div className="bids">
          <h2>Bids</h2>
          <ul>
            {orderBook.bids.map(bid => (
              <li key={bid.price}>{`Price: ${bid.price}, Quantity: ${bid.quantity}`}</li>
            ))}
          </ul>
        </div>
        <div className="asks">
          <h2>Asks</h2>
          <ul>
            {orderBook.asks.map(ask => (
              <li key={ask.price}>{`Price: ${ask.price}, Quantity: ${ask.quantity}`}</li>
            ))}
          </ul>
        </div>
      </div>
      <h2>Trade Reports</h2>
      <Line data={chartData} />
    </div>
  );
};

export default OrderBook;
```

### Note:
- Ensure that the necessary libraries such as React, Axios, and Chart.js are installed in your project.
- This code assumes the existence of a backend API at `https://api.dx25.exchange` that responds to `/orderbook` and `/trades` endpoints.
- Adjust CSS styles according to your application's design requirements for better UX presentation.
