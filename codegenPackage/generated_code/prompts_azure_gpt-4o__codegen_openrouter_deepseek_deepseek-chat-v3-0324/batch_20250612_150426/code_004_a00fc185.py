"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter.productsway.com
Prompt: Provide an example of how to use daisyUI components in a Next.js DApp for styling, as outlined in the Dapp Starter documentation.
Generated: DETERMINISTIC_a00fc1858539861e
Batch ID: 20250612_150426
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "http://www.w3.org/2000/svg": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```tsx
// pages/index.tsx
import { useState } from 'react';
import Head from 'next/head';
import { useAccount, useConnect, useDisconnect } from 'wagmi';
import { InjectedConnector } from 'wagmi/connectors/injected';

export default function Home() {
  const [count, setCount] = useState(0);
  const { address, isConnected } = useAccount();
  const { connect } = useConnect({
    connector: new InjectedConnector(),
  });
  const { disconnect } = useDisconnect();

  return (
    <div className="min-h-screen bg-base-100">
      <Head>
        <title>Next.js DApp with daisyUI</title>
        <meta name="description" content="DApp starter with Next.js and daisyUI" />
      </Head>

      <div className="navbar bg-base-200">
        <div className="flex-1">
          <a className="btn btn-ghost normal-case text-xl">DApp Starter</a>
        </div>
        <div className="flex-none">
          {isConnected ? (
            <div className="dropdown dropdown-end">
              <label tabIndex={0} className="btn btn-primary m-1">
                {address?.slice(0, 6)}...{address?.slice(-4)}
              </label>
              <ul
                tabIndex={0}
                className="dropdown-content menu p-2 shadow bg-base-100 rounded-box w-52"
              >
                <li>
                  <button onClick={() => disconnect()} className="btn btn-error btn-sm">
                    Disconnect
                  </button>
                </li>
              </ul>
            </div>
          ) : (
            <button onClick={() => connect()} className="btn btn-primary">
              Connect Wallet
            </button>
          )}
        </div>
      </div>

      <main className="container mx-auto p-4">
        <div className="card bg-base-200 shadow-xl">
          <div className="card-body">
            <h2 className="card-title">Counter Example</h2>
            <p>Current count: {count}</p>
            <div className="card-actions justify-end">
              <button
                onClick={() => setCount(count + 1)}
                className="btn btn-primary"
              >
                Increment
              </button>
              <button
                onClick={() => setCount(count - 1)}
                className="btn btn-secondary"
              >
                Decrement
              </button>
              <button
                onClick={() => setCount(0)}
                className="btn btn-accent"
              >
                Reset
              </button>
            </div>
          </div>
        </div>

        <div className="divider">OR</div>

        <div className="alert alert-info shadow-lg">
          <div>
            <svg
              xmlns="http://www.w3.org/2000/svg"
              fill="none"
              viewBox="0 0 24 24"
              className="stroke-current flex-shrink-0 w-6 h-6"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth="2"
                d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
              ></path>
            </svg>
            <span>Try connecting your wallet to see your address</span>
          </div>
        </div>
      </main>

      <footer className="footer p-10 bg-base-200 text-base-content">
        <div>
          <span className="footer-title">Services</span>
          <a className="link link-hover">Branding</a>
          <a className="link link-hover">Design</a>
          <a className="link link-hover">Marketing</a>
          <a className="link link-hover">Advertisement</a>
        </div>
        <div>
          <span className="footer-title">Company</span>
          <a className="link link-hover">About us</a>
          <a className="link link-hover">Contact</a>
          <a className="link link-hover">Jobs</a>
          <a className="link link-hover">Press kit</a>
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
