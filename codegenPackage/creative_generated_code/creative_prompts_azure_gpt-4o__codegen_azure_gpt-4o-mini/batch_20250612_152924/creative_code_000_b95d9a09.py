"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mememoguls-en.pages.dev
Prompt: Write a smart contract in Solidity for staking $MGLS tokens, ensuring users can earn rewards based on their share of the staking pool and annual returns percentage, as described in the Meme Moguls ecosystem.
Generated: DETERMINISTIC_b95d9a09b5f98958
Batch ID: 20250612_152924
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract StakingContract is Ownable {
    // Token to be staked
    IERC20 public immutable stakingToken;

    // Annual return percentage (in basis points, 1% = 100 basis points)
    uint256 public annualReturnPercentage;

    // Structure to hold user's staking information
    struct UserInfo {
        uint256 amount;     // Amount of tokens staked by the user
        uint256 rewardDebt; // Reward debt to calculate pending rewards
    }

    // Mapping of user address to their staking information
    mapping(address => UserInfo) public userInfo;

    // Total amount of tokens staked in the contract
    uint256 public totalStaked;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    constructor(IERC20 _stakingToken, uint256 _annualReturnPercentage) {
        require(address(_stakingToken) != address(0), "Invalid token address");
        require(_annualReturnPercentage > 0, "Return percentage must be greater than 0");

        stakingToken = _stakingToken;
        annualReturnPercentage = _annualReturnPercentage;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake 0");

        // Update user's info
        UserInfo storage user = userInfo[msg.sender];
        user.amount += _amount; // Increase user's staked amount

        // Update total staked amount
        totalStaked += _amount;

        // Transfer tokens from user to contract
        bool success = stakingToken.transferFrom(msg.sender, address(this), _amount);
        require(success, "Token transfer failed");

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external {
        UserInfo storage user = userInfo[msg.sender];
        require(user.amount >= _amount, "Insufficient staked amount");

        // Update user's info
        user.amount -= _amount;
        totalStaked -= _amount;

        // Transfer tokens back to user
        bool success = stakingToken.transfer(msg.sender, _amount);
        require(success, "Token transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    // Function to calculate rewards for a user
    function calculateRewards(address _user) public view returns (uint256) {
        UserInfo storage user = userInfo[_user];
        if (totalStaked == 0 || user.amount == 0) return 0;

        // Calculate user's share of the staking pool
        uint256 userShare = (user.amount * 1e18) / totalStaked;

        // Calculate annual rewards based on user's share and annual return percentage
        uint256 annualRewards = (totalStaked * annualReturnPercentage * userShare) / (10000 * 1e18);
        return annualRewards - user.rewardDebt;
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available");

        // Update user's reward debt
        userInfo[msg.sender].rewardDebt += rewards;

        // Transfer rewards to user (assuming a rewards token is implemented)
        bool success = stakingToken.transfer(msg.sender, rewards);
        require(success, "Reward transfer failed");

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to update the annual return percentage (only owner)
    function updateAnnualReturnPercentage(uint256 _newPercentage) external onlyOwner {
        require(_newPercentage > 0, "Return percentage must be greater than 0");
        annualReturnPercentage = _newPercentage;
    }
}
```
