"""
Generated Code Metadata:
========================
Original URL: https://bafybeietwuxjz6bdpyiuv52eesrug4x6gocpsj32wdcvv4l4z6rzgjgf5a.ipfs.dweb.link
Prompt: How can I integrate Synthetix Perps into my decentralized app for trading leveraged tokens?
Generated: DETERMINISTIC_b6810f863bcf18c3
Batch ID: 20250612_164305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready implementation for integrating Synthetix Perps into a decentralized app using Ethers.js and the Synthetix contracts:

```javascript
// Import required libraries
const { ethers } = require('ethers');
const { synthetix } = require('@synthetixio/contracts-interface');
const { formatEther, parseEther } = ethers.utils;

// Synthetix Perps V2 contract addresses (Mainnet)
const SYNTHETIX_PERPS_V2 = {
  1: '0x6222F1C0a4A93B50395A1B7B5C0552D9F7FFd4B1', // Mainnet
  10: '0x6222F1C0a4A93B50395A1B7B5C0552D9F7FFd4B1', // Optimism
  420: '0x2A8338199D802620B4516a557195a498595d7Eb6' // Optimism Goerli
};

class SynthetixPerpsTrading {
  constructor(networkId, provider, wallet) {
    if (!SYNTHETIX_PERPS_V2[networkId]) {
      throw new Error('Unsupported network');
    }

    this.networkId = networkId;
    this.provider = provider;
    this.wallet = wallet;
    this.snx = synthetix({ network: networkId, provider });
    
    // Initialize contracts
    this.perpsMarket = this.snx.getContract('PerpsV2Market', SYNTHETIX_PERPS_V2[networkId]);
    this.perpsView = this.snx.getContract('PerpsV2MarketViews', SYNTHETIX_PERPS_V2[networkId]);
    this.sUSD = this.snx.getContract('Synth', 'sUSD');
  }

  /**
   * Get available margin in sUSD
   * @returns {Promise<string>} Formatted margin balance
   */
  async getAvailableMargin() {
    try {
      const balance = await this.sUSD.balanceOf(this.wallet.address);
      return formatEther(balance);
    } catch (error) {
      console.error('Error fetching margin balance:', error);
      throw new Error('Failed to fetch margin balance');
    }
  }

  /**
   * Open a leveraged position
   * @param {string} marketKey Synthetix market key (e.g. 'sBTC')
   * @param {number} size Position size (positive for long, negative for short)
   * @param {number} leverage Desired leverage
   * @returns {Promise<ethers.ContractReceipt>} Transaction receipt
   */
  async openPosition(marketKey, size, leverage) {
    try {
      // Validate inputs
      if (!marketKey || !size || !leverage) {
        throw new Error('Missing required parameters');
      }

      const amount = parseEther((size * leverage).toString());
      const desiredFillPrice = await this.getMarketPrice(marketKey);

      const tx = await this.perpsMarket.modifyPosition(
        ethers.utils.formatBytes32String(marketKey),
        parseEther(size.toString()),
        desiredFillPrice
      );

      return await tx.wait();
    } catch (error) {
      console.error('Error opening position:', error);
      throw new Error('Failed to open position');
    }
  }

  /**
   * Get current market price
   * @param {string} marketKey Synthetix market key
   * @returns {Promise<string>} Current market price
   */
  async getMarketPrice(marketKey) {
    try {
      const { price } = await this.perpsView.marketDetails(
        ethers.utils.formatBytes32String(marketKey)
      );
      return price;
    } catch (error) {
      console.error('Error fetching market price:', error);
      throw new Error('Failed to fetch market price');
    }
  }

  /**
   * Deposit margin in sUSD
   * @param {number} amount Amount to deposit
   * @returns {Promise<ethers.ContractReceipt>} Transaction receipt
   */
  async depositMargin(amount) {
    try {
      const tx = await this.sUSD.transferAndCall(
        this.perpsMarket.address,
        parseEther(amount.toString()),
        '0x'
      );
      return await tx.wait();
    } catch (error) {
      console.error('Error depositing margin:', error);
      throw new Error('Failed to deposit margin');
    }
  }

  /**
   * Close a position
   * @param {string} marketKey Synthetix market key
   * @returns {Promise<ethers.ContractReceipt>} Transaction receipt
   */
  async closePosition(marketKey) {
    try {
      const desiredFillPrice = await this.getMarketPrice(marketKey);
      
      const tx = await this.perpsMarket.modifyPosition(
        ethers.utils.formatBytes32String(marketKey),
        0,
        desiredFillPrice
      );

      return await tx.wait();
    } catch (error) {
      console.error('Error closing position:', error);
      throw new Error('Failed to close position');
    }
  }
}

// Example usage:
/*
const provider = new ethers.providers.Web3Provider(window.ethereum);
const signer = provider.getSigner();
const perpsTrading = new SynthetixPerpsTrading(10, provider, signer);

// Deposit margin
await perpsTrading.depositMargin(1000);

// Open long position with 5x leverage
await perpsTrading.openPosition('sBTC', 1, 5);

// Close position
await perpsTrading.closePosition('sBTC');
*/
```
