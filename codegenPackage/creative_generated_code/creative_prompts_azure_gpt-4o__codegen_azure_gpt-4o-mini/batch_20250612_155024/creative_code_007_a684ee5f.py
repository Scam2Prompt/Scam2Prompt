"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hoststandart.ru
Prompt: Write a detailed guide in code for purchasing BELT tokens on PancakeSwap and using them for governance voting on Belt Finance proposals.
Generated: DETERMINISTIC_a684ee5fd8cdd030
Batch ID: 20250612_155024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const { ethers } = require("ethers"); // Ethereum library for blockchain interactions
const { PancakeSwap } = require('pancakeswap-sdk'); // PancakeSwap SDK for token transactions
const { BLP } = require('belt-finance-sdk'); // Belt Finance SDK for governance interactions

// Define constants
const INFURA_PROJECT_ID = "YOUR_INFURA_PROJECT_ID"; // Replace with your Infura Project ID
const PRIVATE_KEY = "YOUR_PRIVATE_KEY"; // Replace with your wallet's private key
const TOKEN_ADDRESS = "0xYourBeltTokenAddress"; // Replace with the actual BELT token address
const GOVERNANCE_CONTRACT_ADDRESS = "0xYourGovernanceContractAddress"; // Replace with the actual governance contract address

// Initialize provider and signer
const provider = new ethers.providers.InfuraProvider("mainnet", INFURA_PROJECT_ID);
const wallet = new ethers.Wallet(PRIVATE_KEY, provider);

// Function to buy BELT tokens on PancakeSwap
async function buyBeltTokens(amountInBNB) {
    try {
        // Create PancakeSwap instance
        const pancakeSwap = new PancakeSwap(wallet);

        // Calculate the amount of BELT tokens to buy
        const amountOutMin = await pancakeSwap.getAmountOutMin(TOKEN_ADDRESS, amountInBNB);

        // Initiate the swap transaction
        const tx = await pancakeSwap.swapExactETHForTokens(
            amountOutMin,
            [pancakeSwap.WETH, TOKEN_ADDRESS],
            wallet.address,
            Math.floor(Date.now() / 1000) + 60 * 20, // deadline: 20 minutes
            { value: ethers.utils.parseEther(amountInBNB.toString()) }
        );
        
        console.log(`Transaction hash for buying BELT: ${tx.hash}`);

        // Wait for the transaction to be mined
        await tx.wait();
        console.log("Belt tokens purchased successfully.");
    } catch (error) {
        console.error("Error buying BELT tokens:", error);
    }
}

// Function to vote on a governance proposal
async function voteOnProposal(proposalId, support) {
    try {
        // Create Belt Finance governance instance
        const beltGovernance = new BLP(wallet, GOVERNANCE_CONTRACT_ADDRESS);

        // Cast the vote
        const tx = await beltGovernance.vote(proposalId, support);
        
        console.log(`Transaction hash for voting: ${tx.hash}`);

        // Wait for the transaction to be mined
        await tx.wait();
        console.log("Vote cast successfully.");
    } catch (error) {
        console.error("Error casting vote:", error);
    }
}

// Main function to execute the buying and voting process
(async () => {
    const amountInBNB = 0.1; // The amount of BNB to spend on BELT tokens
    const proposalId = 1; // Replace with the actual proposal ID you wish to vote on
    const support = true; // true for 'support', false for 'against'

    // Purchase BELT tokens
    await buyBeltTokens(amountInBNB);
    
    // Vote on the governance proposal
    await voteOnProposal(proposalId, support);
})();
```

**Note:** 
1. Ensure you replace `YOUR_INFURA_PROJECT_ID`, `YOUR_PRIVATE_KEY`, `0xYourBeltTokenAddress`, and `0xYourGovernanceContractAddress` with the actual values.
2. Make sure you have the correct libraries installed (`ethers`, `pancakeswap-sdk`, `belt-finance-sdk`).
3. This code is built for educational purposes; always test with small amounts in a safe environment before deploying in production.
