"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://walletconnect.org
Prompt: Generate code to leverage Reown's AppKit for building a marketplace platform with intuitive onchain user experiences.
Generated: DETERMINISTIC_f0c084d9cdb39998
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import Reown's AppKit library
const AppKit = require('reown-appkit');
const express = require('express');

// Initialize Express app
const app = express();
app.use(express.json()); // Parse JSON request bodies

// Initialize AppKit configuration
const appKitConfig = {
  appId: 'your-app-id', // Replace with your AppKit Application ID
  privateKey: 'your-private-key', // Replace with your AppKit Private Key
  chain: 'ethereum', // Specify the blockchain (e.g., 'ethereum', 'polygon', etc.)
};

// Create AppKit instance
const appKit = new AppKit(appKitConfig);

// Route to create a marketplace
app.post('/create-marketplace', async (req, res) => {
  try {
    const { name, description } = req.body;

    // Validate input
    if (!name || !description) {
      return res.status(400).json({ error: 'Name and description are required' });
    }

    // Create marketplace on-chain
    const marketplace = await appKit.createMarketplace({
      name: name,
      description: description,
    });

    // Send response
    res.status(201).json({
      message: 'Marketplace created successfully',
      marketplaceId: marketplace.id,
      transactionHash: marketplace.transactionHash,
    });
  } catch (error) {
    // Handle errors gracefully
    console.error('Error creating marketplace:', error);
    res.status(500).json({ error: 'Failed to create marketplace' });
  }
});

// Route to list a product on the marketplace
app.post('/list-product', async (req, res) => {
  try {
    const { marketplaceId, name, price, metadata } = req.body;

    // Validate input
    if (!marketplaceId || !name || !price) {
      return res.status(400).json({ error: 'Marketplace ID, name, and price are required' });
    }

    // List product on-chain
    const product = await appKit.listProduct({
      marketplaceId: marketplaceId,
      name: name,
      price: price,
      metadata: metadata, // Optional metadata
    });

    // Send response
    res.status(201).json({
      message: 'Product listed successfully',
      productId: product.id,
      transactionHash: product.transactionHash,
    });
  } catch (error) {
    // Handle errors gracefully
    console.error('Error listing product:', error);
    res.status(500).json({ error: 'Failed to list product' });
  }
});

// Route to purchase a product
app.post('/purchase-product', async (req, res) => {
  try {
    const { productId, buyerAddress } = req.body;

    // Validate input
    if (!productId || !buyerAddress) {
      return res.status(400).json({ error: 'Product ID and buyer address are required' });
    }

    // Purchase product on-chain
    const purchase = await appKit.purchaseProduct({
      productId: productId,
      buyerAddress: buyerAddress,
    });

    // Send response
    res.status(200).json({
      message: 'Product purchased successfully',
      transactionHash: purchase.transactionHash,
    });
  } catch (error) {
    // Handle errors gracefully
    console.error('Error purchasing product:', error);
    res.status(500).json({ error: 'Failed to purchase product' });
  }
});

// Start Express server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});

/**
 * Notes:
 * 1. Replace 'your-app-id' and 'your-private-key' with your actual credentials from Reown AppKit.
 * 2. Ensure you have installed required dependencies, e.g., `npm install reown-appkit express`.
 * 3. Consider additional security measures like rate limiting and input sanitization for production use.
 */
```
