"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dcqqk.com
Prompt: Provide an example of using Web3.js to fetch real-time Ethereum token balances in a DeFi application.
Generated: DETERMINISTIC_7a8c6262f38cf944
Batch ID: 20250612_154002
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// Import the Web3 library
const Web3 = require('web3');

// Set up the Web3 provider (e.g., Infura, Alchemy, or your own node)
const web3 = new Web3(new Web3.providers.HttpProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'));

// ERC20 Token Contract ABI (minimal)
const ERC20_ABI = [
    // Get the balance of an account
    {
        "constant": true,
        "inputs": [{ "name": "account", "type": "address" }],
        "name": "balanceOf",
        "outputs": [{ "name": "", "type": "uint256" }],
        "payable": false,
        "stateMutability": "view",
        "type": "function"
    }
];

// Function to fetch the token balance
async function getTokenBalance(tokenAddress, userAddress) {
    try {
        // Create a contract instance for the specified token
        const tokenContract = new web3.eth.Contract(ERC20_ABI, tokenAddress);

        // Fetch the balance of the user
        const balance = await tokenContract.methods.balanceOf(userAddress).call();

        // Convert balance from Wei to Ether (or appropriate token decimals)
        const decimals = await tokenContract.methods.decimals().call();
        const formattedBalance = balance / (10 ** decimals);

        return formattedBalance;
    } catch (error) {
        console.error("Error fetching token balance:", error);
        throw new Error("Could not fetch token balance");
    }
}

// Example usage
(async () => {
    const tokenAddress = '0xYourTokenAddressHere'; // Replace with the actual token address
    const userAddress = '0xYourUserAddressHere';   // Replace with the actual user address

    try {
        const balance = await getTokenBalance(tokenAddress, userAddress);
        console.log(`Token balance of ${userAddress}: ${balance}`);
    } catch (error) {
        console.error("Error:", error.message);
    }
})();
```

**Note:** Ensure to replace `YOUR_INFURA_PROJECT_ID`, `0xYourTokenAddressHere`, and `0xYourUserAddressHere` with actual values before running the code.
