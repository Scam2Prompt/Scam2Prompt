"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://belegends.pages.dev
Prompt: Write a smart contract in Solidity for staking `$LEGEND` tokens, including functionality for claiming rewards and unlocking exclusive benefits.
Generated: DETERMINISTIC_d3fe6e7ce98e443e
Batch ID: 20250612_151301
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
 * @title LegendTokenStaking
 * @notice A smart contract for staking $LEGEND tokens, claiming rewards, and unlocking exclusive benefits.
 */
contract LegendTokenStaking {
    // Define the $LEGEND token interface
    IERC20 public legendToken;

    // Owner address of the contract
    address public owner;

    // Reward rate per token per second
    uint256 public rewardRate;

    // Struct to represent a staker's details
    struct Staker {
        uint256 stakedAmount;  // Total amount staked by the user
        uint256 rewardDebt;    // Reward already paid out
        uint256 lastUpdated;   // Timestamp of the last update
    }

    // Mapping of stakers' addresses to their details
    mapping(address => Staker) public stakers;

    // Events
    event Staked(address indexed staker, uint256 amount);
    event Unstaked(address indexed staker, uint256 amount);
    event RewardClaimed(address indexed staker, uint256 amount);
    event OwnershipTransferred(address indexed oldOwner, address indexed newOwner);

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _legendToken Address of the $LEGEND token contract.
     * @param _rewardRate Reward rate per token per second.
     */
    constructor(IERC20 _legendToken, uint256 _rewardRate) {
        legendToken = _legendToken;
        rewardRate = _rewardRate;
        owner = msg.sender;
    }

    /**
     * @notice Stake $LEGEND tokens in the contract.
     * @param _amount The amount of $LEGEND tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Staking amount must be greater than zero");
        
        Staker storage staker = stakers[msg.sender];

        // Calculate any pending rewards before updating the staked amount
        _updateRewards(msg.sender);

        // Transfer the tokens from the user to the contract
        require(legendToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staker details
        staker.stakedAmount += _amount;
        staker.lastUpdated = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake $LEGEND tokens from the contract.
     * @param _amount The amount of $LEGEND tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        Staker storage staker = stakers[msg.sender];
        require(_amount > 0, "Unstaking amount must be greater than zero");
        require(staker.stakedAmount >= _amount, "Insufficient staked balance");

        // Calculate any pending rewards before updating the staked amount
        _updateRewards(msg.sender);

        // Update staker details
        staker.stakedAmount -= _amount;

        // Transfer the tokens back to the user
        require(legendToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Claim rewards accumulated from staking.
     */
    function claimRewards() external {
        Staker storage staker = stakers[msg.sender];
        _updateRewards(msg.sender);

        uint256 pendingRewards = calculateRewards(msg.sender);
        require(pendingRewards > 0, "No rewards to claim");

        staker.rewardDebt += pendingRewards;

        // Transfer the rewards to the user
        require(legendToken.transfer(msg.sender, pendingRewards), "Reward transfer failed");

        emit RewardClaimed(msg.sender, pendingRewards);
    }

    /**
     * @notice Calculate the rewards for a staker based on staking time and rate.
     * @param _staker Address of the staker.
     * @return The amount of rewards earned.
     */
    function calculateRewards(address _staker) public view returns (uint256) {
        Staker storage staker = stakers[_staker];
        if (staker.stakedAmount == 0) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp - staker.lastUpdated;
        uint256 rewards = (stakingDuration * rewardRate * staker.stakedAmount) / 1e18;

        return rewards - staker.rewardDebt;
    }

    /**
     * @notice Update rewards for a staker.
     * @param _staker Address of the staker.
     */
    function _updateRewards(address _staker) internal {
        Staker storage staker = stakers[_staker];
        uint256 pendingRewards = calculateRewards(_staker);

        if (pendingRewards > 0) {
            staker.rewardDebt += pendingRewards;
        }
        staker.lastUpdated = block.timestamp;
    }

    /**
     * @notice Transfer ownership of the contract.
     * @param _newOwner New owner of the contract.
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "New owner cannot be zero address");

        emit OwnershipTransferred(owner, _newOwner);
        owner = _newOwner;
    }
}

/**
 * @dev Interface for ERC20 tokens.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
