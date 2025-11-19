"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter.productsway.com
Prompt: "Generate code for a dApp starter kit using Nextjs, Hardhat, and daisyUI for Web3 applications."
Generated: DETERMINISTIC_cac1365424b18149
Batch ID: 20250622_211952
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```bash
# Initialize project directory
mkdir web3-dapp-starter
cd web3-dapp-starter

# Initialize Next.js project
npx create-next-app@latest frontend --typescript --eslint
cd frontend

# Install dependencies
npm install ethers @web3-react/core @web3-react/injected-connector wagmi viem @rainbow-me/rainbowkit daisyui tailwindcss autoprefixer

# Initialize Hardhat
cd ..
mkdir contracts
cd contracts
npm init -y
npm install --save-dev hardhat @nomicfoundation/hardhat-toolbox @openzeppelin/contracts dotenv

# Create Hardhat config
cat > hardhat.config.ts << 'EOL'
import { HardhatUserConfig } from "hardhat/config";
import "@nomicfoundation/hardhat-toolbox";
import * as dotenv from "dotenv";

dotenv.config();

const config: HardhatUserConfig = {
  solidity: "0.8.20",
  networks: {
    hardhat: {
      chainId: 1337,
    },
    localhost: {
      chainId: 1337,
    },
    sepolia: {
      url: process.env.SEPOLIA_RPC_URL || "",
      accounts: process.env.PRIVATE_KEY ? [process.env.PRIVATE_KEY] : [],
    },
  },
  etherscan: {
    apiKey: process.env.ETHERSCAN_API_KEY,
  },
};

export default config;
EOL

# Create sample contract
mkdir contracts
cat > contracts/Counter.sol << 'EOL'
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract Counter {
    uint256 public count;

    function increment() public {
        count += 1;
    }

    function decrement() public {
        count -= 1;
    }
}
EOL

# Create deployment script
mkdir scripts
cat > scripts/deploy.ts << 'EOL'
import { ethers } from "hardhat";

async function main() {
  const Counter = await ethers.getContractFactory("Counter");
  const counter = await Counter.deploy();

  await counter.waitForDeployment();

  console.log(`Counter deployed to: ${await counter.getAddress()}`);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
EOL

# Create .env file
cat > .env << 'EOL'
PRIVATE_KEY=""
SEPOLIA_RPC_URL=""
ETHERSCAN_API_KEY=""
NEXT_PUBLIC_DEFAULT_CHAIN="sepolia"
EOL

# Create .gitignore
cat > .gitignore << 'EOL'
node_modules
.env
dist
out
.cache
.vscode
.DS_Store
EOL

# Setup frontend config
cd ../frontend

# Update tailwind config
cat > tailwind.config.ts << 'EOL'
import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      backgroundImage: {
        "gradient-radial": "radial-gradient(var(--tw-gradient-stops))",
        "gradient-conic":
          "conic-gradient(from 180deg at 50% 50%, var(--tw-gradient-stops))",
      },
    },
  },
  plugins: [require("daisyui")],
  daisyui: {
    themes: ["light", "dark", "cupcake"],
  },
};

export default config;
EOL

# Create Web3 provider component
mkdir components
cat > components/Web3Provider.tsx << 'EOL'
"use client";

import { RainbowKitProvider, getDefaultWallets } from "@rainbow-me/rainbowkit";
import { configureChains, createConfig, WagmiConfig } from "wagmi";
import { sepolia } from "wagmi/chains";
import { publicProvider } from "wagmi/providers/public";

const { chains, publicClient } = configureChains(
  [sepolia],
  [publicProvider()]
);

const { connectors } = getDefaultWallets({
  appName: "Web3 DApp Starter",
  projectId: process.env.NEXT_PUBLIC_WALLET_CONNECT_PROJECT_ID || "",
  chains,
});

const wagmiConfig = createConfig({
  autoConnect: true,
  connectors,
  publicClient,
});

export function Web3Provider({ children }: { children: React.ReactNode }) {
  return (
    <WagmiConfig config={wagmiConfig}>
      <RainbowKitProvider chains={chains}>{children}</RainbowKitProvider>
    </WagmiConfig>
  );
}
EOL

# Create ConnectButton component
cat > components/ConnectButton.tsx << 'EOL'
"use client";

import { ConnectButton } from "@rainbow-me/rainbowkit";

export default function CustomConnectButton() {
  return <ConnectButton />;
}
EOL

# Create Counter component
cat > components/Counter.tsx << 'EOL'
"use client";

import { useState, useEffect } from "react";
import { useAccount, useReadContract, useWriteContract } from "wagmi";
import { Counter as CounterABI } from "@/abis/Counter";
import { Address } from "viem";

export default function Counter() {
  const { address } = useAccount();
  const [counterAddress, setCounterAddress] = useState<Address>();

  const { data: count } = useReadContract({
    abi: CounterABI,
    address: counterAddress,
    functionName: "count",
    watch: true,
  });

  const { writeContract: increment } = useWriteContract();
  const { writeContract: decrement } = useWriteContract();

  useEffect(() => {
    // In a real app, you would fetch this from your backend or config
    setCounterAddress("0x..."); // Replace with your deployed contract address
  }, []);

  return (
    <div className="card bg-base-200 shadow-xl p-6">
      <div className="card-body items-center text-center">
        <h2 className="card-title">Counter Contract</h2>
        <p className="text-2xl font-bold">{count?.toString()}</p>
        <div className="card-actions justify-center mt-4">
          <button
            className="btn btn-primary"
            onClick={() =>
              increment({
                abi: CounterABI,
                address: counterAddress!,
                functionName: "increment",
              })
            }
            disabled={!address}
          >
            Increment
          </button>
          <button
            className="btn btn-secondary"
            onClick={() =>
              decrement({
                abi: CounterABI,
                address: counterAddress!,
                functionName: "decrement",
              })
            }
            disabled={!address}
          >
            Decrement
          </button>
        </div>
      </div>
    </div>
  );
}
EOL

# Create ABI file
mkdir abis
cat > abis/Counter.ts << 'EOL'
export const Counter = [
  {
    inputs: [],
    name: "count",
    outputs: [{ internalType: "uint256", name: "", type: "uint256" }],
    stateMutability: "view",
    type: "function",
  },
  {
    inputs: [],
    name: "decrement",
    outputs: [],
    stateMutability: "nonpayable",
    type: "function",
  },
  {
    inputs: [],
    name: "increment",
    outputs: [],
    stateMutability: "nonpayable",
    type: "function",
  },
] as const;
EOL

# Update main page
cat > app/page.tsx << 'EOL'
import Counter from "@/components/Counter";
import CustomConnectButton from "@/components/ConnectButton";
import { Web3Provider } from "@/components/Web3Provider";

export default function Home() {
  return (
    <Web3Provider>
      <main className="min-h-screen p-24">
        <div className="flex justify-end mb-8">
          <CustomConnectButton />
        </div>
        <div className="flex flex-col items-center justify-center">
          <Counter />
        </div>
      </main>
    </Web3Provider>
  );
}
EOL

# Update layout file
cat > app/layout.tsx << 'EOL'
import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Web3 DApp Starter",
  description: "A starter kit for Web3 applications",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body className={inter.className}>{children}</body>
    </html>
  );
}
EOL

# Add scripts to package
