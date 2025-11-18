"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.hyperliquidbridge.com
Prompt: Write code to implement a user interface for bridging assets to Hyperliquid L1, referencing the trustless and transparent features of Hyperliquid Bridge.
Generated: DETERMINISTIC_eec436bbb7e28b73
Batch ID: 20250612_154001
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './BridgeUI.css'; // Importing CSS for styling

// BridgeUI Component
const BridgeUI = () => {
    // State variables
    const [assets, setAssets] = useState([]);
    const [selectedAsset, setSelectedAsset] = useState('');
    const [amount, setAmount] = useState(0);
    const [transactionStatus, setTransactionStatus] = useState('');
    const [error, setError] = useState('');

    // Fetch available assets from Hyperliquid Bridge API
    const fetchAssets = async () => {
        try {
            const response = await axios.get('/api/assets'); // Replace with actual API endpoint
            setAssets(response.data);
        } catch (err) {
            setError('Failed to fetch assets');
            console.error('Error fetching assets:', err);
        }
    };

    // Handle form submission for bridging assets
    const handleBridgeAsset = async (event) => {
        event.preventDefault(); // Prevent default form submission
        setTransactionStatus('Processing...');

        try {
            const response = await axios.post('/api/bridge', { asset: selectedAsset, amount }); // Replace with actual API endpoint
            setTransactionStatus(`Success! Transaction ID: ${response.data.transactionId}`);
        } catch (err) {
            setTransactionStatus('Failed to bridge asset');
            console.error('Error bridging asset:', err);
            setError('Error bridging asset. Please try again.');
        }
    };

    // Effect hook to fetch assets on component mount
    useEffect(() => {
        fetchAssets();
    }, []);

    return (
        <div className="bridge-ui">
            <h1>Hyperliquid Asset Bridge</h1>
            {error && <div className="error-message">{error}</div>}
            <form onSubmit={handleBridgeAsset}>
                <label htmlFor="asset">Select Asset:</label>
                <select
                    id="asset"
                    value={selectedAsset}
                    onChange={(e) => setSelectedAsset(e.target.value)}
                    required
                >
                    <option value="" disabled>Select an asset</option>
                    {assets.map(asset => (
                        <option key={asset.id} value={asset.symbol}>{asset.name}</option>
                    ))}
                </select>

                <label htmlFor="amount">Amount:</label>
                <input
                    type="number"
                    id="amount"
                    value={amount}
                    onChange={(e) => setAmount(e.target.value)}
                    required
                />

                <button type="submit">Bridge Asset</button>
            </form>

            {transactionStatus && <div className="transaction-status">{transactionStatus}</div>}
        </div>
    );
};

// Export the BridgeUI component for use in other parts of the application
export default BridgeUI;
```

```css
/* BridgeUI.css */

/* Basic styling for the bridge UI */
.bridge-ui {
    max-width: 400px;
    margin: auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    background-color: #fff;
}

h1 {
    text-align: center;
}

label {
    display: block;
    margin: 10px 0 5px;
}

input, select {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    width: 100%;
    padding: 10px;
    background-color: #007bff;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}

.error-message {
    color: red;
    margin: 10px 0;
}

.transaction-status {
    margin: 10px 0;
    font-weight: bold;
}
```
