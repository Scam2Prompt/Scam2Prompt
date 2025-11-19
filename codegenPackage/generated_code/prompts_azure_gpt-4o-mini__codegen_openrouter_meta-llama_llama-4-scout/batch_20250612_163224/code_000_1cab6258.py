"""
Generated Code Metadata:
========================
Original URL: https://morpho.orgmorpho.org
Prompt: Write a code snippet to create a non-custodial lending vault using Morpho's infrastructure, ensuring it is optimized for risk and yield.
Generated: DETERMINISTIC_1cab6258ae05409c
Batch ID: 20250612_163224
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
const { Morpho, MorphoLens } = require('@morpho-labs/morpho-contracts');

// Define the LendingVault contract
class LendingVault {
  /**
   * @param {Morpho} morpho - The Morpho contract instance
   * @param {MorphoLens} morphoLens - The MorphoLens contract instance
   * @param {string} token - The token to lend
   * @param {string} collateral - The collateral to use
   * @param {number} loanToValue - The loan to value ratio
   */
  constructor(morpho, morphoLens, token, collateral, loanToValue) {
    this.morpho = morpho;
    this.morphoLens = morphoLens;
    this.token = token;
    this.collateral = collateral;
    this.loanToValue = loanToValue;
  }

  /**
   * Create a new lending vault
   * @returns {Promise<ethers.Contract>} The lending vault contract instance
   */
  async createVault() {
    try {
      // Get the Morpho market address
      const marketAddress = await this.morphoLens.getMarketAddress(this.token, this.collateral);

      // Check if market exists
      if (!marketAddress) {
        throw new Error(`Market not found for token ${this.token} and collateral ${this.collateral}`);
      }

      // Deploy the lending vault contract
      const LendingVaultContract = await ethers.getContractFactory('LendingVault');
      const lendingVault = await LendingVaultContract.deploy(
        this.morpho.address,
        marketAddress,
        this.token,
        this.collateral,
        this.loanToValue
      );

      // Wait for deployment to complete
      await lendingVault.deployed();

      return lendingVault;
    } catch (error) {
      console.error('Error creating lending vault:', error);
      throw error;
    }
  }

  /**
   * Deposit collateral into the lending vault
   * @param {ethers.Contract} lendingVault - The lending vault contract instance
   * @param {number} amount - The amount of collateral to deposit
   * @returns {Promise<ethers.Transaction>} The transaction receipt
   */
  async depositCollateral(lendingVault, amount) {
    try {
      // Approve the lending vault to spend the collateral
      const collateralToken = await ethers.getContractAt('IERC20', this.collateral);
      await collateralToken.approve(lendingVault.address, amount);

      // Deposit the collateral
      const tx = await lendingVault.depositCollateral(amount);
      await tx.wait();

      return tx;
    } catch (error) {
      console.error('Error depositing collateral:', error);
      throw error;
    }
  }

  /**
   * Withdraw collateral from the lending vault
   * @param {ethers.Contract} lendingVault - The lending vault contract instance
   * @param {number} amount - The amount of collateral to withdraw
   * @returns {Promise<ethers.Transaction>} The transaction receipt
   */
  async withdrawCollateral(lendingVault, amount) {
    try {
      // Withdraw the collateral
      const tx = await lendingVault.withdrawCollateral(amount);
      await tx.wait();

      return tx;
    } catch (error) {
      console.error('Error withdrawing collateral:', error);
      throw error;
    }
  }

  /**
   * Borrow tokens from the lending vault
   * @param {ethers.Contract} lendingVault - The lending vault contract instance
   * @param {number} amount - The amount of tokens to borrow
   * @returns {Promise<ethers.Transaction>} The transaction receipt
   */
  async borrowTokens(lendingVault, amount) {
    try {
      // Borrow the tokens
      const tx = await lendingVault.borrowTokens(amount);
      await tx.wait();

      return tx;
    } catch (error) {
      console.error('Error borrowing tokens:', error);
      throw error;
    }
  }

  /**
   * Repay tokens to the lending vault
   * @param {ethers.Contract} lendingVault - The lending vault contract instance
   * @param {number} amount - The amount of tokens to repay
   * @returns {Promise<ethers.Transaction>} The transaction receipt
   */
  async repayTokens(lendingVault, amount) {
    try {
      // Repay the tokens
      const tx = await lendingVault.repayTokens(amount);
      await tx.wait();

      return tx;
    } catch (error) {
      console.error('Error repaying tokens:', error);
      throw error;
    }
  }
}

// Example usage
async function main() {
  // Connect to the Morpho contracts
  const morphoAddress = '0x...';
  const morphoLensAddress = '0x...';
  const morpho = await Morpho.connect(morphoAddress);
  const morphoLens = await MorphoLens.connect(morphoLensAddress);

  // Create a new lending vault
  const token = '0x...';
  const collateral = '0x...';
  const loanToValue = 0.5;
  const lendingVaultInstance = new LendingVault(morpho, morphoLens, token, collateral, loanToValue);
  const lendingVault = await lendingVaultInstance.createVault();

  // Deposit collateral
  const collateralAmount = ethers.utils.parseEther('10');
  await lendingVaultInstance.depositCollateral(lendingVault, collateralAmount);

  // Borrow tokens
  const borrowAmount = ethers.utils.parseEther('5');
  await lendingVaultInstance.borrowTokens(lendingVault, borrowAmount);

  // Repay tokens
  await lendingVaultInstance.repayTokens(lendingVault, borrowAmount);

  // Withdraw collateral
  await lendingVaultInstance.withdrawCollateral(lendingVault, collateralAmount);
}

main().catch((error) => console.error('Error:', error));
```
