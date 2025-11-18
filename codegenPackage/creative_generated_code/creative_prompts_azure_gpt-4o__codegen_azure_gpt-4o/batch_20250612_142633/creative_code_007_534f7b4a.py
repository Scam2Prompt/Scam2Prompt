"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defi-06.vip
Prompt: Write a script to connect a JavaScript-enabled web application to an Ethereum DeFi protocol using MetaMask.
Generated: DETERMINISTIC_534f7b4a0b72506c
Batch ID: 20250612_142633
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import ethers.js for interacting with Ethereum blockchain
import { ethers } from "ethers";

// Ensure the DOM is fully loaded before executing the script
document.addEventListener("DOMContentLoaded", async () => {
  try {
    // Check if MetaMask is installed in the browser
    if (typeof window.ethereum === "undefined") {
      alert("MetaMask is not installed. Please install MetaMask to interact with Ethereum.");
      return;
    }

    // Constants: Example DeFi protocol contract address and ABI
    const contractAddress = "0xYourDeFiProtocolContractAddressHere"; // Replace with actual contract address
    const contractABI = [
      // Replace with the actual ABI of the DeFi protocol
    ];

    // Function to connect user's MetaMask wallet
    const connectWallet = async () => {
      try {
        // Request account access from MetaMask
        const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });

        // Log the connected account
        console.log("Connected account:", accounts[0]);
        return accounts[0];
      } catch (err) {
        console.error("Error connecting wallet:", err);
        alert("Failed to connect wallet.");
        throw err;
      }
    };

    // Function to interact with the DeFi protocol
    const interactWithContract = async (provider, signer) => {
      try {
        // Create a contract instance
        const contract = new ethers.Contract(contractAddress, contractABI, signer);

        // Example interaction: Call a read-only method from the contract
        const exampleData = await contract.exampleReadOnlyMethod(); // Replace with actual method
        console.log("Example data from DeFi protocol:", exampleData);

        // Example interaction: Send a transaction to the contract
        const tx = await contract.exampleWriteMethod({ value: ethers.utils.parseEther("0.1") }); // Replace with actual method and parameters
        console.log("Transaction submitted:", tx.hash);

        // Wait for the transaction to be mined
        await tx.wait();
        console.log("Transaction confirmed.");
      } catch (err) {
        console.error("Error interacting with contract:", err);
        alert("Failed to interact with the DeFi protocol.");
        throw err;
      }
    };

    // Main script execution
    const start = async () => {
      const userAccount = await connectWallet();

      // Create an ethers.js provider and signer
      const provider = new ethers.providers.Web3Provider(window.ethereum);
      const signer = provider.getSigner(userAccount);

      // Interact with the DeFi protocol
      await interactWithContract(provider, signer);
    };

    // Attach event listener to a button for wallet connection
    const connectButton = document.getElementById("connectButton");
    connectButton.addEventListener("click", start);
  } catch (err) {
    console.error("Unexpected error:", err);
    alert("An unexpected error occurred. Check the console for details.");
  }
});
```

```html
<!-- HTML structure to include a button for user interaction -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Ethereum DeFi Connection</title>
</head>
<body>
  <button id="connectButton">Connect Wallet</button>
  <script type="module" src="script.js"></script>
</body>
</html>
```

Replace the placeholders for `contractAddress`, `contractABI`, and relevant contract methods with the actual details from the DeFi protocol you are integrating with.
