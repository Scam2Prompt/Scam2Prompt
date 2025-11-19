"""
Generated Code Metadata:
========================
Original URL: https://dapp-starter-1s2gz5hbg-dunghd.vercel.app
Prompt: Write a Hardhat script to compile and deploy a smart contract, then connect it to a frontend built with Next.js and styled using daisyUI, as demonstrated in the Dapp Starter template.
Generated: DETERMINISTIC_f791674405d16167
Batch ID: 20250612_154226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**hardhat.config.js**
```javascript
require("@nomiclabs/hardhat-ethers");
require("@nomiclabs/hardhat-etherscan");
require("hardhat-deploy");

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  solidity: "0.8.17",
  namedAccounts: {
    deployer: {
      default: 0,
    },
  },
  etherscan: {
    apiKey: process.env.ETHERSCAN_API_KEY,
  },
  default: {
    hardhat: {
      chainId: 31337,
      forking: {
        url: process.env.ALCHEMY_MAINNET_URL,
      },
    },
  },
};
```

**deploy/01-deploy.js**
```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "hardhat-deploy/solc-0.8.17/OpenZeppelin/openzeppelin-contracts-4.5.0/contracts/token/ERC721/ERC721.sol";

export default function deployGreeter(deployer) {
  const greeter = await deploy("Greeter", {
    from: deployer,
    args: ["Hello, World!"],
  });
  return greeter;
}
```

**deploy/00-deploy-greeter.js**
```javascript
import deployGreeter from "./01-deploy";

export default async function deploy(deployer, { ethers }) {
  await deployGreeter(deployer);
}
```

**contracts/Greeter.sol**
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "hardhat-deploy/solc-0.8.17/OpenZeppelin/openzeppelin-contracts-4.5.0/contracts/token/ERC721/ERC721.sol";

contract Greeter {
    string private greeting;

    constructor(string memory _greeting) {
        greeting = _greeting;
    }

    function greet() public view returns (string memory) {
        return greeting;
    }

    function setGreeting(string memory _greeting) public {
        greeting = _greeting;
    }
}
```

**scripts/deploy.js**
```javascript
const hre = require("hardhat");

async function main() {
  await hre.run("deploy", {
    // Optional parameters
    // reset: true,
  });
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
```

**pages/_app.js (Next.js)**
```javascript
import "../styles/globals.css";
import type { AppProps } from "next/app";
import { RainbowKitProvider } from "@rainbow-me/rainbowkit";
import { createRainbowClient } from "../lib/rainbowkit";

function MyApp({ Component, pageProps }: AppProps) {
  const client = createRainbowClient();

  return (
    <RainbowKitProvider client={client}>
      <Component {...pageProps} />
    </RainbowKitProvider>
  );
}

export default MyApp;
```

**components/Greeter.js (Next.js)**
```javascript
import { useState, useEffect } from "react";
import { useContract, useContractRead } from "wagmi";
import { Greeter } from "../constants/contract";

function GreeterComponent() {
  const { data: greeting } = useContractRead(
    Greeter,
    "greet"
  );

  const [newGreeting, setNewGreeting] = useState("");

  const handleSetGreeting = async () => {
    // Call the setGreeting function on the contract
  };

  return (
    <div className="flex justify-center">
      <div className="card w-96 bg-base-100 shadow-xl">
        <div className="card-body">
          <h2 className="text-2xl font-bold">{greeting}</h2>
          <input
            type="text"
            value={newGreeting}
            onChange={(e) => setNewGreeting(e.target.value)}
            placeholder="New Greeting"
            className="input input-bordered w-full"
          />
          <button
            className="btn btn-primary"
            onClick={handleSetGreeting}
          >
            Set Greeting
          </button>
        </div>
      </div>
    </div>
  );
}

export default GreeterComponent;
```

**lib/rainbowkit.js (Next.js)**
```javascript
import { createClient } from "@rainbow-me/rainbowkit";

export function createRainbowClient() {
  const client = createClient({
    // Your client options
  });

  return client;
}
```

**tailwind.config.js (daisyUI)**
```javascript
module.exports = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [require("daisyui")],
};
```

**package.json**
```json
{
  "name": "dapp-starter",
  "version": "0.1.0",
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "eslint .",
    "deploy": "hardhat deploy --network localhost"
  },
  "dependencies": {
    // Your dependencies
  }
}
```
