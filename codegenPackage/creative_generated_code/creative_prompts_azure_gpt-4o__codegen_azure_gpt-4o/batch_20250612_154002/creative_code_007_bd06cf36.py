"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdc.name
Prompt: Generate code for a decentralized application (dApp) that allows users to stake USDC and earn rewards on the Ethereum blockchain.
Generated: DETERMINISTIC_bd06cf3637785d49
Batch ID: 20250612_154002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is a Solidity smart contract for a decentralized application (dApp) that allows users to stake USDC and earn rewards on the Ethereum blockchain:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title USDC Staking Contract
 * @dev A decentralized application for staking USDC and earning rewards.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract USDCStaking {
    // USDC token contract address
    address public immutable usdcToken;

    // Represents the staking balances of each user
    mapping(address => uint256) public stakingBalances;

    // Tracks the rewards earned by each user
    mapping(address => uint256) public rewards;

    // Tracks the last time a user staked
    mapping(address => uint256) public lastUpdateTime;

    // Reward rate per second (e.g., 1 reward token per second per staked USDC)
    uint256 public rewardRate = 1;

    // Owner address for administrative tasks
    address public owner;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    /**
     * @dev Modifier to restrict access to owner-only functionality.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Unauthorized: Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _usdcToken Address of the USDC token contract.
     */
    constructor(address _usdcToken) {
        require(_usdcToken != address(0), "Invalid USDC token address");
        usdcToken = _usdcToken;
        owner = msg.sender;
    }

    /**
     * @dev Update rewards for a user based on staking duration.
     * @param user Address of the user to update rewards.
     */
    function updateReward(address user) internal {
        if (stakingBalances[user] > 0) {
            rewards[user] += stakingBalances[user] * rewardRate * (block.timestamp - lastUpdateTime[user]);
        }
        lastUpdateTime[user] = block.timestamp;
    }

    /**
     * @dev Allows users to stake USDC tokens into the contract.
     * @param amount Amount of USDC tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0 tokens");
        updateReward(msg.sender);

        // Transfer USDC tokens from the user to the contract
        IERC20(usdcToken).transferFrom(msg.sender, address(this), amount);

        // Update staking balance
        stakingBalances[msg.sender] += amount;
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Allows users to withdraw their staked USDC tokens.
     * @param amount Amount of USDC tokens to withdraw.
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Cannot withdraw 0 tokens");
        require(stakingBalances[msg.sender] >= amount, "Insufficient balance to withdraw");
        updateReward(msg.sender);

        // Update staking balance
        stakingBalances[msg.sender] -= amount;

        // Transfer USDC tokens back to the user
        IERC20(usdcToken).transfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Allows users to claim their earned rewards.
     */
    function claimReward() external {
        updateReward(msg.sender);

        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards available to claim");

        // Reset the reward balance
        rewards[msg.sender] = 0;

        // Transfer reward tokens (assume reward tokens are managed separately)
        IERC20(usdcToken).transfer(msg.sender, reward);
        emit RewardPaid(msg.sender, reward);
    }

    /**
     * @dev Allows the owner to update the reward rate.
     * @param _rewardRate New reward rate per second.
     */
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        require(_rewardRate > 0, "Reward rate must be greater than 0");
        rewardRate = _rewardRate;
    }

    /**
     * @dev Allows the owner to withdraw excess USDC tokens from the contract.
     * @param amount Amount of USDC tokens to withdraw.
     */
    function withdrawExcessTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Cannot withdraw 0 tokens");
        IERC20(usdcToken).transfer(owner, amount);
    }
}
```

This contract meets the specified requirements and can be deployed on the Ethereum blockchain. It includes staking functionality, reward calculation, withdrawal, and reward claiming. Note that rewards are paid in USDC for simplicity in this implementation. In a real-world scenario, a separate reward token or mechanism might be preferred.
