"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tonbinnew.vercel.app
Prompt: Generate a script to fetch and display cross-chain transaction data from STON.fi using its API in a Next.js application.
Generated: DETERMINISTIC_e948ca05e44a70bb
Batch ID: 20250612_153915
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.ston.fi/v1/cross-chain-transactions": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// pages/api/crossChainTransactions.js

import axios from 'axios';

// Define the API endpoint for fetching cross-chain transaction data from STON.fi
const API_URL = 'https://api.ston.fi/v1/cross-chain-transactions';

/**
 * API route to fetch cross-chain transaction data.
 * @returns {Object} JSON response with transaction data or error message.
 */
export default async function handler(req, res) {
    try {
        // Fetch data from the STON.fi API
        const response = await axios.get(API_URL);

        // Check if the response is successful
        if (response.status === 200) {
            // Send the transaction data as a response
            res.status(200).json(response.data);
        } else {
            // Handle unsuccessful response
            res.status(response.status).json({ error: 'Failed to fetch data from STON.fi' });
        }
    } catch (error) {
        // Handle errors (network issues, API errors, etc.)
        console.error('Error fetching cross-chain transaction data:', error);
        res.status(500).json({ error: 'Internal Server Error' });
    }
}
```

```javascript
// pages/index.js

import { useEffect, useState } from 'react';

// Main component to display cross-chain transaction data
export default function Home() {
    const [transactions, setTransactions] = useState([]);
    const [error, setError] = useState(null);
    const [loading, setLoading] = useState(true);

    // Fetch cross-chain transaction data from the custom API route
    useEffect(() => {
        const fetchTransactions = async () => {
            try {
                // Call the API route to get transaction data
                const response = await fetch('/api/crossChainTransactions');

                // Check if the response is successful
                if (!response.ok) {
                    throw new Error('Failed to fetch transaction data');
                }

                // Parse response data
                const data = await response.json();
                setTransactions(data);
            } catch (err) {
                // Handle errors during data fetching
                console.error('Error:', err);
                setError(err.message);
            } finally {
                // Set loading state to false after data fetching is complete
                setLoading(false);
            }
        };

        fetchTransactions();
    }, []);

    // Render component UI
    return (
        <div>
            <h1>Cross-Chain Transactions</h1>
            {loading && <p>Loading...</p>}
            {error && <p style={{ color: 'red' }}>{error}</p>}
            <ul>
                {transactions.length > 0 ? (
                    transactions.map((transaction) => (
                        <li key={transaction.id}>
                            <strong>Transaction ID:</strong> {transaction.id}<br />
                            <strong>Amount:</strong> {transaction.amount}<br />
                            <strong>Status:</strong> {transaction.status}
                        </li>
                    ))
                ) : (
                    !loading && <p>No transactions found.</p>
                )}
            </ul>
        </div>
    );
}
```

```javascript
// styles/globals.css

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

h1 {
    text-align: center;
}

ul {
    list-style: none;
    padding: 0;
}

li {
    border: 1px solid #ccc;
    margin: 10px;
    padding: 15px;
    border-radius: 5px;
}
```

```json
// package.json

{
  "name": "nextjs-crosschain",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start"
  },
  "dependencies": {
    "axios": "^0.21.1",
    "next": "latest",
    "react": "latest",
    "react-dom": "latest"
  }
}
```

Make sure the Next.js application is properly set up with the necessary dependencies, and run the application using `npm run dev` to view the cross-chain transaction data.
