"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bingomeme.pages.dev
Prompt: Provide code to implement staking functionality for $BINGO tokens, as outlined in Phase 4 of the roadmap. Include a basic smart contract example for staking rewards.
Generated: DETERMINISTIC_153725d5273edf3b
Batch ID: 20250612_153517
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
 * @title BingoTokenStaking
 * @dev A smart contract to implement staking functionality for $BINGO tokens.
 * Users can stake tokens to earn rewards based on the staking period.
 */
contract BingoTokenStaking {
    // Address of the ERC20 $BINGO token contract
    IERC20 public bingoToken;

    // Annual Percentage Yield (APY) for rewards (e.g., 10% = 1000 basis points)
    uint256 public constant APY_BASIS_POINTS = 1000;

    // A constant for year duration in seconds (365 days)
    uint256 public constant SECONDS_IN_YEAR = 365 * 24 * 60 * 60;

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp when staking started
    }

    mapping(address => Stake) public stakes; // Mapping of stakers to their stake details
    mapping(address => uint256) public rewards; // Mapping of stakers to their accumulated rewards

    event Staked(address indexed staker, uint256 amount);
    event Unstaked(address indexed staker, uint256 amount);
    event RewardClaimed(address indexed staker, uint256 reward);

    /**
     * @dev Constructor to set the $BINGO token address.
     * @param _bingoToken Address of the ERC20 $BINGO token contract.
     */
    constructor(IERC20 _bingoToken) {
        bingoToken = _bingoToken;
    }

    /**
     * @dev Stake $BINGO tokens to earn rewards.
     * @param amount Amount of $BINGO tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from caller to contract
        require(bingoToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Calculate rewards for any existing stake
        _updateRewards(msg.sender);

        // Update stake details
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake $BINGO tokens and claim rewards.
     */
    function unstake() external {
        require(stakes[msg.sender].amount > 0, "No tokens staked");

        // Calculate rewards before unstaking
        _updateRewards(msg.sender);

        uint256 amount = stakes[msg.sender].amount;
        stakes[msg.sender].amount = 0; // Reset staked amount
        stakes[msg.sender].timestamp = 0; // Reset timestamp

        // Transfer tokens back to the staker
        require(bingoToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim accumulated rewards.
     */
    function claimRewards() external {
        _updateRewards(msg.sender);
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards available");

        rewards[msg.sender] = 0; // Reset rewards
        require(bingoToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Internal function to update rewards for a staker.
     * @param staker Address of the staker.
     */
    function _updateRewards(address staker) internal {
        Stake storage userStake = stakes[staker];
        if (userStake.amount > 0) {
            uint256 stakingDuration = block.timestamp - userStake.timestamp;
            uint256 reward = (userStake.amount * APY_BASIS_POINTS * stakingDuration) / (SECONDS_IN_YEAR * 10000);
            rewards[staker] += reward;
            userStake.timestamp = block.timestamp; // Reset staking timestamp
        }
    }

    /**
     * @dev View function to calculate pending rewards for a staker.
     * @param staker Address of the staker.
     * @return Pending rewards.
     */
    function pendingRewards(address staker) external view returns (uint256) {
        Stake storage userStake = stakes[staker];
        if (userStake.amount > 0) {
            uint256 stakingDuration = block.timestamp - userStake.timestamp;
            uint256 reward = (userStake.amount * APY_BASIS_POINTS * stakingDuration) / (SECONDS_IN_YEAR * 10000);
            return rewards[staker] + reward;
        }
        return rewards[staker];
    }
}

/**
 * @dev Interface for ERC20 tokens.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
