"""
Generated Code Metadata:
========================
Original URL: https://ethzao.com
Prompt: Generate JavaScript code to enable proper functionality for ETH Pledge on mobile devices.
Generated: DETERMINISTIC_7fdcaa43962cd003
Batch ID: 20250622_204829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// ETH Pledge functionality for mobile devices
// This script enables users to pledge ETH using a Web3-enabled wallet on mobile devices.

// Ensure the script runs only after the DOM is fully loaded
document.addEventListener("DOMContentLoaded", async () => {
  // Check if Web3 is injected by the browser (e.g., MetaMask)
  if (typeof window.ethereum === "undefined") {
    alert("Please install a Web3-enabled wallet like MetaMask to proceed.");
    return;
  }

  // Initialize Web3 provider
  const provider = window.ethereum;

  // Function to request wallet connection
  async function connectWallet() {
    try {
      // Request account access
      const accounts = await provider.request({ method: "eth_requestAccounts" });
      if (accounts.length === 0) {
        throw new Error("No accounts found. Please connect your wallet.");
      }
      return accounts[0]; // Return the first account
    } catch (error) {
      console.error("Error connecting wallet:", error.message);
      alert("Failed to connect wallet. Please try again.");
      throw error;
    }
  }

  // Function to send ETH pledge
  async function sendPledge(amountInEth) {
    try {
      // Validate input
      if (!amountInEth || isNaN(amountInEth) || amountInEth <= 0) {
        throw new Error("Invalid pledge amount. Please enter a valid number.");
      }

      // Convert ETH amount to Wei (smallest unit of ETH)
      const amountInWei = window.web3.utils.toWei(amountInEth.toString(), "ether");

      // Get the connected account
      const account = await connectWallet();

      // Send transaction
      const transactionParameters = {
        from: account, // Sender's address
        to: "0xYourRecipientAddressHere", // Replace with the recipient's address
        value: amountInWei, // Amount in Wei
      };

      const txHash = await provider.request({
        method: "eth_sendTransaction",
        params: [transactionParameters],
      });

      alert(`Transaction sent successfully! TX Hash: ${txHash}`);
    } catch (error) {
      console.error("Error sending pledge:", error.message);
      alert("Failed to send pledge. Please try again.");
    }
  }

  // Attach event listeners to buttons (assuming buttons exist in the HTML)
  const connectButton = document.getElementById("connectWalletButton");
  const pledgeButton = document.getElementById("sendPledgeButton");

  if (connectButton) {
    connectButton.addEventListener("click", async () => {
      try {
        const account = await connectWallet();
        alert(`Wallet connected: ${account}`);
      } catch (error) {
        console.error("Error during wallet connection:", error.message);
      }
    });
  }

  if (pledgeButton) {
    pledgeButton.addEventListener("click", async () => {
      const amountInput = document.getElementById("pledgeAmountInput");
      if (amountInput) {
        const amount = parseFloat(amountInput.value);
        await sendPledge(amount);
      } else {
        alert("Pledge amount input not found.");
      }
    });
  }
});
```

**Note:** Replace `"0xYourRecipientAddressHere"` with the actual Ethereum address where the pledge should be sent. Ensure the HTML includes elements with IDs `connectWalletButton`, `sendPledgeButton`, and `pledgeAmountInput` for the script to work correctly.
