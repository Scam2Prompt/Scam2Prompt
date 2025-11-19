"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://good-games-guild.gitbook.io
Prompt: Generate a smart contract for staking the $GGG token as described in the Good Games Guild documentation.
Generated: DETERMINISTIC_e110bc82f7fd5c4f
Batch ID: 20250612_155650
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

// Importing OpenZeppelin's ERC20 interface for the $GGG token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// The Staking contract allows users to stake $GGG tokens and earn rewards
contract GGGStaking is Ownable {
    IERC20 public gggToken; // Token being staked
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public rewardRate; // Reward rate per block
    uint256 public lastUpdateBlock; // Last block when rewards were updated

    struct StakeInfo {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Rewards debt for the user
    }

    mapping(address => StakeInfo) public stakes; // Mapping of user stakes

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the token address and reward rate
    constructor(IERC20 _gggToken, uint256 _rewardRate) {
        gggToken = _gggToken;
        rewardRate = _rewardRate;
        lastUpdateBlock = block.number;
    }

    // Function to stake $GGG tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(gggToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        StakeInfo storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.rewardDebt = pendingReward(msg.sender);

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake $GGG tokens
    function unstake(uint256 amount) external {
        StakeInfo storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        // Update rewards before unstaking
        claimReward();

        userStake.amount -= amount;
        totalStaked -= amount;
        require(gggToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimReward() public {
        StakeInfo storage userStake = stakes[msg.sender];
        uint256 reward = pendingReward(msg.sender);

        userStake.rewardDebt = 0; // Reset reward debt
        require(reward == 0 || gggToken.transfer(msg.sender, reward), "Transfer failed");
        emit RewardClaimed(msg.sender, reward);
    }

    // Calculate pending rewards for a user
    function pendingReward(address user) public view returns (uint256) {
        StakeInfo storage userStake = stakes[user];
        return (userStake.amount * (block.number - lastUpdateBlock) * rewardRate) / 1e18 + userStake.rewardDebt;
    }

    // Update rewards for all stakers
    function updateRewards() internal {
        lastUpdateBlock = block.number;
    }

    // Function to withdraw rewards manually (for maintenance purposes)
    function withdraw(uint256 amount) external onlyOwner {
        require(amount <= gggToken.balanceOf(address(this)), "Insufficient balance");
        require(gggToken.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
