"""
Generated Code Metadata:
========================
Original URL: https://ethkind.com
Prompt: Generate code to implement a simple Ethereum-based pledge system using JavaScript.
Generated: DETERMINISTIC_1f5c1f0793db11d1
Batch ID: 20250622_210145
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_PROJECT_ID": {
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
// Import required libraries
const Web3 = require('web3');
const { ethers } = require('ethers');

// Define the PledgeSystem contract ABI
const pledgeSystemABI = [
  {
    "inputs": [],
    "stateMutability": "nonpayable",
    "type": "constructor"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "name": "pledger",
        "type": "address"
      },
      {
        "indexed": true,
        "name": "beneficiary",
        "type": "address"
      },
      {
        "indexed": false,
        "name": "amount",
        "type": "uint256"
      },
      {
        "indexed": false,
        "name": "deadline",
        "type": "uint256"
      }
    ],
    "name": "NewPledge",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "name": "pledger",
        "type": "address"
      },
      {
        "indexed": true,
        "name": "beneficiary",
        "type": "address"
      },
      {
        "indexed": false,
        "name": "amount",
        "type": "uint256"
      }
    ],
    "name": "PledgeFulfilled",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "name": "pledger",
        "type": "address"
      },
      {
        "indexed": true,
        "name": "beneficiary",
        "type": "address"
      },
      {
        "indexed": false,
        "name": "amount",
        "type": "uint256"
      }
    ],
    "name": "PledgeRefunded",
    "type": "event"
  },
  {
    "inputs": [
      {
        "name": "beneficiary",
        "type": "address"
      },
      {
        "name": "amount",
        "type": "uint256"
      },
      {
        "name": "deadline",
        "type": "uint256"
      }
    ],
    "name": "createPledge",
    "outputs": [],
    "stateMutability": "payable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "name": "pledger",
        "type": "address"
      },
      {
        "name": "beneficiary",
        "type": "address"
      }
    ],
    "name": "fulfillPledge",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "name": "pledger",
        "type": "address"
      },
      {
        "name": "beneficiary",
        "type": "address"
      }
    ],
    "name": "refundPledge",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "name": "pledger",
        "type": "address"
      },
      {
        "name": "beneficiary",
        "type": "address"
      }
    ],
    "name": "getPledge",
    "outputs": [
      {
        "name": "",
        "type": "address"
      },
      {
        "name": "",
        "type": "uint256"
      },
      {
        "name": "",
        "type": "uint256"
      },
      {
        "name": "",
        "type": "bool"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  }
];

// Define the PledgeSystem contract address
const pledgeSystemAddress = '0x...'; // Replace with deployed contract address

// Create a new Web3 provider
const provider = new ethers.providers.JsonRpcProvider('https://mainnet.infura.io/v3/YOUR_PROJECT_ID');

// Create a new contract instance
const contract = new ethers.Contract(pledgeSystemAddress, pledgeSystemABI, provider);

// Define a class for the pledge system
class PledgeSystem {
  constructor() {
    this.provider = provider;
    this.contract = contract;
  }

  // Create a new pledge
  async createPledge(beneficiary, amount, deadline) {
    try {
      // Get the current account
      const accounts = await this.provider.listAccounts();
      const account = accounts[0];

      // Create a new pledge
      const tx = await this.contract.connect(account).createPledge(beneficiary, amount, deadline, {
        value: amount,
      });

      // Wait for the transaction to confirm
      await tx.wait();

      console.log(`Pledge created: ${tx.hash}`);
    } catch (error) {
      console.error(`Error creating pledge: ${error.message}`);
    }
  }

  // Fulfill a pledge
  async fulfillPledge(pledger, beneficiary) {
    try {
      // Get the current account
      const accounts = await this.provider.listAccounts();
      const account = accounts[0];

      // Fulfill the pledge
      const tx = await this.contract.connect(account).fulfillPledge(pledger, beneficiary);

      // Wait for the transaction to confirm
      await tx.wait();

      console.log(`Pledge fulfilled: ${tx.hash}`);
    } catch (error) {
      console.error(`Error fulfilling pledge: ${error.message}`);
    }
  }

  // Refund a pledge
  async refundPledge(pledger, beneficiary) {
    try {
      // Get the current account
      const accounts = await this.provider.listAccounts();
      const account = accounts[0];

      // Refund the pledge
      const tx = await this.contract.connect(account).refundPledge(pledger, beneficiary);

      // Wait for the transaction to confirm
      await tx.wait();

      console.log(`Pledge refunded: ${tx.hash}`);
    } catch (error) {
      console.error(`Error refunding pledge: ${error.message}`);
    }
  }

  // Get a pledge
  async getPledge(pledger, beneficiary) {
    try {
      // Get the pledge
      const pledge = await this.contract.getPledge(pledger, beneficiary);

      console.log(`Pledge: ${pledge}`);
    } catch (error) {
      console.error(`Error getting pledge: ${error.message}`);
    }
  }
}

// Example usage
async function main() {
  const pledgeSystem = new PledgeSystem();

  // Create a new pledge
  await pledgeSystem.createPledge('0x...', 100, 1643723900);

  // Fulfill a pledge
  await pledgeSystem.fulfillPledge('0x...', '0x...');

  // Refund a pledge
  await pledgeSystem.refundPledge('0x...', '0x...');

  // Get a pledge
  await pledgeSystem.getPledge('0x...', '0x...');
}

main().catch((error) => console.error(error));
```
