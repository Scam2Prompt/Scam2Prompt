"""
Generated Code Metadata:
========================
Original URL: https://geoins.ru
Prompt: Describe the role of the QI token in the QiDao protocol, including its use in governance and staking.
Generated: DETERMINISTIC_70300ec67f4ee809
Batch ID: 20250622_212427
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
 * @title QiDao Protocol QI Token Interface
 * @dev Interface for the QI token functionality in QiDao protocol
 */
interface IQiToken {
    /**
     * @notice Get the balance of QI tokens for an account
     * @param account The address to query balance for
     * @return The QI token balance
     */
    function balanceOf(address account) external view returns (uint256);

    /**
     * @notice Transfer QI tokens to another address
     * @param recipient The address to transfer to
     * @param amount The amount of QI tokens to transfer
     * @return Boolean indicating success
     */
    function transfer(address recipient, uint256 amount) external returns (bool);

    /**
     * @notice Approve another address to spend QI tokens
     * @param spender The address being approved
     * @param amount The amount of QI tokens approved
     * @return Boolean indicating success
     */
    function approve(address spender, uint256 amount) external returns (bool);

    /**
     * @notice Get the remaining allowance for a spender
     * @param owner The address owning the tokens
     * @param spender The address allowed to spend
     * @return The remaining allowance
     */
    function allowance(address owner, address spender) external view returns (uint256);

    /**
     * @notice Transfer QI tokens from one address to another using allowance
     * @param sender The address sending the tokens
     * @param recipient The address receiving the tokens
     * @param amount The amount of QI tokens to transfer
     * @return Boolean indicating success
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    // Governance functions
    /**
     * @notice Delegate voting power to another address
     * @param delegatee The address to delegate votes to
     */
    function delegate(address delegatee) external;

    /**
     * @notice Get the current votes for an account
     * @param account The address to query votes for
     * @return The number of current votes
     */
    function getCurrentVotes(address account) external view returns (uint256);

    // Staking functions
    /**
     * @notice Stake QI tokens to earn rewards
     * @param amount The amount of QI tokens to stake
     */
    function stake(uint256 amount) external;

    /**
     * @notice Unstake QI tokens
     * @param amount The amount of QI tokens to unstake
     */
    function unstake(uint256 amount) external;

    /**
     * @notice Claim staking rewards
     */
    function claimRewards() external;

    /**
     * @notice Get the staked balance for an account
     * @param account The address to query staked balance for
     * @return The amount of staked QI tokens
     */
    function stakedBalanceOf(address account) external view returns (uint256);

    /**
     * @notice Get the total staked QI tokens
     * @return The total amount of staked QI tokens
     */
    function totalStaked() external view returns (uint256);

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event DelegateChanged(address indexed delegator, address indexed fromDelegate, address indexed toDelegate);
    event DelegateVotesChanged(address indexed delegate, uint256 previousBalance, uint256 newBalance);
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
}
```
