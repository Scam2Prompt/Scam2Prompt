"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mpeppe-is.web.app
Prompt: Create a code snippet for a decentralized application (dApp) that allows users to stake $MPEPE tokens in DeFi liquidity pools and earn rewards.
Generated: DETERMINISTIC_859fb319d3054b19
Batch ID: 20250612_155428
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
 * @title StakingContract
 * @dev A decentralized application (dApp) for staking $MPEPE tokens into a liquidity pool and earning rewards.
 */
contract StakingContract {
    // State variables
    address public owner; // Owner of the contract
    IERC20 public mpepeToken; // ERC20 token to be staked ($MPEPE)
    uint256 public rewardRate; // Reward rate (tokens per second)
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public stakingStartTime; // Timestamp when staking begins

    // Data structure to track user stakes
    struct StakeInfo {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Amount of rewards already claimed
        uint256 lastUpdated; // Last timestamp when rewards were calculated
    }

    // Mapping to track stakes by user address
    mapping(address => StakeInfo) public stakes;

    // Events
    event TokensStaked(address indexed user, uint256 amount);
    event TokensUnstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRate);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor initializes the contract
    constructor(address _mpepeToken, uint256 _rewardRate) {
        require(_mpepeToken != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        owner = msg.sender;
        mpepeToken = IERC20(_mpepeToken);
        rewardRate = _rewardRate;
        stakingStartTime = block.timestamp;
    }

    /**
     * @dev Allows users to stake $MPEPE tokens.
     * @param _amount Amount of $MPEPE tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Transfer $MPEPE tokens from the user to the contract
        mpepeToken.transferFrom(msg.sender, address(this), _amount);

        // Update staking info
        StakeInfo storage userStake = stakes[msg.sender];
        _updateRewards(msg.sender);
        userStake.amount += _amount;
        userStake.lastUpdated = block.timestamp;
        totalStaked += _amount;

        emit TokensStaked(msg.sender, _amount);
    }

    /**
     * @dev Allows users to unstake their $MPEPE tokens.
     * @param _amount Amount of $MPEPE tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        StakeInfo storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked balance");

        // Update rewards before unstaking
        _updateRewards(msg.sender);

        // Deduct unstaked amount from user's stake
        userStake.amount -= _amount;
        userStake.lastUpdated = block.timestamp;
        totalStaked -= _amount;

        // Transfer $MPEPE tokens back to the user
        mpepeToken.transfer(msg.sender, _amount);

        emit TokensUnstaked(msg.sender, _amount);
    }

    /**
     * @dev Allows users to claim accumulated rewards.
     */
    function claimRewards() external {
        StakeInfo storage userStake = stakes[msg.sender];
        _updateRewards(msg.sender);

        uint256 rewardsToClaim = userStake.rewardDebt;
        require(rewardsToClaim > 0, "No rewards available to claim");

        // Reset reward debt
        userStake.rewardDebt = 0;

        // Transfer rewards to the user
        mpepeToken.transfer(msg.sender, rewardsToClaim);

        emit RewardsClaimed(msg.sender, rewardsToClaim);
    }

    /**
     * @dev Updates the reward rate. Only callable by the owner.
     * @param _newRate New reward rate (tokens per second).
     */
    function updateRewardRate(uint256 _newRate) external onlyOwner {
        require(_newRate > 0, "Reward rate must be greater than zero");
        rewardRate = _newRate;
        emit RewardRateUpdated(_newRate);
    }

    /**
     * @dev Internal function to handle reward calculations and updates.
     * @param _user Address of the user whose rewards are being updated.
     */
    function _updateRewards(address _user) internal {
        StakeInfo storage userStake = stakes[_user];

        // Calculate the elapsed time since the last update
        uint256 elapsedTime = block.timestamp - userStake.lastUpdated;

        // Calculate the rewards earned during the elapsed time
        uint256 rewardsEarned = (userStake.amount * rewardRate * elapsedTime) / 1e18;

        // Update reward debt and last updated timestamp
        userStake.rewardDebt += rewardsEarned;
        userStake.lastUpdated = block.timestamp;
    }
}

/**
 * @dev Interface for ERC20 tokens.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
