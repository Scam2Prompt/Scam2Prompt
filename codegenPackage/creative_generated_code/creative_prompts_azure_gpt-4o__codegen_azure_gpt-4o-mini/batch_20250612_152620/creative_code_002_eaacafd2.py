"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://betswirl.xyz
Prompt: Generate code to implement a token economy for a decentralized gaming platform, including features like staking, governance, and rewards, using the BetSwirl model.
Generated: DETERMINISTIC_eaacafd2c8a5497c
Batch ID: 20250612_152620
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract BetSwirlToken is ERC20, ERC20Burnable, Ownable {
    using SafeMath for uint256;
    
    uint256 public stakingRewardRate; // Percentage of rewards for staking
    uint256 public totalStaked; // Total tokens staked in the contract

    mapping(address => uint256) public stakedBalances; // User staked balances
    mapping(address => uint256) public lastStakeTime; // Last time user staked
    mapping(address => uint256) public rewards; // Rewards for users

    event Staked(address indexed user, uint256 amount, uint256 totalStaked);
    event Unstaked(address indexed user, uint256 amount, uint256 totalStaked);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to initialize token and parameters
    constructor(string memory name, string memory symbol, uint256 initialSupply, uint256 _stakingRewardRate) ERC20(name, symbol) {
        _mint(msg.sender, initialSupply * (10 ** decimals()));
        stakingRewardRate = _stakingRewardRate;
    }

    // Stake tokens in the contract
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to stake");

        // Update rewards before staking
        _updateRewards(msg.sender);

        // Transfer tokens to contract
        _transfer(msg.sender, address(this), amount);
        stakedBalances[msg.sender] = stakedBalances[msg.sender].add(amount);
        totalStaked = totalStaked.add(amount);
        lastStakeTime[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount, totalStaked);
    }

    // Unstake tokens from the contract
    function unstake(uint256 amount) external {
        require(amount > 0 && amount <= stakedBalances[msg.sender], "Invalid unstake amount");

        // Update rewards before unstaking
        _updateRewards(msg.sender);

        // Transfer tokens back to user
        _transfer(address(this), msg.sender, amount);
        stakedBalances[msg.sender] = stakedBalances[msg.sender].sub(amount);
        totalStaked = totalStaked.sub(amount);

        emit Unstaked(msg.sender, amount, totalStaked);
    }

    // Claim rewards for user
    function claimRewards() external {
        _updateRewards(msg.sender);
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        // Reset user rewards
        rewards[msg.sender] = 0;
        _mint(msg.sender, reward);

        emit RewardPaid(msg.sender, reward);
    }

    // Internal function to update user rewards based on staking duration
    function _updateRewards(address user) internal {
        if (stakedBalances[user] > 0) {
            uint256 stakingDuration = block.timestamp.sub(lastStakeTime[user]);
            uint256 reward = stakedBalances[user]
                .mul(stakingRewardRate)
                .mul(stakingDuration)
                .div(365 days)
                .div(100); // Convert to percentage

            rewards[user] = rewards[user].add(reward);
        }
        lastStakeTime[user] = block.timestamp; // Update the last stake time
    }

    // Set a new staking reward rate (only owner can call)
    function setStakingRewardRate(uint256 newRate) external onlyOwner {
        stakingRewardRate = newRate;
    }

    // View function to check user's total rewards
    function viewRewards(address user) external view returns (uint256) {
        return rewards[user];
    }
}
```
