"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defi-03.vip
Prompt: Create a smart contract example for a DeFi application on Ethereum that supports staking ETH.
Generated: DETERMINISTIC_ede9da6492549ff8
Batch ID: 20250612_142633
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

/**
 * @title DeFi Staking Contract
 * @dev Smart contract for staking ETH with rewards distribution in Ethereum.
 * Users can stake ETH and withdraw their staked amount along with rewards.
 */
contract ETHStaking {
    // Mapping to track user balances
    mapping(address => uint256) public stakes;

    // Mapping to track user rewards
    mapping(address => uint256) public rewards;

    // Total amount staked in the contract
    uint256 public totalStaked;

    // Annual percentage yield (APY) for rewards (e.g., 10% = 1000)
    uint256 public constant APY = 1000;

    // Timestamp when staking starts
    mapping(address => uint256) public stakingStartTime;

    // Owner of the contract
    address public owner;

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount, uint256 reward);

    // Constructor to set the owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to allow users to stake ETH.
     */
    function stake() external payable {
        require(msg.value > 0, "Cannot stake 0 ETH");

        // Calculate pending rewards before updating stake
        if (stakes[msg.sender] > 0) {
            rewards[msg.sender] += calculateReward(msg.sender);
        }

        // Update staking information
        stakes[msg.sender] += msg.value;
        stakingStartTime[msg.sender] = block.timestamp;

        // Increment total staked amount
        totalStaked += msg.value;

        emit Staked(msg.sender, msg.value);
    }

    /**
     * @dev Function to allow users to withdraw their staked ETH along with rewards.
     */
    function withdraw() external {
        require(stakes[msg.sender] > 0, "No staked ETH to withdraw");

        // Calculate total reward
        uint256 reward = calculateReward(msg.sender) + rewards[msg.sender];
        uint256 stakedAmount = stakes[msg.sender];

        // Reset user staking data
        stakes[msg.sender] = 0;
        rewards[msg.sender] = 0;
        stakingStartTime[msg.sender] = 0;

        // Decrement total staked amount
        totalStaked -= stakedAmount;

        // Transfer staked ETH and reward
        uint256 totalPayout = stakedAmount + reward;
        (bool success, ) = msg.sender.call{value: totalPayout}("");
        require(success, "Withdrawal failed");

        emit Withdrawn(msg.sender, stakedAmount, reward);
    }

    /**
     * @dev Function to calculate reward for a user based on APY and staking time.
     * @param user Address of the user.
     * @return Reward amount in wei.
     */
    function calculateReward(address user) public view returns (uint256) {
        uint256 stakingDuration = block.timestamp - stakingStartTime[user];
        uint256 rewardRatePerSecond = (stakes[user] * APY) / 10000 / 365 / 24 / 60 / 60;
        return stakingDuration * rewardRatePerSecond;
    }

    /**
     * @dev Function to allow the owner to deposit ETH to the contract for rewards distribution.
     * This ensures the contract has enough balance to pay out rewards.
     */
    function depositRewards() external payable onlyOwner {
        require(msg.value > 0, "Cannot deposit 0 ETH");
    }

    /**
     * @dev Function to allow the owner to withdraw any excess balance from the contract.
     * Ensures the contract retains enough ETH to cover all staked amounts and rewards.
     */
    function withdrawExcessBalance(uint256 amount) external onlyOwner {
        require(address(this).balance >= totalStaked, "Insufficient contract balance");
        require(address(this).balance - totalStaked >= amount, "Cannot withdraw below required reserve");

        (bool success, ) = owner.call{value: amount}("");
        require(success, "Withdraw failed");
    }

    /**
     * @dev Fallback function to handle ETH transfers directly to the contract.
     */
    receive() external payable {}
}
```
