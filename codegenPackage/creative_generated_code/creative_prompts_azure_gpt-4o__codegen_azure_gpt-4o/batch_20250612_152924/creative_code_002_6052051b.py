"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tradecurvemarket-en.pages.dev
Prompt: Using Solidity, write a smart contract that integrates with the Tradecurve ecosystem to enable users to stake TCRV tokens and receive stablecoin rewards.
Generated: DETERMINISTIC_6052051bedafa777
Batch ID: 20250612_152924
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
 * @title Tradecurve Staking Contract
 * @notice This contract allows users to stake TCRV tokens and receive stablecoin rewards.
 * @author Tradecurve Development Team
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

contract TradecurveStaking {
    // Address of the TCRV token contract
    IERC20 public immutable TCRV;

    // Address of the stablecoin token contract (used for rewards)
    IERC20 public immutable stablecoin;

    // Owner of the contract
    address public owner;

    // Struct to store user staking information
    struct Staker {
        uint256 amountStaked;
        uint256 rewardDebt;
    }

    // Mapping to store staking details of each user
    mapping(address => Staker) public stakers;

    // Total tokens staked in the contract
    uint256 public totalStaked;

    // Reward rate per token staked (e.g. 1 TCRV -> 0.01 stablecoin per block)
    uint256 public rewardRatePerBlock;

    // Last block at which rewards were distributed
    uint256 public lastRewardBlock;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 rewardAmount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    constructor(
        address _TCRV,
        address _stablecoin,
        uint256 _rewardRatePerBlock
    ) {
        require(_TCRV != address(0), "Invalid TCRV address");
        require(_stablecoin != address(0), "Invalid stablecoin address");

        TCRV = IERC20(_TCRV);
        stablecoin = IERC20(_stablecoin);
        rewardRatePerBlock = _rewardRatePerBlock;
        owner = msg.sender;
    }

    /**
     * @notice Allows users to stake TCRV tokens in the contract.
     * @param _amount Amount of TCRV tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Transfer TCRV tokens from user to contract
        require(TCRV.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        // Calculate pending rewards for the user
        _updateRewards(msg.sender);

        // Update user staking data
        stakers[msg.sender].amountStaked += _amount;

        // Update total staked tokens
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Allows users to unstake their TCRV tokens and claim rewards.
     * @param _amount Amount of TCRV tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Unstake amount must be greater than zero");
        require(stakers[msg.sender].amountStaked >= _amount, "Insufficient staked balance");

        // Calculate pending rewards for the user
        _updateRewards(msg.sender);

        // Update user staking data
        stakers[msg.sender].amountStaked -= _amount;

        // Update total staked tokens
        totalStaked -= _amount;

        // Transfer TCRV tokens back to the user
        require(TCRV.transfer(msg.sender, _amount), "Transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Claims accumulated stablecoin rewards for the user.
     */
    function claimRewards() external {
        // Calculate pending rewards for the user
        _updateRewards(msg.sender);

        uint256 rewardAmount = stakers[msg.sender].rewardDebt;
        require(rewardAmount > 0, "No rewards available");

        // Reset the user's reward debt
        stakers[msg.sender].rewardDebt = 0;

        // Transfer stablecoins to the user
        require(stablecoin.transfer(msg.sender, rewardAmount), "Transfer failed");

        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    /**
     * @notice Updates reward calculations and ensures proper accounting.
     * @param _user Address of the user whose rewards are being updated.
     */
    function _updateRewards(address _user) internal {
        if (totalStaked > 0) {
            uint256 blocksSinceLastReward = block.number - lastRewardBlock;
            uint256 totalReward = blocksSinceLastReward * rewardRatePerBlock * totalStaked;

            // Update last reward block
            lastRewardBlock = block.number;

            // Distribute rewards proportionally to user's stake
            uint256 userShare = (stakers[_user].amountStaked * totalReward) / totalStaked;
            stakers[_user].rewardDebt += userShare;
        } else {
            lastRewardBlock = block.number;
        }
    }

    /**
     * @notice Updates the reward rate per block. Can only be called by the owner.
     * @param _newRewardRate New reward rate per block.
     */
    function setRewardRate(uint256 _newRewardRate) external onlyOwner {
        rewardRatePerBlock = _newRewardRate;
    }

    /**
     * @notice Withdraws tokens from the contract in case of emergency. Can only be called by the owner.
     * @param _token Address of the token to withdraw.
     * @param _amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(address _token, uint256 _amount) external onlyOwner {
        require(IERC20(_token).transfer(owner, _amount), "Transfer failed");
    }
}
```
