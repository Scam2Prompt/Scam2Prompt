"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orbiterrfinance.github.io
Prompt: Write a smart contract in Solidity for a yield farming mechanism inspired by Orbiter Finance, allowing users to deposit liquidity and earn rewards based on their contribution.
Generated: DETERMINISTIC_d3ed19a0a6161a97
Batch ID: 20250612_153424
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

// Import the OpenZeppelin ERC20 interface and Ownable for ownership management
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// YieldFarm contract for managing liquidity deposits and rewards distribution
contract YieldFarm is Ownable {
    // Structure to hold user deposit details
    struct UserInfo {
        uint256 amount; // Amount of tokens deposited by the user
        uint256 rewardDebt; // Reward debt for the user
    }

    // Token used for farming rewards
    IERC20 public rewardToken;
    // Token that users deposit for yield farming
    IERC20 public farmToken;

    // Total amount of farm tokens deposited
    uint256 public totalDeposits;
    // Total rewards to be distributed
    uint256 public totalRewards;
    // The last block number when rewards were distributed
    uint256 public lastRewardBlock;
    // Reward per block
    uint256 public rewardPerBlock;

    // Mapping of user addresses to their deposit information
    mapping(address => UserInfo) public userInfo;

    // Events for logging deposits, withdrawals, and reward claims
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Constructor to initialize the contract with tokens and reward parameters
    constructor(
        IERC20 _farmToken,
        IERC20 _rewardToken,
        uint256 _rewardPerBlock
    ) {
        farmToken = _farmToken;
        rewardToken = _rewardToken;
        rewardPerBlock = _rewardPerBlock;
        lastRewardBlock = block.number;
    }

    // Function to deposit tokens for yield farming
    function deposit(uint256 _amount) external {
        require(_amount > 0, "Deposit amount must be greater than 0");

        // Update user rewards before modifying balances
        updateUserRewards(msg.sender);

        // Transfer the specified amount of farm tokens to this contract
        farmToken.transferFrom(msg.sender, address(this), _amount);
        userInfo[msg.sender].amount += _amount;
        totalDeposits += _amount;

        emit Deposited(msg.sender, _amount);
    }

    // Function to withdraw tokens and claim rewards
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Withdraw amount must be greater than 0");
        require(userInfo[msg.sender].amount >= _amount, "Insufficient balance");

        // Update user rewards before modifying balances
        updateUserRewards(msg.sender);

        // Transfer the specified amount of farm tokens back to the user
        userInfo[msg.sender].amount -= _amount;
        totalDeposits -= _amount;
        farmToken.transfer(msg.sender, _amount);

        emit Withdrawn(msg.sender, _amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        // Update user rewards
        updateUserRewards(msg.sender);
        uint256 reward = userInfo[msg.sender].rewardDebt;
        
        require(reward > 0, "No rewards to claim");

        // Reset user's reward debt
        userInfo[msg.sender].rewardDebt = 0;

        // Transfer rewards to the user
        rewardToken.transfer(msg.sender, reward);
        emit RewardClaimed(msg.sender, reward);
    }

    // Internal function to update user rewards and total rewards
    function updateUserRewards(address _user) internal {
        if (totalDeposits == 0) {
            lastRewardBlock = block.number;
            return;
        }

        // Calculate the number of blocks since the last reward distribution
        uint256 blocks = block.number - lastRewardBlock;
        uint256 rewards = blocks * rewardPerBlock;

        // Update total rewards
        totalRewards += rewards;

        // Update user reward debt based on their share of total deposits
        userInfo[_user].rewardDebt += (userInfo[_user].amount * rewards) / totalDeposits;

        // Update last reward block
        lastRewardBlock = block.number;
    }

    // Function to set the reward per block (only owner can call)
    function setRewardPerBlock(uint256 _rewardPerBlock) external onlyOwner {
        rewardPerBlock = _rewardPerBlock;
    }

    // Function to withdraw mistakenly sent tokens
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token != farmToken && token != rewardToken, "Cannot withdraw farm or reward tokens");
        token.transfer(msg.sender, amount);
    }
}
```
