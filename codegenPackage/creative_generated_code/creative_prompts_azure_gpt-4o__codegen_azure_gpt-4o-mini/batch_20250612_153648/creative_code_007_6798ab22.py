"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-minetrex.pages.dev
Prompt: Write a script using ethers.js to automate the purchase and staking of BTCMTX tokens during the presale phase, ensuring compatibility with Ethereum wallets.
Generated: DETERMINISTIC_6798ab229a93b0a7
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the ethers library
const { ethers } = require("ethers");

// Define the main function to automate the purchase and staking of BTCMTX tokens
async function automatePurchaseAndStake() {
    // Define provider, wallet, and contract addresses
    const provider = new ethers.providers.InfuraProvider("homestead", "YOUR_INFURA_PROJECT_ID"); // Replace with your Infura project ID
    const walletPrivateKey = "YOUR_PRIVATE_KEY"; // Replace with your wallet's private key
    const wallet = new ethers.Wallet(walletPrivateKey, provider);
    
    const presaleContractAddress = "PRESALE_CONTRACT_ADDRESS"; // Replace with the presale contract address
    const stakingContractAddress = "STAKING_CONTRACT_ADDRESS"; // Replace with the staking contract address
    const btcmtxTokenAddress = "BTCMTX_TOKEN_ADDRESS"; // Replace with the BTCMTX token address

    // Define abi for presale and staking contracts
    const presaleAbi = [
        "function purchaseTokens(uint256 amount) external payable",
        "function getTokenPrice() external view returns (uint256)"
    ];

    const stakingAbi = [
        "function stakeTokens(uint256 amount) external"
    ];

    // Create instances of the contracts
    const presaleContract = new ethers.Contract(presaleContractAddress, presaleAbi, wallet);
    const stakingContract = new ethers.Contract(stakingContractAddress, stakingAbi, wallet);

    try {
        // Fetch the token price
        const tokenPrice = await presaleContract.getTokenPrice();
        console.log(`Current token price: ${ethers.utils.formatEther(tokenPrice)} ETH`);

        // Define the amount of tokens to purchase
        const tokenAmountToPurchase = ethers.utils.parseUnits("10", 18); // Change "10" to the desired amount

        // Calculate the total cost
        const totalCost = tokenPrice.mul(tokenAmountToPurchase).div(ethers.constants.WeiPerEther);
        console.log(`Total cost for ${tokenAmountToPurchase.toString()} tokens: ${ethers.utils.formatEther(totalCost)} ETH`);

        // Send the transaction to purchase tokens
        const purchaseTx = await presaleContract.purchaseTokens(tokenAmountToPurchase, {
            value: totalCost
        });
        
        console.log(`Purchase transaction sent: ${purchaseTx.hash}`);
        await purchaseTx.wait();
        console.log(`Purchase transaction confirmed: ${purchaseTx.hash}`);

        // Approve the staking contract to spend the purchased tokens
        const btcmtxTokenContract = new ethers.Contract(btcmtxTokenAddress, [
            "function approve(address spender, uint256 amount) external returns (bool)"
        ], wallet);
        
        const approvalTx = await btcmtxTokenContract.approve(stakingContractAddress, tokenAmountToPurchase);
        console.log(`Approval transaction sent: ${approvalTx.hash}`);
        await approvalTx.wait();
        console.log(`Approval transaction confirmed: ${approvalTx.hash}`);

        // Stake the purchased tokens
        const stakeTx = await stakingContract.stakeTokens(tokenAmountToPurchase);
        console.log(`Stake transaction sent: ${stakeTx.hash}`);
        await stakeTx.wait();
        console.log(`Stake transaction confirmed: ${stakeTx.hash}`);

        console.log("Successfully purchased and staked BTCMTX tokens!");

    } catch (error) {
        console.error("An error occurred during the process:", error);
    }
}

// Execute the main function
automatePurchaseAndStake();
```

**Note:** 
- Make sure you replace placeholders like `YOUR_INFURA_PROJECT_ID`, `YOUR_PRIVATE_KEY`, `PRESALE_CONTRACT_ADDRESS`, `STAKING_CONTRACT_ADDRESS`, and `BTCMTX_TOKEN_ADDRESS` with actual values before running the script.
- Ensure that you handle your private key securely and never expose it in public repositories.
