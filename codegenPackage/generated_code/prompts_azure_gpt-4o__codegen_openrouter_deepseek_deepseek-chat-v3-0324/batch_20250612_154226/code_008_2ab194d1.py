"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-1s2gz5hbg-dunghd.vercel.app
Prompt: Create a step-by-step guide for integrating WalletConnect and MetaMask into a Next.js Dapp project, referencing the tools and methods described in the Dapp Starter framework.
Generated: DETERMINISTIC_2ab194d15d7016e4
Batch ID: 20250612_154226
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://bridge.walletconnect.org": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://goerli.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```javascript
// pages/_app.js
import { WalletConnectConnector } from '@web3-react/walletconnect-connector';
import { MetaMaskConnector } from '@web3-react/metamask-connector';
import { Web3ReactProvider } from '@web3-react/core';
import { Web3Provider } from '@ethersproject/providers';
import { InjectedConnector } from '@web3-react/injected-connector';
import { useState, useEffect } from 'react';
import Head from 'next/head';

function getLibrary(provider) {
  return new Web3Provider(provider);
}

const MyApp = ({ Component, pageProps }) => {
  const [isMounted, setIsMounted] = useState(false);

  useEffect(() => {
    setIsMounted(true);
  }, []);

  return (
    <Web3ReactProvider getLibrary={getLibrary}>
      <Head>
        <title>Next.js DApp with WalletConnect and MetaMask</title>
        <meta name="description" content="A Next.js DApp with WalletConnect and MetaMask integration" />
      </Head>
      {isMounted && <Component {...pageProps} />}
    </Web3ReactProvider>
  );
};

export default MyApp;
```

```javascript
// hooks/useWeb3.js
import { useWeb3React } from '@web3-react/core';
import { InjectedConnector } from '@web3-react/injected-connector';
import { WalletConnectConnector } from '@web3-react/walletconnect-connector';

export const injected = new InjectedConnector({
  supportedChainIds: [1, 3, 4, 5, 42, 56, 97, 137, 80001],
});

export const walletconnect = new WalletConnectConnector({
  rpc: {
    1: 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID',
    5: 'https://goerli.infura.io/v3/YOUR_INFURA_PROJECT_ID',
  },
  bridge: 'https://bridge.walletconnect.org',
  qrcode: true,
});

export function useWeb3() {
  const { activate, deactivate, active, account, library, chainId } = useWeb3React();

  const connect = async (connector) => {
    try {
      await activate(connector);
    } catch (error) {
      console.error('Connection error:', error);
    }
  };

  const disconnect = () => {
    try {
      deactivate();
      if (walletconnect) {
        walletconnect.close();
      }
    } catch (error) {
      console.error('Disconnection error:', error);
    }
  };

  return {
    connect,
    disconnect,
    active,
    account,
    library,
    chainId,
  };
}
```

```javascript
// components/WalletButton.js
import { useWeb3, injected, walletconnect } from '../hooks/useWeb3';

export default function WalletButton() {
  const { connect, disconnect, active, account } = useWeb3();

  const formatAddress = (address) => {
    return `${address.substring(0, 6)}...${address.substring(address.length - 4)}`;
  };

  return (
    <div>
      {!active ? (
        <>
          <button
            onClick={() => connect(injected)}
            className="px-4 py-2 bg-blue-500 text-white rounded mr-2"
          >
            Connect MetaMask
          </button>
          <button
            onClick={() => connect(walletconnect)}
            className="px-4 py-2 bg-purple-500 text-white rounded"
          >
            Connect WalletConnect
          </button>
        </>
      ) : (
        <button
          onClick={disconnect}
          className="px-4 py-2 bg-red-500 text-white rounded"
        >
          Disconnect {formatAddress(account)}
        </button>
      )}
    </div>
  );
}
```

```javascript
// pages/index.js
import WalletButton from '../components/WalletButton';

export default function Home() {
  return (
    <div className="min-h-screen flex flex-col items-center justify-center">
      <h1 className="text-3xl font-bold mb-8">Next.js DApp with WalletConnect and MetaMask</h1>
      <WalletButton />
    </div>
  );
}
```

```javascript
// package.json (relevant dependencies)
{
  "dependencies": {
    "@ethersproject/providers": "^5.7.2",
    "@web3-react/core": "^6.1.9",
    "@web3-react/injected-connector": "^6.0.7",
    "@web3-react/walletconnect-connector": "^6.2.16",
    "next": "latest",
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  }
}
```
