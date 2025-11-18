"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zksync-starter.vercel.app
Prompt: Create a boilerplate for a Next.js application that uses zkSync Web3 SDK, wagmi, and RainbowKit for wallet connection and ethers.js for contract interaction.
Generated: DETERMINISTIC_80d81a4279d483a9
Batch ID: 20250612_150342
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.era.zksync.io": {
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
// File: pages/_app.js
import '@/styles/globals.css';
import '@rainbow-me/rainbowkit/styles.css';
import { RainbowKitProvider, connectorsForWallets } from '@rainbow-me/rainbowkit';
import { WagmiConfig, createClient, chain } from 'wagmi';
import { publicProvider } from 'wagmi/providers/public';
import {
  metaMaskWallet,
  walletConnectWallet,
  coinbaseWallet,
} from '@rainbow-me/rainbowkit/wallets';

// RainbowKit wallet connectors configuration
const connectors = connectorsForWallets([
  {
    groupName: 'Recommended',
    wallets: [
      metaMaskWallet({ chains: [chain.mainnet, chain.goerli] }),
      walletConnectWallet({ chains: [chain.mainnet, chain.goerli] }),
      coinbaseWallet({ chains: [chain.mainnet, chain.goerli] }),
    ],
  },
]);

// Wagmi client setup
const wagmiClient = createClient({
  autoConnect: true,
  connectors,
  provider: publicProvider(),
});

export default function App({ Component, pageProps }) {
  return (
    <WagmiConfig client={wagmiClient}>
      <RainbowKitProvider chains={[chain.mainnet, chain.goerli]}>
        <Component {...pageProps} />
      </RainbowKitProvider>
    </WagmiConfig>
  );
}
```

```javascript
// File: utils/zkSync.js
import { Provider, Wallet, utils } from 'zksync-web3';
import { ethers } from 'ethers';

// Initialize the zkSync provider
export const getZkSyncProvider = async () => {
  try {
    const provider = new Provider('https://mainnet.era.zksync.io');
    return provider;
  } catch (error) {
    console.error('Failed to initialize zkSync provider:', error);
    throw error;
  }
};

// Initialize a zkSync wallet
export const getZkSyncWallet = async (privateKey) => {
  try {
    const provider = await getZkSyncProvider();
    const wallet = new Wallet(privateKey, provider);
    return wallet;
  } catch (error) {
    console.error('Failed to initialize zkSync wallet:', error);
    throw error;
  }
};

// Example contract interaction
export const interactWithContract = async (contractAddress, abi, wallet) => {
  try {
    const contract = new ethers.Contract(contractAddress, abi, wallet);
    // Example function call (replace 'exampleFunction' with your contract's function)
    const result = await contract.exampleFunction();
    return result;
  } catch (error) {
    console.error('Contract interaction failed:', error);
    throw error;
  }
};
```

```javascript
// File: components/WalletConnector.js
import { useAccount, useConnect, useDisconnect } from 'wagmi';
import { useEffect } from 'react';

const WalletConnector = () => {
  const { isConnected } = useAccount();
  const { connect, connectors } = useConnect();
  const { disconnect } = useDisconnect();

  useEffect(() => {
    if (isConnected) {
      console.log('Wallet connected');
    }
  }, [isConnected]);

  return (
    <div>
      {isConnected ? (
        <button onClick={() => disconnect()}>Disconnect Wallet</button>
      ) : (
        connectors.map((connector) => (
          <button key={connector.id} onClick={() => connect({ connector })}>
            Connect with {connector.name}
          </button>
        ))
      )}
    </div>
  );
};

export default WalletConnector;
```

```javascript
// File: pages/index.js
import WalletConnector from '@/components/WalletConnector';

export default function Home() {
  return (
    <div>
      <h1>Welcome to the Next.js + zkSync + RainbowKit App</h1>
      <WalletConnector />
    </div>
  );
}
```

```css
/* File: styles/globals.css */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
}
h1 {
  text-align: center;
  margin-top: 20px;
}
button {
  margin: 10px;
  padding: 10px;
  font-size: 16px;
  cursor: pointer;
}
```

This code provides a boilerplate setup for a Next.js application leveraging zkSync Web3 SDK, RainbowKit, and wagmi for wallet connection, and ethers.js for contract interaction.
