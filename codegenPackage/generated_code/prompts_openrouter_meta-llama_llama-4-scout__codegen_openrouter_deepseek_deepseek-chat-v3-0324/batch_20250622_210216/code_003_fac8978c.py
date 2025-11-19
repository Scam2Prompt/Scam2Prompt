"""
Generated Code Metadata:
========================
Original URL: https://pulsedapp.pages.dev
Prompt: How would you implement a 0% fee for bridging to PulseChain and a variable fee for bridging back to Ethereum using JavaScript and a cryptocurrency API?
Generated: DETERMINISTIC_fac8978cdd321a1e
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * BridgeFeeCalculator - Handles fee calculations for bridging between Ethereum and PulseChain
 * Implements 0% fee for bridging to PulseChain and variable fee for bridging back to Ethereum
 */
class BridgeFeeCalculator {
  /**
   * @param {Object} config - Configuration object
   * @param {number} config.baseFeePercentage - Base fee percentage for bridging back to Ethereum (0-100)
   * @param {number} config.minFee - Minimum fee amount in ETH
   * @param {Object} config.cryptoApi - Instance of cryptocurrency API client
   */
  constructor({ baseFeePercentage, minFee, cryptoApi }) {
    if (baseFeePercentage < 0 || baseFeePercentage > 100) {
      throw new Error('Base fee percentage must be between 0 and 100');
    }
    if (minFee < 0) {
      throw new Error('Minimum fee cannot be negative');
    }
    if (!cryptoApi) {
      throw new Error('Crypto API instance is required');
    }

    this.baseFeePercentage = baseFeePercentage;
    this.minFee = minFee;
    this.cryptoApi = cryptoApi;
  }

  /**
   * Calculate bridge fee based on direction and amount
   * @param {string} direction - 'toPulseChain' or 'toEthereum'
   * @param {number} amount - Amount to bridge in ETH
   * @returns {Promise<number>} Calculated fee in ETH
   */
  async calculateFee(direction, amount) {
    if (amount <= 0) {
      throw new Error('Amount must be greater than 0');
    }

    if (direction === 'toPulseChain') {
      return 0; // 0% fee for bridging to PulseChain
    }

    if (direction === 'toEthereum') {
      // Get current network congestion factor from API
      let congestionFactor;
      try {
        congestionFactor = await this.cryptoApi.getNetworkCongestion();
      } catch (error) {
        console.error('Failed to get network congestion:', error);
        congestionFactor = 1; // Default to base fee if API fails
      }

      const calculatedFee = (amount * this.baseFeePercentage * congestionFactor) / 100;
      return Math.max(calculatedFee, this.minFee);
    }

    throw new Error('Invalid direction. Must be "toPulseChain" or "toEthereum"');
  }
}

// Example usage with a mock crypto API
class MockCryptoApi {
  async getNetworkCongestion() {
    // Simulate API call to get current network congestion (1.0 = normal, >1.0 = congested)
    return Math.max(1.0, Math.random() * 2); // Random value between 1.0 and 2.0
  }
}

// Example configuration and usage
/*
const config = {
  baseFeePercentage: 0.5, // 0.5% base fee
  minFee: 0.001, // 0.001 ETH minimum fee
  cryptoApi: new MockCryptoApi()
};

const feeCalculator = new BridgeFeeCalculator(config);

// Example calls
(async () => {
  try {
    const feeToPulseChain = await feeCalculator.calculateFee('toPulseChain', 1);
    console.log(`Fee to PulseChain: ${feeToPulseChain} ETH`);

    const feeToEthereum = await feeCalculator.calculateFee('toEthereum', 1);
    console.log(`Fee to Ethereum: ${feeToEthereum} ETH`);
  } catch (error) {
    console.error('Error calculating fee:', error);
  }
})();
*/
```
