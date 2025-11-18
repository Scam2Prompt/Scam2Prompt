"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-flockerz-com.pages.dev
Prompt: Write JavaScript code using Web3.js to connect a MetaMask wallet and execute a staking transaction for $FLOCK tokens.
Generated: DETERMINISTIC_4ca7f2ef08221c02
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import Web3 library
const Web3 = require('web3');

// Constants for the FLOCK token and staking contract
const FLOCK_TOKEN_ADDRESS = "0xYourFlockTokenAddress";        // Replace with actual FLOCK token address
const STAKING_CONTRACT_ADDRESS = "0xYourStakingContractAddress"; // Replace with actual staking contract address
const FLOCK_ABI = [];                                       // Replace with the ABI of $FLOCK token
const STAKING_CONTRACT_ABI = [];                           // Replace with the ABI of staking contract

// Initialize Web3 instance
let web3;

// Connect MetaMask wallet and execute staking transaction
async function connectWalletAndStake(amountToStake) {
    try {
        // Check if MetaMask is installed
        if (typeof window.ethereum === 'undefined') {
            throw new Error("MetaMask is not installed. Please install MetaMask to use this feature.");
        }

        // Request wallet connection
        await window.ethereum.request({ method: 'eth_requestAccounts' });

        // Create a Web3 instance
        web3 = new Web3(window.ethereum);

        // Get the connected account
        const accounts = await web3.eth.getAccounts();
        const userAddress = accounts[0];
        console.log(`Connected wallet address: ${userAddress}`);

        // Get the FLOCK token contract instance
        const flockTokenContract = new web3.eth.Contract(FLOCK_ABI, FLOCK_TOKEN_ADDRESS);

        // Get the staking contract instance
        const stakingContract = new web3.eth.Contract(STAKING_CONTRACT_ABI, STAKING_CONTRACT_ADDRESS);

        // Convert staking amount to the token's smallest unit (e.g., Wei for Ether)
        const decimals = await flockTokenContract.methods.decimals().call();
        const stakingAmount = web3.utils.toBN(amountToStake * (10 ** decimals));

        console.log(`Staking amount in smallest unit: ${stakingAmount.toString()}`);

        // Approve staking contract to spend tokens on behalf of the user
        console.log("Approving staking contract...");
        const approvalTx = await flockTokenContract.methods
            .approve(STAKING_CONTRACT_ADDRESS, stakingAmount)
            .send({ from: userAddress });
        console.log("Approval transaction successful: ", approvalTx.transactionHash);

        // Execute staking transaction
        console.log("Executing staking transaction...");
        const stakingTx = await stakingContract.methods
            .stakeTokens(stakingAmount)
            .send({ from: userAddress });
        console.log("Staking transaction successful: ", stakingTx.transactionHash);

        console.log("Staking completed successfully!");

    } catch (error) {
        console.error("Error during wallet connection or staking:", error.message);
    }
}

// Example usage: Stake 100 FLOCK tokens
connectWalletAndStake(100);
```

**Notes:**
1. Replace `FLOCK_TOKEN_ADDRESS`, `STAKING_CONTRACT_ADDRESS`, `FLOCK_ABI`, and `STAKING_CONTRACT_ABI` with the actual values for your token and staking contract.
2. Make sure the MetaMask wallet is installed and the user is logged into the wallet.
3. Add any extra error handling based on your application's specific needs.
