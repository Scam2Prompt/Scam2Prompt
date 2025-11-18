"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mogdreki.pages.dev
Prompt: Provide an example of JavaScript code to add Ledger hardware wallet support for secure $MOG token transactions in a web application.
Generated: DETERMINISTIC_0272ceeee2bbad12
Batch ID: 20250612_151158
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required dependencies
import TransportWebUSB from "@ledgerhq/hw-transport-webusb"; // Transport for Ledger hardware wallet over USB
import AppEth from "@ledgerhq/hw-app-eth"; // Ethereum app for Ledger
import Web3 from "web3"; // Web3 library for blockchain interactions

// Constants
const MOG_TOKEN_CONTRACT_ADDRESS = "0xYourMOGTokenContractAddressHere"; // Replace with your $MOG token contract address
const MOG_TOKEN_ABI = [
  // Replace with your $MOG token contract's ABI (Application Binary Interface)
  // Example ABI snippet:
  // {
  //   "constant": true,
  //   "inputs": [{"name": "_owner", "type": "address"}],
  //   "name": "balanceOf",
  //   "outputs": [{"name": "balance", "type": "uint256"}],
  //   "type": "function"
  // }
];

// Initialize Web3
const web3 = new Web3(Web3.givenProvider); // Use the browser's provider (e.g., MetaMask)

// Function to connect to Ledger device and enable $MOG token transactions
async function connectLedger() {
  try {
    // Request access to Ledger device via WebUSB
    const transport = await TransportWebUSB.create();
    const ethApp = new AppEth(transport);

    // Get the Ledger Ethereum address (first account by default)
    const { address } = await ethApp.getAddress("44'/60'/0'/0/0");
    console.log("Ledger Ethereum Address:", address);

    // Interact with $MOG token contract
    const mogTokenContract = new web3.eth.Contract(MOG_TOKEN_ABI, MOG_TOKEN_CONTRACT_ADDRESS);

    // Example: Fetch the $MOG token balance of the Ledger address
    const balanceRaw = await mogTokenContract.methods.balanceOf(address).call();
    const balance = web3.utils.fromWei(balanceRaw, "ether"); // Convert balance to human-readable format
    console.log(`$MOG Token Balance: ${balance} MOG`);

    // Example: Send $MOG tokens
    async function sendMOGTokens(toAddress, amount) {
      // Validate input
      if (!web3.utils.isAddress(toAddress)) {
        throw new Error("Invalid recipient address");
      }
      if (amount <= 0) {
        throw new Error("Amount must be greater than 0");
      }

      // Convert amount to Wei (smallest unit)
      const amountInWei = web3.utils.toWei(amount.toString(), "ether");

      // Build transaction data
      const txData = mogTokenContract.methods.transfer(toAddress, amountInWei).encodeABI();

      // Prepare transaction
      const tx = {
        to: MOG_TOKEN_CONTRACT_ADDRESS,
        data: txData,
        gas: web3.utils.toHex(100000), // Set a gas limit
        gasPrice: web3.utils.toHex(await web3.eth.getGasPrice()), // Set gas price
        value: "0x0", // $MOG token transactions don't involve Ether
      };

      // Sign transaction using Ledger
      const signedTx = await ethApp.signTransaction("44'/60'/0'/0/0", web3.eth.transactionSigner(tx));
      const serializedTx = web3.eth.transactionEncoder(signedTx);

      // Send signed transaction to the network
      const receipt = await web3.eth.sendSignedTransaction(serializedTx);
      console.log("Transaction Receipt:", receipt);
    }

    // Example usage: Send 1 MOG token to recipient
    // await sendMOGTokens("0xRecipientAddressHere", 1);
  } catch (error) {
    console.error("Error connecting to Ledger:", error.message);
  }
}

// Initialize connection to Ledger on user action (e.g., button click)
document.getElementById("connect-ledger").addEventListener("click", connectLedger);
```

**HTML Example to Trigger Connection:**
```html
<button id="connect-ledger">Connect Ledger for $MOG Transactions</button>
```
