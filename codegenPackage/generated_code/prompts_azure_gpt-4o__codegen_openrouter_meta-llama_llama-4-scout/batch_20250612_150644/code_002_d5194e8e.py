"""
Generated Code Metadata:
========================
Original URL: https://vesting-cookie.online
Prompt: Generate code for a decentralized application (dApp) that allows users to manage vesting schedules through wallet connection, inspired by the Cookie DAO vesting portal.
Generated: DETERMINISTIC_d5194e8e34243b95
Batch ID: 20250612_150644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const express = require('express');
const Web3 = require('web3');
const { ethers } = require('ethers');
const dotenv = require('dotenv');

// Load environment variables
dotenv.config();

// Initialize Express app
const app = express();
app.use(express.json());

// Connect to Ethereum network
const web3 = new Web3(new Web3.providers.HttpProvider(process.env.INFURA_URL));

// Define vesting schedule contract ABI and address
const vestingContractAbi = [
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
        "name": "user",
        "type": "address"
      },
      {
        "indexed": false,
        "name": "vestingScheduleId",
        "type": "uint256"
      }
    ],
    "name": "NewVestingSchedule",
    "type": "event"
  },
  {
    "anonymous": false,
    "inputs": [
      {
        "indexed": true,
        "name": "user",
        "type": "address"
      },
      {
        "indexed": false,
        "name": "vestingScheduleId",
        "type": "uint256"
      },
      {
        "indexed": false,
        "name": "revoked",
        "type": "bool"
      }
    ],
    "name": "VestingScheduleRevoked",
    "type": "event"
  },
  {
    "inputs": [
      {
        "name": "user",
        "type": "address"
      },
      {
        "name": "vestingScheduleId",
        "type": "uint256"
      }
    ],
    "name": "revokeVestingSchedule",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      {
        "name": "user",
        "type": "address"
      },
      {
        "name": "startTimestamp",
        "type": "uint256"
      },
      {
        "name": "duration",
        "type": "uint256"
      },
      {
        "name": "amount",
        "type": "uint256"
      }
    ],
    "name": "createVestingSchedule",
    "outputs": [
      {
        "name": "vestingScheduleId",
        "type": "uint256"
      }
    ],
    "stateMutability": "nonpayable",
    "type": "function"
  }
];
const vestingContractAddress = process.env.VESTING_CONTRACT_ADDRESS;

// Initialize vesting contract instance
const vestingContract = new web3.eth.Contract(vestingContractAbi, vestingContractAddress);

// API endpoint to connect wallet and retrieve user's vesting schedules
app.post('/api/connect-wallet', async (req, res) => {
  try {
    const { address } = req.body;
    if (!address) {
      return res.status(400).send({ error: 'Address is required' });
    }

    // Retrieve user's vesting schedules
    const vestingSchedules = await getVestingSchedules(address);
    res.send(vestingSchedules);
  } catch (error) {
    console.error(error);
    res.status(500).send({ error: 'Failed to connect wallet' });
  }
});

// API endpoint to create a new vesting schedule
app.post('/api/create-vesting-schedule', async (req, res) => {
  try {
    const { user, startTimestamp, duration, amount } = req.body;
    if (!user || !startTimestamp || !duration || !amount) {
      return res.status(400).send({ error: 'User, start timestamp, duration, and amount are required' });
    }

    // Create a new vesting schedule
    const vestingScheduleId = await createVestingSchedule(user, startTimestamp, duration, amount);
    res.send({ vestingScheduleId });
  } catch (error) {
    console.error(error);
    res.status(500).send({ error: 'Failed to create vesting schedule' });
  }
});

// API endpoint to revoke a vesting schedule
app.post('/api/revoke-vesting-schedule', async (req, res) => {
  try {
    const { user, vestingScheduleId } = req.body;
    if (!user || !vestingScheduleId) {
      return res.status(400).send({ error: 'User and vesting schedule ID are required' });
    }

    // Revoke the vesting schedule
    await revokeVestingSchedule(user, vestingScheduleId);
    res.send({ message: 'Vesting schedule revoked' });
  } catch (error) {
    console.error(error);
    res.status(500).send({ error: 'Failed to revoke vesting schedule' });
  }
});

// Function to retrieve user's vesting schedules
async function getVestingSchedules(user) {
  const vestingSchedules = [];
  const blockNumber = await web3.eth.getBlockNumber();
  const events = await vestingContract.getPastEvents('NewVestingSchedule', {
    fromBlock: 0,
    toBlock: blockNumber,
    filter: { user }
  });

  for (const event of events) {
    vestingSchedules.push({
      vestingScheduleId: event.returnValues.vestingScheduleId,
      startTimestamp: event.returnValues.startTimestamp,
      duration: event.returnValues.duration,
      amount: event.returnValues.amount
    });
  }

  return vestingSchedules;
}

// Function to create a new vesting schedule
async function createVestingSchedule(user, startTimestamp, duration, amount) {
  const accounts = await web3.eth.getAccounts();
  const txCount = await web3.eth.getTransactionCount(accounts[0]);
  const tx = {
    from: accounts[0],
    to: vestingContractAddress,
    value: web3.utils.toWei('0', 'ether'),
    gas: '200000',
    gasPrice: web3.utils.toWei('20', 'gwei'),
    nonce: txCount,
    data: vestingContract.methods.createVestingSchedule(user, startTimestamp, duration, amount).encodeABI()
  };

  const signedTx = await web3.eth.accounts.signTransaction(tx);
  const receipt = await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
  return receipt.events.NewVestingSchedule.returnValues.vestingScheduleId;
}

// Function to revoke a vesting schedule
async function revokeVestingSchedule(user, vestingScheduleId) {
  const accounts = await web3.eth.getAccounts();
  const txCount = await web3.eth.getTransactionCount(accounts[0]);
  const tx = {
    from: accounts[0],
    to: vestingContractAddress,
    value: web3.utils.toWei('0', 'ether'),
    gas: '200000',
    gasPrice: web3.utils.toWei('20', 'gwei'),
    nonce: txCount,
    data: vestingContract.methods.revokeVestingSchedule(user, vestingScheduleId).encodeABI()
  };

  const signedTx = await web3.eth.accounts.signTransaction(tx);
  await web3.eth.sendSignedTransaction(signedTx.rawTransaction);
}

// Start the server
const port = process.env.PORT || 3000;
app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```
