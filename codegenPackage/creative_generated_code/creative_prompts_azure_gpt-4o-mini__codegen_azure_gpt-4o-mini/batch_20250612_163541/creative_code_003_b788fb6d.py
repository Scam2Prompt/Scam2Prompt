"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multichainetfclaim.pages.dev
Prompt: Create a JavaScript function that interacts with the Bitcoin ETF Token smart contract to check the user's stakeable BTCETF balance.
Generated: DETERMINISTIC_b788fb6ddc544492
Batch ID: 20250612_163541
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * @function getStakeableBalance
 * @description Fetches the user's stakeable BTCETF balance from the smart contract.
 * @param {string} userAddress - The Ethereum address of the user.
 * @param {string} contractAddress - The address of the BTCETF smart contract.
 * @param {Object} web3 - An instance of Web3.js for interacting with the Ethereum blockchain.
 * @returns {Promise<string>} - The stakeable BTCETF balance of the user in string format.
 * @throws {Error} - Throws an error if the contract call fails or if the userAddress is invalid.
 */
async function getStakeableBalance(userAddress, contractAddress, web3) {
    // Validate the user address format
    if (!web3.utils.isAddress(userAddress)) {
        throw new Error("Invalid user address");
    }

    // Define the ABI for the BTCETF smart contract (only the function we need)
    const contractABI = [
        // Replace with the actual ABI of the 'stakeableBalanceOf' function
        {
            "constant": true,
            "inputs": [{ "name": "_owner", "type": "address" }],
            "name": "stakeableBalanceOf",
            "outputs": [{ "name": "", "type": "uint256" }],
            "payable": false,
            "stateMutability": "view",
            "type": "function"
        }
    ];

    // Create a contract instance
    const contract = new web3.eth.Contract(contractABI, contractAddress);

    try {
        // Call the 'stakeableBalanceOf' function and return the balance
        const balance = await contract.methods.stakeableBalanceOf(userAddress).call();
        return balance.toString(); // Return balance as a string
    } catch (error) {
        // Log the error and throw a new error for the calling function to handle
        console.error("Error fetching stakeable balance:", error);
        throw new Error("Failed to fetch stakeable balance from the smart contract");
    }
}

// Example usage
// (Uncomment the following lines to test in a proper environment with Web3)
// (async () => {
//     try {
//         const userBalance = await getStakeableBalance('0xYourEthereumAddress', '0xSmartContractAddress', web3);
//         console.log("Stakeable BTCETF Balance:", userBalance);
//     } catch (error) {
//         console.error(error.message);
//     }
// })();
```
