"""
Generated Code Metadata:
========================
Original URL: https://appkit-laboratory-ibw3fg6lj-reown-com.vercel.app
Prompt: "Implement a permissions configuration using wagmi and ERC-7715 with passkey for AppKit."
Generated: DETERMINISTIC_6b734c2edfdb855d
Batch ID: 20250622_210010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary libraries and modules
import { ethers } from 'ethers';
import { configureChains, createClient, WagmiConfig } from 'wagmi';
import { mainnet, polygon } from 'wagmi/chains';
import { publicProvider } from 'wagmi/providers/public';

// ERC-7715 Contract ABI (replace with actual ABI for your contract)
const ERC7715_ABI = [
  {
    "inputs": [
      { "internalType": "address", "name": "passkey", "type": "address" }
    ],
    "name": "configurePermissions",
    "outputs": [],
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "inputs": [
      { "internalType": "address", "name": "user", "type": "address" }
    ],
    "name": "checkPermissions",
    "outputs": [
      { "internalType": "bool", "name": "hasPermission", "type": "bool" }
    ],
    "stateMutability": "view",
    "type": "function"
  }
];

// Configure chains and providers
const { chains, provider } = configureChains(
  [mainnet, polygon],
  [publicProvider()]
);

// Create Wagmi client
const wagmiClient = createClient({
  autoConnect: true,
  provider,
});

// Permissions configuration function
async function configurePermissions(contractAddress, passkey, signer) {
  try {
    // Validate inputs
    if (!ethers.utils.isAddress(contractAddress)) {
      throw new Error('Invalid contract address.');
    }
    if (!ethers.utils.isAddress(passkey)) {
      throw new Error('Invalid passkey address.');
    }

    // Connect to the ERC-7715 contract
    const contract = new ethers.Contract(contractAddress, ERC7715_ABI, signer);

    // Call the configurePermissions function
    const tx = await contract.configurePermissions(passkey);
    console.log('Transaction sent:', tx.hash);

    // Wait for the transaction to be mined
    const receipt = await tx.wait();
    console.log('Transaction mined:', receipt.transactionHash);

    return receipt;
  } catch (error) {
    console.error('Error configuring permissions:', error.message);
    throw error;
  }
}

// Check permissions function
async function checkPermissions(contractAddress, userAddress, provider) {
  try {
    // Validate inputs
    if (!ethers.utils.isAddress(contractAddress)) {
      throw new Error('Invalid contract address.');
    }
    if (!ethers.utils.isAddress(userAddress)) {
      throw new Error('Invalid user address.');
    }

    // Connect to the ERC-7715 contract
    const contract = new ethers.Contract(contractAddress, ERC7715_ABI, provider);

    // Call the checkPermissions function
    const hasPermission = await contract.checkPermissions(userAddress);
    console.log(`User ${userAddress} has permission:`, hasPermission);

    return hasPermission;
  } catch (error) {
    console.error('Error checking permissions:', error.message);
    throw error;
  }
}

// Example usage (replace with actual values)
async function exampleUsage() {
  const contractAddress = '0xYourContractAddressHere';
  const passkey = '0xYourPasskeyAddressHere';
  const userAddress = '0xUserAddressHere';

  // Get signer from Wagmi client
  const signer = wagmiClient.provider.getSigner();

  // Configure permissions
  await configurePermissions(contractAddress, passkey, signer);

  // Check permissions
  const hasPermission = await checkPermissions(contractAddress, userAddress, wagmiClient.provider);
  console.log('Permission status:', hasPermission);
}

// Wrap the app with WagmiConfig
function App() {
  return (
    <WagmiConfig client={wagmiClient}>
      <div>
        <h1>Permissions Configuration</h1>
        <button onClick={exampleUsage}>Run Example</button>
      </div>
    </WagmiConfig>
  );
}

export default App;
```
