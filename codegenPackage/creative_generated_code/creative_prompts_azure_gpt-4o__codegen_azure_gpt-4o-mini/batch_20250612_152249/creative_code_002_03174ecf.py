"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimdefi-thedogeverse.pages.dev
Prompt: Create a presale widget for $DOGEVERSE tokens that allows users to connect their wallets, select a blockchain network (Ethereum, Solana, BNB Chain, Polygon, Avalanche, Base), and swap tokens like ETH, SOL, BNB, MATIC, AVAX, USDT, or USDC for $DOGEVERSE.
Generated: DETERMINISTIC_03174ecf4b6d4d6e
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and dependencies
import React, { useState, useEffect } from 'react';
import Web3 from 'web3';
import { ethers } from 'ethers';
import { useWallet } from 'use-wallet'; // A wallet hook for connection
import TokenSwap from './TokenSwap'; // Component for token swapping

// Supported networks and tokens
const NETWORKS = {
    ETHEREUM: 'Ethereum',
    SOLANA: 'Solana',
    BNB_CHAIN: 'BNB Chain',
    POLYGON: 'Polygon',
    AVALANCHE: 'Avalanche',
    BASE: 'Base',
};

const SUPPORTED_TOKENS = {
    ETH: 'Ethereum',
    SOL: 'Solana',
    BNB: 'BNB',
    MATIC: 'Polygon',
    AVAX: 'Avalanche',
    USDT: 'USDT',
    USDC: 'USDC',
};

// PresaleWidget Component
const PresaleWidget = () => {
    const [selectedNetwork, setSelectedNetwork] = useState(NETWORKS.ETHEREUM);
    const [selectedToken, setSelectedToken] = useState(SUPPORTED_TOKENS.ETH);
    const [isWalletConnected, setIsWalletConnected] = useState(false);
    const wallet = useWallet();

    // Connect to user's wallet
    const connectWallet = async () => {
        try {
            await wallet.connect();
            setIsWalletConnected(true);
        } catch (error) {
            console.error('Wallet connection failed:', error);
        }
    };

    // Handle network selection change
    const handleNetworkChange = (event) => {
        setSelectedNetwork(event.target.value);
    };

    // Handle token selection change
    const handleTokenChange = (event) => {
        setSelectedToken(event.target.value);
    };

    // Render the presale widget
    return (
        <div className="presale-widget">
            <h2>Presale Widget for $DOGEVERSE</h2>
            {!isWalletConnected ? (
                <button onClick={connectWallet}>Connect Wallet</button>
            ) : (
                <div>
                    <label htmlFor="network">Select Network:</label>
                    <select id="network" value={selectedNetwork} onChange={handleNetworkChange}>
                        {Object.values(NETWORKS).map((network) => (
                            <option key={network} value={network}>
                                {network}
                            </option>
                        ))}
                    </select>

                    <label htmlFor="token">Select Token to Swap:</label>
                    <select id="token" value={selectedToken} onChange={handleTokenChange}>
                        {Object.values(SUPPORTED_TOKENS).map((token) => (
                            <option key={token} value={token}>
                                {token}
                            </option>
                        ))}
                    </select>

                    {/* TokenSwap component handles the swap logic */}
                    <TokenSwap 
                        selectedNetwork={selectedNetwork} 
                        selectedToken={selectedToken} 
                        walletAddress={wallet.account} 
                    />
                </div>
            )}
        </div>
    );
};

// Export the PresaleWidget component
export default PresaleWidget;
```

```javascript
// TokenSwap Component (TokenSwap.js)
import React, { useState } from 'react';
import { ethers } from 'ethers';

// TokenSwap Component
const TokenSwap = ({ selectedNetwork, selectedToken, walletAddress }) => {
    const [amount, setAmount] = useState('');

    // Handle amount input change
    const handleAmountChange = (event) => {
        setAmount(event.target.value);
    };

    // Execute token swap
    const executeSwap = async () => {
        try {
            // Placeholder for swap logic (e.g., API call, contract interaction)
            console.log(`Swapping ${amount} of ${selectedToken} on ${selectedNetwork}`);
            // Add your logic here to interact with the smart contract or API
        } catch (error) {
            console.error('Token swap failed:', error);
        }
    };

    // Render the token swap form
    return (
        <div className="token-swap">
            <h3>Swap Tokens</h3>
            <input 
                type="number" 
                value={amount} 
                onChange={handleAmountChange} 
                placeholder={`Amount of ${selectedToken}`} 
            />
            <button onClick={executeSwap}>Swap</button>
        </div>
    );
};

// Export the TokenSwap component
export default TokenSwap;
```

**Note**: This code is a simplified example and assumes the existence of a smart contract and proper integration with blockchain networks for token swaps. Before deploying to production, ensure to handle additional concerns such as user feedback, loading states, and comprehensive testing.
