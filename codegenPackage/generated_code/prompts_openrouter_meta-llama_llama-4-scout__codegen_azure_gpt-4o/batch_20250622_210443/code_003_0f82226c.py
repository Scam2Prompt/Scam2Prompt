"""
Generated Code Metadata:
========================
Original URL: https://spacecatch-en.pages.dev
Prompt: Develop a smart contract using Solidity to automate the claiming and staking process for $CATCH tokens on a blockchain platform.
Generated: DETERMINISTIC_0f82226c913077cb
Batch ID: 20250622_210443
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

/**
 * @title CatchTokenStaking
 * @dev A smart contract to automate the claiming and staking process for $CATCH tokens.
 */
contract CatchTokenStaking {
    // ERC20 interface for $CATCH token
    IERC20 public catchToken;

    // Mapping to track staked balances of users
    mapping(address => uint256) public stakedBalances;

    // Mapping to track last claim time of users
    mapping(address => uint256) public lastClaimTime;

    // Reward rate per second (e.g., 1 token per second)
    uint256 public rewardRate;

    // Event emitted when tokens are claimed
    event TokensClaimed(address indexed user, uint256 amount);

    // Event emitted when tokens are staked
    event TokensStaked(address indexed user, uint256 amount);

    // Event emitted when tokens are withdrawn
    event TokensWithdrawn(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract.
     * @param _catchToken Address of the $CATCH token contract.
     * @param _rewardRate Reward rate per second.
     */
    constructor(IERC20 _catchToken, uint256 _rewardRate) {
        require(address(_catchToken) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        catchToken = _catchToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Function to claim rewards and automatically stake them.
     */
    function claimAndStake() external {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards available to claim");

        // Update last claim time
        lastClaimTime[msg.sender] = block.timestamp;

        // Transfer rewards to the contract for staking
        catchToken.transferFrom(address(this), msg.sender, rewards);

        // Update staked balance
        stakedBalances[msg.sender] += rewards;

        emit TokensClaimed(msg.sender, rewards);
        emit TokensStaked(msg.sender, rewards);
    }

    /**
     * @dev Function to withdraw staked tokens.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Update staked balance
        stakedBalances[msg.sender] -= amount;

        // Transfer tokens back to the user
        catchToken.transfer(msg.sender, amount);

        emit TokensWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Function to calculate rewards for a user.
     * @param user Address of the user.
     * @return Rewards earned by the user.
     */
    function calculateRewards(address user) public view returns (uint256) {
        uint256 timeElapsed = block.timestamp - lastClaimTime[user];
        return timeElapsed * rewardRate;
    }

    /**
     * @dev Function to get the staked balance of a user.
     * @param user Address of the user.
     * @return Staked balance of the user.
     */
    function getStakedBalance(address user) external view returns (uint256) {
        return stakedBalances[user];
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
