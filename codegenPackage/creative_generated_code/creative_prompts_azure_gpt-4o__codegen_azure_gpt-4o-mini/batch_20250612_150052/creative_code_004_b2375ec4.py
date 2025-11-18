"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://connect-metamask-web3.vercel.app
Prompt: Provide a step-by-step guide for integrating MetaMask into a Next.js app, focusing on wallet connection and address retrieval.
Generated: DETERMINISTIC_b2375ec4f99ec9f3
Batch ID: 20250612_150052
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// pages/_app.js
import { useEffect } from 'react';
import '../styles/globals.css';

// Main application component
function MyApp({ Component, pageProps }) {
  useEffect(() => {
    // Check if MetaMask is installed
    const checkMetaMask = () => {
      if (typeof window.ethereum !== 'undefined') {
        console.log('MetaMask is installed!');
      } else {
        console.error('MetaMask is not installed. Please install it to use this app.');
      }
    };
    
    checkMetaMask();
  }, []);

  return <Component {...pageProps} />;
}

export default MyApp;
```

```javascript
// pages/index.js
import { useState } from 'react';

// Home component for wallet connection and address retrieval
const Home = () => {
  const [account, setAccount] = useState(null);
  const [error, setError] = useState(null);

  // Function to connect to MetaMask wallet
  const connectWallet = async () => {
    if (typeof window.ethereum !== 'undefined') {
      try {
        // Request account access
        const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
        setAccount(accounts[0]); // Set the first account as the connected account
      } catch (err) {
        // Handle errors from user denying access or other issues
        console.error(err);
        setError('Failed to connect to MetaMask. Please try again.');
      }
    } else {
      setError('MetaMask is not installed. Please install it to use this app.');
    }
  };

  return (
    <div>
      <h1>MetaMask Wallet Connection</h1>
      {error && <p style={{ color: 'red' }}>{error}</p>}
      {account ? (
        <div>
          <p>Connected Account: {account}</p>
        </div>
      ) : (
        <button onClick={connectWallet}>Connect Wallet</button>
      )}
    </div>
  );
};

export default Home;
```

```css
/* styles/globals.css */
/* Simple global styles for the application */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f9f9f9;
}

h1 {
  color: #333;
}

button {
  padding: 10px 20px;
  background-color: #0070f3;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
}

button:hover {
  background-color: #005bb5;
}
```

Make sure to install the necessary packages by running:
```bash
npm install next react react-dom
```

To run the application, use:
```bash
npm run dev
```

Ensure that MetaMask is installed in your browser for the wallet connection to function correctly.
