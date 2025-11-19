"""
Generated Code Metadata:
========================
Original URL: https://cryptoallstars-launch.web.app
Prompt: Generate a smart contract code snippet in Solidity for a multi-token, multi-chain meme coin staking system similar to MemeVault.
Generated: DETERMINISTIC_4df419744403e72d
Batch ID: 20250622_211541
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
 * @title MultiTokenMultiChainStaking
 * @dev A smart contract for staking multiple meme tokens across multiple chains.
 */
contract MultiTokenMultiChainStaking {
    // Struct to store staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of when the stake was made
        uint256 chainId; // Chain ID where the stake was made
    }

    // Mapping of user address to token address to stake details
    mapping(address => mapping(address => Stake)) public stakes;

    // Mapping of token address to reward rate (per second)
    mapping(address => uint256) public rewardRates;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, address indexed token, uint256 amount, uint256 chainId);

    // Event emitted when a user withdraws staked tokens
    event Withdrawn(address indexed user, address indexed token, uint256 amount, uint256 chainId);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, address indexed token, uint256 rewardAmount);

    /**
     * @dev Stake tokens for a specific chain.
     * @param token Address of the token to stake.
     * @param amount Amount of tokens to stake.
     * @param chainId ID of the chain where staking is happening.
     */
    function stake(address token, uint256 amount, uint256 chainId) external {
        require(amount > 0, "Stake amount must be greater than zero");
        require(rewardRates[token] > 0, "Token is not supported for staking");

        // Transfer tokens from the user to the contract
        require(IERC20(token).transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update staking information
        stakes[msg.sender][token] = Stake({
            amount: stakes[msg.sender][token].amount + amount,
            timestamp: block.timestamp,
            chainId: chainId
        });

        emit Staked(msg.sender, token, amount, chainId);
    }

    /**
     * @dev Withdraw staked tokens.
     * @param token Address of the token to withdraw.
     */
    function withdraw(address token) external {
        Stake storage userStake = stakes[msg.sender][token];
        require(userStake.amount > 0, "No tokens staked");

        uint256 amount = userStake.amount;

        // Reset the stake
        userStake.amount = 0;
        userStake.timestamp = 0;

        // Transfer tokens back to the user
        require(IERC20(token).transfer(msg.sender, amount), "Token transfer failed");

        emit Withdrawn(msg.sender, token, amount, userStake.chainId);
    }

    /**
     * @dev Claim staking rewards.
     * @param token Address of the token to claim rewards for.
     */
    function claimRewards(address token) external {
        Stake storage userStake = stakes[msg.sender][token];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate rewards based on the reward rate and staking duration
        uint256 stakingDuration = block.timestamp - userStake.timestamp;
        uint256 rewardAmount = stakingDuration * rewardRates[token] * userStake.amount / 1e18;

        // Update the staking timestamp
        userStake.timestamp = block.timestamp;

        // Transfer rewards to the user
        require(IERC20(token).transfer(msg.sender, rewardAmount), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, token, rewardAmount);
    }

    /**
     * @dev Set reward rate for a token.
     * @param token Address of the token.
     * @param rate Reward rate per second (scaled by 1e18).
     */
    function setRewardRate(address token, uint256 rate) external {
        // Only the contract owner can set reward rates (add access control in production)
        rewardRates[token] = rate;
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
