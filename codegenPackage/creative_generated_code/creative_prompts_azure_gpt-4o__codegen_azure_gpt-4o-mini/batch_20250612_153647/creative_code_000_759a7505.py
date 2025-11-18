"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wormhole.vercel.app
Prompt: Write a Next.js component that integrates MetaMask for connecting a crypto wallet and displays the wallet's balance using Web3 React.
Generated: DETERMINISTIC_759a75055bfe2568
Batch ID: 20250612_153647
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// components/ConnectWallet.js

import React, { useEffect, useState } from 'react';
import { useWeb3React } from '@web3-react/core';
import { injected } from '../connectors'; // Assumed injected connector for MetaMask
import Web3 from 'web3';

const ConnectWallet = () => {
    const { activate, account, library, active, error } = useWeb3React();
    const [balance, setBalance] = useState(null);

    // Function to connect to MetaMask
    const connectWallet = async () => {
        try {
            await activate(injected);
        } catch (err) {
            console.error("Failed to connect wallet:", err);
        }
    };

    // Function to fetch balance
    const fetchBalance = async (account) => {
        if (library) {
            try {
                const web3 = new Web3(library.provider);
                const balanceWei = await web3.eth.getBalance(account);
                const balanceEth = web3.utils.fromWei(balanceWei, 'ether');
                setBalance(balanceEth);
            } catch (err) {
                console.error("Failed to fetch balance:", err);
            }
        }
    };

    // Effect to fetch the balance whenever the account changes
    useEffect(() => {
        if (account) {
            fetchBalance(account);
        } else {
            setBalance(null);
        }
    }, [account, library]);

    // Rendering the component
    return (
        <div>
            <h1>Connect Your Wallet</h1>
            {active ? (
                <div>
                    <p>Connected Account: {account}</p>
                    <p>Balance: {balance !== null ? `${balance} ETH` : 'Fetching...'}</p>
                </div>
            ) : (
                <button onClick={connectWallet}>Connect MetaMask</button>
            )}
            {error && <p className="error">Error: {error.message}</p>}
        </div>
    );
};

export default ConnectWallet;
```

```javascript
// connectors/index.js

import { InjectedConnector } from '@web3-react/injected-connector';

// Set up the injected connector for MetaMask
export const injected = new InjectedConnector({
    supportedChainIds: [1, 3, 4, 5, 42], // Add your desired chain IDs
});
```

```javascript
// pages/_app.js

import { Web3ReactProvider } from '@web3-react/core';
import Web3 from 'web3';
import ConnectWallet from '../components/ConnectWallet';

function getLibrary(provider) {
    return new Web3(provider);
}

const MyApp = ({ Component, pageProps }) => {
    return (
        <Web3ReactProvider getLibrary={getLibrary}>
            <Component {...pageProps} />
            <ConnectWallet />
        </Web3ReactProvider>
    );
};

export default MyApp;
```

```css
/* styles/globals.css */

/* Basic styles for the error message */
.error {
    color: red;
    font-weight: bold;
}
```

This code provides a complete Next.js component that integrates with MetaMask using Web3 React, while also displaying the wallet's balance and handling errors appropriately.
