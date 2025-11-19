"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lifi.website
Prompt: What are the best practices for using the LiFi SDK in a web application?
Generated: DETERMINISTIC_1ab83f9325c52e6c
Batch ID: 20250612_161745
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's an example of clean, production-ready JavaScript code demonstrating best practices when using the LiFi SDK in a web application:

```javascript
// Import the LiFi SDK
import LiFi from '@lifinance/sdk';

// Initialize the LiFi SDK instance
const lifi = new LiFi();

/**
 * Function to fetch available routes for swapping tokens
 * @param {Object} swapOptions - Configuration for token swap
 * @param {string} swapOptions.fromToken - Address or symbol of the token to swap from
 * @param {string} swapOptions.toToken - Address or symbol of the token to swap to
 * @param {number} swapOptions.amount - Amount of the `fromToken` to swap
 * @param {string} swapOptions.fromChain - Chain ID or name of the source chain
 * @param {string} swapOptions.toChain - Chain ID or name of the destination chain
 * @returns {Promise<Object>} - Returns the best routes available for the swap
 */
async function fetchSwapRoutes(swapOptions) {
  const { fromToken, toToken, amount, fromChain, toChain } = swapOptions;

  try {
    // Validate input parameters
    if (!fromToken || !toToken || !amount || !fromChain || !toChain) {
      throw new Error('All swap options must be provided.');
    }

    // Use LiFi SDK to retrieve routes
    const routes = await lifi.getRoutes({
      fromToken,
      toToken,
      amount,
      fromChain,
      toChain,
    });

    return routes;
  } catch (error) {
    console.error('Error fetching swap routes:', error.message);
    throw error; // Rethrow error for further handling
  }
}

/**
 * Function to execute a token swap
 * @param {Object} route - Route information obtained from `fetchSwapRoutes`
 * @returns {Promise<Object>} - Returns the transaction receipt upon successful execution
 */
async function executeSwap(route) {
  try {
    if (!route) {
      throw new Error('Route information is required to execute a swap.');
    }

    // Execute the swap using the LiFi SDK
    const receipt = await lifi.executeRoute({
      route, // Route object containing transaction details
    });

    return receipt;
  } catch (error) {
    console.error('Error executing swap:', error.message);
    throw error; // Rethrow error for further handling
  }
}

// Example usage of the above functions:

// Define swap options
const swapOptions = {
  fromToken: '0xEeeeeEeeeEeEeeEeEeEeeEEEeeeeEeeeeeeeEEeE', // Example: ETH
  toToken: '0xA0b86991c6218b36c1d19d4a2e9eb0ce3606eb48', // Example: USDC
  amount: 1000000000000000000, // Example: 1 ETH in wei
  fromChain: '1', // Ethereum Mainnet chain ID
  toChain: '1', // Same chain ID for Ethereum Mainnet
};

// Fetch routes and execute a swap
(async () => {
  try {
    // Fetch available routes
    const routes = await fetchSwapRoutes(swapOptions);

    if (routes && routes.routes && routes.routes.length > 0) {
      console.log('Available routes:', routes.routes);

      // Select the best route (here, the first one as an example)
      const bestRoute = routes.routes[0];

      // Execute the swap
      const receipt = await executeSwap(bestRoute);
      console.log('Swap successful! Transaction receipt:', receipt);
    } else {
      console.log('No routes available for the given swap options.');
    }
  } catch (error) {
    console.error('Error during swap process:', error.message);
  }
})();
```

This code demonstrates clean, functional usage of the LiFi SDK in a production-ready web application, following the best practices outlined in your request. Add your preferred error monitoring tools or logs for production environments as needed.
