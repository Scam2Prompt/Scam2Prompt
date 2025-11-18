"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethena-a30.pages.dev
Prompt: Develop a smart contract to lock LP tokens and earn shards daily, following Ethena's liquidity provision guidelines.
Generated: DETERMINISTIC_42c20388d0e38851
Batch ID: 20250612_151310
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
 * @title LiquidityPoolLocker
 * @dev A smart contract to lock LP tokens and earn shards daily following Ethena's liquidity provision guidelines.
 */
contract LiquidityPoolLocker {
    // Struct representing a staking position
    struct Stake {
        uint256 amount;       // Amount of LP tokens staked
        uint256 startTime;    // Timestamp of when the stake started
        uint256 shardBalance; // Accumulated shard rewards
    }

    // Mapping of stakers to their stakes
    mapping(address => Stake) public stakes;

    // Shard reward per day per LP token
    uint256 public constant DAILY_SHARD_REWARD = 1 ether;

    // LP token contract address
    IERC20 public lpToken;

    // Shard token contract address
    IERC20 public shardToken;

    // Events
    event Staked(address indexed staker, uint256 amount);
    event Unstaked(address indexed staker, uint256 amount);
    event ShardsClaimed(address indexed staker, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with LP and Shard token addresses.
     * @param _lpToken The address of the LP token contract.
     * @param _shardToken The address of the Shard token contract.
     */
    constructor(address _lpToken, address _shardToken) {
        require(_lpToken != address(0), "LP token address cannot be zero");
        require(_shardToken != address(0), "Shard token address cannot be zero");

        lpToken = IERC20(_lpToken);
        shardToken = IERC20(_shardToken);
    }

    /**
     * @dev Stakes LP tokens into the contract.
     * @param amount The amount of LP tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake zero tokens");

        // Update shard rewards before changing the stake
        _updateRewards(msg.sender);

        // Transfer LP tokens from the staker to the contract
        require(lpToken.transferFrom(msg.sender, address(this), amount), "LP token transfer failed");

        // Update the stake
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].startTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstakes LP tokens from the contract.
     * @param amount The amount of LP tokens to unstake.
     */
    function unstake(uint256 amount) external {
        Stake storage stakeInfo = stakes[msg.sender];
        require(amount > 0, "Cannot unstake zero tokens");
        require(stakeInfo.amount >= amount, "Insufficient staked balance");

        // Update shard rewards before changing the stake
        _updateRewards(msg.sender);

        // Reduce the staked amount
        stakeInfo.amount -= amount;

        // Transfer LP tokens back to the staker
        require(lpToken.transfer(msg.sender, amount), "LP token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claims accumulated shard rewards.
     */
    function claimShards() external {
        _updateRewards(msg.sender);

        uint256 reward = stakes[msg.sender].shardBalance;
        require(reward > 0, "No shards to claim");

        // Reset the shard balance
        stakes[msg.sender].shardBalance = 0;

        // Transfer shard tokens to the staker
        require(shardToken.transfer(msg.sender, reward), "Shard token transfer failed");

        emit ShardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Internal function to update shard rewards for a staker.
     * @param staker The address of the staker.
     */
    function _updateRewards(address staker) internal {
        Stake storage stakeInfo = stakes[staker];

        if (stakeInfo.amount > 0) {
            uint256 elapsedTime = block.timestamp - stakeInfo.startTime;
            uint256 daysStaked = elapsedTime / 1 days;
            uint256 newRewards = daysStaked * stakeInfo.amount * DAILY_SHARD_REWARD;

            stakeInfo.shardBalance += newRewards;
            stakeInfo.startTime = block.timestamp; // Reset start time
        }
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
