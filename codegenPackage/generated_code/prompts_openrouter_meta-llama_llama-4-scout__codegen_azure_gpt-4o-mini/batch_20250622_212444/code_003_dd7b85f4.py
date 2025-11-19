"""
Generated Code Metadata:
========================
Original URL: https://mintpad-x-monad-early.testnet.mintopia.top
Prompt: Generate a smart contract code for a referral program on Monad Testnet, where users earn 0.00000000666 tMON for every mint made through their referral link.
Generated: DETERMINISTIC_dd7b85f46d3938ac
Batch ID: 20250622_212444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title ReferralProgram
 * @dev A smart contract for a referral program where users earn tMON for referrals.
 */
contract ReferralProgram is Ownable {
    // Token interface for tMON
    IERC20 public token;

    // Mapping to track referrals
    mapping(address => address) public referrals;
    mapping(address => uint256) public referralRewards;

    // Reward amount for each mint through a referral
    uint256 public constant REWARD_AMOUNT = 6660000000; // 0.00000000666 tMON

    // Event emitted when a new referral is registered
    event ReferralRegistered(address indexed referrer, address indexed referee);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to set the token address.
     * @param _tokenAddress The address of the tMON token contract.
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        token = IERC20(_tokenAddress);
    }

    /**
     * @dev Function to register a referral.
     * @param referrer The address of the referrer.
     */
    function registerReferral(address referrer) external {
        require(referrer != msg.sender, "You cannot refer yourself");
        require(referrals[msg.sender] == address(0), "Referral already registered");

        // Register the referral
        referrals[msg.sender] = referrer;

        // Emit the referral registration event
        emit ReferralRegistered(referrer, msg.sender);
    }

    /**
     * @dev Function to mint tokens (simulated for this example).
     * @param amount The amount of tokens to mint.
     */
    function mintTokens(uint256 amount) external {
        // Simulate minting process
        // In a real scenario, this would involve actual token minting logic

        // Check if the user has a referrer
        address referrer = referrals[msg.sender];
        if (referrer != address(0)) {
            // Increment the referrer's reward
            referralRewards[referrer] += REWARD_AMOUNT;
        }
    }

    /**
     * @dev Function for users to claim their referral rewards.
     */
    function claimRewards() external {
        uint256 amount = referralRewards[msg.sender];
        require(amount > 0, "No rewards to claim");

        // Reset the user's rewards to prevent re-entrancy
        referralRewards[msg.sender] = 0;

        // Transfer the rewards to the user
        require(token.transfer(msg.sender, amount), "Token transfer failed");

        // Emit the rewards claimed event
        emit RewardsClaimed(msg.sender, amount);
    }

    /**
     * @dev Function to withdraw tokens from the contract (only owner).
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer tokens to the owner
        require(token.transfer(msg.sender, amount), "Token transfer failed");
    }
}
```
