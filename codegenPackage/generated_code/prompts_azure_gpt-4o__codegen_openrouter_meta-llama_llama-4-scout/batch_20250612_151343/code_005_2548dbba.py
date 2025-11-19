"""
Generated Code Metadata:
========================
Original URL: https://blockdag-8bz.pages.dev
Prompt: Develop a modular architecture for a blockchain explorer UI that aligns with BlockDAG's roadmap requirements.
Generated: DETERMINISTIC_2548dbba75b5de1b
Batch ID: 20250612_151343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// blockchain-explorer.js

/**
 * Blockchain Explorer UI
 * 
 * This module provides a modular architecture for a blockchain explorer UI
 * that aligns with BlockDAG's roadmap requirements.
 */

// Import dependencies
const express = require('express');
const app = express();
const mongoose = require('mongoose');
const logger = require('./logger');
const blockService = require('./services/block.service');
const transactionService = require('./services/transaction.service');
const addressService = require('./services/address.service');

// Connect to MongoDB
mongoose.connect('mongodb://localhost/blockdag', { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => logger.info('Connected to MongoDB'))
  .catch((err) => logger.error('Error connecting to MongoDB:', err));

// Define API routes
const apiRoutes = require('./routes/api.routes');
app.use('/api', apiRoutes);

// Define UI routes
const uiRoutes = require('./routes/ui.routes');
app.use('/', uiRoutes);

// Error handling middleware
app.use((err, req, res, next) => {
  logger.error('Error:', err);
  res.status(500).send({ message: 'Internal Server Error' });
});

// Start server
const port = 3000;
app.listen(port, () => {
  logger.info(`Server started on port ${port}`);
});
```

```javascript
// services/block.service.js

/**
 * Block Service
 * 
 * Provides functions for interacting with blocks in the blockchain.
 */

const mongoose = require('mongoose');
const Block = require('../models/block.model');

/**
 * Get all blocks
 * 
 * @returns {Promise<Block[]>} A promise that resolves to an array of blocks.
 */
async function getAllBlocks() {
  try {
    return await Block.find().sort({ timestamp: -1 });
  } catch (err) {
    throw new Error('Error getting blocks:', err);
  }
}

/**
 * Get block by hash
 * 
 * @param {string} hash The hash of the block to retrieve.
 * @returns {Promise<Block>} A promise that resolves to the block.
 */
async function getBlockByHash(hash) {
  try {
    return await Block.findOne({ hash });
  } catch (err) {
    throw new Error('Error getting block:', err);
  }
}

module.exports = { getAllBlocks, getBlockByHash };
```

```javascript
// services/transaction.service.js

/**
 * Transaction Service
 * 
 * Provides functions for interacting with transactions in the blockchain.
 */

const mongoose = require('mongoose');
const Transaction = require('../models/transaction.model');

/**
 * Get all transactions
 * 
 * @returns {Promise<Transaction[]>} A promise that resolves to an array of transactions.
 */
async function getAllTransactions() {
  try {
    return await Transaction.find().sort({ timestamp: -1 });
  } catch (err) {
    throw new Error('Error getting transactions:', err);
  }
}

/**
 * Get transaction by hash
 * 
 * @param {string} hash The hash of the transaction to retrieve.
 * @returns {Promise<Transaction>} A promise that resolves to the transaction.
 */
async function getTransactionByHash(hash) {
  try {
    return await Transaction.findOne({ hash });
  } catch (err) {
    throw new Error('Error getting transaction:', err);
  }
}

module.exports = { getAllTransactions, getTransactionByHash };
```

```javascript
// services/address.service.js

/**
 * Address Service
 * 
 * Provides functions for interacting with addresses in the blockchain.
 */

const mongoose = require('mongoose');
const Address = require('../models/address.model');

/**
 * Get address balance
 * 
 * @param {string} address The address to retrieve the balance for.
 * @returns {Promise<number>} A promise that resolves to the balance.
 */
async function getAddressBalance(address) {
  try {
    const addr = await Address.findOne({ address });
    return addr.balance;
  } catch (err) {
    throw new Error('Error getting address balance:', err);
  }
}

module.exports = { getAddressBalance };
```

```javascript
// models/block.model.js

/**
 * Block Model
 * 
 * Represents a block in the blockchain.
 */

const mongoose = require('mongoose');

const blockSchema = new mongoose.Schema({
  hash: String,
  previousHash: String,
  timestamp: Date,
  transactions: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Transaction' }]
});

const Block = mongoose.model('Block', blockSchema);

module.exports = Block;
```

```javascript
// models/transaction.model.js

/**
 * Transaction Model
 * 
 * Represents a transaction in the blockchain.
 */

const mongoose = require('mongoose');

const transactionSchema = new mongoose.Schema({
  hash: String,
  from: String,
  to: String,
  amount: Number,
  timestamp: Date
});

const Transaction = mongoose.model('Transaction', transactionSchema);

module.exports = Transaction;
```

```javascript
// models/address.model.js

/**
 * Address Model
 * 
 * Represents an address in the blockchain.
 */

const mongoose = require('mongoose');

const addressSchema = new mongoose.Schema({
  address: String,
  balance: Number
});

const Address = mongoose.model('Address', addressSchema);

module.exports = Address;
```

```javascript
// routes/api.routes.js

/**
 * API Routes
 * 
 * Defines API routes for the blockchain explorer.
 */

const express = require('express');
const router = express.Router();
const blockService = require('../services/block.service');
const transactionService = require('../services/transaction.service');
const addressService = require('../services/address.service');

router.get('/blocks', async (req, res) => {
  try {
    const blocks = await blockService.getAllBlocks();
    res.json(blocks);
  } catch (err) {
    res.status(500).json({ message: 'Error getting blocks' });
  }
});

router.get('/blocks/:hash', async (req, res) => {
  try {
    const block = await blockService.getBlockByHash(req.params.hash);
    res.json(block);
  } catch (err) {
    res.status(404).json({ message: 'Block not found' });
  }
});

router.get('/transactions', async (req, res) => {
  try {
    const transactions = await transactionService.getAllTransactions();
    res.json(transactions);
  } catch (err) {
    res.status(500).json({ message: 'Error getting transactions' });
  }
});

router.get('/transactions/:hash', async (req, res) => {
  try {
    const transaction = await transactionService.getTransactionByHash(req.params.hash);
    res.json(transaction);
  } catch (err) {
    res.status(404).json({ message: 'Transaction not found' });
  }
});

router.get('/addresses/:address/balance', async (req, res) => {
  try {
    const balance = await addressService.getAddressBalance(req.params.address);
    res.json({ balance });
  } catch (err) {
    res.status(404).json({ message: 'Address not found' });
  }
});

module.exports = router;
```

```javascript
// routes/ui.routes.js

/**
 * UI Routes
 * 
 * Defines UI routes for the blockchain explorer.
 */

const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
  res.render('index');
});

module.exports = router;
```

```javascript
// logger.js

/**
 * Logger
 * 
 * Provides a simple logging utility.
 */

const winston = require('winston');

const logger = winston.createLogger({
  level: 'info',
  format: winston.format.json(),
  transports: [
    new winston.transports.Console(),
    new winston.transports.File({ filename: 'error.log', level: 'error' }),
    new winston.transports.File({ filename: 'combined.log' })
  ]
});

module.exports = logger;
```
