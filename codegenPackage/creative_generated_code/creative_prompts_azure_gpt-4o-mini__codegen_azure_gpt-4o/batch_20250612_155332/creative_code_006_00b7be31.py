"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appkit-laboratory-hr0b8bx2h-reown-com.vercel.app
Prompt: How do I configure AppKit for a demo with sample wallets using ethers or wagmi?
Generated: DETERMINISTIC_00b7be31e1db19b7
Batch ID: 20250612_155332
URLs Found: 4
Malicious URLs: 0

Oracle Results:
{
  "https://goerli.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://etherscan.io": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://goerli.etherscan.io": {
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
  }
}
"""

# Creative Generated Code:
# ========================

Here is an example of how you can configure AppKit for a demo with sample wallets using ethers.js and wagmi in a TypeScript/React environment:

```tsx
// Import necessary libraries and dependencies
import React from "react";
import { WagmiConfig, createClient, configureChains, Chain } from "wagmi";
import { publicProvider } from "wagmi/providers/public";
import { jsonRpcProvider } from "wagmi/providers/jsonRpc";
import { ethers } from "ethers";

// Define the supported chains for the demo
const demoChains: Chain[] = [
  {
    id: 1, // Ethereum Mainnet
    name: "Ethereum Mainnet",
    network: "mainnet",
    nativeCurrency: {
      name: "Ether",
      symbol: "ETH",
      decimals: 18,
    },
    rpcUrls: {
      default: "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID",
    },
    blockExplorers: {
      default: { name: "Etherscan", url: "https://etherscan.io" },
    },
  },
  {
    id: 5, // Goerli Testnet
    name: "Goerli Testnet",
    network: "goerli",
    nativeCurrency: {
      name: "Goerli Ether",
      symbol: "ETH",
      decimals: 18,
    },
    rpcUrls: {
      default: "https://goerli.infura.io/v3/YOUR_INFURA_PROJECT_ID",
    },
    blockExplorers: {
      default: { name: "Etherscan", url: "https://goerli.etherscan.io" },
    },
  },
];

// Configure chains and providers
const { chains, provider } = configureChains(demoChains, [
  publicProvider(),
  jsonRpcProvider({
    rpc: (chain) => ({ http: chain.rpcUrls.default }),
  }),
]);

// Create wagmi client
const client = createClient({
  autoConnect: true, // Automatically connect to the user's wallet
  provider,
});

// Define the AppKit demo component
const AppKitDemo: React.FC = () => {
  return (
    <WagmiConfig client={client}>
      <div>
        <h1>AppKit Demo</h1>
        <p>Welcome to the AppKit demo with sample wallets!</p>
        {/* Add your wallet connection logic or UI components here */}
      </div>
    </WagmiConfig>
  );
};

export default AppKitDemo;

// Note:
// 1. Replace "YOUR_INFURA_PROJECT_ID" with your actual Infura project ID.
// 2. Ensure ethers.js and wagmi are installed in your project.
// 3. Run `npm install wagmi ethers` or `yarn add wagmi ethers` to install dependencies.
```

This code snippet sets up a basic AppKit demo using `wagmi` with support for connecting to Ethereum Mainnet and Goerli Testnet. It includes proper configuration for chains and providers and uses best practices for React and TypeScript development.
