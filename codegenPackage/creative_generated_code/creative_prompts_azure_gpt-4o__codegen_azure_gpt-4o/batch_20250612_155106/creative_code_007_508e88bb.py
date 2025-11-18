"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tronlink.cloud
Prompt: Provide an example of how to use TronLink Wallet's EVM network support to interact with Ethereum, BSC, and BTTC tokens.
Generated: DETERMINISTIC_508e88bbb31f1bf1
Batch ID: 20250612_155106
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary dependencies
const Web3 = require('web3'); // Web3.js library to interact with EVM-compatible networks

// Ensure TronLink is installed and available in the browser
if (typeof window.tronWeb === 'undefined') {
  console.error("TronLink Wallet is not detected. Please install TronLink.");
} else {
  // Initialize TronLink's Web3 provider
  const web3 = new Web3(window.tronWeb);

  // Example contract addresses for Ethereum, BSC, and BTTC tokens (replace with actual contract addresses)
  const tokenAddresses = {
    ethereum: '0xYourEthereumTokenContractAddress',
    bsc: '0xYourBSCTokenContractAddress',
    bttc: '0xYourBTTCTokenContractAddress',
  };

  // ERC-20 ABI (simplified for token interaction)
  const erc20ABI = [
    {
      constant: true,
      inputs: [{ name: '_owner', type: 'address' }],
      name: 'balanceOf',
      outputs: [{ name: 'balance', type: 'uint256' }],
      type: 'function',
    },
    {
      constant: false,
      inputs: [
        { name: '_to', type: 'address' },
        { name: '_value', type: 'uint256' },
      ],
      name: 'transfer',
      outputs: [{ name: 'success', type: 'bool' }],
      type: 'function',
    },
  ];

  /**
   * Function to get token balance
   * @param {string} tokenAddress - The token contract address
   * @param {string} userAddress - The user's wallet address
   */
  const getTokenBalance = async (tokenAddress, userAddress) => {
    try {
      const tokenContract = new web3.eth.Contract(erc20ABI, tokenAddress);
      const balance = await tokenContract.methods.balanceOf(userAddress).call();
      console.log(`Balance for token at ${tokenAddress}: `, balance);
      return balance;
    } catch (error) {
      console.error('Error fetching token balance:', error);
    }
  };

  /**
   * Function to transfer tokens
   * @param {string} tokenAddress - The token contract address
   * @param {string} recipientAddress - The recipient's wallet address
   * @param {number} amount - The amount of tokens to transfer
   */
  const transferTokens = async (tokenAddress, recipientAddress, amount) => {
    try {
      const accounts = await web3.eth.getAccounts(); // Get connected accounts
      const senderAddress = accounts[0]; // Use the first account
      const tokenContract = new web3.eth.Contract(erc20ABI, tokenAddress);

      const transaction = tokenContract.methods.transfer(recipientAddress, amount);
      const result = await transaction.send({ from: senderAddress });
      console.log('Transfer successful:', result);
      return result;
    } catch (error) {
      console.error('Error transferring tokens:', error);
    }
  };

  // Example usage
  const exampleUserAddress = '0xYourWalletAddress';
  const exampleRecipient = '0xRecipientWalletAddress';
  const transferAmount = 100; // Example transfer amount

  // Fetch balances for Ethereum, BSC, and BTTC tokens
  Object.keys(tokenAddresses).forEach(async (network) => {
    const tokenAddress = tokenAddresses[network];
    await getTokenBalance(tokenAddress, exampleUserAddress);
  });

  // Transfer tokens on Ethereum (example)
  transferTokens(tokenAddresses.ethereum, exampleRecipient, transferAmount);
}
```
