"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anylimitedcentralize.pages.dev
Prompt: Create a smart contract for a referral rewards system that awards 5000 $RIFT tokens per referral, as outlined on the Rift Swap platform.
Generated: DETERMINISTIC_e5fccbcaf1b90891
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import the ERC20 interface for token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for the Referral Rewards System
contract ReferralRewards is Ownable {
    // Token to be used for rewards
    IERC20 public riftToken;

    // Amount of tokens rewarded per referral
    uint256 public constant REWARD_AMOUNT = 5000 * 10**18; // Assuming 18 decimals

    // Mapping to track referrals
    mapping(address => address) public referrals;
    mapping(address => uint256) public referralCount;

    // Events for logging
    event ReferralAdded(address indexed referrer, address indexed referee);
    event RewardClaimed(address indexed referrer, uint256 amount);

    // Constructor to initialize the token address
    constructor(address _riftToken) {
        require(_riftToken != address(0), "Invalid token address");
        riftToken = IERC20(_riftToken);
    }

    // Function to refer a new user
    function refer(address _referee) external {
        require(_referee != address(0), "Invalid referee address");
        require(referrals[_referee] == address(0), "Referee already referred");

        // Store the referral relationship
        referrals[_referee] = msg.sender;
        referralCount[msg.sender] += 1;

        emit ReferralAdded(msg.sender, _referee);
    }

    // Function to claim rewards for referrals
    function claimRewards() external {
        uint256 rewardAmount = referralCount[msg.sender] * REWARD_AMOUNT;

        require(rewardAmount > 0, "No rewards available to claim");
        require(riftToken.balanceOf(address(this)) >= rewardAmount, "Insufficient contract balance");

        // Reset the referral count for the caller after claiming
        referralCount[msg.sender] = 0;

        // Transfer the reward tokens to the referrer
        bool success = riftToken.transfer(msg.sender, rewardAmount);
        require(success, "Token transfer failed");

        emit RewardClaimed(msg.sender, rewardAmount);
    }

    // Function to withdraw tokens from the contract in case of an emergency or to collect fees
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(riftToken.balanceOf(address(this)) >= amount, "Insufficient balance in contract");

        bool success = riftToken.transfer(msg.sender, amount);
        require(success, "Token withdrawal failed");
    }

    // Function to view referral count for a specific address
    function getReferralCount(address user) external view returns (uint256) {
        return referralCount[user];
    }

    // Function to get the referrer of a specific address
    function getReferrer(address user) external view returns (address) {
        return referrals[user];
    }
}
```
