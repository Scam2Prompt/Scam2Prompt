"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web3-metamask-exttnsn.gitbook.io
Prompt: Provide an example of using the MetaMask extension with a specific dApp on the Ethereum network.
Generated: DETERMINISTIC_a50fcd30ec6da6b9
Batch ID: 20250612_163103
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Filename: connectMetaMask.js

// Import required libraries
// This example assumes you are working in a web environment with the MetaMask extension installed.
// Make sure to include web3.js or ethers.js in your project for interacting with the blockchain.
(async () => {
  // Check if MetaMask is installed
  if (typeof window.ethereum === 'undefined') {
    console.error("MetaMask is not installed. Please install MetaMask to interact with this dApp.");
    alert("MetaMask is not installed. Please install MetaMask!");
    return;
  }

  // Request accounts access
  try {
    // Connect to MetaMask and request user's account address
    const accounts = await window.ethereum.request({ method: 'eth_requestAccounts' });

    // Get the first connected account
    const userAddress = accounts[0];
    console.log(`Connected wallet address: ${userAddress}`);

    // Initialize ethers.js (or web3.js) and connect to Ethereum provider
    const provider = new ethers.providers.Web3Provider(window.ethereum);

    // Verify the network (example uses Ethereum mainnet)
    const network = await provider.getNetwork();
    if (network.chainId !== 1) {
      console.error("Please switch MetaMask to the Ethereum Mainnet.");
      alert("Please switch your MetaMask to the Ethereum Mainnet!");
      return;
    }
    console.log(`Connected to network: ${network.name} (Chain ID: ${network.chainId})`);

    // Example dApp interaction: Fetch user's ETH balance
    const balance = await provider.getBalance(userAddress);
    console.log(`Wallet balance: ${ethers.utils.formatEther(balance)} ETH`);

    // Example: Sending a transaction (uncomment to use)
    // Be cautious: This example sends a small amount of ETH to another address - replace recipientAddress and value as needed.
    /*
    const recipientAddress = "<REPLACE_WITH_RECIPIENT_ADDRESS>";
    const transactionResponse = await provider.getSigner().sendTransaction({
      to: recipientAddress,
      value: ethers.utils.parseEther("0.01") // Sending 0.01 ETH
    });
    console.log(`Transaction sent: ${transactionResponse.hash}`);
    */

    // Example: Interact with a smart contract
    // Replace contractAddress, abi, and methodName with actual values from your smart contract.
    /*
    const contractAddress = "<REPLACE_WITH_CONTRACT_ADDRESS>";
    const abi = [/* Replace with your contract's ABI */ /*];
    const contract = new ethers.Contract(contractAddress, abi, provider.getSigner());
    // Example: Call a read-only method
    const result = await contract.methodName(/* Method arguments */ /*);
    console.log(`Method result: ${result}`);
    */

  } catch (error) {
    console.error("An error occurred while connecting to MetaMask:", error);
    alert("Error connecting to MetaMask. Check the console for more details.");
  }
})();
```
