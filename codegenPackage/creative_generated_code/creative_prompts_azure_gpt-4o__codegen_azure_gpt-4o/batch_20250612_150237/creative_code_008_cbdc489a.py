"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogegovapp.com
Prompt: Write a Solidity contract that supports staking and unstaking $DOGEGOV memecoin, incorporating the community-driven principles described on the DOGEGOV website.
Generated: DETERMINISTIC_cbdc489af7d742c5
Batch ID: 20250612_150237
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
 * @title DogeGovStaking
 * @dev A staking contract for the $DOGEGOV memecoin that allows users to stake and unstake tokens.
 *      Implements community-driven principles by allowing users to earn staking rewards.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function totalSupply() external view returns (uint256);
}

contract DogeGovStaking {
    // Address of the $DOGEGOV token
    IERC20 public dogeGovToken;

    // Mapping to track staked balances for each user
    mapping(address => uint256) public stakedBalances;

    // Mapping to track last staking timestamps for rewards calculation
    mapping(address => uint256) public lastStakedTimestamp;

    // Annual Percentage Yield (APY) for staking rewards (e.g., 10% APY)
    uint256 public constant REWARD_APY = 10;

    // Owner of the staking contract
    address public owner;

    /// @dev Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    /// @dev Modifier to restrict functions to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    constructor(IERC20 _dogeGovToken) {
        dogeGovToken = _dogeGovToken;
        owner = msg.sender;
    }

    /**
     * @dev Function to stake $DOGEGOV tokens.
     * @param amount Number of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");
        require(dogeGovToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer the tokens from the user to the contract
        bool success = dogeGovToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Update staked balance and timestamp
        stakedBalances[msg.sender] += amount;
        lastStakedTimestamp[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to unstake $DOGEGOV tokens and claim rewards.
     */
    function unstake() external {
        uint256 stakedAmount = stakedBalances[msg.sender];
        require(stakedAmount > 0, "No staked tokens to unstake");

        // Calculate staking duration
        uint256 stakingDuration = block.timestamp - lastStakedTimestamp[msg.sender];

        // Calculate rewards based on APY and staking duration
        uint256 reward = calculateReward(stakedAmount, stakingDuration);

        // Reset the user's staked balance
        stakedBalances[msg.sender] = 0;

        // Reset the user's staking timestamp
        lastStakedTimestamp[msg.sender] = 0;

        // Transfer staked tokens and rewards back to the user
        bool successStaked = dogeGovToken.transfer(msg.sender, stakedAmount);
        bool successReward = dogeGovToken.transfer(msg.sender, reward);
        require(successStaked && successReward, "Token transfer failed");

        emit Unstaked(msg.sender, stakedAmount, reward);
    }

    /**
     * @dev Function to calculate staking rewards.
     * @param amount Number of staked tokens.
     * @param duration Staking duration in seconds.
     * @return Reward amount.
     */
    function calculateReward(uint256 amount, uint256 duration) public pure returns (uint256) {
        // Annual reward = (amount * REWARD_APY) / 100
        // Pro-rata reward for staking duration = (annualReward * duration) / 365 days
        uint256 annualReward = (amount * REWARD_APY) / 100;
        uint256 reward = (annualReward * duration) / (365 days);
        return reward;
    }

    /**
     * @dev Emergency function for the owner to withdraw all tokens from the contract.
     * @param to Address to send withdrawn tokens to.
     */
    function emergencyWithdraw(address to) external onlyOwner {
        uint256 contractBalance = dogeGovToken.balanceOf(address(this));
        require(contractBalance > 0, "No tokens to withdraw");

        bool success = dogeGovToken.transfer(to, contractBalance);
        require(success, "Token transfer failed");
    }
}
```
