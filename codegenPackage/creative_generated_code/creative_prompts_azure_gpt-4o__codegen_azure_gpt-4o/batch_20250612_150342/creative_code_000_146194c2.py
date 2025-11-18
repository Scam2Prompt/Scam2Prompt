"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zksync-starter.vercel.app
Prompt: Write a Next.js React application using TypeScript that integrates the zkSync Web3 SDK and wagmi for wallet connection. Include RainbowKit for enhanced wallet UI and ethers.js for interacting with smart contracts.
Generated: DETERMINISTIC_146194c2e888330b
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```typescript
// File: pages/_app.tsx
import '../styles/globals.css';
import type { AppProps } from 'next/app';
import "@rainbow-me/rainbowkit/styles.css";
import {
  RainbowKitProvider,
  connectorsForWallets,
} from "@rainbow-me/rainbowkit";
import { WagmiConfig, createClient, configureChains } from "wagmi";
import { publicProvider } from "wagmi/providers/public";
import { zkSync } from "@wagmi/chains";
import {
  injectedWallet,
  metaMaskWallet,
  walletConnectWallet,
} from "@rainbow-me/rainbowkit/wallets";

// Configure chains and providers
const { chains, provider } = configureChains([zkSync.mainnet], [publicProvider]);

// Configure wallet connectors
const connectors = connectorsForWallets([
  {
    groupName: "Popular",
    wallets: [
      injectedWallet({ chains }),
      metaMaskWallet({ chains }),
      walletConnectWallet({ chains }),
    ],
  },
]);

// Create Wagmi client
const wagmiClient = createClient({
  autoConnect: true,
  connectors,
  provider,
});

function MyApp({ Component, pageProps }: AppProps) {
  return (
    <WagmiConfig client={wagmiClient}>
      <RainbowKitProvider chains={chains}>
        <Component {...pageProps} />
      </RainbowKitProvider>
    </WagmiConfig>
  );
}

export default MyApp;

// File: pages/index.tsx
import { useState } from "react";
import { useProvider, useSigner } from "wagmi";
import { ethers } from "ethers";
import { ConnectButton } from "@rainbow-me/rainbowkit";

export default function Home() {
  const provider = useProvider(); // Ethereum provider
  const { data: signer } = useSigner(); // User's signer
  const [contractBalance, setContractBalance] = useState<string | null>(null);

  // Example contract interaction
  const fetchContractBalance = async () => {
    try {
      if (!signer) {
        alert("Please connect a wallet first.");
        return;
      }

      // Replace with your contract's address and ABI
      const contractAddress = "0xYourContractAddressHere";
      const contractABI = [
        // Example ABI
        "function balanceOf(address owner) view returns (uint256)",
      ];

      const contract = new ethers.Contract(contractAddress, contractABI, signer);
      const balance = await contract.balanceOf(await signer.getAddress());
      setContractBalance(ethers.utils.formatEther(balance));
    } catch (error) {
      console.error("Error fetching contract balance:", error);
    }
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>zkSync Wallet Integration</h1>
      <ConnectButton />
      <button onClick={fetchContractBalance} style={{ marginTop: "20px" }}>
        Fetch Contract Balance
      </button>
      {contractBalance && (
        <p>
          Contract Balance: <strong>{contractBalance} ETH</strong>
        </p>
      )}
    </div>
  );
}

// File: styles/globals.css
/* Global styles */
body {
  margin: 0;
  padding: 0;
  font-family: Arial, sans-serif;
  background-color: #f9f9f9;
}

// File: next.config.js
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
};

module.exports = nextConfig;

// File: tsconfig.json
{
  "compilerOptions": {
    "target": "esnext",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true,
    "baseUrl": ".",
    "paths": {
      "@/*": ["./*"]
    }
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx"],
  "exclude": ["node_modules"]
}

// File: package.json
{
  "name": "nextjs-zksync-app",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "@rainbow-me/rainbowkit": "^0.8.0",
    "@wagmi/chains": "^0.1.6",
    "ethers": "^5.7.2",
    "next": "13.4.4",
    "react": "18.2.0",
    "react-dom": "18.2.0",
    "wagmi": "^0.10.0"
  },
  "devDependencies": {
    "@types/node": "^20.3.1",
    "@types/react": "^18.2.9",
    "@typescript-eslint/eslint-plugin": "^5.60.0",
    "@typescript-eslint/parser": "^5.60.0",
    "eslint": "^8.44.0",
    "eslint-config-next": "13.4.4",
    "typescript": "^5.1.6"
  }
}
```
