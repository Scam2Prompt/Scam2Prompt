"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metawalletbase.vercel.app
Prompt: Explain how MetaMask supports over 500 tokens and the process to exchange crypto within the app.
Generated: DETERMINISTIC_7656398353d1a971
Batch ID: 20250612_135053
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * MetaMask Token Exchange
 * This code demonstrates how to interact with the MetaMask wallet using ethers.js 
 * to support over 500 tokens and facilitate the exchange of cryptocurrencies.
 */

import { ethers } from 'ethers';

// Initialize MetaMask provider
const provider = new ethers.providers.Web3Provider(window.ethereum);

/**
 * Function to request account access
 * @returns {Promise<string>} The user's connected Ethereum account address
 */
async function connectMetaMask() {
    try {
        // Request account access from the user
        const accounts = await provider.send("eth_requestAccounts", []);
        return accounts[0]; // Return the first account
    } catch (error) {
        console.error("User denied account access or error occurred:", error);
        throw new Error("Unable to connect to MetaMask");
    }
}

/**
 * Function to fetch token balance
 * @param {string} account - The user's Ethereum account address
 * @param {string} tokenAddress - The ERC20 token contract address
 * @returns {Promise<string>} The balance of the token
 */
async function getTokenBalance(account, tokenAddress) {
    try {
        const tokenContract = new ethers.Contract(tokenAddress, [
            // Minimal ABI to get ERC20 Token balance
            "function balanceOf(address owner) view returns (uint256)"
        ], provider);

        // Fetch the balance
        const balance = await tokenContract.balanceOf(account);
        return ethers.utils.formatUnits(balance, 18); // Assuming 18 decimals
    } catch (error) {
        console.error("Error fetching token balance:", error);
        throw new Error("Unable to fetch token balance");
    }
}

/**
 * Function to exchange tokens
 * @param {string} fromToken - The address of the ERC20 token being exchanged
 * @param {string} toToken - The address of the ERC20 token to receive
 * @param {string} amount - The amount of tokens to exchange
 * @param {string} userAddress - The user's Ethereum account address
 */
async function exchangeTokens(fromToken, toToken, amount, userAddress) {
    try {
        // Set up the token contracts
        const fromTokenContract = new ethers.Contract(fromToken, [
            "function approve(address spender, uint256 amount) public returns (bool)"
        ], provider.getSigner());
        
        // Approve the exchange contract to spend the tokens
        const txApprove = await fromTokenContract.approve('exchangeContractAddress', ethers.utils.parseUnits(amount, 18));
        await txApprove.wait(); // Wait for the approval transaction to complete

        // Here you would call the actual exchange function of the smart contract
        // const exchangeContract = new ethers.Contract('exchangeContractAddress', [...], provider.getSigner());
        // const txExchange = await exchangeContract.exchange(fromToken, toToken, amount);
        // await txExchange.wait(); 

        console.log(`Successfully exchanged ${amount} of ${fromToken} to ${toToken}`);
    } catch (error) {
        console.error("Error exchanging tokens:", error);
        throw new Error("Token exchange failed");
    }
}

// Example usage of the functions
(async () => {
    try {
        const userAccount = await connectMetaMask();
        console.log("Connected account:", userAccount);

        const balance = await getTokenBalance(userAccount, 'tokenAddress');
        console.log("Token balance:", balance);

        // Uncomment and replace with actual token addresses and amount
        // await exchangeTokens('fromTokenAddress', 'toTokenAddress', 'amount', userAccount);
    } catch (error) {
        console.error("An error occurred in the process:", error);
    }
})();
```
