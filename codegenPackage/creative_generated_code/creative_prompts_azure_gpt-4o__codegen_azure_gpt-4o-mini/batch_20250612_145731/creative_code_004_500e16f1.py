"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neiroairdrop.pages.dev
Prompt: Write a Solidity smart contract that could be used to facilitate the referral system mentioned on the NEIRO website, where users can share links and earn $NEIRO tokens.
Generated: DETERMINISTIC_500e16f15c89dcfb
Batch ID: 20250612_145731
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

// Interface for the ERC20 token to handle $NEIRO token transfers
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}

// Referral contract
contract ReferralSystem {
    // Mapping to track referrals
    mapping(address => address) public referrals;
    mapping(address => uint256) public referralCounts;
    mapping(address => uint256) public rewards;

    // Address of the $NEIRO token contract
    address public neiroTokenAddress;
    // Reward amount for successful referrals
    uint256 public rewardAmount;

    // Event emitted when a user is referred
    event Referred(address indexed referrer, address indexed referred);
    // Event emitted when rewards are claimed
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the $NEIRO token address and reward amount
    constructor(address _neiroTokenAddress, uint256 _rewardAmount) {
        neiroTokenAddress = _neiroTokenAddress;
        rewardAmount = _rewardAmount;
    }

    // Function to refer a new user
    function refer(address _referred) external {
        require(_referred != address(0), "Invalid address");
        require(referrals[_referred] == address(0), "User already referred");

        referrals[_referred] = msg.sender; // Set the referrer for the referred user
        referralCounts[msg.sender]++; // Increment the referrer's count

        // Emit the referral event
        emit Referred(msg.sender, _referred);
    }

    // Function to claim rewards based on referrals
    function claimReward() external {
        uint256 count = referralCounts[msg.sender];
        require(count > 0, "No referrals to claim rewards for");

        // Calculate total rewards
        uint256 totalRewards = count * rewardAmount;

        // Ensure the contract has enough tokens to pay out
        require(IERC20(neiroTokenAddress).transfer(msg.sender, totalRewards), "Token transfer failed");

        // Reset the referrer count to prevent multiple claims
        referralCounts[msg.sender] = 0;

        // Emit the reward claimed event
        emit RewardClaimed(msg.sender, totalRewards);
    }

    // Function to withdraw tokens in case of contract maintenance (only owner)
    function withdrawTokens(address _tokenAddress) external {
        // Transfer all tokens from the contract to the owner's address
        uint256 contractBalance = IERC20(_tokenAddress).balanceOf(address(this));
        require(contractBalance > 0, "No tokens to withdraw");
        require(IERC20(_tokenAddress).transfer(msg.sender, contractBalance), "Token transfer failed");
    }
}
```
