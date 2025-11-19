"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metamask.sewakamerabandung.id
Prompt: Can you provide a code example for using MetaMask to connect a dApp to the Ethereum blockchain?
Generated: DETERMINISTIC_61aa7b6e5cfe8c83
Batch ID: 20250612_135906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import Web3.js for Ethereum blockchain interaction
import Web3 from 'web3';

// Define a function to connect the dApp to MetaMask
async function connectToMetaMask() {
  try {
    // Check if MetaMask is installed
    if (typeof window.ethereum === 'undefined') {
      throw new Error('MetaMask is not installed. Please install MetaMask to use this dApp.');
    }

    // Request account access from MetaMask
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

    // Create a Web3 instance
    const web3 = new Web3(window.ethereum);

    // Get the user's Ethereum address (first connected account)
    const userAddress = accounts[0];
    console.log(`Connected account: ${userAddress}`);

    // Get the current network ID
    const networkId = await web3.eth.net.getId();
    console.log(`Connected to network ID: ${networkId}`);

    // Return Web3 instance and user details for further interaction
    return { web3, userAddress, networkId };
  } catch (error) {
    console.error(`Error connecting to MetaMask: ${error.message}`);
    throw error; // Re-throw the error for higher-level handling
  }
}

// Define a function to interact with a smart contract on Ethereum
async function interactWithContract(web3, contractAddress, abi, userAddress) {
  try {
    // Create a contract instance
    const contract = new web3.eth.Contract(abi, contractAddress);

    // Example: Call a read-only method from the smart contract
    const data = await contract.methods.someReadOnlyFunction().call();
    console.log(`Data from contract: ${data}`);

    // Example: Send a transaction to the smart contract
    const receipt = await contract.methods.someStateChangingFunction().send({ from: userAddress });
    console.log(`Transaction receipt: ${receipt}`);

    // Return the contract instance for further interaction
    return contract;
  } catch (error) {
    console.error(`Error interacting with contract: ${error.message}`);
    throw error; // Re-throw the error for higher-level handling
  }
}

// Example usage
(async () => {
  try {
    // Connect to MetaMask
    const { web3, userAddress, networkId } = await connectToMetaMask();

    // Define smart contract details
    const contractAddress = '0xYourContractAddressHere';
    const abi = [
      // Replace with your contract's ABI
      {
        constant: true,
        inputs: [],
        name: 'someReadOnlyFunction',
        outputs: [{ name: '', type: 'string' }],
        type: 'function',
      },
      {
        constant: false,
        inputs: [],
        name: 'someStateChangingFunction',
        outputs: [],
        type: 'function',
      },
    ];

    // Interact with the smart contract
    const contract = await interactWithContract(web3, contractAddress, abi, userAddress);
    console.log('Contract interaction completed successfully');
  } catch (error) {
    console.error(`Error in dApp workflow: ${error.message}`);
  }
})();
```
