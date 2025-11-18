"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unstaked-token.world
Prompt: Develop a smart contract in Solidity to automate staking and unstaking of $UNSD tokens, ensuring compatibility with Ethereum-based wallets.
Generated: DETERMINISTIC_afb99c1253832f58
Batch ID: 20250612_154131
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
 * @title UNSDTokenStaking
 * @dev A smart contract for staking and unstaking $UNSD tokens.
 * Users can stake tokens to earn rewards and unstake tokens at any time.
 * Compatible with Ethereum-based wallets.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract UNSDTokenStaking {
    // Token contract interface
    IERC20 public unsdToken;

    // Reward rate per token per second (example: 0.0001 UNSD tokens per second)
    uint256 public rewardRate = 1e14;

    // Data structure to hold staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Rewards already paid out
        uint256 lastUpdated; // Timestamp of last stake/unstake
    }

    // Mapping of user address to their respective stake
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the $UNSD token address.
     * @param _unsdToken Address of the $UNSD token contract.
     */
    constructor(address _unsdToken) {
        require(_unsdToken != address(0), "Invalid token address");
        unsdToken = IERC20(_unsdToken);
    }

    /**
     * @dev Stake $UNSD tokens into the contract.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than zero");

        // Update rewards for the user before staking
        _updateRewards(msg.sender);

        // Transfer tokens from the user to the contract
        require(unsdToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update staking information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].lastUpdated = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake $UNSD tokens and claim rewards.
     * @param amount Amount of tokens to unstake.
     */
    function unstake(uint256 amount) external {
        require(amount > 0, "Unstake amount must be greater than zero");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked balance");

        // Update rewards for the user before unstaking
        _updateRewards(msg.sender);

        // Deduct staked amount
        stakes[msg.sender].amount -= amount;

        // Transfer tokens back to the user
        require(unsdToken.transfer(msg.sender, amount), "Token transfer failed");

        stakes[msg.sender].lastUpdated = block.timestamp;

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim accumulated rewards without unstaking.
     */
    function claimRewards() external {
        // Update rewards for the user
        _updateRewards(msg.sender);

        uint256 pendingRewards = stakes[msg.sender].rewardDebt;
        require(pendingRewards > 0, "No rewards available");

        // Reset reward debt
        stakes[msg.sender].rewardDebt = 0;

        // Transfer rewards to the user
        require(unsdToken.transfer(msg.sender, pendingRewards), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, pendingRewards);
    }

    /**
     * @dev Internal function to update staking rewards for a user.
     * @param user Address of the user whose rewards are being updated.
     */
    function _updateRewards(address user) internal {
        Stake storage stakeInfo = stakes[user];
        uint256 stakedAmount = stakeInfo.amount;

        if (stakedAmount > 0) {
            // Calculate pending rewards
            uint256 timeElapsed = block.timestamp - stakeInfo.lastUpdated;
            uint256 rewards = (stakedAmount * rewardRate * timeElapsed) / 1e18;

            // Add rewards to reward debt
            stakeInfo.rewardDebt += rewards;
        }

        // Update lastUpdated timestamp
        stakeInfo.lastUpdated = block.timestamp;
    }

    /**
     * @dev Retrieve staking information for a given user.
     * @param user Address of the user.
     * @return amount Staked token amount.
     * @return rewardDebt Accumulated rewards.
     * @return lastUpdated Last update timestamp.
     */
    function getStake(address user)
        external
        view
        returns (uint256 amount, uint256 rewardDebt, uint256 lastUpdated)
    {
        Stake storage stakeInfo = stakes[user];
        return (stakeInfo.amount, stakeInfo.rewardDebt, stakeInfo.lastUpdated);
    }
}
```
