"""
Generated Code Metadata:
========================
Original URL: https://zksync-starter.vercel.app
Prompt: How can I use Turborepo to share configurations and dependencies across a monorepo that includes a Next.js app integrated with zkSync Web3 SDK and a Hardhat project for zkSync smart contracts?
Generated: DETERMINISTIC_011619ecaade5152
Batch ID: 20250612_150342
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://zksync2-testnet.zksync.dev": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://zksync2-${network}.zksync.dev`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://turbo.build/schema.json": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```json
// turbo.json
{
  "$schema": "https://turbo.build/schema.json",
  "pipeline": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": ["dist/**", "build/**"]
    },
    "lint": {
      "dependsOn": [],
      "outputs": []
    },
    "dev": {
      "cache": false
    },
    "test": {
      "dependsOn": ["build"],
      "outputs": []
    }
  }
}
```

```json
// package.json (root)
{
  "name": "zk-monorepo",
  "version": "1.0.0",
  "private": true,
  "workspaces": [
    "apps/*",
    "packages/*"
  ],
  "scripts": {
    "build": "turbo run build",
    "dev": "turbo run dev",
    "lint": "turbo run lint",
    "test": "turbo run test",
    "clean": "rm -rf node_modules && rm -rf apps/*/node_modules && rm -rf packages/*/node_modules"
  },
  "devDependencies": {
    "turbo": "^1.10.12"
  }
}
```

```json
// packages/config/package.json
{
  "name": "@zk-monorepo/config",
  "version": "1.0.0",
  "main": "index.js",
  "types": "index.d.ts",
  "license": "MIT",
  "dependencies": {
    "dotenv": "^16.0.3",
    "ethers": "^5.7.2",
    "zksync-web3": "^0.14.3"
  }
}
```

```javascript
// packages/config/index.js
const { ethers } = require('ethers');
const { Wallet, Provider } = require('zksync-web3');
require('dotenv').config();

const getProvider = (network = 'testnet') => {
  return new Provider(`https://zksync2-${network}.zksync.dev`);
};

const getWallet = (privateKey, network = 'testnet') => {
  const provider = getProvider(network);
  return new Wallet(privateKey || process.env.PRIVATE_KEY, provider);
};

module.exports = {
  getProvider,
  getWallet,
  networks: {
    testnet: 'testnet',
    mainnet: 'mainnet'
  }
};
```

```json
// apps/next-app/package.json
{
  "name": "@zk-monorepo/next-app",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint"
  },
  "dependencies": {
    "@zk-monorepo/config": "*",
    "next": "^13.4.7",
    "react": "^18.2.0",
    "react-dom": "^18.2.0"
  },
  "devDependencies": {
    "eslint": "^8.36.0",
    "eslint-config-next": "^13.4.7"
  }
}
```

```json
// apps/hardhat-project/package.json
{
  "name": "@zk-monorepo/hardhat-project",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "compile": "hardhat compile",
    "test": "hardhat test",
    "deploy": "hardhat run scripts/deploy.js --network zkSyncTestnet"
  },
  "dependencies": {
    "@zk-monorepo/config": "*",
    "@matterlabs/hardhat-zksync-deploy": "^0.6.2",
    "@matterlabs/hardhat-zksync-solc": "^0.3.16",
    "ethers": "^5.7.2",
    "zksync-web3": "^0.14.3"
  },
  "devDependencies": {
    "@nomicfoundation/hardhat-toolbox": "^2.0.0",
    "hardhat": "^2.12.6"
  }
}
```

```javascript
// apps/hardhat-project/hardhat.config.js
require("@nomicfoundation/hardhat-toolbox");
require("@matterlabs/hardhat-zksync-deploy");
require("@matterlabs/hardhat-zksync-solc");
require("@zk-monorepo/config");

/** @type import('hardhat/config').HardhatUserConfig */
module.exports = {
  zksolc: {
    version: "1.3.5",
    compilerSource: "binary",
    settings: {},
  },
  defaultNetwork: "zkSyncTestnet",
  networks: {
    zkSyncTestnet: {
      url: "https://zksync2-testnet.zksync.dev",
      ethNetwork: "goerli",
      zksync: true,
    },
  },
  solidity: {
    version: "0.8.17",
  },
};
```

```javascript
// apps/next-app/pages/index.js
import { getWallet, networks } from '@zk-monorepo/config';

export default function Home() {
  const connectWallet = async () => {
    try {
      const wallet = getWallet();
      const address = await wallet.getAddress();
      console.log('Connected wallet:', address);
    } catch (error) {
      console.error('Error connecting wallet:', error);
    }
  };

  return (
    <div>
      <h1>zkSync Next.js App</h1>
      <button onClick={connectWallet}>Connect Wallet</button>
    </div>
  );
}
```

```javascript
// apps/hardhat-project/scripts/deploy.js
const { getWallet } = require('@zk-monorepo/config');
const { deployContract } = require('@matterlabs/hardhat-zksync-deploy');

async function main() {
  const wallet = getWallet();
  const artifact = await deployContract(
    wallet,
    "Greeter",
    ["Hello, zkSync!"],
    { gasLimit: 500000 }
  );

  console.log(`Contract deployed to: ${artifact.address}`);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
```
