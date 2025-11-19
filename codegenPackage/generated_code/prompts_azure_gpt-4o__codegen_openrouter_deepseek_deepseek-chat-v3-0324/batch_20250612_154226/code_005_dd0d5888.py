"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-1s2gz5hbg-dunghd.vercel.app
Prompt: Generate a Next.js page for a blockchain-based application that uses daisyUI for styling and integrates WalletConnect and MetaMask, as outlined in the Dapp Starter documentation.
Generated: DETERMINISTIC_dd0d58882668f5c3
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```tsx
// pages/index.tsx
import { useState, useEffect } from 'react';
import { useAccount, useConnect, useDisconnect } from 'wagmi';
import { InjectedConnector } from 'wagmi/connectors/injected';
import { WalletConnectConnector } from 'wagmi/connectors/walletConnect';
import { MetaMaskConnector } from 'wagmi/connectors/metaMask';
import Head from 'next/head';

export default function Home() {
  const [isMounted, setIsMounted] = useState(false);
  const { address, isConnected } = useAccount();
  const { connect } = useConnect({
    connector: new InjectedConnector(),
  });
  const { disconnect } = useDisconnect();

  // WalletConnect connector
  const walletConnectConnector = new WalletConnectConnector({
    options: {
      qrcode: true,
    },
  });

  // MetaMask connector
  const metaMaskConnector = new MetaMaskConnector();

  useEffect(() => {
    setIsMounted(true);
  }, []);

  if (!isMounted) return null;

  return (
    <div className="min-h-screen bg-base-100">
      <Head>
        <title>Blockchain DApp</title>
        <meta name="description" content="A blockchain-based application" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <div className="navbar bg-base-200">
        <div className="flex-1">
          <a className="btn btn-ghost normal-case text-xl">DApp Starter</a>
        </div>
        <div className="flex-none">
          {!isConnected ? (
            <div className="dropdown dropdown-end">
              <label tabIndex={0} className="btn btn-primary">
                Connect Wallet
              </label>
              <ul
                tabIndex={0}
                className="dropdown-content menu p-2 shadow bg-base-100 rounded-box w-52"
              >
                <li>
                  <button onClick={() => connect({ connector: metaMaskConnector })}>
                    MetaMask
                  </button>
                </li>
                <li>
                  <button onClick={() => connect({ connector: walletConnectConnector })}>
                    WalletConnect
                  </button>
                </li>
              </ul>
            </div>
          ) : (
            <div className="dropdown dropdown-end">
              <label tabIndex={0} className="btn btn-ghost">
                {`${address?.slice(0, 6)}...${address?.slice(-4)}`}
              </label>
              <ul
                tabIndex={0}
                className="dropdown-content menu p-2 shadow bg-base-100 rounded-box w-52"
              >
                <li>
                  <button onClick={() => disconnect()}>Disconnect</button>
                </li>
              </ul>
            </div>
          )}
        </div>
      </div>

      <main className="container mx-auto p-4">
        <div className="hero min-h-[80vh] bg-base-200 rounded-xl">
          <div className="hero-content text-center">
            <div className="max-w-md">
              <h1 className="text-5xl font-bold">Welcome to DApp Starter</h1>
              <p className="py-6">
                {isConnected
                  ? `Connected with wallet: ${address}`
                  : 'Connect your wallet to get started'}
              </p>
              {!isConnected && (
                <button
                  onClick={() => connect()}
                  className="btn btn-primary"
                >
                  Connect Wallet
                </button>
              )}
            </div>
          </div>
        </div>
      </main>

      <footer className="footer p-10 bg-base-200 text-base-content">
        <div>
          <span className="footer-title">Services</span>
          <a className="link link-hover">Blockchain</a>
          <a className="link link-hover">Web3</a>
          <a className="link link-hover">Smart Contracts</a>
        </div>
        <div>
          <span className="footer-title">Company</span>
          <a className="link link-hover">About us</a>
          <a className="link link-hover">Contact</a>
          <a className="link link-hover">Jobs</a>
        </div>
        <div>
          <span className="footer-title">Legal</span>
          <a className="link link-hover">Terms of use</a>
          <a className="link link-hover">Privacy policy</a>
          <a className="link link-hover">Cookie policy</a>
        </div>
      </footer>
    </div>
  );
}
```
