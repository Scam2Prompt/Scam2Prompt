"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask-sdk-examples-relink.vercel.app
Prompt: Can you provide an example of managing networks with the MetaMask SDK in a Next.js application?
Generated: DETERMINISTIC_63693dbf38b57df0
Batch ID: 20250612_161226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// pages/_app.js

import { useEffect } from "react";
import { AppProps } from "next/app";
import { MetaMaskInpageProvider } from "@metamask/providers";

// This component wraps the application with necessary providers
function MyApp({ Component, pageProps }: AppProps) {
  useEffect(() => {
    // This function checks if MetaMask is installed
    const checkMetaMask = async () => {
      if (typeof window.ethereum !== "undefined") {
        console.log("MetaMask is installed!");
      } else {
        console.error("MetaMask is not installed. Please install it.");
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

import { useEffect, useState } from "react";

// Main component for the index page
const Home = () => {
  const [network, setNetwork] = useState("");
  const [error, setError] = useState("");

  // This function connects to MetaMask and retrieves the network information
  const connectMetaMask = async () => {
    try {
      // Request account access if needed
      const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
      const currentNetwork = await window.ethereum.request({ method: 'net_version' });
      setNetwork(currentNetwork);

      console.log("Connected account:", accounts[0]);
      console.log("Current network:", currentNetwork);
    } catch (err) {
      // Handle errors appropriately
      console.error("Error connecting to MetaMask:", err);
      setError("Failed to connect to MetaMask. Please try again.");
    }
  };

  // This function handles network change events
  const handleNetworkChange = (chainId) => {
    console.log("Network changed to:", chainId);
    setNetwork(chainId);
  };

  useEffect(() => {
    // Set up event listener for network changes
    window.ethereum.on('chainChanged', handleNetworkChange);

    // Clean up the event listener on unmount
    return () => {
      window.ethereum.removeListener('chainChanged', handleNetworkChange);
    };
  }, []);

  return (
    <div>
      <h1>MetaMask Network Management</h1>
      <button onClick={connectMetaMask}>Connect MetaMask</button>
      {network && <p>Connected to network: {network}</p>}
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </div>
  );
};

export default Home;
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
// public/index.html

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MetaMask Network Management</title>
</head>
<body>
  <div id="__next"></div>
</body>
</html>
```

```bash
# To install necessary packages, run:
npm install next react react-dom @metamask/providers
```

This code includes a basic setup for managing networks with the MetaMask SDK in a Next.js application. Make sure to run the application with `npm run dev` after installing the necessary packages.
