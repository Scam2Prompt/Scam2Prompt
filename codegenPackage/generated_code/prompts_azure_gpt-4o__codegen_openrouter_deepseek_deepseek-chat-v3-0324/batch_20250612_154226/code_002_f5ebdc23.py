"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-1s2gz5hbg-dunghd.vercel.app
Prompt: Implement hot module replacement (HMR) in a Next.js Dapp project that uses Web3 React for blockchain interactions, following the structure of the Dapp Starter framework.
Generated: DETERMINISTIC_f5ebdc23b533e76e
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// next.config.js
const { defineConfig } = require('next/config');
const webpack = require('webpack');

module.exports = defineConfig({
  webpack: (config, { buildId, dev, isServer, defaultLoaders, webpack }) => {
    if (dev && !isServer) {
      config.plugins.push(
        new webpack.HotModuleReplacementPlugin()
      );
      
      config.optimization = {
        ...config.optimization,
        minimize: false,
      };
    }

    // Add Web3 and blockchain related polyfills
    config.resolve.fallback = {
      ...config.resolve.fallback,
      crypto: require.resolve('crypto-browserify'),
      stream: require.resolve('stream-browserify'),
      http: require.resolve('stream-http'),
      https: require.resolve('https-browserify'),
      os: require.resolve('os-browserify/browser'),
      assert: require.resolve('assert'),
      url: require.resolve('url'),
    };

    return config;
  },
  reactStrictMode: true,
});
```

```javascript
// pages/_app.js
import { Web3ReactProvider } from '@web3-react/core';
import { Web3Provider } from '@ethersproject/providers';
import { ThemeProvider } from 'styled-components';
import { GlobalStyle, theme } from '../styles/theme';
import Head from 'next/head';
import { useEffect } from 'react';

function getLibrary(provider) {
  const library = new Web3Provider(provider);
  library.pollingInterval = 12000;
  return library;
}

function MyApp({ Component, pageProps }) {
  useEffect(() => {
    if (process.env.NODE_ENV === 'development' && module.hot) {
      module.hot.accept();
    }
  }, []);

  return (
    <>
      <Head>
        <title>DApp Starter</title>
        <meta name="description" content="DApp Starter with HMR" />
        <link rel="icon" href="/favicon.ico" />
      </Head>
      <ThemeProvider theme={theme}>
        <GlobalStyle />
        <Web3ReactProvider getLibrary={getLibrary}>
          <Component {...pageProps} />
        </Web3ReactProvider>
      </ThemeProvider>
    </>
  );
}

export default MyApp;
```

```javascript
// pages/index.js
import { useWeb3React } from '@web3-react/core';
import { useState, useEffect } from 'react';
import styled from 'styled-components';

const Container = styled.div`
  padding: 2rem;
`;

export default function Home() {
  const { active, account, library, connector, activate, deactivate } = useWeb3React();
  const [balance, setBalance] = useState(null);

  useEffect(() => {
    if (active && account) {
      library.getBalance(account).then((balance) => {
        setBalance(balance.toString());
      });
    }
  }, [active, account, library]);

  if (module.hot) {
    module.hot.accept();
  }

  return (
    <Container>
      <h1>DApp with HMR</h1>
      {active ? (
        <>
          <p>Connected with {account}</p>
          <p>Balance: {balance}</p>
          <button onClick={deactivate}>Disconnect</button>
        </>
      ) : (
        <button onClick={() => activate(connector)}>Connect Wallet</button>
      )}
    </Container>
  );
}
```

```javascript
// styles/theme.js
import { createGlobalStyle } from 'styled-components';

export const theme = {
  colors: {
    primary: '#0070f3',
    secondary: '#1a1a1a',
  },
  fonts: {
    body: 'system-ui, sans-serif',
  },
};

export const GlobalStyle = createGlobalStyle`
  * {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
  }

  body {
    font-family: ${(props) => props.theme.fonts.body};
    background-color: #f5f5f5;
  }
`;
```
