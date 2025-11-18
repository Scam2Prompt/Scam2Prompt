"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aerodrome-finac.xyz
Prompt: Write JavaScript code to connect to an Ethereum wallet using `window.ethereum.request` and enable buttons for sending Ether and checking balances, as described in the webpage.
Generated: DETERMINISTIC_584e9721dbbf1855
Batch ID: 20250612_155115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Ensure the DOM is fully loaded before executing the script
document.addEventListener("DOMContentLoaded", () => {
  const connectButton = document.getElementById("connectWalletButton");
  const sendEtherButton = document.getElementById("sendEtherButton");
  const checkBalanceButton = document.getElementById("checkBalanceButton");

  let userAccount = null;

  /**
   * Connect to MetaMask wallet
   */
  async function connectWallet() {
    if (typeof window.ethereum === "undefined") {
      alert("MetaMask is not installed. Please install it to use this feature.");
      return;
    }

    try {
      // Request accounts from MetaMask
      const accounts = await window.ethereum.request({ method: "eth_requestAccounts" });
      if (accounts.length === 0) {
        alert("No accounts found. Please make sure your MetaMask wallet is unlocked.");
      } else {
        userAccount = accounts[0];
        alert(`Connected to wallet: ${userAccount}`);
        sendEtherButton.disabled = false;
        checkBalanceButton.disabled = false;
      }
    } catch (error) {
      console.error("Error connecting wallet:", error);
      alert("Failed to connect wallet. Please check the console for details.");
    }
  }

  /**
   * Send Ether from connected wallet to a specified address
   */
  async function sendEther() {
    if (!userAccount) {
      alert("Please connect your wallet first.");
      return;
    }

    const recipientAddress = prompt("Enter recipient wallet address:");
    const amountInEther = prompt("Enter amount to send (in Ether):");

    if (!recipientAddress || !amountInEther) {
      alert("Recipient address and amount are required.");
      return;
    }

    try {
      const transactionParameters = {
        to: recipientAddress, // The recipient address
        from: userAccount, // The sender address
        value: window.ethereum.utils.toHex(window.ethereum.utils.toWei(amountInEther, "ether")), // Convert Ether to Wei
      };

      await window.ethereum.request({
        method: "eth_sendTransaction",
        params: [transactionParameters],
      });

      alert("Transaction sent successfully!");
    } catch (error) {
      console.error("Error sending Ether:", error);
      alert("Failed to send Ether. Please check the console for details.");
    }
  }

  /**
   * Check the balance of the connected wallet
   */
  async function checkBalance() {
    if (!userAccount) {
      alert("Please connect your wallet first.");
      return;
    }

    try {
      const balanceInWei = await window.ethereum.request({
        method: "eth_getBalance",
        params: [userAccount, "latest"], // Fetch balance for the latest block
      });

      const balanceInEther = window.ethereum.utils.fromWei(balanceInWei, "ether"); // Convert Wei to Ether
      alert(`Wallet Balance: ${balanceInEther} ETH`);
    } catch (error) {
      console.error("Error checking balance:", error);
      alert("Failed to check balance. Please check the console for details.");
    }
  }

  // Bind event listeners to buttons
  connectButton.addEventListener("click", connectWallet);
  sendEtherButton.addEventListener("click", sendEther);
  checkBalanceButton.addEventListener("click", checkBalance);

  // Disable action buttons until wallet is connected
  sendEtherButton.disabled = true;
  checkBalanceButton.disabled = true;
});
```
