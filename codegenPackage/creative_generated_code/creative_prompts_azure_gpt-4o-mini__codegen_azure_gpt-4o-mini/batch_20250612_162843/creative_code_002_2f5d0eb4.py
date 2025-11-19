"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton-app.vercel.app
Prompt: Can you provide code examples for implementing staking features in a dApp on the TON Blockchain?
Generated: DETERMINISTIC_2f5d0eb4975efb10
Batch ID: 20250612_162843
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Imports necessary libraries for interacting with the TON Blockchain
const TonClient = require("@tonclient/core").TonClient;
const { libNode } = require("@tonclient/lib-node");

// Initialize the TON Client
TonClient.useBinaryLibrary(libNode);

const client = new TonClient({
    network: {
        server_address: "net.ton.dev",
    },
});

// Staking smart contract address
const STAKING_CONTRACT_ADDRESS = "your_staking_contract_address_here";

// Function to stake tokens
async function stakeTokens(amount, walletAddress) {
    try {
        // Validate input parameters
        if (amount <= 0) throw new Error("Stake amount must be greater than zero");
        
        // Prepare the staking transaction
        const stakeMessage = {
            address: STAKING_CONTRACT_ADDRESS,
            function_name: "stake",
            input: {
                amount: amount,
                walletAddress: walletAddress,
            },
        };

        // Send the staking transaction
        const result = await client.functions.sendMessage(stakeMessage);
        console.log("Staking transaction result:", result);
    } catch (error) {
        console.error("Error staking tokens:", error);
    }
}

// Function to unstake tokens
async function unstakeTokens(amount, walletAddress) {
    try {
        // Validate input parameters
        if (amount <= 0) throw new Error("Unstake amount must be greater than zero");

        // Prepare the unstaking transaction
        const unstakeMessage = {
            address: STAKING_CONTRACT_ADDRESS,
            function_name: "unstake",
            input: {
                amount: amount,
                walletAddress: walletAddress,
            },
        };

        // Send the unstaking transaction
        const result = await client.functions.sendMessage(unstakeMessage);
        console.log("Unstaking transaction result:", result);
    } catch (error) {
        console.error("Error unstaking tokens:", error);
    }
}

// Function to check staking balance
async function checkStakingBalance(walletAddress) {
    try {
        // Prepare the balance query
        const balanceQuery = {
            address: STAKING_CONTRACT_ADDRESS,
            function_name: "getBalance",
            input: {
                walletAddress: walletAddress,
            },
        };

        // Fetch the staking balance
        const balance = await client.functions.getFunctionResponse(balanceQuery);
        console.log("Staking balance:", balance);
        return balance;
    } catch (error) {
        console.error("Error fetching staking balance:", error);
    }
}

// Example Usage
(async () => {
    const walletAddress = "your_wallet_address_here";
    
    // Staking tokens
    await stakeTokens(100, walletAddress);
    
    // Checking staking balance
    await checkStakingBalance(walletAddress);
    
    // Unstaking tokens
    await unstakeTokens(50, walletAddress);
})();

// Properly closing the TON Client connection
process.on('exit', () => {
    client.close();
});
```
