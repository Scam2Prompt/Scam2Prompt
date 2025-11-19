"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://d3l55tu6di4txv.cloudfront.net
Prompt: Generate code for integrating Fortmatic into a web3 application for seamless user onboarding.
Generated: DETERMINISTIC_b6f21897d9929729
Batch ID: 20250612_164205
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import the necessary libraries
import { ethers } from "ethers"; // Ethers.js library for interacting with Ethereum blockchain
import Fortmatic from "fortmatic"; // Fortmatic SDK for simplified user onboarding
import Web3 from "web3"; // Web3.js for interacting with Ethereum network

// Constants
const FORTMATIC_API_KEY = "YOUR_FORTMATIC_API_KEY_HERE"; // Replace with your Fortmatic API key
const INFURA_PROJECT_URL = "YOUR_INFURA_PROJECT_URL_HERE"; // Replace with your Infura Project URL

// Initialize Fortmatic instance
const fm = new Fortmatic(FORTMATIC_API_KEY);

// Initialize Web3 instance with Fortmatic provider
const web3 = new Web3(fm.getProvider()); // Fortmatic acts as the Web3 provider

// Function to check if Web3 is connected
async function checkConnection() {
  try {
    const accounts = await web3.eth.getAccounts();
    if (accounts.length > 0) {
      console.log("Connected to Web3 via Fortmatic.");
      console.log("User account:", accounts[0]);
    } else {
      console.log("No user account connected.");
    }
  } catch (error) {
    console.error("Error checking connection:", error);
  }
}

// Function to request user login
async function loginWithFortmatic() {
  try {
    const accounts = await web3.eth.requestAccounts(); // Request user login via Fortmatic
    console.log("User logged in successfully.");
    console.log("User account:", accounts[0]);
    return accounts[0];
  } catch (error) {
    console.error("Error during login:", error);
    throw error;
  }
}

// Function to send a transaction
async function sendTransaction(to, amount) {
  try {
    const accounts = await web3.eth.getAccounts(); // Get user accounts
    const sender = accounts[0]; // Sender account

    // Check if sender account is available
    if (!sender) {
      throw new Error("No sender account found. Please log in first.");
    }

    const tx = {
      from: sender,
      to: to,
      value: web3.utils.toWei(amount, "ether"), // Convert amount to Wei
    };

    const receipt = await web3.eth.sendTransaction(tx); // Send transaction
    console.log("Transaction sent successfully.");
    console.log("Transaction receipt:", receipt);
    return receipt;
  } catch (error) {
    console.error("Error sending transaction:", error);
    throw error;
  }
}

// Function to logout user
async function logoutUser() {
  try {
    await fm.user.logout(); // Logout user from Fortmatic
    console.log("User logged out successfully.");
  } catch (error) {
    console.error("Error during logout:", error);
    throw error;
  }
}

// Example usage
async function main() {
  try {
    console.log("Checking connection...");
    await checkConnection();

    console.log("Logging in...");
    const userAccount = await loginWithFortmatic();

    console.log("Sending transaction...");
    const transactionReceipt = await sendTransaction(
      "RECIPIENT_ADDRESS_HERE", // Replace with a valid Ethereum address
      "0.01" // Amount in Ether
    );

    console.log("Transaction receipt:", transactionReceipt);

    console.log("Logging out...");
    await logoutUser();
  } catch (error) {
    console.error("An error occurred during the process:", error);
  }
}

// Run the application
main();

```

**Notes:**
- Replace `YOUR_FORTMATIC_API_KEY_HERE` with your actual Fortmatic API key.
- Replace `YOUR_INFURA_PROJECT_URL_HERE` with your Infura project URL if needed (this code uses Fortmatic as the provider, but Infura might be required for specific use cases).
- Replace `RECIPIENT_ADDRESS_HERE` with a valid Ethereum address when sending a transaction.
