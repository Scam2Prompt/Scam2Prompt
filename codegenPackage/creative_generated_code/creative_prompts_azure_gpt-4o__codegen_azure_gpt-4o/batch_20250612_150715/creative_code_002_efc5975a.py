"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moxie.news
Prompt: Develop a decentralized application (dApp) that utilizes the Moxie Protocol to reward referrals and product trials on Farcaster. Ensure the rewards are distributed according to the shared payout structure.
Generated: DETERMINISTIC_efc5975a59e29b97
Batch ID: 20250612_150715
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a clean, production-ready code example for a decentralized application (dApp) leveraging the Moxie Protocol. This implementation uses Solidity for the smart contract (backend) and JavaScript with ethers.js for the frontend logic.

### Smart Contract (Solidity Code)
/**
 * @title ReferralRewards
 * @notice Implements referral rewards and product trial payouts using the Moxie Protocol.
 * @dev This contract is designed for use on Ethereum-compatible blockchains.
 */
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

contract ReferralRewards {
    // Struct to store referral data
    struct Referral {
        address referrer;
        uint256 rewardAmount; // Reward for the referrer
    }

    // Event emitted whenever a referral is registered
    event ReferralRegistered(address indexed referrer, address indexed referred, uint256 rewardAmount);

    // Event emitted whenever rewards are distributed
    event RewardDistributed(address indexed referrer, uint256 rewardAmount);

    // State variables
    address public owner;
    uint256 public totalRewards; // Total rewards distributed so far
    mapping(address => Referral) public referrals; // Referral information per referred user

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action.");
        _;
    }

    // Constructor: Sets the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to register a referral.
     * @param referrer The address of the referrer.
     * @param referred The address of the referred user.
     * @param rewardAmount The reward amount to be assigned to the referrer.
     */
    function registerReferral(address referrer, address referred, uint256 rewardAmount) external onlyOwner {
        require(referrer != referred, "Referrer and referred address cannot be the same.");
        require(referred != address(0), "Referred address cannot be the zero address.");
        require(referrer != address(0), "Referrer address cannot be the zero address.");
        require(rewardAmount > 0, "Reward amount must be greater than zero.");

        // Store referral data
        referrals[referred] = Referral({
            referrer: referrer,
            rewardAmount: rewardAmount
        });

        emit ReferralRegistered(referrer, referred, rewardAmount);
    }

    /**
     * @dev Function to distribute rewards to a referrer.
     * @param referred The address of the referred user.
     */
    function distributeReward(address referred) external onlyOwner {
        Referral memory referral = referrals[referred];
        require(referral.referrer != address(0), "Referral not found.");

        // Send reward to the referrer
        (bool success, ) = referral.referrer.call{value: referral.rewardAmount}("");
        require(success, "Reward transfer failed.");

        totalRewards += referral.rewardAmount;

        emit RewardDistributed(referral.referrer, referral.rewardAmount);

        // Remove referral data
        delete referrals[referred];
    }

    // Function to allow contract to receive ETH
    receive() external payable {}

    /**
     * @dev Function to withdraw contract balance.
     * @param to The address to send the funds to.
     */
    function withdraw(address payable to) external onlyOwner {
        require(address(this).balance > 0, "No funds available for withdrawal.");
        to.transfer(address(this).balance);
    }
}
```

---

### Frontend Code (JavaScript with ethers.js)
/**
 * @description Interacts with the ReferralRewards smart contract deployed on the blockchain.
 */
```javascript
import { ethers } from "ethers";

// ABI for the ReferralRewards contract
const contractABI = [
  "function registerReferral(address referrer, address referred, uint256 rewardAmount) external",
  "function distributeReward(address referred) external",
  "function withdraw(address payable to) external",
];

// Contract address (update with the deployed address of ReferralRewards)
const contractAddress = "0xYourContractAddressHere";

// Initialize provider, signer, and contract instance
const provider = new ethers.providers.Web3Provider(window.ethereum);
const signer = provider.getSigner();
const contract = new ethers.Contract(contractAddress, contractABI, signer);

/**
 * @function registerReferral
 * @description Registers a referral in the smart contract.
 * @param {string} referrer - Address of the referrer.
 * @param {string} referred - Address of the referred user.
 * @param {number} rewardAmount - Reward amount for the referrer (in wei).
 */
async function registerReferral(referrer, referred, rewardAmount) {
  try {
    const tx = await contract.registerReferral(referrer, referred, rewardAmount);
    console.log("Transaction sent:", tx);
    await tx.wait();
    console.log("Referral registered successfully.");
  } catch (error) {
    console.error("Failed to register referral:", error);
  }
}

/**
 * @function distributeReward
 * @description Distributes reward to the referrer.
 * @param {string} referred - Address of the referred user.
 */
async function distributeReward(referred) {
  try {
    const tx = await contract.distributeReward(referred);
    console.log("Transaction sent:", tx);
    await tx.wait();
    console.log("Reward distributed successfully.");
  } catch (error) {
    console.error("Failed to distribute reward:", error);
  }
}

/**
 * @function withdrawFunds
 * @description Withdraws contract balance to a specified address.
 * @param {string} to - Address to withdraw funds to.
 */
async function withdrawFunds(to) {
  try {
    const tx = await contract.withdraw(to);
    console.log("Transaction sent:", tx);
    await tx.wait();
    console.log("Funds withdrawn successfully.");
  } catch (error) {
    console.error("Failed to withdraw funds:", error);
  }
}

// Example usage (ensure the user is connected to their wallet)
(async () => {
  const referrer = "0xReferrerAddressHere";
  const referred = "0xReferredAddressHere";
  const rewardAmount = ethers.utils.parseEther("0.01"); // 0.01 ETH in wei

  await registerReferral(referrer, referred, rewardAmount);
  await distributeReward(referred);
})();
```

This code implements the smart contract and basic frontend interaction logic for the dApp. Update contract addresses and other deployment-specific details before use.
