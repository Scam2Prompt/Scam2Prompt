"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://drophunter.net
Prompt: Create a Node.js script that fetches data from an API and identifies changes in product inventory, simulating functionality similar to Drop Hunter.
Generated: DETERMINISTIC_483a2e550dea5473
Batch ID: 20250612_151644
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://example.com/api/products": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// drop-hunter.js

// Import necessary modules
const axios = require('axios'); // For HTTP requests
const fs = require('fs'); // For reading and writing local files

// Configuration for the script
const CONFIG = {
  apiUrl: 'https://example.com/api/products', // Replace with the real API URL
  dataFile: 'inventory.json', // File to store the previous inventory state
  checkInterval: 60000, // Interval to check for updates (in milliseconds)
};

// Function to fetch product data from the API
async function fetchProductData(apiUrl) {
  try {
    const response = await axios.get(apiUrl);
    return response.data; // Return the fetched data (assuming it's JSON)
  } catch (error) {
    console.error('Error fetching product data:', error.message);
    throw new Error('Failed to fetch product data');
  }
}

// Function to load previous inventory state from file
function loadPreviousInventory(filePath) {
  try {
    if (fs.existsSync(filePath)) {
      const data = fs.readFileSync(filePath, 'utf-8');
      return JSON.parse(data); // Parse and return JSON data
    }
    return {}; // Return an empty object if file doesn't exist
  } catch (error) {
    console.error('Error loading previous inventory:', error.message);
    return {}; // Return an empty object on error
  }
}

// Function to save current inventory state to file
function saveInventory(filePath, inventory) {
  try {
    fs.writeFileSync(filePath, JSON.stringify(inventory, null, 2));
  } catch (error) {
    console.error('Error saving inventory:', error.message);
  }
}

// Function to compare inventories and identify changes
function compareInventories(previousInventory, currentInventory) {
  const changes = [];
  const previousKeys = Object.keys(previousInventory);
  const currentKeys = Object.keys(currentInventory);

  // Check for new products and restocked items
  currentKeys.forEach((productId) => {
    const currentItem = currentInventory[productId];
    const previousItem = previousInventory[productId];
    if (!previousItem) {
      changes.push({ type: 'new', product: currentItem });
    } else if (currentItem.stock > previousItem.stock) {
      changes.push({ type: 'restocked', product: currentItem });
    }
  });

  // Check for out-of-stock items
  previousKeys.forEach((productId) => {
    const previousItem = previousInventory[productId];
    const currentItem = currentInventory[productId];
    if (currentItem && currentItem.stock === 0 && previousItem.stock > 0) {
      changes.push({ type: 'out-of-stock', product: currentItem });
    }
  });

  return changes;
}

// Function to monitor inventory changes
async function monitorInventory() {
  console.log('Starting inventory monitoring...');

  try {
    // Load previous inventory from file
    const previousInventory = loadPreviousInventory(CONFIG.dataFile);

    // Fetch current inventory from the API
    const currentInventoryData = await fetchProductData(CONFIG.apiUrl);

    // Transform current inventory into an easily comparable format
    const currentInventory = currentInventoryData.reduce((acc, item) => {
      acc[item.id] = item; // Map product ID to product object
      return acc;
    }, {});

    // Compare inventories and identify changes
    const changes = compareInventories(previousInventory, currentInventory);

    // Log detected changes
    if (changes.length > 0) {
      console.log('Detected inventory changes:');
      changes.forEach((change) => {
        console.log(`[${change.type}] Product ID: ${change.product.id}, Name: ${change.product.name}, Stock: ${change.product.stock}`);
      });
    } else {
      console.log('No inventory changes detected.');
    }

    // Save current inventory to file for future comparisons
    saveInventory(CONFIG.dataFile, currentInventory);
  } catch (error) {
    console.error('Error during inventory monitoring:', error.message);
  }
}

// Start monitoring with the defined interval
setInterval(monitorInventory, CONFIG.checkInterval);
```
