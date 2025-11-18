"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eternallaunch.pages.dev
Prompt: Generate a Solidity contract for staking $BVM tokens to join the allowlist for Eternal AI's public sale with boost eligibility.
Generated: DETERMINISTIC_7c2c1dc202520b36
Batch ID: 20250612_153400
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

// Interface for ERC20 token standard
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

// Main contract for staking $BVM tokens to join the allowlist
contract EternalAIAllowlist {
    // Token to be staked for joining the allowlist
    IERC20 public bvmToken;

    // Staker's information containing the amount staked and boost eligibility status
    struct StakerInfo {
        uint256 amountStaked;
        bool isBoostEligible;
    }

    // Mapping from user address to their staker information
    mapping(address => StakerInfo) public stakers;

    // Event emitted when a user stakes tokens
    event TokensStaked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event TokensUnstaked(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the $BVM token address
    constructor(address _bvmTokenAddress) {
        require(_bvmTokenAddress != address(0), "Invalid token address");
        bvmToken = IERC20(_bvmTokenAddress);
    }

    // Stake function for users to stake $BVM tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer tokens from user to the contract
        bool success = bvmToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update the staker's information
        stakers[msg.sender].amountStaked += amount;
        stakers[msg.sender].isBoostEligible = true; // Example eligibility condition

        emit TokensStaked(msg.sender, amount);
    }

    // Unstake function for users to withdraw their staked tokens
    function unstake(uint256 amount) external {
        StakerInfo storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");

        // Update the staker's information
        staker.amountStaked -= amount;

        // Transfer tokens back to the user
        bool success = bvmToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");

        // Check if user is eligible for boost and update status
        if (staker.amountStaked == 0) {
            staker.isBoostEligible = false;
        }

        emit TokensUnstaked(msg.sender, amount);
    }

    // Function to check a user's staking details
    function getStakerInfo(address user) external view returns (uint256 amountStaked, bool isBoostEligible) {
        StakerInfo memory staker = stakers[user];
        return (staker.amountStaked, staker.isBoostEligible);
    }
}
```
