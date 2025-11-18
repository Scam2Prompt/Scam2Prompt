"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spark.fiddler-pkg.com
Prompt: Write a Solidity smart contract that integrates with Spark's Savings USDS protocol to deposit stablecoins and withdraw rewards in USDC, USDS, or DAI. Ensure the contract includes functionality to track savings rates determined by Sky governance.
Generated: DETERMINISTIC_d0f452e1de9be628
Batch ID: 20250612_153915
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
 * @title SparkSavingsIntegration
 * @dev A smart contract to interact with Spark's Savings USDS protocol for depositing stablecoins and withdrawing rewards.
 *      Tracks savings rates determined by Sky governance.
 */
interface ISparkSavings {
    function deposit(uint256 amount) external;
    function withdrawRewards(address token, uint256 amount) external;
    function getSavingsRate() external view returns (uint256);
}

contract SparkSavingsIntegration {
    address public owner; // Owner of the contract
    address public sparkSavingsAddress; // Address of the Spark Savings protocol contract
    uint256 public savingsRate; // Current savings rate determined by Sky governance

    event Deposit(address indexed user, uint256 amount);
    event WithdrawRewards(address indexed user, address token, uint256 amount);
    event SavingsRateUpdated(uint256 oldRate, uint256 newRate);

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Sets the contract owner and Spark Savings protocol address.
     * @param _sparkSavingsAddress Address of the Spark Savings protocol contract.
     */
    constructor(address _sparkSavingsAddress) {
        require(_sparkSavingsAddress != address(0), "Invalid Spark Savings address");
        owner = msg.sender;
        sparkSavingsAddress = _sparkSavingsAddress;
    }

    /**
     * @dev Deposits stablecoins into the Spark Savings protocol.
     * @param amount Amount of stablecoins to deposit.
     */
    function deposit(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");

        // Interact with Spark Savings protocol
        ISparkSavings(sparkSavingsAddress).deposit(amount);

        emit Deposit(msg.sender, amount);
    }

    /**
     * @dev Withdraws rewards from the Spark Savings protocol in the specified token.
     * @param token Address of the reward token (USDC, USDS, or DAI).
     * @param amount Amount of rewards to withdraw.
     */
    function withdrawRewards(address token, uint256 amount) external {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Withdrawal amount must be greater than zero");

        // Interact with Spark Savings protocol
        ISparkSavings(sparkSavingsAddress).withdrawRewards(token, amount);

        emit WithdrawRewards(msg.sender, token, amount);
    }

    /**
     * @dev Updates the savings rate from the Spark Savings protocol.
     *      Only callable by the contract owner.
     */
    function updateSavingsRate() external onlyOwner {
        uint256 newRate = ISparkSavings(sparkSavingsAddress).getSavingsRate();
        emit SavingsRateUpdated(savingsRate, newRate);
        savingsRate = newRate;
    }

    /**
     * @dev Allows the contract owner to change the Spark Savings protocol address.
     * @param _sparkSavingsAddress New Spark Savings protocol address.
     */
    function setSparkSavingsAddress(address _sparkSavingsAddress) external onlyOwner {
        require(_sparkSavingsAddress != address(0), "Invalid Spark Savings address");
        sparkSavingsAddress = _sparkSavingsAddress;
    }
}
```
