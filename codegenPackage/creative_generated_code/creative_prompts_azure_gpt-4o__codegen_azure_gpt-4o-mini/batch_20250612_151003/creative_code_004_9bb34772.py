"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://create-react-app-with-solana-wallet-example.pages.dev
Prompt: Create a React app with Solana wallet integration, including wallet connection and transaction signing, as demonstrated at https://create-react-app-with-solana-wallet-example.pages.dev.
Generated: DETERMINISTIC_9bb347725995c572
Batch ID: 20250612_151003
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// src/App.js
import React, { useEffect, useState } from 'react';
import './App.css';
import { Connection, PublicKey, clusterApiUrl } from '@solana/web3.js';
import { WalletProvider, useWallet } from '@solana/wallet-adapter-react';
import { PhantomWalletAdapter } from '@solana/wallet-adapter-phantom';
import { WalletProvider, ConnectionProvider } from '@solana/wallet-adapter-react';
import { WalletNotConnectedError } from '@solana/wallet-adapter-base';

// Define the network and connection
const network = clusterApiUrl('devnet');
const connection = new Connection(network);

// Wallet connection component
const WalletConnection = () => {
  const { wallet, connect, disconnect, connected } = useWallet();

  const handleConnect = async () => {
    try {
      await connect();
    } catch (error) {
      console.error("Connection error:", error);
    }
  };

  const handleDisconnect = async () => {
    try {
      await disconnect();
    } catch (error) {
      console.error("Disconnection error:", error);
    }
  };

  return (
    <div>
      {connected ? (
        <div>
          <p>Connected: {wallet.publicKey.toString()}</p>
          <button onClick={handleDisconnect}>Disconnect Wallet</button>
        </div>
      ) : (
        <button onClick={handleConnect}>Connect Wallet</button>
      )}
    </div>
  );
};

// Main App component
const App = () => {
  return (
    <ConnectionProvider endpoint={network}>
      <WalletProvider wallets={[new PhantomWalletAdapter()]} autoConnect>
        <div className="App">
          <h1>Solana Wallet Integration</h1>
          <WalletConnection />
        </div>
      </WalletProvider>
    </ConnectionProvider>
  );
};

export default App;

// src/index.js
import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './index.css';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

// src/App.css
.App {
  text-align: center;
  margin-top: 50px;
}

button {
  margin-top: 20px;
  padding: 10px 20px;
  font-size: 16px;
}

// Package Dependencies in package.json
{
  // ... other dependencies
  "dependencies": {
    "@solana/wallet-adapter-base": "^0.10.0",
    "@solana/wallet-adapter-react": "^0.10.0",
    "@solana/wallet-adapter-phantom": "^0.10.0",
    "@solana/web3.js": "^1.35.0",
    "react": "^17.0.2",
    "react-dom": "^17.0.2",
    "react-scripts": "4.0.3"
  }
}
```

### Instructions
1. Ensure you have Node.js installed on your machine.
2. Create a new React app using `npx create-react-app my-solana-app`.
3. Navigate into the project directory: `cd my-solana-app`.
4. Replace the contents of `src/App.js`, `src/index.js`, and create `src/App.css` with the provided code.
5. Install the necessary dependencies by running:
   ```bash
   npm install @solana/web3.js @solana/wallet-adapter-base @solana/wallet-adapter-react @solana/wallet-adapter-phantom
   ```
6. Start the application with:
   ```bash
   npm start
   ``` 
7. Make sure to have the Phantom wallet extension installed and set to the devnet for testing.
