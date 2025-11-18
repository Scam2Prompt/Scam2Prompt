"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mmetadaflkugigns.webflow.io
Prompt: Provide code to interact with MetaMask's self-custodial wallet features, including sending, receiving, and bridging tokens across supported networks like BNB Smart Chain and Arbitrum One.
Generated: DETERMINISTIC_63d69b7bd3ca2ce6
Batch ID: 20250612_145130
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import dependencies
import Web3 from 'web3';

// Initialize constants
const METAMASK_PROVIDER = window.ethereum; // MetaMask provider injected into the browser
const BNB_CHAIN_ID = '0x38'; // Chain ID for Binance Smart Chain
const ARBITRUM_CHAIN_ID = '0xa4b1'; // Chain ID for Arbitrum One

/**
 * Connect to MetaMask wallet
 * @returns {Promise<string>} User's wallet address
 */
async function connectToMetaMask() {
  if (!METAMASK_PROVIDER) {
    throw new Error('MetaMask is not installed in the browser.');
  }

  // Request account access from MetaMask
  const accounts = await METAMASK_PROVIDER.request({ method: 'eth_requestAccounts' });
  return accounts[0]; // Return the first wallet address
}

/**
 * Switch network in MetaMask
 * @param {string} chainId - Chain ID to switch to
 * @returns {Promise<void>}
 */
async function switchNetwork(chainId) {
  try {
    await METAMASK_PROVIDER.request({
      method: 'wallet_switchEthereumChain',
      params: [{ chainId }],
    });
  } catch (error) {
    if (error.code === 4902) {
      throw new Error('The requested chain is not added to MetaMask.');
    } else {
      throw error;
    }
  }
}

/**
 * Send tokens to another address
 * @param {string} from - Sender's wallet address
 * @param {string} to - Recipient's wallet address
 * @param {string} tokenAddress - ERC-20 token contract address
 * @param {string} amount - Amount of tokens to send (in wei)
 * @returns {Promise<string>} Transaction hash
 */
async function sendTokens(from, to, tokenAddress, amount) {
  const web3 = new Web3(METAMASK_PROVIDER);

  // ABI for ERC-20 token transfer function
  const erc20Abi = [
    {
      constant: false,
      inputs: [
        { name: '_to', type: 'address' },
        { name: '_value', type: 'uint256' },
      ],
      name: 'transfer',
      outputs: [{ name: '', type: 'bool' }],
      type: 'function',
    },
  ];

  const contract = new web3.eth.Contract(erc20Abi, tokenAddress);

  // Send transaction
  const tx = await contract.methods.transfer(to, amount).send({ from });
  return tx.transactionHash; // Return the transaction hash
}

/**
 * Bridge tokens between supported networks
 * (Note: Bridging typically requires an external bridge service. This function demonstrates sending tokens 
 * between networks, but bridging should integrate third-party APIs or smart contracts.)
 * @param {string} from - Sender's wallet address
 * @param {string} to - Recipient's wallet address
 * @param {string} tokenAddress - ERC-20 token contract address
 * @param {string} amount - Amount of tokens to bridge (in wei)
 * @param {string} targetChainId - Target chain ID
 * @returns {Promise<string>} Transaction hash
 */
async function bridgeTokens(from, to, tokenAddress, amount, targetChainId) {
  const currentChainId = await METAMASK_PROVIDER.request({ method: 'eth_chainId' });

  if (currentChainId !== targetChainId) {
    await switchNetwork(targetChainId); // Switch to the target network in MetaMask
  }

  // Send tokens (assuming token exists on the target chain and can be transferred directly)
  return await sendTokens(from, to, tokenAddress, amount);
}

/**
 * Example usage
 */
async function example() {
  try {
    // Connect to MetaMask
    const userAddress = await connectToMetaMask();
    console.log('Connected wallet address:', userAddress);

    // Switch to Binance Smart Chain
    await switchNetwork(BNB_CHAIN_ID);
    console.log('Switched to Binance Smart Chain.');

    // Send tokens on Binance Smart Chain
    const txHash = await sendTokens(
      userAddress,
      '0xRecipientAddressHere',
      '0xTokenContractAddressHere',
      Web3.utils.toWei('1', 'ether') // Sending 1 token
    );
    console.log('Transaction hash:', txHash);

    // Bridge tokens to Arbitrum
    const bridgeTxHash = await bridgeTokens(
      userAddress,
      '0xRecipientAddressHereOnArbitrum',
      '0xTokenContractAddressHere',
      Web3.utils.toWei('1', 'ether'), // Sending 1 token
      ARBITRUM_CHAIN_ID
    );
    console.log('Bridge transaction hash:', bridgeTxHash);
  } catch (error) {
    console.error('Error:', error.message);
  }
}

// Call the example function to demonstrate usage
example();
```
