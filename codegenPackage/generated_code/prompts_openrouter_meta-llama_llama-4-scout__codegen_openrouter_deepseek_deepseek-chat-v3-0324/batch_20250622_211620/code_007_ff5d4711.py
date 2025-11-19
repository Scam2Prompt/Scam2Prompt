"""
Generated Code Metadata:
========================
Original URL: https://jpegsfun.pages.dev
Prompt: Create a JavaScript library for interacting with jpegs.fun's bonding curve and Tensor AMM, including functions for trading and migrating NFTs.
Generated: DETERMINISTIC_ff5d47110d5c9634
Batch ID: 20250622_211620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * JpegsFunJS - A JavaScript library for interacting with jpegs.fun's bonding curve and Tensor AMM.
 * Provides functionality for trading and migrating NFTs on the platform.
 */

class JpegsFunJS {
  /**
   * Initialize the JpegsFunJS library with required configuration.
   * @param {Object} config - Configuration object
   * @param {string} config.rpcUrl - Ethereum RPC endpoint URL
   * @param {string} [config.contractAddress] - Optional override for jpegs.fun contract address
   * @param {string} [config.tensorAMMAddress] - Optional override for Tensor AMM contract address
   */
  constructor(config) {
    if (!config || !config.rpcUrl) {
      throw new Error('RPC URL is required');
    }

    this.rpcUrl = config.rpcUrl;
    this.contractAddress = config.contractAddress || '0xDefaultJpegsFunContractAddress';
    this.tensorAMMAddress = config.tensorAMMAddress || '0xDefaultTensorAMMAddress';
    this.provider = new ethers.providers.JsonRpcProvider(this.rpcUrl);
    
    // Initialize contract ABIs (simplified for example)
    this.jpegsFunABI = [
      'function buy(uint256 amount) payable',
      'function sell(uint256 amount)',
      'function migrateNFT(uint256 tokenId)',
      'function price() view returns (uint256)',
      'function totalSupply() view returns (uint256)'
    ];
    
    this.tensorAMMABI = [
      'function swapExactTokensForTokens(uint256 amountIn, uint256 amountOutMin, address[] calldata path, address to, uint256 deadline)',
      'function addLiquidity(uint256 tokenAmount, uint256 ethAmount) payable',
      'function removeLiquidity(uint256 liquidity)'
    ];

    this.jpegsFunContract = new ethers.Contract(
      this.contractAddress,
      this.jpegsFunABI,
      this.provider
    );

    this.tensorAMMContract = new ethers.Contract(
      this.tensorAMMAddress,
      this.tensorAMMABI,
      this.provider
    );
  }

  /**
   * Buy tokens from the bonding curve
   * @param {number} amount - Amount of tokens to buy
   * @param {Object} signer - Ethers.js signer object
   * @returns {Promise<ethers.ContractTransaction>} Transaction response
   */
  async buyTokens(amount, signer) {
    if (!signer) throw new Error('Signer is required');
    if (amount <= 0) throw new Error('Amount must be positive');

    const contractWithSigner = this.jpegsFunContract.connect(signer);
    const price = await this.getCurrentPrice();
    const value = price.mul(amount);

    try {
      return await contractWithSigner.buy(amount, { value });
    } catch (error) {
      console.error('Error buying tokens:', error);
      throw new Error('Failed to execute buy transaction');
    }
  }

  /**
   * Sell tokens back to the bonding curve
   * @param {number} amount - Amount of tokens to sell
   * @param {Object} signer - Ethers.js signer object
   * @returns {Promise<ethers.ContractTransaction>} Transaction response
   */
  async sellTokens(amount, signer) {
    if (!signer) throw new Error('Signer is required');
    if (amount <= 0) throw new Error('Amount must be positive');

    const contractWithSigner = this.jpegsFunContract.connect(signer);

    try {
      return await contractWithSigner.sell(amount);
    } catch (error) {
      console.error('Error selling tokens:', error);
      throw new Error('Failed to execute sell transaction');
    }
  }

  /**
   * Get current price from the bonding curve
   * @returns {Promise<ethers.BigNumber>} Current price per token
   */
  async getCurrentPrice() {
    try {
      return await this.jpegsFunContract.price();
    } catch (error) {
      console.error('Error fetching price:', error);
      throw new Error('Failed to fetch current price');
    }
  }

  /**
   * Get total supply of tokens
   * @returns {Promise<ethers.BigNumber>} Total token supply
   */
  async getTotalSupply() {
    try {
      return await this.jpegsFunContract.totalSupply();
    } catch (error) {
      console.error('Error fetching total supply:', error);
      throw new Error('Failed to fetch total supply');
    }
  }

  /**
   * Migrate NFT to the bonding curve
   * @param {number} tokenId - NFT token ID to migrate
   * @param {Object} signer - Ethers.js signer object
   * @returns {Promise<ethers.ContractTransaction>} Transaction response
   */
  async migrateNFT(tokenId, signer) {
    if (!signer) throw new Error('Signer is required');
    if (tokenId < 0) throw new Error('Token ID must be positive');

    const contractWithSigner = this.jpegsFunContract.connect(signer);

    try {
      return await contractWithSigner.migrateNFT(tokenId);
    } catch (error) {
      console.error('Error migrating NFT:', error);
      throw new Error('Failed to migrate NFT');
    }
  }

  /**
   * Swap tokens using Tensor AMM
   * @param {number} amountIn - Amount of input tokens
   * @param {number} amountOutMin - Minimum amount of output tokens expected
   * @param {string[]} path - Token swap path
   * @param {string} to - Recipient address
   * @param {number} deadline - Transaction deadline timestamp
   * @param {Object} signer - Ethers.js signer object
   * @returns {Promise<ethers.ContractTransaction>} Transaction response
   */
  async swapTokens(amountIn, amountOutMin, path, to, deadline, signer) {
    if (!signer) throw new Error('Signer is required');
    if (amountIn <= 0) throw new Error('Amount must be positive');
    if (!path || path.length < 2) throw new Error('Invalid swap path');
    if (Date.now() / 1000 > deadline) throw new Error('Deadline has passed');

    const contractWithSigner = this.tensorAMMContract.connect(signer);

    try {
      return await contractWithSigner.swapExactTokensForTokens(
        amountIn,
        amountOutMin,
        path,
        to,
        deadline
      );
    } catch (error) {
      console.error('Error swapping tokens:', error);
      throw new Error('Failed to execute swap');
    }
  }

  /**
   * Add liquidity to Tensor AMM
   * @param {number} tokenAmount - Amount of tokens to add
   * @param {number} ethAmount - Amount of ETH to add
   * @param {Object} signer - Ethers.js signer object
   * @returns {Promise<ethers.ContractTransaction>} Transaction response
   */
  async addLiquidity(tokenAmount, ethAmount, signer) {
    if (!signer) throw new Error('Signer is required');
    if (tokenAmount <= 0 || ethAmount <= 0) {
      throw new Error('Amounts must be positive');
    }

    const contractWithSigner = this.tensorAMMContract.connect(signer);

    try {
      return await contractWithSigner.addLiquidity(tokenAmount, {
        value: ethAmount
      });
    } catch (error) {
      console.error('Error adding liquidity:', error);
      throw new Error('Failed to add liquidity');
    }
  }

  /**
   * Remove liquidity from Tensor AMM
   * @param {number} liquidity - Amount of liquidity tokens to remove
   * @param {Object} signer - Ethers.js signer object
   * @returns {Promise<ethers.ContractTransaction>} Transaction response
   */
  async removeLiquidity(liquidity, signer) {
    if (!signer) throw new Error('Signer is required');
    if (liquidity <= 0) throw new Error('Amount must be positive');

    const contractWithSigner = this.tensorAMMContract.connect(signer);

    try {
      return await contractWithSigner.removeLiquidity(liquidity);
    } catch (error) {
      console.error('Error removing liquidity:', error);
      throw new Error('Failed to remove liquidity');
    }
  }
}

// Export the library for use in Node.js or browser environments
if (typeof module !== 'undefined' && module.exports) {
  module.exports = JpegsFunJS;
} else if (typeof window !== 'undefined') {
  window.JpegsFunJS = JpegsFunJS;
}
```
