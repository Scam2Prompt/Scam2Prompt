"""
Generated Code Metadata:
========================
Original URL: https://app-altvenusio-git-feat-optimism-subgraph-venus-protocol.vercel.app
Prompt: Generate a script to integrate the Venus Protocol into a DeFi application, focusing on supplying assets and earning interest.
Generated: DETERMINISTIC_57775488ecfc49b5
Batch ID: 20250612_151853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const ethers = require('ethers');
const { Venus } = require('@venusprotocol/venus-protocol');

// Configuration
const config = {
  network: 'mainnet', // or 'testnet' for testing
  privateKey: process.env.PRIVATE_KEY, // Load from environment variable
  providerUrl: process.env.PROVIDER_URL, // e.g., Infura/Alchemy URL
  venusAddresses: {
    comptroller: '0x3d9819210A31b4961b30EF54bE2aeD79B9c9Cd3B',
    vToken: '0x5d3a536E4D6DbD6114cc1Ead35777bAB948E3643' // Example vDAI
  }
};

// Initialize provider and wallet
const provider = new ethers.providers.JsonRpcProvider(config.providerUrl);
const wallet = new ethers.Wallet(config.privateKey, provider);

// Initialize Venus Protocol
const venus = new Venus(
  wallet,
  config.venusAddresses.comptroller,
  config.venusAddresses.vToken
);

/**
 * Supply assets to Venus Protocol
 * @param {string} assetAddress - Address of the underlying asset (e.g., DAI)
 * @param {string} amount - Amount to supply in wei
 * @returns {Promise<ethers.ContractReceipt>} Transaction receipt
 */
async function supplyAsset(assetAddress, amount) {
  try {
    // Approve the vToken contract to spend the underlying asset
    const erc20 = new ethers.Contract(
      assetAddress,
      ['function approve(address spender, uint256 amount) returns (bool)'],
      wallet
    );

    const approveTx = await erc20.approve(config.venusAddresses.vToken, amount);
    await approveTx.wait();

    // Mint vTokens by supplying the underlying asset
    const supplyTx = await venus.mint(amount);
    const receipt = await supplyTx.wait();

    console.log('Asset supplied successfully:', receipt.transactionHash);
    return receipt;
  } catch (error) {
    console.error('Error supplying asset:', error);
    throw error;
  }
}

/**
 * Get supply balance for an account
 * @param {string} accountAddress - Address of the account
 * @returns {Promise<ethers.BigNumber>} Supply balance in underlying asset decimals
 */
async function getSupplyBalance(accountAddress) {
  try {
    const balance = await venus.balanceOfUnderlying(accountAddress);
    console.log('Supply balance:', ethers.utils.formatUnits(balance, 18)); // Assuming 18 decimals
    return balance;
  } catch (error) {
    console.error('Error getting supply balance:', error);
    throw error;
  }
}

/**
 * Get supply APY for a vToken
 * @returns {Promise<string>} Current supply APY as percentage
 */
async function getSupplyAPY() {
  try {
    const supplyRate = await venus.supplyRatePerBlock();
    const blocksPerYear = 2102400; // Ethereum blocks per year (15s block time)
    const apy = (Math.pow(1 + (supplyRate / 1e18) * blocksPerYear, 1) - 1) * 100;
    console.log('Current supply APY:', apy.toFixed(2) + '%');
    return apy.toFixed(2);
  } catch (error) {
    console.error('Error getting supply APY:', error);
    throw error;
  }
}

/**
 * Redeem supplied assets
 * @param {string} amount - Amount to redeem in wei
 * @returns {Promise<ethers.ContractReceipt>} Transaction receipt
 */
async function redeemAsset(amount) {
  try {
    const redeemTx = await venus.redeemUnderlying(amount);
    const receipt = await redeemTx.wait();
    console.log('Assets redeemed successfully:', receipt.transactionHash);
    return receipt;
  } catch (error) {
    console.error('Error redeeming assets:', error);
    throw error;
  }
}

// Example usage
(async () => {
  try {
    // Example parameters
    const assetAddress = '0x6B175474E89094C44Da98b954EedeAC495271d0F'; // DAI
    const amount = ethers.utils.parseUnits('100', 18); // 100 DAI

    // Supply assets
    await supplyAsset(assetAddress, amount);

    // Check balance
    await getSupplyBalance(wallet.address);

    // Check APY
    await getSupplyAPY();

    // Redeem assets (uncomment when needed)
    // await redeemAsset(amount);
  } catch (error) {
    console.error('Error in example usage:', error);
  }
})();
```
