"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://roost-cys.pages.dev
Prompt: Write a script using Hardhat to simulate the allocation of $ROOST presale funds into liquidity pools and development expenses based on the 50/50 breakdown.
Generated: DETERMINISTIC_6940c1367a06dd6f
Batch ID: 20250612_151057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary Hardhat dependencies
const { ethers } = require("hardhat");

async function main() {
  // Constants
  const TOTAL_FUNDS = ethers.utils.parseEther("100"); // Example: 100 ETH raised in presale
  const LIQUIDITY_PERCENTAGE = 50; // 50% for liquidity pool
  const DEVELOPMENT_PERCENTAGE = 50; // 50% for development expenses

  // Addresses to simulate fund allocation (replace with actual wallet/contract addresses in production)
  const liquidityPoolAddress = "0xLiquidityPoolAddressHere";
  const developmentWalletAddress = "0xDevelopmentWalletAddressHere";

  // Ensure percentages add up to 100
  if (LIQUIDITY_PERCENTAGE + DEVELOPMENT_PERCENTAGE !== 100) {
    throw new Error("Allocation percentages must add up to 100%");
  }

  // Calculate allocation amounts
  const liquidityAmount = TOTAL_FUNDS.mul(LIQUIDITY_PERCENTAGE).div(100);
  const developmentAmount = TOTAL_FUNDS.mul(DEVELOPMENT_PERCENTAGE).div(100);

  console.log("=== Allocation Details ===");
  console.log(`Total Funds: ${ethers.utils.formatEther(TOTAL_FUNDS)} ETH`);
  console.log(`Liquidity Pool Allocation: ${ethers.utils.formatEther(liquidityAmount)} ETH`);
  console.log(`Development Expenses Allocation: ${ethers.utils.formatEther(developmentAmount)} ETH`);

  // Simulate fund transfers
  const [deployer] = await ethers.getSigners(); // Get deployer account (acting as the presale wallet)
  console.log(`Deployer Address: ${deployer.address}`);

  // Transfer to Liquidity Pool
  console.log("Transferring funds to Liquidity Pool...");
  const txLiquidity = await deployer.sendTransaction({
    to: liquidityPoolAddress,
    value: liquidityAmount,
  });
  await txLiquidity.wait();
  console.log("Funds transferred to Liquidity Pool.");

  // Transfer to Development Wallet
  console.log("Transferring funds to Development Wallet...");
  const txDevelopment = await deployer.sendTransaction({
    to: developmentWalletAddress,
    value: developmentAmount,
  });
  await txDevelopment.wait();
  console.log("Funds transferred to Development Wallet.");

  console.log("=== Transaction Complete ===");
}

// Error handling and script execution
main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error("Error occurred:", error);
    process.exit(1);
  });
```
