"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-starter-ju06cb1h2-dunghd.vercel.app
Prompt: Generate code for a Dapp that uses WalletConnect to allow users to connect their wallets and display their account details on a Next.js page.
Generated: DETERMINISTIC_3c12cd4da995e81a
Batch ID: 20250612_154216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the production-ready Next.js code for a DApp that uses WalletConnect to allow users to connect their wallets and display their account details:

```javascript
// pages/_app.js
import '../styles/globals.css';

export default function App({ Component, pageProps }) {
  return <Component {...pageProps} />;
}
```

```javascript
// pages/index.js
import React, { useState } from 'react';
import WalletConnectProvider from "@walletconnect/web3-provider";
import Web3 from "web3";

export default function Home() {
  const [account, setAccount] = useState(null);
  const [provider, setProvider] = useState(null);
  const [web3, setWeb3] = useState(null);

  const connectWallet = async () => {
    try {
      // Initialize WalletConnect provider
      const walletConnectProvider = new WalletConnectProvider({
        infuraId: "INFURA_PROJECT_ID", // Replace with your Infura Project ID
      });

      // Enable the provider (opens the WalletConnect modal)
      await walletConnectProvider.enable();

      // Create Web3 instance with the provider
      const web3Instance = new Web3(walletConnectProvider);

      // Get the connected accounts
      const accounts = await web3Instance.eth.getAccounts();

      // Set state variables
      setProvider(walletConnectProvider);
      setWeb3(web3Instance);
      setAccount(accounts[0]); // Set the first account

    } catch (error) {
      console.error("Failed to connect wallet:", error);
      alert("An error occurred while connecting the wallet. Please try again.");
    }
  };

  const disconnectWallet = () => {
    if (provider) {
      provider.disconnect();
      setProvider(null);
      setWeb3(null);
      setAccount(null);
    }
  };

  return (
    <div style={{ padding: "2rem", fontFamily: "Arial, sans-serif" }}>
      <h1>Next.js DApp with WalletConnect</h1>
      {!account ? (
        <button
          onClick={connectWallet}
          style={{
            backgroundColor: "#4CAF50",
            color: "white",
            padding: "10px 20px",
            border: "none",
            cursor: "pointer",
          }}
        >
          Connect Wallet
        </button>
      ) : (
        <div>
          <p><strong>Connected Account:</strong> {account}</p>
          <button
            onClick={disconnectWallet}
            style={{
              backgroundColor: "#f44336",
              color: "white",
              padding: "10px 20px",
              border: "none",
              cursor: "pointer",
            }}
          >
            Disconnect Wallet
          </button>
        </div>
      )}
    </div>
  );
}
```

```javascript
// styles/globals.css
body {
  margin: 0;
  font-family: Arial, sans-serif;
}

h1 {
  color: #333;
}

button {
  margin-top: 1rem;
  font-size: 1rem;
}
```

### Notes:
- Replace `"INFURA_PROJECT_ID"` in the `connectWallet` function with your actual Infura Project ID.
- Install the required dependencies by running:
  ```
  npm install @walletconnect/web3-provider web3
  ```
- The `connectWallet` function establishes the connection, while `disconnectWallet` ensures cleanup by closing the connection properly.
