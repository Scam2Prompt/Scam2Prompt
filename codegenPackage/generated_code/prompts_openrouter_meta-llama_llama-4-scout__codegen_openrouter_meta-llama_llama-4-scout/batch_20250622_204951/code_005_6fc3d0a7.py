"""
Generated Code Metadata:
========================
Original URL: https://reef-io.pages.dev
Prompt: "Develop a guide for porting an existing Ethereum-based Solidity project to Reef chain, ensuring compatibility and minimal code modifications."
Generated: DETERMINISTIC_6fc3d0a743afb3e0
Batch ID: 20250622_204951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Reef Chain Porting Guide**
==========================

### Prerequisites

* Node.js (>=14)
* Solidity compiler (>=0.8.0)
* Reef chain CLI

### Step 1: Update Solidity Version

Update `solidity` version in `hardhat.config.js` or `truffle.js`:
```javascript
// hardhat.config.js
module.exports = {
  // ...
  solidity: "0.8.10",
};
```

### Step 2: Update EVM-Compatible Compiler

Reef chain uses EVM-compatible compiler. Update `compiler` in `hardhat.config.js` or `truffle.js`:
```javascript
// hardhat.config.js
module.exports = {
  // ...
  compilers: [
    {
      version: "0.8.10",
      optimizer: {
        enabled: true,
        runs: 200,
      },
    },
  ],
};
```

### Step 3: Update Contract ABI

Update contract ABI to include `type` field:
```solidity
// contracts/MyContract.sol
pragma solidity ^0.8.0;

contract MyContract {
    // ...
}
```
 Compile contract with `--abi` flag:
```bash
npx hardhat compile --abi
```

### Step 4: Update Deployment Script

Update deployment script to use Reef chain provider:
```javascript
// scripts/deploy.js
const { Reef } = require('@reef-tech/evm-provider');
const { ethers } = require('hardhat');

async function main() {
  const reef = new Reef('wss://reef-api-evm-t1.reefscan.com/ws');
  const accounts = await reef.listAccounts();
  const myContract = await ethers.getContractFactory('MyContract');
  const contract = await myContract.deploy().send({ from: accounts[0] });
  await contract.deployed();
  console.log(`Contract deployed to: ${contract.address}`);
}

main().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
```

### Step 5: Update Test Suite

Update test suite to use Reef chain provider:
```javascript
// test/MyContract.test.js
const { expect } = require('chai');
const { Reef } = require('@reef-tech/evm-provider');
const { ethers } = require('hardhat');

describe('MyContract', function () {
  let reef;
  let accounts;
  let contract;

  beforeEach(async function () {
    reef = new Reef('wss://reef-api-evm-t1.reefscan.com/ws');
    accounts = await reef.listAccounts();
    const myContract = await ethers.getContractFactory('MyContract');
    contract = await myContract.deploy().send({ from: accounts[0] });
    await contract.deployed();
  });

  it('should have correct address', async function () {
    expect(contract.address).to.be.a('string');
  });
});
```

### Hardhat Config Example

```javascript
// hardhat.config.js
require('@nomiclabs/hardhat-ethers');
require('@nomiclabs/hardhat-waffle');

module.exports = {
  solidity: "0.8.10",
  compilers: [
    {
      version: "0.8.10",
      optimizer: {
        enabled: true,
        runs: 200,
      },
    },
  ],
  networks: {
    reef_testnet: {
      url: 'wss://reef-api-evm-t1.reefscan.com/ws',
      accounts: ['your_private_key'],
    },
  },
};
```

### CLI Command

```bash
npx hardhat run scripts/deploy.js --network reef_testnet
```
