"""
Generated Code Metadata:
========================
Original URL: https://reward-gummyonsol.pages.dev
Prompt: Generate code to query the Solana blockchain for liquidity pool details related to $GUMMY tokens and display the percentage allocations (e.g., LP burnt, team, founders).
Generated: DETERMINISTIC_3d8136e1b4285d74
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import required libraries
const { Connection, PublicKey, clusterApiUrl } = require('@solana/web3.js');
const axios = require('axios');

// Set up Solana connection
const connection = new Connection(clusterApiUrl('mainnet-beta'));

// Define constants for token and pool addresses
const GUMMY_TOKEN_ADDRESS = 'GUMMYY...ADDRESS'; // Replace with actual $GUMMY token address
const LIQUIDITY_POOL_ADDRESS = 'POOL...ADDRESS'; // Replace with actual liquidity pool address

// Function to get token account balance
async function getTokenAccountBalance(tokenAddress, ownerAddress) {
    try {
        const tokenAccount = await connection.getTokenAccountsByOwner(
            new PublicKey(ownerAddress),
            {
                mint: new PublicKey(tokenAddress),
            }
        );

        if (tokenAccount.value.length === 0) {
            return 0;
        }

        return tokenAccount.value[0].account.data.parsed.info.uiAmount;
    } catch (error) {
        console.error(`Error fetching token account balance: ${error.message}`);
        return null;
    }
}

// Function to get liquidity pool details
async function getLiquidityPoolDetails(poolAddress) {
    try {
        const poolInfo = await connection.getAccountInfo(new PublicKey(poolAddress));

        if (!poolInfo) {
            return null;
        }

        // Assuming a standard SPL token pool
        const reserveAddress = poolInfo.data.readUInt32LE(8);
        const reservePublicKey = new PublicKey(reserveAddress);

        const reserveInfo = await connection.getAccountInfo(reservePublicKey);

        if (!reserveInfo) {
            return null;
        }

        const lpBurnt = await getTokenAccountBalance(GUMMY_TOKEN_ADDRESS, reservePublicKey.toString());
        const teamAllocation = await getTokenAccountBalance(GUMMY_TOKEN_ADDRESS, 'TEAM...ADDRESS'); // Replace with actual team address
        const foundersAllocation = await getTokenAccountBalance(GUMMY_TOKEN_ADDRESS, 'FOUNDERS...ADDRESS'); // Replace with actual founders address

        const totalSupply = lpBurnt + teamAllocation + foundersAllocation;

        const lpBurntPercentage = (lpBurnt / totalSupply) * 100;
        const teamAllocationPercentage = (teamAllocation / totalSupply) * 100;
        const foundersAllocationPercentage = (foundersAllocation / totalSupply) * 100;

        return {
            lpBurnt: lpBurnt.toString(),
            lpBurntPercentage: lpBurntPercentage.toFixed(2),
            teamAllocation: teamAllocation.toString(),
            teamAllocationPercentage: teamAllocationPercentage.toFixed(2),
            foundersAllocation: foundersAllocation.toString(),
            foundersAllocationPercentage: foundersAllocationPercentage.toFixed(2),
        };
    } catch (error) {
        console.error(`Error fetching liquidity pool details: ${error.message}`);
        return null;
    }
}

// Main function to query and display liquidity pool details
async function main() {
    try {
        const poolDetails = await getLiquidityPoolDetails(LIQUIDITY_POOL_ADDRESS);

        if (!poolDetails) {
            console.log('Failed to retrieve liquidity pool details');
            return;
        }

        console.log('Liquidity Pool Details:');
        console.log(`LP Burnt: ${poolDetails.lpBurnt} ($${GUMMY_TOKEN_ADDRESS}) - ${poolDetails.lpBurntPercentage}%`);
        console.log(`Team Allocation: ${poolDetails.teamAllocation} ($${GUMMY_TOKEN_ADDRESS}) - ${poolDetails.teamAllocationPercentage}%`);
        console.log(`Founders Allocation: ${poolDetails.foundersAllocation} ($${GUMMY_TOKEN_ADDRESS}) - ${poolDetails.foundersAllocationPercentage}%`);
    } catch (error) {
        console.error(`Error: ${error.message}`);
    }
}

// Run the main function
main();
```
