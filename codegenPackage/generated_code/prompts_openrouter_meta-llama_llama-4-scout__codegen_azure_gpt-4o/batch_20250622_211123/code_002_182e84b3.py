"""
Generated Code Metadata:
========================
Original URL: https://www.staderlabs.fi
Prompt: Design a smart contract on BNB Chain that integrates with Stader Labs' liquid staking solution, allowing users to stake BNB and earn rewards while maintaining liquidity.
Generated: DETERMINISTIC_182e84b33e30e2c4
Batch ID: 20250622_211123
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
 * @title LiquidStakingContract
 * @dev A smart contract that integrates with Stader Labs' liquid staking solution on the BNB Chain.
 * Allows users to stake BNB, earn rewards, and maintain liquidity.
 */
interface IStaderLiquidStaking {
    function stake() external payable;
    function getReward() external;
    function withdraw(uint256 amount) external;
}

contract LiquidStakingContract {
    // Address of the Stader Labs liquid staking contract
    address public staderLiquidStakingAddress;

    // Mapping to track user balances in the contract
    mapping(address => uint256) public userBalances;

    // Event emitted when a user stakes BNB
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user withdraws BNB
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user);

    /**
     * @dev Constructor to initialize the Stader Labs liquid staking contract address.
     * @param _staderLiquidStakingAddress Address of the Stader Labs liquid staking contract.
     */
    constructor(address _staderLiquidStakingAddress) {
        require(_staderLiquidStakingAddress != address(0), "Invalid staking contract address");
        staderLiquidStakingAddress = _staderLiquidStakingAddress;
    }

    /**
     * @dev Stake BNB into the Stader Labs liquid staking contract.
     * The user must send BNB along with the transaction.
     */
    function stakeBNB() external payable {
        require(msg.value > 0, "Must send BNB to stake");

        // Update user balance
        userBalances[msg.sender] += msg.value;

        // Interact with the Stader Labs liquid staking contract
        IStaderLiquidStaking(staderLiquidStakingAddress).stake{value: msg.value}();

        emit Staked(msg.sender, msg.value);
    }

    /**
     * @dev Withdraw staked BNB from the contract.
     * @param amount The amount of BNB to withdraw.
     */
    function withdrawBNB(uint256 amount) external {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(userBalances[msg.sender] >= amount, "Insufficient balance");

        // Update user balance
        userBalances[msg.sender] -= amount;

        // Interact with the Stader Labs liquid staking contract to withdraw
        IStaderLiquidStaking(staderLiquidStakingAddress).withdraw(amount);

        // Transfer BNB back to the user
        payable(msg.sender).transfer(amount);

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim staking rewards from the Stader Labs liquid staking contract.
     */
    function claimRewards() external {
        // Interact with the Stader Labs liquid staking contract to claim rewards
        IStaderLiquidStaking(staderLiquidStakingAddress).getReward();

        emit RewardsClaimed(msg.sender);
    }

    /**
     * @dev Fallback function to accept BNB deposits.
     */
    receive() external payable {
        revert("Use stakeBNB function to stake BNB");
    }

    /**
     * @dev Fallback function for non-existent function calls.
     */
    fallback() external payable {
        revert("Function not supported");
    }
}
```
