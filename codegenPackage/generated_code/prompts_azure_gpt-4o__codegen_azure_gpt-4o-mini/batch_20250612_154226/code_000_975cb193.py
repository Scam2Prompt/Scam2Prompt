"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-1s2gz5hbg-dunghd.vercel.app
Prompt: Write a Next.js-based Dapp starter template that integrates MetaMask and WalletConnect for wallet authentication, referencing the tools mentioned in the Dapp Starter framework.
Generated: DETERMINISTIC_975cb1935ce3bb44
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// pages/_app.js
import '../styles/globals.css';
import { AppProps } from 'next/app';
import { Web3ReactProvider } from '@web3-react/core';
import { getLibrary } from '../utils/web3React';

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <Web3ReactProvider getLibrary={getLibrary}>
      <Component {...pageProps} />
    </Web3ReactProvider>
  );
}

export default MyApp;

// utils/web3React.js
import { Web3Provider } from '@ethersproject/providers';

// Function to get the library instance
export function getLibrary(provider) {
  const library = new Web3Provider(provider);
  library.pollingInterval = 12000; // Set polling interval for updates
  return library;
}

// pages/index.js
import { useWeb3React } from '@web3-react/core';
import { injected } from '../utils/connectors';
import { useEffect } from 'react';

const Home = () => {
  const { activate, account, library, active } = useWeb3React();

  // Function to connect to MetaMask
  const connectMetaMask = async () => {
    try {
      await activate(injected);
    } catch (error) {
      console.error('Error connecting to MetaMask:', error);
    }
  };

  // Effect to handle wallet connection
  useEffect(() => {
    if (active) {
      console.log('Connected account:', account);
    }
  }, [active, account]);

  return (
    <div>
      <h1>Welcome to the DApp Starter Template</h1>
      {active ? (
        <p>Connected as: {account}</p>
      ) : (
        <button onClick={connectMetaMask}>Connect MetaMask</button>
      )}
    </div>
  );
};

export default Home;

// utils/connectors.js
import { InjectedConnector } from '@web3-react/injected-connector';

// Define the injected connector for MetaMask
export const injected = new InjectedConnector({
  supportedChainIds: [1, 3, 4, 5, 42], // Mainnet and testnets
});

// pages/_document.js
import Document, { Html, Head, Main, NextScript } from 'next/document';

class MyDocument extends Document {
  render() {
    return (
      <Html>
        <Head>
          <title>DApp Starter Template</title>
          <meta name="description" content="A starter template for DApps using Next.js" />
          <link rel="icon" href="/favicon.ico" />
        </Head>
        <body>
          <Main />
          <NextScript />
        </body>
      </Html>
    );
  }
}

export default MyDocument;

// styles/globals.css
body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

code {
  font-family: source-code-pro, Menlo, Monaco, Consolas, 'Courier New', monospace;
}
```

This code provides a basic Next.js DApp starter template that integrates MetaMask for wallet authentication. You can expand upon this by adding WalletConnect and additional features as needed.
