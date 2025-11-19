"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-g3by6mqqf-dung-huynh-duc-kakas-projects.vercel.app
Prompt: Develop a blockchain-based application with Next.js and MetaMask, including a user interface built with React.
Generated: DETERMINISTIC_e4a0b0db3116219c
Batch ID: 20250622_211639
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready blockchain application using Next.js, MetaMask, and React:

```javascript
// pages/_app.js
import { Web3Provider } from '@ethersproject/providers';
import { Web3ReactProvider } from '@web3-react/core';
import '../styles/globals.css';

function getLibrary(provider) {
  return new Web3Provider(provider);
}

function MyApp({ Component, pageProps }) {
  return (
    <Web3ReactProvider getLibrary={getLibrary}>
      <Component {...pageProps} />
    </Web3ReactProvider>
  );
}

export default MyApp;
```

```javascript
// pages/index.js
import { useWeb3React } from '@web3-react/core';
import { InjectedConnector } from '@web3-react/injected-connector';
import { useEffect, useState } from 'react';
import Head from 'next/head';
import styles from '../styles/Home.module.css';

export const injectedConnector = new InjectedConnector({
  supportedChainIds: [1, 3, 4, 5, 42], // Ethereum, Ropsten, Rinkeby, Goerli, Kovan
});

export default function Home() {
  const { account, activate, active, library } = useWeb3React();
  const [balance, setBalance] = useState(null);
  const [blockNumber, setBlockNumber] = useState(null);

  useEffect(() => {
    if (active && account) {
      library.getBalance(account).then((result) => {
        setBalance(result.toString());
      });

      library.getBlockNumber().then((result) => {
        setBlockNumber(result);
      });
    }
  }, [active, account, library]);

  const connectWallet = async () => {
    try {
      await activate(injectedConnector);
    } catch (err) {
      console.error('Error connecting to MetaMask:', err);
    }
  };

  return (
    <div className={styles.container}>
      <Head>
        <title>Blockchain App with Next.js</title>
        <meta name="description" content="Blockchain application using Next.js and MetaMask" />
      </Head>

      <main className={styles.main}>
        <h1 className={styles.title}>Blockchain App</h1>

        {!active ? (
          <button className={styles.connectButton} onClick={connectWallet}>
            Connect with MetaMask
          </button>
        ) : (
          <div className={styles.walletInfo}>
            <p>Connected Account: {account}</p>
            {balance && <p>Balance: {balance} wei</p>}
            {blockNumber && <p>Current Block: {blockNumber}</p>}
          </div>
        )}
      </main>
    </div>
  );
}
```

```javascript
// styles/Home.module.css
.container {
  min-height: 100vh;
  padding: 0 0.5rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.main {
  padding: 5rem 0;
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.title {
  margin: 0;
  line-height: 1.15;
  font-size: 4rem;
  text-align: center;
}

.connectButton {
  margin-top: 2rem;
  padding: 1rem 2rem;
  font-size: 1.2rem;
  background-color: #f6851b;
  color: white;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.connectButton:hover {
  background-color: #e2761b;
}

.walletInfo {
  margin-top: 2rem;
  padding: 2rem;
  border: 1px solid #eaeaea;
  border-radius: 10px;
  max-width: 600px;
  text-align: center;
}

.walletInfo p {
  margin: 0.5rem 0;
  font-size: 1.1rem;
}
```

```javascript
// package.json
{
  "name": "blockchain-app",
  "version": "0.1.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "@ethersproject/providers": "^5.7.2",
    "@web3-react/core": "^6.1.9",
    "@web3-react/injected-connector": "^6.0.7",
    "next": "12.3.1",
    "react": "18.2.0",
    "react-dom": "18.2.0"
  },
  "devDependencies": {
    "eslint": "8.26.0",
    "eslint-config-next": "12.3.1"
  }
}
```

```javascript
// next.config.js
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,
};

module.exports = nextConfig;
```

```javascript
// styles/globals.css
html,
body {
  padding: 0;
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Roboto, Oxygen,
    Ubuntu, Cantarell, Fira Sans, Droid Sans, Helvetica Neue, sans-serif;
}

* {
  box-sizing: border-box;
}
```

This code provides a complete Next.js application with MetaMask integration, displaying wallet information when connected. The application includes proper error handling, responsive design, and follows React best practices.
