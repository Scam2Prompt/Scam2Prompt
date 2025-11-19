"""
Generated Code Metadata:
========================
Original URL: https://greenbitcoinweb.pages.dev
Prompt: Develop a simple smart contract in Solidity to automate the staking and reward distribution process for Green Bitcoin on the Ethereum blockchain.
Generated: DETERMINISTIC_0a18ebc3d21e182b
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract GreenBitcoinStaking {
    // State variables
    address public owner;
    uint256 public totalStaked;
    uint256 public rewardRate; // Reward rate per block
    mapping(address => uint256) public stakedAmount;
    mapping(address => uint256) public lastStakeBlock;
    mapping(address => uint256) public rewards;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(uint256 _rewardRate) {
        owner = msg.sender;
        rewardRate = _rewardRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Update rewards before staking
        _updateRewards(msg.sender);

        // Transfer tokens from user to contract
        // Assuming the contract has been approved to spend the tokens
        // Replace `IERC20` with the actual token interface
        // IERC20(tokenAddress).transferFrom(msg.sender, address(this), amount);

        stakedAmount[msg.sender] += amount;
        totalStaked += amount;
        lastStakeBlock[msg.sender] = block.number;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedAmount[msg.sender] >= amount, "Insufficient staked amount");

        // Update rewards before unstaking
        _updateRewards(msg.sender);

        stakedAmount[msg.sender] -= amount;
        totalStaked -= amount;

        // Transfer tokens back to user
        // IERC20(tokenAddress).transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        _updateRewards(msg.sender);
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        rewards[msg.sender] = 0;

        // Transfer rewards to user
        // IERC20(tokenAddress).transfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    // Internal function to update rewards for a user
    function _updateRewards(address user) internal {
        uint256 blocksStaked = block.number - lastStakeBlock[user];
        if (blocksStaked > 0) {
            uint256 reward = blocksStaked * rewardRate * stakedAmount[user];
            rewards[user] += reward;
            lastStakeBlock[user] = block.number;
        }
    }

    // Function to set the reward rate (only owner)
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    // Function to withdraw contract balance (only owner)
    function withdraw(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient balance");
        payable(owner).transfer(amount);
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
