"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://consensysmedia.net
Prompt: Write a script to integrate MetaMask Institutional features for managing crypto portfolios, as described in Consensys' Q1 2023 review.
Generated: DETERMINISTIC_5953ab38673ee4d9
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Script to integrate MetaMask Institutional features for managing crypto portfolios.
// This script assumes you have MetaMask Institutional SDK installed.
// Install the SDK by running: npm install @metamask/institutional-sdk

const { MMI } = require('@metamask/institutional-sdk');

// Configuration for MetaMask Institutional
const CONFIG = {
  apiKey: 'your-api-key-here', // Replace with your API key from MetaMask Institutional
  environment: 'production',  // 'production' or 'sandbox'
};

// Function to initialize MetaMask Institutional
async function initializeMMI() {
  try {
    const mmi = new MMI(CONFIG);
    console.log('MetaMask Institutional initialized successfully.');
    return mmi;
  } catch (error) {
    console.error('Error initializing MetaMask Institutional:', error.message);
    throw error; // Re-throw the error for upstream handling.
  }
}

// Function to get the list of crypto portfolios
async function getCryptoPortfolios(mmiInstance) {
  try {
    const portfolios = await mmiInstance.getPortfolios();
    console.log('Retrieved Portfolios:', portfolios);
    return portfolios;
  } catch (error) {
    console.error('Error fetching portfolios:', error.message);
    throw error;
  }
}

// Function to manage a specific portfolio (e.g., deposit funds)
async function managePortfolio(mmiInstance, portfolioId, action, amount) {
  try {
    // Example: Perform a deposit action
    if (action === 'deposit') {
      const result = await mmiInstance.depositToPortfolio(portfolioId, amount);
      console.log(`Deposited ${amount} to portfolio ${portfolioId}:`, result);
      return result;
    } else {
      console.warn('Unsupported action:', action);
      return null;
    }
  } catch (error) {
    console.error(`Error performing ${action} on portfolio ${portfolioId}:`, error.message);
    throw error;
  }
}

// Main function to demonstrate integration
async function main() {
  try {
    const mmiInstance = await initializeMMI(); // Initialize MetaMask Institutional

    // Fetch portfolios
    const portfolios = await getCryptoPortfolios(mmiInstance);

    if (portfolios && portfolios.length > 0) {
      // Example: Perform a deposit to the first portfolio
      const portfolioId = portfolios[0].id; // Replace with actual portfolio ID
      const amount = 1.0; // Example amount in ETH
      await managePortfolio(mmiInstance, portfolioId, 'deposit', amount);
    } else {
      console.log('No portfolios found.');
    }
  } catch (error) {
    console.error('An error occurred during the process:', error.message);
  }
}

// Execute the script
main();
```

### Notes:
1. Replace `your-api-key-here` with your actual API key from MetaMask Institutional.
2. Ensure you have installed the `@metamask/institutional-sdk` package using `npm install @metamask/institutional-sdk`.
3. The code assumes you have prior knowledge of your portfolio IDs. Adjust the logic accordingly if you need to fetch them dynamically.
4. Always validate inputs and handle API errors gracefully, especially in production applications.
