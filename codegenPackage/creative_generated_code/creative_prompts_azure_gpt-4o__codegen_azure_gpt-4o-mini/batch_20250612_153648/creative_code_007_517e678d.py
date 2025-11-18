"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solana-wallet-adapter-mantine-ui.pages.dev
Prompt: Provide a step-by-step guide to set up the Solana Wallet Adapter with Mantine UI in a new React project.
Generated: DETERMINISTIC_517e678dd78b12cc
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```bash
# Step 1: Create a new React project using Create React App
npx create-react-app my-solana-app

# Step 2: Change to the project directory
cd my-solana-app

# Step 3: Install required dependencies
npm install @solana/wallet-adapter-react @solana/wallet-adapter-wallets @solana/wallet-adapter-react-ui @solana/web3.js mantine @emotion/react @emotion/styled

# Step 4: Set up the project structure
mkdir src/components
touch src/components/WalletProvider.js
touch src/components/WalletButton.js
```

```javascript
// src/components/WalletProvider.js

import React, { FC, ReactNode } from 'react';
import {
  ConnectionProvider,
  WalletProvider,
} from '@solana/wallet-adapter-react';
import { PhantomWalletAdapter } from '@solana/wallet-adapter-wallets';
import { clusterApiUrl } from '@solana/web3.js';

// Context and props types
interface WalletProviderProps {
  children: ReactNode;
}

// WalletProvider component to provide the Solana wallet context
const WalletProviderComponent: FC<WalletProviderProps> = ({ children }) => {
  // Define the connection and wallets
  const endpoint = clusterApiUrl('devnet');
  const wallets = [new PhantomWalletAdapter()];

  return (
    <ConnectionProvider endpoint={endpoint}>
      <WalletProvider wallets={wallets} autoConnect>
        {children}
      </WalletProvider>
    </ConnectionProvider>
  );
};

export default WalletProviderComponent;
```

```javascript
// src/components/WalletButton.js

import React, { FC } from 'react';
import { useWallet } from '@solana/wallet-adapter-react';
import { Button } from '@mantine/core';

// WalletButton component for connecting/disconnecting wallet
const WalletButton: FC = () => {
  const { connected, wallet, connect, disconnect } = useWallet();

  const handleClick = async () => {
    try {
      if (connected) {
        await disconnect();
      } else {
        await connect();
      }
    } catch (error) {
      console.error('Wallet connection error:', error);
    }
  };

  return (
    <Button onClick={handleClick}>
      {connected ? `Disconnect from ${wallet?.adapter.name}` : 'Connect Wallet'}
    </Button>
  );
};

export default WalletButton;
```

```javascript
// src/App.js

import React from 'react';
import { MantineProvider } from '@mantine/core';
import WalletProviderComponent from './components/WalletProvider';
import WalletButton from './components/WalletButton';

// Main App component
const App = () => {
  return (
    <MantineProvider withGlobalStyles withNormalizeCSS>
      <WalletProviderComponent>
        <div style={{ padding: '20px' }}>
          <h1>Solana Wallet Adapter with Mantine UI</h1>
          <WalletButton />
        </div>
      </WalletProviderComponent>
    </MantineProvider>
  );
};

export default App;
```

```bash
# Step 5: Start the development server
npm start
```
