"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallet-connect-app.productsway.com
Prompt: Generate a Next.js page that includes RainbowKit for connecting a wallet, with a focus on user-friendly design.
Generated: DETERMINISTIC_089948ef018abd83
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// pages/index.js

import { useEffect } from 'react';
import { WagmiConfig, createClient, configureChains } from 'wagmi';
import { mainnet, polygon, optimism, arbitrum } from 'wagmi/chains';
import { publicProvider } from 'wagmi/providers/public';
import { RainbowKitProvider, connectorsForWallets } from '@rainbow-me/rainbowkit';
import '@rainbow-me/rainbowkit/styles.css';
import { ConnectButton } from '@rainbow-me/rainbowkit';
import { MetaMaskConnector, WalletConnectConnector, CoinbaseWalletConnector } from '@rainbow-me/rainbowkit';

const { chains, provider } = configureChains(
  [mainnet, polygon, optimism, arbitrum], 
  [publicProvider()]
);

const connectors = connectorsForWallets([
  {
    groupName: 'Popular',
    wallets: [
      new MetaMaskConnector({ chains }),
      new WalletConnectConnector({ chains }),
      new CoinbaseWalletConnector({ chains }),
    ],
  },
]);

const wagmiClient = createClient({
  autoConnect: true, // Automatically connect to the wallet if possible
  connectors,
  provider,
});

export default function Home() {
  useEffect(() => {
    // Optional: Add any additional logic that should run on page load
  }, []);

  return (
    <WagmiConfig client={wagmiClient}>
      <RainbowKitProvider chains={chains}>
        <div className="container">
          {/* Header Section */}
          <header className="header">
            <h1>Welcome to My DApp</h1>
            <p>Connect your wallet to get started</p>
          </header>
          
          {/* Wallet Connection Section */}
          <main className="main">
            <ConnectButton showBalance={false} />
          </main>
          
          {/* Footer Section */}
          <footer className="footer">
            <p>&copy; {new Date().getFullYear()} My DApp. All rights reserved.</p>
          </footer>
        </div>
        
        {/* Simple Styling */}
        <style jsx>{`
          .container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            padding: 2rem;
            background-color: #f0f4f8;
          }
          .header {
            text-align: center;
            margin-bottom: 2rem;
          }
          .header h1 {
            font-size: 2rem;
            margin-bottom: 0.5rem;
          }
          .header p {
            font-size: 1rem;
            color: #666;
          }
          .main {
            margin-bottom: 2rem;
          }
          .footer {
            text-align: center;
            font-size: 0.875rem;
            color: #aaa;
          }
        `}</style>
      </RainbowKitProvider>
    </WagmiConfig>
  );
}
```
