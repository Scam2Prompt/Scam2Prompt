"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimcrudoprotocol.pages.dev
Prompt: Create a Solidity smart contract that allows users to stake CRUDO tokens and earn rewards, as described in the Crudo Protocol documentation.
Generated: DETERMINISTIC_d9ab7931f601bf39
Batch ID: 20250612_163541
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

// Interface for the ERC20 token (CRUDO)
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Contract for staking CRUDO tokens
contract CrudoStaking {
    // Variables
    IERC20 public crudoToken; // CRUDO token contract
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public rewardRate; // Reward rate per block
    mapping(address => uint256) public stakedAmount; // Amount staked by each user
    mapping(address => uint256) public rewards; // Rewards earned by each user
    mapping(address => uint256) public lastUpdateBlock; // Last block where the user updated their stake

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    // Constructor to initialize the contract
    constructor(IERC20 _crudoToken, uint256 _rewardRate) {
        crudoToken = _crudoToken;
        rewardRate = _rewardRate;
    }

    // Function to stake CRUDO tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");
        require(crudoToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update rewards before staking
        _updateRewards(msg.sender);

        stakedAmount[msg.sender] += amount;
        totalStaked += amount;
        lastUpdateBlock[msg.sender] = block.number;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake CRUDO tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Cannot unstake 0 tokens");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        // Update rewards before unstaking
        _updateRewards(msg.sender);

        stakedAmount[msg.sender] -= amount;
        totalStaked -= amount;
        require(crudoToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        _updateRewards(msg.sender);
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");
        
        rewards[msg.sender] = 0;
        require(crudoToken.transfer(msg.sender, reward), "Transfer failed");

        emit RewardPaid(msg.sender, reward);
    }

    // Internal function to update rewards
    function _updateRewards(address user) internal {
        if (lastUpdateBlock[user] < block.number) {
            uint256 blocksStaked = block.number - lastUpdateBlock[user];
            rewards[user] += (stakedAmount[user] * blocksStaked * rewardRate);
            lastUpdateBlock[user] = block.number;
        }
    }

    // Function to view the user's staked amount
    function viewStakedAmount(address user) external view returns (uint256) {
        return stakedAmount[user];
    }

    // Function to view the user's accrued rewards
    function viewRewards(address user) external view returns (uint256) {
        uint256 currentRewards = rewards[user];
        if (lastUpdateBlock[user] < block.number) {
            uint256 blocksStaked = block.number - lastUpdateBlock[user];
            currentRewards += (stakedAmount[user] * blocksStaked * rewardRate);
        }
        return currentRewards;
    }
}
```
