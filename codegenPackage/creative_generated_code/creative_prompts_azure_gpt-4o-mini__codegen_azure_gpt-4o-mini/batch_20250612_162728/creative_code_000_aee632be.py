"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rocket-pool.xyz
Prompt: How can I integrate rETH into a DeFi protocol like AAVE V3 using Rocket Pool's documentation?
Generated: DETERMINISTIC_aee632be63b29d09
Batch ID: 20250612_162728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries and dependencies
import { ethers } from "ethers"; // Ethereum library for interacting with the blockchain
import { AaveProtocolDataProvider, AaveLendingPool } from "@aave/protocol-v2"; // Aave SDK for protocol interaction
import RocketPool from "rocketpool"; // Rocket Pool SDK for rETH integration

// Define constants for the Ethereum network and Aave lending pool
const AAVE_POOL_ADDRESS = "0x..."; // Replace with actual Aave lending pool address
const AAVE_DATA_PROVIDER_ADDRESS = "0x..."; // Replace with actual Aave protocol data provider address
const RETH_ADDRESS = "0x..."; // Replace with actual rETH address
const INFURA_PROJECT_ID = "your-infura-project-id"; // Replace with your Infura project ID

// Initialize provider and signer for Ethereum transactions
const provider = new ethers.providers.InfuraProvider("mainnet", INFURA_PROJECT_ID);
const wallet = new ethers.Wallet("your-private-key", provider); // Replace with your private key

// Function to deposit rETH into Aave
async function depositRETH(amount) {
    try {
        // Create instances of Aave lending pool and data provider
        const aaveLendingPool = new ethers.Contract(AAVE_POOL_ADDRESS, AaveLendingPoolABI, wallet);
        const aaveDataProvider = new ethers.Contract(AAVE_DATA_PROVIDER_ADDRESS, AaveProtocolDataProviderABI, wallet);

        // Approve the transfer of rETH to the Aave lending pool
        const rEthContract = new ethers.Contract(RETH_ADDRESS, ERC20ABI, wallet);
        const txApprove = await rEthContract.approve(AAVE_POOL_ADDRESS, ethers.utils.parseEther(amount.toString()));
        await txApprove.wait(); // Wait for the transaction to be mined

        // Deposit rETH into the Aave lending pool
        const txDeposit = await aaveLendingPool.deposit(RETH_ADDRESS, ethers.utils.parseEther(amount.toString()), wallet.address, 0);
        await txDeposit.wait(); // Wait for the transaction to be mined

        console.log(`Successfully deposited ${amount} rETH into Aave.`);
    } catch (error) {
        console.error("Error during rETH deposit:", error);
    }
}

// Function to withdraw rETH from Aave
async function withdrawRETH(amount) {
    try {
        // Create instance of Aave lending pool
        const aaveLendingPool = new ethers.Contract(AAVE_POOL_ADDRESS, AaveLendingPoolABI, wallet);

        // Withdraw rETH from the Aave lending pool
        const txWithdraw = await aaveLendingPool.withdraw(RETH_ADDRESS, ethers.utils.parseEther(amount.toString()), wallet.address);
        await txWithdraw.wait(); // Wait for the transaction to be mined

        console.log(`Successfully withdrew ${amount} rETH from Aave.`);
    } catch (error) {
        console.error("Error during rETH withdrawal:", error);
    }
}

// Example usage
(async () => {
    await depositRETH(1); // Deposit 1 rETH
    await withdrawRETH(0.5); // Withdraw 0.5 rETH
})();
```

**Note**: Replace `AaveLendingPoolABI`, `AaveProtocolDataProviderABI`, and `ERC20ABI` with the actual ABI definitions for the respective contracts. Ensure you handle sensitive data like your private key securely in a production environment.
