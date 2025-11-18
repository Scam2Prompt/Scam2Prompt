"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crudoprotocol-io.web.app
Prompt: Develop a blockchain-based staking mechanism for CRUDO tokens, allowing token holders to generate passive income.
Generated: DETERMINISTIC_9643848d84a97efc
Batch ID: 20250612_145711
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

// Interface for the CRUDO token
interface ICRUDOToken is IERC20 {
    function mint(address to, uint256 amount) external;
}

// Staking contract for CRUDO tokens
contract CRUDOStaking is Ownable {
    // Token being staked
    ICRUDOToken public crudoToken;

    // Struct to hold user staking information
    struct Staker {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Reward debt for the staker
    }

    // Mapping of user addresses to their staking information
    mapping(address => Staker) public stakers;

    // Total amount of staked tokens
    uint256 public totalStaked;
    
    // Reward rate per block
    uint256 public rewardPerBlock;

    // Total rewards distributed
    uint256 public totalRewards;

    // Events for staking and unstaking
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to initialize the staking contract
    constructor(ICRUDOToken _crudoToken, uint256 _rewardPerBlock) {
        crudoToken = _crudoToken;
        rewardPerBlock = _rewardPerBlock;
    }

    // Function to stake tokens
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake 0 tokens");
        require(crudoToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        Staker storage staker = stakers[msg.sender];

        // Update user rewards before changing amount
        updateRewards(msg.sender);

        // Update staker's amount and total staked
        staker.amount += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function to unstake tokens
    function unstake(uint256 _amount) external {
        Staker storage staker = stakers[msg.sender];

        require(_amount > 0, "Cannot unstake 0 tokens");
        require(staker.amount >= _amount, "Insufficient staked amount");

        // Update user rewards before changing amount
        updateRewards(msg.sender);

        // Update staker's amount and total staked
        staker.amount -= _amount;
        totalStaked -= _amount;

        require(crudoToken.transfer(msg.sender, _amount), "Transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        updateRewards(msg.sender);
        uint256 reward = stakers[msg.sender].rewardDebt;

        require(reward > 0, "No rewards to claim");

        // Reset reward debt
        stakers[msg.sender].rewardDebt = 0;

        // Mint CRUDO tokens as rewards
        crudoToken.mint(msg.sender, reward);
        totalRewards += reward;

        emit RewardPaid(msg.sender, reward);
    }

    // Internal function to update rewards for a user
    function updateRewards(address _staker) internal {
        Staker storage staker = stakers[_staker];
        
        // Calculate pending rewards
        uint256 pendingReward = (staker.amount * rewardPerBlock) - staker.rewardDebt;
        
        // Update the staker's reward debt
        staker.rewardDebt += pendingReward;
    }

    // Admin function to update reward rate
    function setRewardPerBlock(uint256 _rewardPerBlock) external onlyOwner {
        rewardPerBlock = _rewardPerBlock;
    }

    // Function to withdraw any ERC20 token accidentally sent to this contract
    function rescueTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(crudoToken), "Cannot withdraw staked tokens");
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }
}
```
