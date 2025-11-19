"""
Generated Code Metadata:
========================
Original URL: https://cheemspet.web.app
Prompt: Create a Node.js API that allows users to interact with the Cheems token, such as buying, selling, or transferring tokens, while ensuring a 100% fair launch and no team reserves.
Generated: DETERMINISTIC_d204d9a7a425e922
Batch ID: 20250622_212546
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required modules
const express = require('express');
const app = express();
const Web3 = require('web3');
const { CheemsToken } = require('./CheemsToken');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Set up Web3 provider
const web3 = new Web3(new Web3.providers.HttpProvider(process.env.INFURA_URL));

// Set up Cheems token contract
const cheemsTokenAddress = process.env.CHEEMS_TOKEN_ADDRESS;
const cheemsToken = new CheemsToken(cheemsTokenAddress, web3);

// Enable CORS and JSON parsing
app.use((req, res, next) => {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept");
  next();
});
app.use(express.json());

// Define API endpoints

/**
 * @api {post} /buy Buy Cheems tokens
 * @apiBody {string} account - User's Ethereum account address
 * @apiBody {string} amount - Amount of tokens to buy (in ETH)
 */
app.post('/buy', async (req, res) => {
  try {
    const { account, amount } = req.body;
    if (!account || !amount) {
      return res.status(400).send({ error: 'Missing required parameters' });
    }

    // Validate account and amount
    if (!web3.utils.isAddress(account)) {
      return res.status(400).send({ error: 'Invalid account address' });
    }

    const ethAmount = web3.utils.toWei(amount, 'ether');
    if (ethAmount <= 0) {
      return res.status(400).send({ error: 'Invalid amount' });
    }

    // Buy tokens
    const tx = await cheemsToken.buyTokens(account, ethAmount);
    res.send({ txHash: tx.hash });
  } catch (error) {
    console.error(error);
    res.status(500).send({ error: 'Failed to buy tokens' });
  }
});

/**
 * @api {post} /sell Sell Cheems tokens
 * @apiBody {string} account - User's Ethereum account address
 * @apiBody {string} amount - Amount of tokens to sell (in Cheems)
 */
app.post('/sell', async (req, res) => {
  try {
    const { account, amount } = req.body;
    if (!account || !amount) {
      return res.status(400).send({ error: 'Missing required parameters' });
    }

    // Validate account and amount
    if (!web3.utils.isAddress(account)) {
      return res.status(400).send({ error: 'Invalid account address' });
    }

    const tokenAmount = web3.utils.toWei(amount, 'cheems');
    if (tokenAmount <= 0) {
      return res.status(400).send({ error: 'Invalid amount' });
    }

    // Sell tokens
    const tx = await cheemsToken.sellTokens(account, tokenAmount);
    res.send({ txHash: tx.hash });
  } catch (error) {
    console.error(error);
    res.status(500).send({ error: 'Failed to sell tokens' });
  }
});

/**
 * @api {post} /transfer Transfer Cheems tokens
 * @apiBody {string} from - Sender's Ethereum account address
 * @apiBody {string} to - Recipient's Ethereum account address
 * @apiBody {string} amount - Amount of tokens to transfer (in Cheems)
 */
app.post('/transfer', async (req, res) => {
  try {
    const { from, to, amount } = req.body;
    if (!from || !to || !amount) {
      return res.status(400).send({ error: 'Missing required parameters' });
    }

    // Validate accounts and amount
    if (!web3.utils.isAddress(from) || !web3.utils.isAddress(to)) {
      return res.status(400).send({ error: 'Invalid account address' });
    }

    const tokenAmount = web3.utils.toWei(amount, 'cheems');
    if (tokenAmount <= 0) {
      return res.status(400).send({ error: 'Invalid amount' });
    }

    // Transfer tokens
    const tx = await cheemsToken.transfer(from, to, tokenAmount);
    res.send({ txHash: tx.hash });
  } catch (error) {
    console.error(error);
    res.status(500).send({ error: 'Failed to transfer tokens' });
  }
});

// Start server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

```javascript
// CheemsToken.js
const web3 = require('web3');
const CheemsTokenABI = require('./CheemsTokenABI.json');

class CheemsToken {
  constructor(address, web3) {
    this.address = address;
    this.web3 = web3;
    this.contract = new web3.eth.Contract(CheemsTokenABI, address);
  }

  async buyTokens(account, amount) {
    const accounts = await this.web3.eth.getAccounts();
    const tx = await this.contract.methods.buyTokens().send({ from: account, value: amount });
    return tx;
  }

  async sellTokens(account, amount) {
    const tx = await this.contract.methods.sellTokens(amount).send({ from: account });
    return tx;
  }

  async transfer(from, to, amount) {
    const tx = await this.contract.methods.transfer(to, amount).send({ from: from });
    return tx;
  }
}

module.exports = { CheemsToken };
```

```json
// CheemsTokenABI.json
[
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
        "name": "from",
        "type": "address"
      },
      {
        "indexed": true,
        "name": "to",
        "type": "address"
      },
      {
        "indexed": false,
        "name": "value",
        "type": "uint256"
      }
    ],
    "name": "Transfer",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "name": "owner",
        "type": "address"
      },
      {
        "indexed": true,
        "name": "spender",
        "type": "address"
      },
      {
        "indexed": false,
        "name": "value",
        "type": "uint256"
      }
    ],
    "name": "Approval",
    "type": "event"
  },
  {
    "inputs": [],
    "name": "name",
    "outputs": [
      {
        "internalType": "string",
        "name": "",
        "type": "string"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "symbol",
    "outputs": [
      {
        "internalType": "string",
        "name": "",
        "type": "string"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "totalSupply",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "owner",
        "type": "address"
      }
    ],
    "name": "balanceOf",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [],
    "name": "buyTokens",
    "outputs": [],
    "stateMutability": "payable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "owner",
        "type": "address"
      },
      {
        "internalType": "address",
        "name": "spender",
        "type": "address"
      }
    ],
    "name": "allowance",
    "outputs": [
      {
        "internalType": "uint256",
        "name": "",
        "type": "uint256"
      }
    ],
    "stateMutability": "view",
    "type": "function"
  },
  {
    "inputs": [
      {
        "internalType": "address",
        "name": "spender",
        "type": "address"
      },
      {
        "internalType": "uint256",
        "name": "amount",
        "type": "uint256"
      }
    ],
    "name": "approve",
    "outputs": [
      {
        "internalType": "bool",
        "name": "",
        "type": "bool"
      }
    ],
    "stateMutability": "nonpayable",
    "
