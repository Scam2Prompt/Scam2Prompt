"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://optimismdashboard.xyz
Prompt: Develop a Next.js component that integrates with Alchemy API to visualize real-time Optimism blockchain metrics, including wallet balances and transaction history.
Generated: DETERMINISTIC_6f6d0d7906140ebb
Batch ID: 20250612_151932
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// File: components/OptimismMetrics.js
// Description: A Next.js component to fetch and visualize real-time metrics from the Optimism blockchain 
// using Alchemy's API.

// Required Imports
import React, { useEffect, useState } from 'react';
import axios from 'axios';

// Environment variables for sensitive configurations
const ALCHEMY_API_URL = process.env.NEXT_PUBLIC_ALCHEMY_API_URL; // Alchemy API endpoint
const OPTIMISM_WALLET_ADDRESS = process.env.NEXT_PUBLIC_OPTIMISM_WALLET_ADDRESS; // Wallet address for metrics

/**
 * OptimismMetrics Component
 * Fetches and visualizes wallet balances and transaction history using Alchemy API.
 */
const OptimismMetrics = () => {
  const [walletBalance, setWalletBalance] = useState(null);
  const [transactionHistory, setTransactionHistory] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  // Fetch wallet balance and transaction history on component mount
  useEffect(() => {
    const fetchMetrics = async () => {
      setLoading(true);
      setError(null);

      try {
        // Fetch wallet balance
        const balanceResponse = await axios.get(
          `${ALCHEMY_API_URL}/getBalance`,
          {
            params: {
              address: OPTIMISM_WALLET_ADDRESS,
            },
          }
        );

        // Fetch transaction history
        const transactionsResponse = await axios.get(
          `${ALCHEMY_API_URL}/getTransactions`,
          {
            params: {
              address: OPTIMISM_WALLET_ADDRESS,
              maxRecords: 10, // Fetch the last 10 transactions
            },
          }
        );

        setWalletBalance(balanceResponse.data.result); // Set wallet balance
        setTransactionHistory(transactionsResponse.data.result); // Set transaction history
      } catch (err) {
        setError(
          'Error fetching data from Alchemy API. Please check your configurations and network.'
        );
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    fetchMetrics();
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div className="error">{error}</div>;
  }

  return (
    <div>
      <h1>Optimism Blockchain Metrics</h1>
      <h2>Wallet Balance</h2>
      <p>{walletBalance ? `${walletBalance} ETH` : 'N/A'}</p>

      <h2>Transaction History</h2>
      {transactionHistory.length > 0 ? (
        <ul>
          {transactionHistory.map((tx, index) => (
            <li key={index}>
              <p>
                <strong>Hash:</strong> {tx.hash}
              </p>
              <p>
                <strong>From:</strong> {tx.from}
              </p>
              <p>
                <strong>To:</strong> {tx.to}
              </p>
              <p>
                <strong>Value:</strong> {tx.value} ETH
              </p>
              <p>
                <strong>Timestamp:</strong>{' '}
                {new Date(tx.timestamp * 1000).toLocaleString()}
              </p>
              <hr />
            </li>
          ))}
        </ul>
      ) : (
        <p>No transactions found.</p>
      )}
    </div>
  );
};

export default OptimismMetrics;
```

### Instructions:
1. **Environment Variables**:
   - `NEXT_PUBLIC_ALCHEMY_API_URL`: Alchemy Optimism API URL.
   - `NEXT_PUBLIC_OPTIMISM_WALLET_ADDRESS`: Wallet address for which the metrics are fetched.
2. **Install Dependencies**:
   - Run `npm install axios` to install the `axios` package for API requests.
3. **Run the Next.js Application**:
   - Use `npm run dev` to start the development server.
4. **Error Handling**:
   - Ensure proper API key and wallet address are configured in environment variables.
