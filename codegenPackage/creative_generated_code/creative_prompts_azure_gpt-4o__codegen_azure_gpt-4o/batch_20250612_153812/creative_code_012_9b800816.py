"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://consensysmedia.net
Prompt: Develop a blockchain-based ticketing system using the MetaMask Institutional API, inspired by Consensys' partnership with Sports Illustrated Tickets.
Generated: DETERMINISTIC_9b8008167416559c
Batch ID: 20250612_153812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const Web3 = require("web3");
require("dotenv").config(); // Load environment variables from .env file
const { MetaMaskSDK } = require("@metamask-institutional/sdk"); // MetaMask Institutional SDK

// Connect to Ethereum network
const web3 = new Web3(process.env.INFURA_URL); // Use Infura for Ethereum RPC connection

// MetaMask Institutional Configuration
const metamaskSDK = new MetaMaskSDK({
  apiKey: process.env.MMI_API_KEY, // API key for MetaMask Institutional
  clientId: process.env.MMI_CLIENT_ID, // Client ID for MetaMask Institutional
});

// Smart contract ABI (replace with your deployed contract ABI)
const ticketContractABI = [
  {
    constant: false,
    inputs: [{ name: "ticketId", type: "uint256" }],
    name: "purchaseTicket",
    outputs: [{ name: "success", type: "bool" }],
    type: "function",
  },
  {
    constant: true,
    inputs: [{ name: "ticketId", type: "uint256" }],
    name: "getTicketDetails",
    outputs: [
      { name: "owner", type: "address" },
      { name: "price", type: "uint256" },
      { name: "eventName", type: "string" },
    ],
    type: "function",
  },
];

// Smart contract address (replace with your deployed contract address)
const ticketContractAddress = process.env.TICKET_CONTRACT_ADDRESS;

// Instantiate smart contract
const ticketContract = new web3.eth.Contract(ticketContractABI, ticketContractAddress);

// Function to purchase a ticket
async function purchaseTicket(ticketId) {
  try {
    // Get user's wallet address from MetaMask Institutional
    const accounts = await metamaskSDK.getAccounts();
    const userAccount = accounts[0];

    // Fetch ticket price
    const ticketDetails = await ticketContract.methods.getTicketDetails(ticketId).call();
    const ticketPrice = ticketDetails.price;

    // Send purchase transaction
    const receipt = await ticketContract.methods
      .purchaseTicket(ticketId)
      .send({ from: userAccount, value: ticketPrice });

    console.log("Ticket purchased successfully:", receipt);
  } catch (error) {
    console.error("Error purchasing ticket:", error.message);
  }
}

// Function to get ticket details
async function getTicketDetails(ticketId) {
  try {
    // Fetch ticket details from the blockchain
    const details = await ticketContract.methods.getTicketDetails(ticketId).call();
    console.log(`Ticket Details:
      Owner: ${details.owner}
      Price: ${web3.utils.fromWei(details.price, "ether")} ETH
      Event Name: ${details.eventName}`);
  } catch (error) {
    console.error("Error fetching ticket details:", error.message);
  }
}

// Example usage (ensure environment variables and contract details are properly set)
(async () => {
  const ticketId = 1; // Example ticket ID

  console.log("Fetching ticket details...");
  await getTicketDetails(ticketId);

  console.log("Purchasing ticket...");
  await purchaseTicket(ticketId);

  console.log("Fetching ticket details after purchase...");
  await getTicketDetails(ticketId);
})();

// Notes:
// 1. Replace the contract ABI and address with your deployed contract details.
// 2. Set up INFURA_URL, MMI_API_KEY, MMI_CLIENT_ID, and TICKET_CONTRACT_ADDRESS in your .env file.
// 3. Ensure MetaMask Institutional access is properly configured for your organization.
```
