"""
Generated Code Metadata:
========================
Original URL: https://kid-69m.pages.dev
Prompt: Create a prototype for a Web3-enabled e-commerce platform where AKCB holders can purchase exclusive streetwear and physical collectibles tied to their NFTs.
Generated: DETERMINISTIC_992600483d32d960
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Web3 E-commerce Platform Prototype**
=====================================

**dependencies:**
* `web3`: 1.8.0
* `ethers.js`: 5.4.1
* `mongodb`: 3.6.3
* `express`: 4.17.1

**models/User.js**
```javascript
// Import required libraries
const mongoose = require('mongoose');

/**
 * User model
 * @typedef {Object} User
 * @property {string} _id
 * @property {string} address
 * @property {string[]} nftIds
 */
const userSchema = new mongoose.Schema({
  address: { type: String, unique: true },
  nftIds: [{ type: String }]
});

module.exports = mongoose.model('User', userSchema);
```

**models/NFT.js**
```javascript
// Import required libraries
const mongoose = require('mongoose');

/**
 * NFT model
 * @typedef {Object} NFT
 * @property {string} _id
 * @property {string} name
 * @property {string} description
 * @property {string} image
 * @property {number} price
 */
const nftSchema = new mongoose.Schema({
  name: String,
  description: String,
  image: String,
  price: Number
});

module.exports = mongoose.model('NFT', nftSchema);
```

**models/Product.js**
```javascript
// Import required libraries
const mongoose = require('mongoose');

/**
 * Product model
 * @typedef {Object} Product
 * @property {string} _id
 * @property {string} name
 * @property {string} description
 * @property {string} image
 * @property {number} price
 * @property {string} nftId
 */
const productSchema = new mongoose.Schema({
  name: String,
  description: String,
  image: String,
  price: Number,
  nftId: { type: String, ref: 'NFT' }
});

module.exports = mongoose.model('Product', productSchema);
```

**utils/web3.js**
```javascript
// Import required libraries
const Web3 = require('web3');
const { ethers } = require('ethers');

/**
 * Web3 utility functions
 */
const web3 = new Web3(process.env.INFURA_URL);
const provider = new ethers.providers.InfuraProvider('mainnet', process.env.INFURA_PROJECT_ID);

module.exports = {
  /**
   * Get user's NFTs
   * @param {string} address
   * @returns {Promise<string[]>}
   */
  async getUserNFTs(address) {
    try {
      const balance = await provider.getBalance(address);
      if (balance.eq(0)) {
        throw new Error('User has no balance');
      }
      // Assuming AKCB contract ABI and address are known
      const akcbContract = new ethers.Contract('0x...', ['function balanceOf(address owner) view returns (uint256)'], provider);
      const nftIds = [];
      for (let i = 0; i < await akcbContract.balanceOf(address); i++) {
        const tokenId = await akcbContract.tokenOfOwnerByIndex(address, i);
        nftIds.push(tokenId.toString());
      }
      return nftIds;
    } catch (error) {
      console.error(error);
      throw error;
    }
  },

  /**
   * Verify user's ownership of NFT
   * @param {string} address
   * @param {string} nftId
   * @returns {Promise<boolean>}
   */
  async verifyNFT(address, nftId) {
    try {
      // Assuming AKCB contract ABI and address are known
      const akcbContract = new ethers.Contract('0x...', ['function ownerOf(uint256 tokenId) view returns (address)'], provider);
      const owner = await akcbContract.ownerOf(nftId);
      return owner.toLowerCase() === address.toLowerCase();
    } catch (error) {
      console.error(error);
      throw error;
    }
  }
};
```

**controllers/UserController.js**
```javascript
// Import required libraries
const express = require('express');
const router = express.Router();
const User = require('../models/User');
const web3 = require('../utils/web3');

/**
 * User controller
 */
router.get('/:address', async (req, res) => {
  try {
    const address = req.params.address;
    const user = await User.findOne({ address });
    if (!user) {
      res.status(404).send({ message: 'User not found' });
      return;
    }
    res.send(user);
  } catch (error) {
    console.error(error);
    res.status(500).send({ message: 'Internal Server Error' });
  }
});

router.post('/:address/nfts', async (req, res) => {
  try {
    const address = req.params.address;
    const nftIds = await web3.getUserNFTs(address);
    const user = await User.findOneAndUpdate({ address }, { nftIds }, { upsert: true, new: true });
    res.send(user);
  } catch (error) {
    console.error(error);
    res.status(500).send({ message: 'Internal Server Error' });
  }
});

module.exports = router;
```

**controllers/ProductController.js**
```javascript
// Import required libraries
const express = require('express');
const router = express.Router();
const Product = require('../models/Product');
const web3 = require('../utils/web3');

/**
 * Product controller
 */
router.get('/', async (req, res) => {
  try {
    const products = await Product.find().populate('nftId');
    res.send(products);
  } catch (error) {
    console.error(error);
    res.status(500).send({ message: 'Internal Server Error' });
  }
});

router.post('/:productId/purchase', async (req, res) => {
  try {
    const productId = req.params.productId;
    const product = await Product.findById(productId);
    if (!product) {
      res.status(404).send({ message: 'Product not found' });
      return;
    }
    const { address } = req.body;
    const nftId = product.nftId;
    const isOwner = await web3.verifyNFT(address, nftId);
    if (!isOwner) {
      res.status(401).send({ message: 'Unauthorized' });
      return;
    }
    // Process payment and shipment
    res.send({ message: 'Product purchased successfully' });
  } catch (error) {
    console.error(error);
    res.status(500).send({ message: 'Internal Server Error' });
  }
});

module.exports = router;
```

**app.js**
```javascript
// Import required libraries
const express = require('express');
const app = express();
const mongoose = require('mongoose');
const userController = require('./controllers/UserController');
const productController = require('./controllers/ProductController');

mongoose.connect('mongodb://localhost/web3-ecommerce', { useNewUrlParser: true, useUnifiedTopology: true });

app.use(express.json());
app.use('/users', userController);
app.use('/products', productController);

app.listen(3000, () => {
  console.log('Server listening on port 3000');
});
```
