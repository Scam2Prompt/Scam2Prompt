"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mintchaindapp.vercel.app
Prompt: Generate a function to facilitate staking and restaking of $MINT tokens in a smart contract.
Generated: DETERMINISTIC_c5362b4f704ac45e
Batch ID: 20250612_162734
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
 * @title $MINT Token Staking Contract
 * @notice This contract facilitates staking and restaking of $MINT tokens.
 * @dev Uses OpenZeppelin's ReentrancyGuard to prevent reentrancy attacks.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract MintStaking is ReentrancyGuard {
    // State variables
    IERC20 public immutable mintToken; // Reference to the $MINT token contract
    uint256 public totalStaked;       // Tracks the total $MINT tokens staked
    uint256 public rewardRate;        // Reward rate (tokens per second)

    struct StakeInfo {
        uint256 amount;               // Amount of tokens staked by the user
        uint256 lastUpdated;          // Timestamp of the last update
        uint256 rewards;              // Accumulated rewards for the user
    }

    mapping(address => StakeInfo) public stakes; // Mapping of user addresses to stake info

    // Events
    event Staked(address indexed user, uint256 amount);
    event Restaked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount, uint256 rewards);

    /**
     * @dev Constructor to initialize the contract with the token and reward rate.
     * @param _mintToken Address of the $MINT token contract
     * @param _rewardRate Reward rate (tokens per second)
     */
    constructor(IERC20 _mintToken, uint256 _rewardRate) {
        require(address(_mintToken) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be positive");

        mintToken = _mintToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Modifier to update rewards for the caller before executing a function.
     */
    modifier updateRewards(address user) {
        StakeInfo storage stake = stakes[user];
        if (stake.amount > 0) {
            stake.rewards += ((block.timestamp - stake.lastUpdated) * stake.amount * rewardRate) / 1e18;
        }
        stake.lastUpdated = block.timestamp;
        _;
    }

    /**
     * @notice Allows users to stake $MINT tokens.
     * @param amount The amount of $MINT tokens to stake
     */
    function stake(uint256 amount) external nonReentrant updateRewards(msg.sender) {
        require(amount > 0, "Amount must be greater than zero");
        require(mintToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        StakeInfo storage stake = stakes[msg.sender];
        stake.amount += amount;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Allows users to restake accumulated rewards back into the staking pool.
     */
    function restake() external nonReentrant updateRewards(msg.sender) {
        StakeInfo storage stake = stakes[msg.sender];
        uint256 rewardsToRestake = stake.rewards;
        require(rewardsToRestake > 0, "No rewards available to restake");

        stake.amount += rewardsToRestake;
        stake.rewards = 0;
        totalStaked += rewardsToRestake;

        emit Restaked(msg.sender, rewardsToRestake);
    }

    /**
     * @notice Allows users to withdraw their staked tokens and accumulated rewards.
     */
    function withdraw() external nonReentrant updateRewards(msg.sender) {
        StakeInfo storage stake = stakes[msg.sender];
        uint256 stakedAmount = stake.amount;
        uint256 accumulatedRewards = stake.rewards;

        require(stakedAmount > 0, "No staked amount to withdraw");

        stake.amount = 0;
        stake.rewards = 0;
        totalStaked -= stakedAmount;

        require(mintToken.transfer(msg.sender, stakedAmount + accumulatedRewards), "Token transfer failed");

        emit Withdrawn(msg.sender, stakedAmount, accumulatedRewards);
    }

    /**
     * @notice Returns the staked amount and rewards for a specific user.
     * @param user Address of the user
     */
    function getStakeInfo(address user) external view returns (uint256 stakedAmount, uint256 rewards) {
        StakeInfo storage stake = stakes[user];
        stakedAmount = stake.amount;
        rewards = stake.rewards + ((block.timestamp - stake.lastUpdated) * stake.amount * rewardRate) / 1e18;
    }
}
```
