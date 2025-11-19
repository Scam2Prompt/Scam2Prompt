"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maga-hat.fund
Prompt: Create a function in JavaScript that checks the balance of a $MAGA token holder on a decentralized exchange.
Generated: DETERMINISTIC_7b22c13832b8bd1f
Batch ID: 20250612_163601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to get the balance of a $MAGA token holder on a decentralized exchange.
 * @param {string} walletAddress - The wallet address of the token holder.
 * @param {string} contractAddress - The contract address of the $MAGA token.
 * @param {object} web3Instance - A Web3 instance connected to the blockchain network.
 * @returns {Promise<string>} - Returns the balance of $MAGA tokens in the wallet.
 */
async function getMagaTokenBalance(walletAddress, contractAddress, web3Instance) {
  try {
    // Input validation
    if (!web3Instance || typeof web3Instance !== 'object') {
      throw new Error('Invalid Web3 instance provided.');
    }
    if (!walletAddress || !web3Instance.utils.isAddress(walletAddress)) {
      throw new Error('Invalid wallet address provided.');
    }
    if (!contractAddress || !web3Instance.utils.isAddress(contractAddress)) {
      throw new Error('Invalid contract address provided.');
    }

    // ABI for an ERC-20 token contract (standard interface for balanceOf function)
    const erc20ABI = [
      {
        constant: true,
        inputs: [{ name: '_owner', type: 'address' }],
        name: 'balanceOf',
        outputs: [{ name: 'balance', type: 'uint256' }],
        type: 'function',
      },
    ];

    // Create a contract instance for the $MAGA token
    const contract = new web3Instance.eth.Contract(erc20ABI, contractAddress);

    // Call the balanceOf function to get the user's balance
    const balance = await contract.methods.balanceOf(walletAddress).call();

    // Convert the balance (usually a large integer) into a readable format
    return web3Instance.utils.fromWei(balance, 'ether'); // Assuming the token uses 18 decimals (commonly used)
  } catch (error) {
    // Log or rethrow the error for better debugging
    console.error('Error fetching token balance:', error.message);
    throw error;
  }
}

module.exports = { getMagaTokenBalance };
```

This function requires a `Web3.js` instance connected to the blockchain network, a valid wallet address, and the $MAGA token's contract address to function properly.
