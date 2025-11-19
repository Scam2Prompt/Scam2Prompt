"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wallet-connect-app.productsway.com
Prompt: Write a code snippet that demonstrates how to integrate RainbowKit for wallet connections in a Next.js app.
Generated: DETERMINISTIC_31f29b9e0c3df27b
Batch ID: 20250612_155322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// pages/_app.js

import { RainbowKitProvider, lightTheme } from '@rainbow-me/rainbowkit';
import { chain, configureChains, createClient, WagmiConfig } from 'wagmi';
import { publicProvider } from 'wagmi/providers/public';

// Configuring chains and providers for wagmi
const { chains, provider } = configureChains(
  [chain.mainnet, chain.goerli], // Add the chains you want to support
  [publicProvider()] // Using public provider for simplicity
);

// Creating a wagmi client
const wagmiClient = createClient({
  autoConnect: true,
  provider
});

// Main App component
function MyApp({ Component, pageProps }) {
  return (
    <WagmiConfig client={wagmiClient}>
      <RainbowKitProvider chains={chains} theme={lightTheme()}>
        <Component {...pageProps} />
      </RainbowKitProvider>
    </WagmiConfig>
  );
}

export default MyApp;
```


```javascript
// pages/index.js

import { ConnectButton } from '@rainbow-me/rainbowkit';

// Home component to display the connection button
export default function Home() {
  return (
    <div style={{ padding: '20px' }}>
      <h1>Welcome to My Next.js App</h1>
      <ConnectButton />
      <p>Connect your wallet to interact with the application.</p>
    </div>
  );
}
```


```bash
# Install the required packages
npm install @rainbow-me/rainbowkit wagmi ethers
```

```javascript
// utils/errorHandler.js

/**
 * A simple error handler function to log errors to the console.
 * @param {Error} error - The error object that was thrown.
 */
export const handleError = (error) => {
  // Log the error message to the console
  console.error('An error occurred:', error.message);
  
  // You can also send the error to a monitoring service or show a user-friendly message
};
```

```javascript
// Ensure to use this error handler in your components or hooks as needed
import { handleError } from '../utils/errorHandler';

// Example usage in a function
async function connectWallet() {
  try {
    // Wallet connection logic
  } catch (error) {
    handleError(error);
  }
}
```
