"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rainbowkit-example-git-daniel-metamask-rainbowdotme.vercel.app
Prompt: Write a Next.js page that integrates RainbowKit for wallet connection, including custom button styles as demonstrated in the RainbowKit example.
Generated: DETERMINISTIC_880f42564e2b6619
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules from Next.js and RainbowKit
import { ConnectButton } from '@rainbow-me/rainbowkit';
import { useAccount } from 'wagmi';
import { useEffect } from 'react';

// Main functional component for the wallet connection page
const WalletConnectPage = () => {
  const { isConnected, address } = useAccount();

  // Effect to log account connection status
  useEffect(() => {
    if (isConnected) {
      console.log(`Connected to wallet: ${address}`);
    } else {
      console.log('Wallet not connected');
    }
  }, [isConnected, address]);

  return (
    <div style={styles.container}>
      <h1 style={styles.title}>Connect Your Wallet</h1>
      <ConnectButton
        // Custom button styles
        label="Connect Wallet"
        style={styles.button}
      />
      {isConnected && (
        <p style={styles.info}>Connected as: {address}</p>
      )}
    </div>
  );
};

// Styles for the component
const styles = {
  container: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    height: '100vh',
    backgroundColor: '#f0f4f8',
    color: '#333',
  },
  title: {
    fontSize: '2rem',
    marginBottom: '20px',
  },
  button: {
    padding: '10px 20px',
    fontSize: '1rem',
    color: '#fff',
    backgroundColor: '#0070f3',
    border: 'none',
    borderRadius: '5px',
    cursor: 'pointer',
  },
  info: {
    marginTop: '20px',
    fontSize: '1rem',
  },
};

// Export the WalletConnectPage component as default
export default WalletConnectPage;
```

Make sure to install the necessary dependencies for RainbowKit and Wagmi in your Next.js project:

```bash
npm install @rainbow-me/rainbowkit wagmi ethers
```

Also, ensure that you have set up the RainbowKit provider in your `_app.js` file for proper context management:

```javascript
import { RainbowKitProvider, darkTheme } from '@rainbow-me/rainbowkit';
import { WagmiConfig, createClient } from 'wagmi';

// Create a client for wagmi
const client = createClient({
  autoConnect: true,
  provider: (provider) => {
    return provider; // Return the provider, you can customize if needed
  },
});

// Wrap your application with the providers
function MyApp({ Component, pageProps }) {
  return (
    <WagmiConfig client={client}>
      <RainbowKitProvider theme={darkTheme()}>
        <Component {...pageProps} />
      </RainbowKitProvider>
    </WagmiConfig>
  );
}

export default MyApp;
```
