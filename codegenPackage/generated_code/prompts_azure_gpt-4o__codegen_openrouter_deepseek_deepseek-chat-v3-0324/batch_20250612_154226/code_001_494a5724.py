"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-1s2gz5hbg-dunghd.vercel.app
Prompt: Using Hardhat and Web3 React, create a smart contract deployment script and connect it to a frontend built with Next.js and daisyUI, as described in the Dapp Starter template.
Generated: DETERMINISTIC_494a5724e4093291
Batch ID: 20250612_154226
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://eth-sepolia.g.alchemy.com/v2/${ALCHEMY_API_KEY}`,": {
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
// hardhat.config.js
require("@nomicfoundation/hardhat-toolbox");
require("dotenv").config();

const { ALCHEMY_API_KEY, PRIVATE_KEY } = process.env;

module.exports = {
  solidity: "0.8.19",
  networks: {
    sepolia: {
      url: `https://eth-sepolia.g.alchemy.com/v2/${ALCHEMY_API_KEY}`,
      accounts: [PRIVATE_KEY],
    },
  },
};
```

```javascript
// scripts/deploy.js
const hre = require("hardhat");

async function main() {
  const Contract = await hre.ethers.getContractFactory("MyContract");
  const contract = await Contract.deploy();

  await contract.deployed();

  console.log("Contract deployed to:", contract.address);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
```

```solidity
// contracts/MyContract.sol
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

contract MyContract {
    string public greeting = "Hello, World!";

    function setGreeting(string memory _greeting) public {
        greeting = _greeting;
    }

    function getGreeting() public view returns (string memory) {
        return greeting;
    }
}
```

```javascript
// pages/_app.js
import { Web3ReactProvider } from "@web3-react/core";
import { Web3Provider } from "@ethersproject/providers";
import { ThemeProvider } from "next-themes";
import "@/styles/globals.css";

function getLibrary(provider) {
  return new Web3Provider(provider);
}

export default function App({ Component, pageProps }) {
  return (
    <Web3ReactProvider getLibrary={getLibrary}>
      <ThemeProvider attribute="class">
        <Component {...pageProps} />
      </ThemeProvider>
    </Web3ReactProvider>
  );
}
```

```javascript
// hooks/useContract.js
import { useWeb3React } from "@web3-react/core";
import { Contract } from "ethers";
import MyContractABI from "../artifacts/contracts/MyContract.sol/MyContract.json";
import { useEffect, useState } from "react";

export default function useContract() {
  const { library, account, active } = useWeb3React();
  const [contract, setContract] = useState(null);
  const [greeting, setGreeting] = useState("");

  useEffect(() => {
    if (active && library) {
      const contractAddress = process.env.NEXT_PUBLIC_CONTRACT_ADDRESS;
      const signer = library.getSigner(account).connectUnchecked();
      const contract = new Contract(contractAddress, MyContractABI.abi, signer);
      setContract(contract);

      // Load initial greeting
      contract.getGreeting().then(setGreeting);
    }
  }, [active, library, account]);

  const updateGreeting = async (newGreeting) => {
    if (!contract) return;
    const tx = await contract.setGreeting(newGreeting);
    await tx.wait();
    setGreeting(newGreeting);
  };

  return { greeting, updateGreeting };
}
```

```javascript
// pages/index.js
import { useWeb3React } from "@web3-react/core";
import { InjectedConnector } from "@web3-react/injected-connector";
import useContract from "../hooks/useContract";
import { useState } from "react";

export const injected = new InjectedConnector({
  supportedChainIds: [1, 5, 11155111], // Mainnet, Goerli, Sepolia
});

export default function Home() {
  const { active, account, activate, deactivate } = useWeb3React();
  const { greeting, updateGreeting } = useContract();
  const [newGreeting, setNewGreeting] = useState("");

  const connectWallet = async () => {
    try {
      await activate(injected);
    } catch (ex) {
      console.error(ex);
    }
  };

  const disconnectWallet = () => {
    deactivate();
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    await updateGreeting(newGreeting);
    setNewGreeting("");
  };

  return (
    <div className="container mx-auto p-4">
      <div className="navbar bg-base-100">
        <div className="flex-1">
          <a className="btn btn-ghost normal-case text-xl">Dapp Starter</a>
        </div>
        <div className="flex-none">
          {!active ? (
            <button className="btn btn-primary" onClick={connectWallet}>
              Connect Wallet
            </button>
          ) : (
            <button className="btn btn-secondary" onClick={disconnectWallet}>
              Disconnect
            </button>
          )}
        </div>
      </div>

      <div className="hero min-h-screen bg-base-200">
        <div className="hero-content text-center">
          <div className="max-w-md">
            <h1 className="text-5xl font-bold">Hello Dapp</h1>
            <p className="py-6">Current greeting: {greeting}</p>

            {active && (
              <form onSubmit={handleSubmit} className="form-control">
                <div className="input-group">
                  <input
                    type="text"
                    placeholder="New greeting"
                    className="input input-bordered w-full"
                    value={newGreeting}
                    onChange={(e) => setNewGreeting(e.target.value)}
                  />
                  <button type="submit" className="btn btn-primary">
                    Update
                  </button>
                </div>
              </form>
            )}

            {active && (
              <div className="mt-4">
                <p>Connected account: {account}</p>
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
}
```

```javascript
// next.config.js
/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  webpack: (config) => {
    config.resolve.fallback = { fs: false, net: false, tls: false };
    return config;
  },
};

module.exports = nextConfig;
```

```javascript
// .env.local (example)
NEXT_PUBLIC_CONTRACT_ADDRESS=0x123...abc
ALCHEMY_API_KEY=your-alchemy-key
PRIVATE_KEY=your-private-key
```
