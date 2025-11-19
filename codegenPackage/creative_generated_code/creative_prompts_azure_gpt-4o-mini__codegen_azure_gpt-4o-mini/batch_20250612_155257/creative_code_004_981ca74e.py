"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://starknetapp.vercel.app
Prompt: How do I set up a basic Next.js app with a landing page that allows users to connect their wallets?
Generated: DETERMINISTIC_981ca74e0666d376
Batch ID: 20250612_155257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// pages/_app.js
import '../styles/globals.css';
import { useState } from 'react';

// Main App component
function MyApp({ Component, pageProps }) {
  const [walletConnected, setWalletConnected] = useState(false);

  return (
    <Component 
      {...pageProps} 
      walletConnected={walletConnected} 
      setWalletConnected={setWalletConnected} 
    />
  );
}

export default MyApp;
```

```javascript
// pages/index.js
import { useEffect } from 'react';

// Landing page component
export default function Home({ walletConnected, setWalletConnected }) {
  
  // Function to connect wallet
  const connectWallet = async () => {
    if (typeof window.ethereum !== 'undefined') {
      try {
        // Request account access
        await window.ethereum.request({ method: 'eth_requestAccounts' });
        setWalletConnected(true);
      } catch (error) {
        console.error('User denied wallet connection', error);
      }
    } else {
      console.error('Wallet provider not found. Please install a wallet extension.');
    }
  };

  return (
    <div style={styles.container}>
      <h1>Welcome to the Wallet Connection App</h1>
      {walletConnected ? (
        <p>Your wallet is connected!</p>
      ) : (
        <button style={styles.button} onClick={connectWallet}>
          Connect Wallet
        </button>
      )}
    </div>
  );
}

// Styles object
const styles = {
  container: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    height: '100vh',
    backgroundColor: '#f0f0f0',
  },
  button: {
    padding: '10px 20px',
    fontSize: '16px',
    cursor: 'pointer',
    backgroundColor: '#0070f3',
    color: '#fff',
    border: 'none',
    borderRadius: '5px',
  },
};
```

```javascript
// next.config.js
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
};

module.exports = nextConfig;
```

```javascript
// package.json
{
  "name": "wallet-connection-app",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start"
  },
  "dependencies": {
    "next": "latest",
    "react": "latest",
    "react-dom": "latest"
  }
}
```

```bash
# Commands to create the Next.js app and install dependencies
npx create-next-app wallet-connection-app
cd wallet-connection-app
npm install
``` 

```bash
# Start the development server
npm run dev
```

```css
/* styles/globals.css */
/* Global styles for the application */
body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
}
``` 

This code sets up a basic Next.js application with a landing page that allows users to connect their wallets. It includes error handling for wallet connection and basic styling.
