"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dapp-rx.pages.dev
Prompt: Provide an example of how to implement staking and harvesting of assets in a DApp using the MultiChain Protocol.
Generated: DETERMINISTIC_ff949d649fde1ed1
Batch ID: 20250612_163627
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

// Import necessary OpenZeppelin contracts
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract interface
interface IStaking {
    function stake(uint256 amount) external;
    function harvest() external;
}

// Main Staking and Harvesting DApp contract
contract StakingDApp is Ownable {
    IERC20 public rewardToken; // The token to be rewarded
    IERC20 public stakeToken;  // The token that users will stake

    // Structure to store user data
    struct UserInfo {
        uint256 amount; // Amount of tokens staked by user
        uint256 rewardDebt; // Reward debt for the user
    }

    // Mapping of user addresses to their information
    mapping(address => UserInfo) public userInfo;

    // Total staked amount
    uint256 public totalStaked;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when rewards are harvested
    event Harvested(address indexed user, uint256 amount);

    // Constructor to initialize the contract with token addresses
    constructor(IERC20 _rewardToken, IERC20 _stakeToken) {
        rewardToken = _rewardToken;
        stakeToken = _stakeToken;
    }

    // Stake tokens into the contract
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");

        // Update user info
        UserInfo storage user = userInfo[msg.sender];
        user.amount += amount;
        totalStaked += amount;

        // Transfer stake tokens from user to contract
        bool success = stakeToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        emit Staked(msg.sender, amount);
    }

    // Harvest rewards for the user
    function harvest() external {
        UserInfo storage user = userInfo[msg.sender];

        // Calculate pending rewards (dummy calculation as example)
        uint256 pendingReward = user.amount * 1e18 / totalStaked; // Example reward calculation
        require(pendingReward > 0, "No rewards available");

        // Update user's reward debt
        user.rewardDebt += pendingReward;

        // Transfer rewards to user
        bool success = rewardToken.transfer(msg.sender, pendingReward);
        require(success, "Reward transfer failed");

        emit Harvested(msg.sender, pendingReward);
    }

    // Function to withdraw staked tokens (optional)
    function withdraw(uint256 amount) external {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= amount, "Insufficient staked amount");

        // Update user info
        user.amount -= amount;
        totalStaked -= amount;

        // Transfer stake tokens back to user
        bool success = stakeToken.transfer(msg.sender, amount);
        require(success, "Token transfer failed");
    }

    // Function to get user staked amount
    function getUserInfo(address user) external view returns (uint256 stakedAmount, uint256 rewardDebt) {
        UserInfo storage userInfo = userInfo[user];
        return (userInfo.amount, userInfo.rewardDebt);
    }
}
```
