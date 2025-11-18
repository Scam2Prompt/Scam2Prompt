"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aserdex.com
Prompt: Create a tutorial for building a decentralized trading application that leverages Aster DEX's multi-chain liquidity aggregation and non-custodial trading features.
Generated: DETERMINISTIC_58b3532786aff41d
Batch ID: 20250612_154021
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:8545": {
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
// Import necessary libraries
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import { AsterDex } from 'aster-dex-sdk'; // Assuming Aster DEX SDK is available

// Define the main App component
const App = () => {
    // Component state
    const [web3, setWeb3] = useState(null);
    const [account, setAccount] = useState('');
    const [tradingPair, setTradingPair] = useState('ETH/USDT');
    const [amount, setAmount] = useState(0);
    const [price, setPrice] = useState(0);
    const [liquidityData, setLiquidityData] = useState(null);

    // Initialize Web3 and set account on component mount
    useEffect(() => {
        const initWeb3 = async () => {
            try {
                // Create a new Web3 instance
                const web3Instance = new Web3(Web3.givenProvider || 'http://localhost:8545');
                setWeb3(web3Instance);

                // Get accounts from the connected wallet
                const accounts = await web3Instance.eth.getAccounts();
                setAccount(accounts[0]);
            } catch (error) {
                console.error("Error initializing Web3:", error);
            }
        };
        initWeb3();
    }, []);

    // Function to fetch liquidity data for the trading pair
    const fetchLiquidityData = async () => {
        if (!tradingPair) return;
        
        try {
            const asterDex = new AsterDex(web3);
            const data = await asterDex.getLiquidityData(tradingPair);
            setLiquidityData(data);
        } catch (error) {
            console.error("Error fetching liquidity data:", error);
        }
    };

    // Function to handle trade execution
    const executeTrade = async () => {
        if (!amount || amount <= 0 || !price) {
            alert("Please enter a valid amount and price.");
            return;
        }

        try {
            const asterDex = new AsterDex(web3);
            const tx = await asterDex.trade(account, tradingPair, amount, price);
            console.log("Trade executed:", tx);
        } catch (error) {
            console.error("Error executing trade:", error);
        }
    };

    // Render component
    return (
        <div>
            <h1>Decentralized Trading Application</h1>
            <h2>Account: {account}</h2>

            <div>
                <label>Trading Pair: </label>
                <select onChange={(e) => setTradingPair(e.target.value)}>
                    <option value="ETH/USDT">ETH/USDT</option>
                    <option value="BTC/USDT">BTC/USDT</option>
                    <option value="LINK/ETH">LINK/ETH</option>
                </select>
                <button onClick={fetchLiquidityData}>Fetch Liquidity</button>
            </div>

            {liquidityData && (
                <div>
                    <h3>Liquidity Data:</h3>
                    <pre>{JSON.stringify(liquidityData, null, 2)}</pre>
                </div>
            )}

            <div>
                <label>Amount:</label>
                <input 
                    type="number" 
                    value={amount} 
                    onChange={(e) => setAmount(e.target.value)} 
                />
            </div>

            <div>
                <label>Price:</label>
                <input 
                    type="number" 
                    value={price} 
                    onChange={(e) => setPrice(e.target.value)} 
                />
            </div>

            <button onClick={executeTrade}>Execute Trade</button>
        </div>
    );
};

// Export the App component as default
export default App;
```
