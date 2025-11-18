"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doge-coin20.pages.dev
Prompt: Create a script using Web3.js or ethers.js to connect a decentralized wallet and facilitate the purchase of ERC-20 tokens, mimicking the DOGE20 presale widget functionality.
Generated: DETERMINISTIC_731c7799a99bc01d
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required modules
const ethers = require('ethers');

// Define constants
const INFURA_PROJECT_ID = 'your_infura_project_id'; // Replace with your Infura Project ID
const ERC20_TOKEN_ADDRESS = '0xYourTokenAddress';  // Replace with the ERC-20 contract address
const TOKEN_ABI = [
  // Minimal example ABI containing the `transfer` and `balanceOf` functions
  "function transfer(address to, uint amount) external returns (bool)",
  "function balanceOf(address owner) external view returns (uint)"
];

// Initialize the provider and signer
const provider = new ethers.providers.InfuraProvider('mainnet', INFURA_PROJECT_ID);
let signer;

// Connect wallet function
async function connectWallet() {
  try {
    // Check if the browser has an Ethereum provider (like MetaMask)
    if (!window.ethereum) {
      console.error('No Ethereum provider found. Please install MetaMask.');
      return;
    }

    // Prompt user to connect their wallet
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });
    const connectedAccount = accounts[0];
    console.log(`Wallet connected: ${connectedAccount}`);

    // Initialize the signer with the connected wallet
    signer = new ethers.providers.Web3Provider(window.ethereum).getSigner();
    return connectedAccount;
  } catch (error) {
    console.error('Error connecting wallet:', error);
  }
}

// Purchase ERC-20 tokens function
async function purchaseTokens(receiverAddress, amountInEther) {
  try {
    if (!signer) {
      console.error('Wallet not connected. Please connect your wallet first.');
      return;
    }

    const senderAddress = await signer.getAddress();
    console.log(`Purchasing tokens from ${senderAddress} to ${receiverAddress}`);

    // Convert Ether amount to Wei
    const amountInWei = ethers.utils.parseEther(amountInEther.toString());

    // Create a contract instance for the ERC-20 token
    const tokenContract = new ethers.Contract(ERC20_TOKEN_ADDRESS, TOKEN_ABI, signer);

    // Simulate sending tokens to the receiver address
    const transferTx = await tokenContract.transfer(receiverAddress, amountInWei);
    console.log('Transaction submitted. Waiting for confirmation...');

    // Wait for transaction to be mined
    const receipt = await transferTx.wait();
    console.log('Transaction confirmed:', receipt.transactionHash);

    return receipt;
  } catch (error) {
    console.error('Error purchasing tokens:', error);
  }
}

(async () => {
  // Example usage
  const receiverAddress = '0xReceiverAddress';  // Replace with the receiver's address
  const amountInEther = 0.01;                  // Replace with the desired amount in Ether

  console.log('Connecting wallet...');
  const walletAddress = await connectWallet();
  if (walletAddress) {
    console.log(`Purchasing tokens for ${receiverAddress} with ${amountInEther} Ether...`);
    const receipt = await purchaseTokens(receiverAddress, amountInEther);
    if (receipt) {
      console.log('Purchase completed successfully.');
    }
  }
})();
```

### Notes:
1. Replace placeholder values (e.g., `your_infura_project_id`, `0xYourTokenAddress`, `0xReceiverAddress`) with appropriate values before running the script.
2. Ensure the user's browser has a Web3-enabled wallet like MetaMask installed.
3. The token contract ABI should match the actual ERC-20 token contract being used; you may need to expand the ABI for additional functionality.
