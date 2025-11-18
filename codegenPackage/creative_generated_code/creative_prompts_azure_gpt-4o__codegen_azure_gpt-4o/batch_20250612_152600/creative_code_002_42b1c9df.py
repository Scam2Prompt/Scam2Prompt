"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethcll.com
Prompt: Create a script using ethers.js to enable ETH pledging functionality, ensuring compatibility with mobile devices.
Generated: DETERMINISTIC_42b1c9df1d0e388a
Batch ID: 20250612_152600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules from ethers.js
const { ethers } = require("ethers");

// Define the main function to initialize and manage pledging functionality
async function enablePledging() {
  // Check if the user has a Web3 provider (e.g., MetaMask, etc.)
  if (typeof window.ethereum === "undefined") {
    console.error("No Web3 provider detected! Please install MetaMask or another provider.");
    return;
  }

  // Create a provider instance using the injected web3 provider
  const provider = new ethers.providers.Web3Provider(window.ethereum);

  // Request the user's wallet connection
  try {
    await provider.send("eth_requestAccounts", []);
  } catch (error) {
    console.error("Failed to connect wallet:", error.message);
    return;
  }

  // Access the signer (user account) from the provider
  const signer = provider.getSigner();

  // Function to pledge ETH
  async function pledgeETH(amountInEth) {
    try {
      // Validate input amount
      if (isNaN(amountInEth) || parseFloat(amountInEth) <= 0) {
        throw new Error("Invalid ETH amount. Please enter a positive number.");
      }

      // Convert the amount from ETH to Wei (smallest denomination)
      const amountInWei = ethers.utils.parseEther(amountInEth.toString());

      // Create and send a transaction
      const tx = await signer.sendTransaction({
        to: "0xYourPledgeRecipientAddressHere", // Replace with desired recipient address
        value: amountInWei, // Amount to send in Wei
      });

      console.log("Transaction sent successfully:", tx.hash);

      // Wait for the transaction to be mined
      const receipt = await tx.wait();
      console.log("Transaction confirmed:", receipt);
    } catch (error) {
      console.error("Error while pledging ETH:", error.message);
    }
  }

  // Example of pledging an amount (replace with dynamic logic if needed)
  // This is for demonstration purposes only. In production, integrate with UI/inputs.
  const exampleAmountToPledge = "0.1"; // 0.1 ETH
  pledgeETH(exampleAmountToPledge);
}

// Run the main function
enablePledging();
```

Replace `"0xYourPledgeRecipientAddressHere"` with the Ethereum address to which the ETH should be pledged.
