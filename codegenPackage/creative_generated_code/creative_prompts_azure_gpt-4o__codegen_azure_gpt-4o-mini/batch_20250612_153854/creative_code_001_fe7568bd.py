"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://yel.financial
Prompt: Generate code to implement a referral points system for the Yei money market protocol on Sei, ensuring compatibility with wallet connections.
Generated: DETERMINISTIC_fe7568bdd5878ab8
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
import { WalletConnectProvider } from "@walletconnect/web3-provider";
import Web3 from "web3";

// Constants for the referral system
const REFERRAL_BONUS = 10; // Points awarded for each successful referral
const POINTS_THRESHOLD = 50; // Minimum points to redeem rewards

// Initialize Web3 instance
const provider = new WalletConnectProvider({
  infuraId: "YOUR_INFURA_ID", // Replace with your Infura project ID
});
const web3 = new Web3(provider);

// Class for managing the referral points system
class ReferralPointsSystem {
  constructor() {
    this.referrals = new Map(); // Map to store user referrals and points
  }

  // Method to add a referral
  addReferral(referrerAddress, referredAddress) {
    // Check if the referrer exists
    if (!this.referrals.has(referrerAddress)) {
      this.referrals.set(referrerAddress, { points: 0, referredUsers: [] });
    }

    // Add the referred address and award points
    this.referrals.get(referrerAddress).points += REFERRAL_BONUS;
    this.referrals.get(referrerAddress).referredUsers.push(referredAddress);
  }

  // Method to check points for a user
  checkPoints(address) {
    if (this.referrals.has(address)) {
      return this.referrals.get(address).points;
    } else {
      return 0; // User has no referrals
    }
  }

  // Method to redeem points
  redeemPoints(address) {
    if (!this.referrals.has(address)) {
      throw new Error("User not found in the referral system.");
    }

    const user = this.referrals.get(address);
    if (user.points < POINTS_THRESHOLD) {
      throw new Error("Insufficient points to redeem rewards.");
    }

    // Reset points after redemption
    user.points = 0;
    return "Points redeemed successfully!";
  }
}

// Initialize the referral points system
const referralSystem = new ReferralPointsSystem();

/**
 * Connect to wallet and interact with the referral system
 */
async function connectWallet() {
  try {
    // Enable session (triggers QR Code modal)
    await provider.enable();

    // Get accounts
    const accounts = await web3.eth.getAccounts();
    console.log("Connected account:", accounts[0]);

    // Example usage of the referral system
    referralSystem.addReferral(accounts[0], "0xReferredUserAddress"); // Example referrer and referred address
    console.log("Points:", referralSystem.checkPoints(accounts[0])); // Check points for the referrer
    console.log(referralSystem.redeemPoints(accounts[0])); // Redeem points if threshold is met

  } catch (error) {
    console.error("Error connecting to wallet:", error);
  }
}

// Execute wallet connection
connectWallet();
```
