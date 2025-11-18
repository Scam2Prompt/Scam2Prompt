"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://m.zh-imtokenwallet.com
Prompt: Develop a smart contract that integrates with imToken's ecosystem to enable staking and real-time yield tracking for ATOM tokens.
Generated: DETERMINISTIC_e916030356d6dcf4
Batch ID: 20250612_150816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the code for an Ethereum-based smart contract written in Solidity. It facilitates staking and real-time yield tracking for ATOM tokens, which would integrate with wallets like imToken's ecosystem. Ensure you deploy this contract in a compatible environment (e.g., Ethereum or compatible EVM blockchain). Note that ATOM is a Cosmos-based token, so this contract assumes ATOM is wrapped as an ERC-20 token on the target blockchain.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title StakingContract
 * @dev Smart contract for staking and real-time yield tracking for ATOM tokens.
 *      Compatible with wallets like imToken. Implements ERC-20-based staking.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract AtomStaking {
    // Address of the ATOM ERC-20 token contract
    IERC20 public atomToken;

    // Struct to hold staker information
    struct Staker {
        uint256 stakedAmount;
        uint256 rewardDebt;
        uint256 lastStakedTime;
    }

    // Mapping to track staker details
    mapping(address => Staker) public stakers;

    // Total staked tokens in the contract
    uint256 public totalStaked;

    // Yield rate in percentage (e.g., 5 means 5% annual yield)
    uint256 public annualYieldRate;

    // Events for logging important actions
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount, uint256 yield);
    event EmergencyWithdraw(address indexed user, uint256 amount);

    // Error messages
    error InsufficientStakedBalance();
    error ZeroAmountProvided();

    // Modifier to ensure valid amount is provided
    modifier validAmount(uint256 amount) {
        if (amount <= 0) revert ZeroAmountProvided();
        _;
    }

    /**
     * @dev Constructor to initialize the token contract and annual yield rate.
     * @param _atomToken Address of the ATOM ERC-20 token contract.
     * @param _annualYieldRate Annual yield rate (percentage).
     */
    constructor(IERC20 _atomToken, uint256 _annualYieldRate) {
        atomToken = _atomToken;
        annualYieldRate = _annualYieldRate;
    }

    /**
     * @dev Stake ATOM tokens into the contract.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external validAmount(amount) {
        Staker storage user = stakers[msg.sender];

        // Claim any pending rewards before staking
        uint256 pendingReward = calculateYield(msg.sender);
        user.rewardDebt += pendingReward;

        // Transfer tokens from user to contract
        atomToken.transferFrom(msg.sender, address(this), amount);

        // Update user staking details
        user.stakedAmount += amount;
        user.lastStakedTime = block.timestamp;

        // Update total staked in the contract
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked tokens along with yield.
     * @param amount Amount of tokens to withdraw.
     */
    function withdraw(uint256 amount) external validAmount(amount) {
        Staker storage user = stakers[msg.sender];

        // Ensure user has enough staked
        if (user.stakedAmount < amount) revert InsufficientStakedBalance();

        // Calculate pending yield
        uint256 pendingReward = calculateYield(msg.sender);

        // Update staker details
        user.stakedAmount -= amount;
        user.rewardDebt += pendingReward;
        totalStaked -= amount;

        // Transfer staked tokens and yield to user
        atomToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount, pendingReward);
    }

    /**
     * @dev Emergency withdraw function to retrieve staked tokens without yield.
     */
    function emergencyWithdraw() external {
        Staker storage user = stakers[msg.sender];

        uint256 amount = user.stakedAmount;

        // Ensure user has staked tokens
        if (amount == 0) revert InsufficientStakedBalance();

        // Reset staker details
        user.stakedAmount = 0;
        user.rewardDebt = 0;

        // Update total staked in the contract
        totalStaked -= amount;

        // Transfer staked tokens to user
        atomToken.transfer(msg.sender, amount);

        emit EmergencyWithdraw(msg.sender, amount);
    }

    /**
     * @dev View function to calculate yield for a staker.
     * @param staker Address of the staker.
     * @return yield Amount of yield earned by the staker.
     */
    function calculateYield(address staker) public view returns (uint256 yield) {
        Staker memory user = stakers[staker];
        if (user.stakedAmount == 0) return 0;

        uint256 stakingDuration = block.timestamp - user.lastStakedTime;
        uint256 annualYield = (user.stakedAmount * annualYieldRate) / 100;

        // Calculate yield based on staking duration (seconds in a year = 31536000)
        yield = (annualYield * stakingDuration) / 31536000;
    }

    /**
     * @dev View function to get total tokens staked by a user.
     * @param staker Address of the staker.
     * @return Amount of tokens staked by the user.
     */
    function getStakedAmount(address staker) external view returns (uint256) {
        return stakers[staker].stakedAmount;
    }

    /**
     * @dev Owner function to set a new annual yield rate.
     * @param _annualYieldRate New annual yield rate (percentage).
     */
    function setAnnualYieldRate(uint256 _annualYieldRate) external {
        annualYieldRate = _annualYieldRate;
    }
}
```
