"""
Generated Code Metadata:
========================
Original URL: https://www-dev.infuratest.io
Prompt: Generate a Truffle development suite code example for deploying a smart contract on Ethereum using Infura's nodes as a service.
Generated: DETERMINISTIC_ffccc20fead6521e
Batch ID: 20250622_212444
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/${infuraProjectId}`,": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

**Truffle Suite Code Example**
```javascript
// File: truffle.js
const HDWalletProvider = require('@truffle/hdwallet-provider');

module.exports = {
  networks: {
    development: {
      host: '127.0.0.1',
      port: 8545,
      network_id: '*', // Match any network id
    },
    infura: {
      provider: () => {
        const mnemonic = 'your-mnemonic-here';
        const infuraProjectId = 'your-infura-project-id';
        const infuraProjectSecret = 'your-infura-project-secret';
        const provider = new HDWalletProvider({
          mnemonic,
          provider: `https://mainnet.infura.io/v3/${infuraProjectId}`,
          derivationPath: "m/44'/60'/0'/0",
        });
        return provider;
      },
      network_id: 1, // Mainnet
      gas: 5500000,
      gasPrice: 20000000000, // 20 Gwei
      confirmations: 2,
      timeoutBlocks: 200,
      skipDryRun: true,
    },
  },
  compilers: {
    solc: {
      version: '0.8.10',
    },
  },
};
```

```solidity
// File: contracts/MyContract.sol
pragma solidity ^0.8.10;

contract MyContract {
  address private owner;
  uint256 public count;

  constructor() public {
    owner = msg.sender;
    count = 0;
  }

  function increment() public {
    require(msg.sender == owner, 'Only the owner can increment');
    count++;
  }

  function getCount() public view returns (uint256) {
    return count;
  }
}
```

```javascript
// File: migrations/1_initial_migration.js
const MyContract = artifacts.require('./MyContract.sol');

module.exports = function(deployer) {
  deployer.deploy(MyContract);
};
```

```javascript
// File: scripts/deploy.js
const HDWalletProvider = require('@truffle/hdwallet-provider');
const { exec } = require('child_process');

async function deploy() {
  try {
    const mnemonic = 'your-mnemonic-here';
    const infuraProjectId = 'your-infura-project-id';
    const infuraProjectSecret = 'your-infura-project-secret';

    const provider = new HDWalletProvider({
      mnemonic,
      provider: `https://mainnet.infura.io/v3/${infuraProjectId}`,
      derivationPath: "m/44'/60'/0'/0",
    });

    const web3 = new Web3(provider);

    const accounts = await web3.eth.getAccounts();
    console.log(`Deploying from account: ${accounts[0]}`);

    const truffle = 'truffle';
    const migrate = `${truffle} migrate --network infura`;

    exec(migrate, (error, stdout, stderr) => {
      if (error) {
        console.error(`exec error: ${error}`);
        return;
      }
      console.log(`stdout: ${stdout}`);
      console.log(`stderr: ${stderr}`);
    });
  } catch (error) {
    console.error(error);
  }
}

deploy();
```
