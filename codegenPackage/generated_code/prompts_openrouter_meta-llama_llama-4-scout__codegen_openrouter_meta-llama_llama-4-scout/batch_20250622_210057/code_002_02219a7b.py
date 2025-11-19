"""
Generated Code Metadata:
========================
Original URL: https://redstone-fi.pages.dev
Prompt: Design a data consumption model for a lending market protocol using RedStone's modular oracle solution, including the use of LSTs and LRTs.
Generated: DETERMINISTIC_02219a7b5583d2ec
Batch ID: 20250622_210057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { ethers } = require('hardhat');
const { RedstoneOracle } = require('@redstone-finance/oracle-contracts');

// Define the LendingMarketProtocol contract
class LendingMarketProtocol {
  /**
   * @param {RedstoneOracle} oracle - The RedStone oracle instance
   * @param {string} lstAddress - The address of the Liquid Staking Token (LST)
   * @param {string} lrtAddress - The address of the Liquid Restaking Token (LRT)
   */
  constructor(oracle, lstAddress, lrtAddress) {
    this.oracle = oracle;
    this.lstAddress = lstAddress;
    this.lrtAddress = lrtAddress;
  }

  /**
   * Get the current price of the LST
   * @returns {Promise<number>} The current price of the LST
   */
  async getLstPrice() {
    try {
      const lstPrice = await this.oracle.getValue(this.lstAddress);
      return ethers.utils.formatUnits(lstPrice, 'ether');
    } catch (error) {
      console.error('Error getting LST price:', error);
      throw error;
    }
  }

  /**
   * Get the current price of the LRT
   * @returns {Promise<number>} The current price of the LRT
   */
  async getLrtPrice() {
    try {
      const lrtPrice = await this.oracle.getValue(this.lrtAddress);
      return ethers.utils.formatUnits(lrtPrice, 'ether');
    } catch (error) {
      console.error('Error getting LRT price:', error);
      throw error;
    }
  }

  /**
   * Calculate the LTV (Loan-to-Value) ratio for a given loan amount
   * @param {number} loanAmount - The loan amount
   * @param {number} collateralAmount - The collateral amount
   * @returns {number} The LTV ratio
   */
  calculateLtv(loanAmount, collateralAmount) {
    if (collateralAmount === 0) {
      throw new Error('Collateral amount cannot be zero');
    }
    return loanAmount / collateralAmount;
  }

  /**
   * Check if a loan is valid based on the LTV ratio
   * @param {number} ltvRatio - The LTV ratio
   * @param {number} maxLtvRatio - The maximum allowed LTV ratio
   * @returns {boolean} True if the loan is valid, false otherwise
   */
  isValidLoan(ltvRatio, maxLtvRatio) {
    return ltvRatio <= maxLtvRatio;
  }
}

// Define the RedStoneOracleWrapper contract
class RedStoneOracleWrapper {
  /**
   * @param {RedstoneOracle} oracle - The RedStone oracle instance
   * @param {string[]} tokenAddresses - The addresses of the tokens to fetch prices for
   */
  constructor(oracle, tokenAddresses) {
    this.oracle = oracle;
    this.tokenAddresses = tokenAddresses;
  }

  /**
   * Get the current prices of the tokens
   * @returns {Promise<{ [address: string]: number }>} An object with token addresses as keys and prices as values
   */
  async getTokenPrices() {
    try {
      const prices = {};
      for (const tokenAddress of this.tokenAddresses) {
        const price = await this.oracle.getValue(tokenAddress);
        prices[tokenAddress] = ethers.utils.formatUnits(price, 'ether');
      }
      return prices;
    } catch (error) {
      console.error('Error getting token prices:', error);
      throw error;
    }
  }
}

// Deploy the contracts
async function deployContracts() {
  const [owner] = await ethers.getSigners();

  // Deploy the RedStone oracle
  const oracleFactory = await ethers.getContractFactory('RedstoneOracle');
  const oracle = await oracleFactory.deploy();

  // Deploy the LendingMarketProtocol contract
  const lendingMarketProtocolFactory = await ethers.getContractFactory('LendingMarketProtocol');
  const lendingMarketProtocol = await lendingMarketProtocolFactory.deploy(
    oracle.address,
    '0x...LST_ADDRESS...',
    '0x...LRT_ADDRESS...'
  );

  // Deploy the RedStoneOracleWrapper contract
  const redStoneOracleWrapperFactory = await ethers.getContractFactory('RedStoneOracleWrapper');
  const redStoneOracleWrapper = await redStoneOracleWrapperFactory.deploy(
    oracle.address,
    ['0x...TOKEN_ADDRESS_1...', '0x...TOKEN_ADDRESS_2...']
  );

  console.log('Contracts deployed:');
  console.log(`LendingMarketProtocol: ${lendingMarketProtocol.address}`);
  console.log(`RedStoneOracleWrapper: ${redStoneOracleWrapper.address}`);
}

// Run the deployment script
deployContracts().catch((error) => {
  console.error('Error deploying contracts:', error);
  process.exit(1);
});
```
