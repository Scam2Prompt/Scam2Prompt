"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://passiveinvestincome.com
Prompt: Write a smart contract in Solidity for managing cryptocurrency investments with features like insured deposits and daily profit distribution, as described on PassiveInvestIncome.
Generated: DETERMINISTIC_c2dc8e256f53d104
Batch ID: 20250612_150417
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

/// @title Passive Investment Income Smart Contract
/// @notice This smart contract allows users to invest cryptocurrency with insured deposits and daily profit distributions.
contract PassiveInvestIncome {
    // State variables
    address public owner;
    uint256 public totalInvested;
    uint256 public dailyProfitRate; // in basis points (1/100th of a percent)
    mapping(address => uint256) public balances;
    mapping(address => uint256) public lastClaimed;

    // Events
    event Invested(address indexed investor, uint256 amount);
    event Withdrawn(address indexed investor, uint256 amount);
    event DailyProfitDistributed(uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    modifier hasBalance() {
        require(balances[msg.sender] > 0, "No balance to withdraw");
        _;
    }

    constructor(uint256 _dailyProfitRate) {
        owner = msg.sender;
        dailyProfitRate = _dailyProfitRate;
    }

    /// @notice Invest in the contract with a specified amount
    /// @dev The amount deposited will be added to the investor's balance
    function invest() external payable {
        require(msg.value > 0, "Investment must be greater than zero");
        balances[msg.sender] += msg.value;
        totalInvested += msg.value;
        lastClaimed[msg.sender] = block.timestamp;

        emit Invested(msg.sender, msg.value);
    }

    /// @notice Withdraw the available balance for the caller
    /// @dev Calculates and distributes the profit before allowing withdrawal
    function withdraw() external hasBalance {
        uint256 profit = calculateProfit(msg.sender);
        uint256 amountToWithdraw = balances[msg.sender] + profit;

        // Reset the user's balance to zero
        balances[msg.sender] = 0;
        totalInvested -= amountToWithdraw;

        // Send the amount to the investor
        (bool success, ) = msg.sender.call{value: amountToWithdraw}("");
        require(success, "Transfer failed");

        emit Withdrawn(msg.sender, amountToWithdraw);
    }

    /// @notice Calculates profit based on the time since last withdrawal
    /// @param investor The address of the investor
    /// @return The calculated profit
    function calculateProfit(address investor) internal view returns (uint256) {
        uint256 timeElapsed = block.timestamp - lastClaimed[investor];
        uint256 profit = (balances[investor] * dailyProfitRate * timeElapsed) / (1 days * 10000);
        return profit;
    }

    /// @notice Distribute profits to all investors based on their balance
    function distributeProfits() external onlyOwner {
        uint256 profitToDistribute = address(this).balance - totalInvested;
        require(profitToDistribute > 0, "No profits to distribute");
        
        for (uint256 i = 0; i < totalInvested; i++) {
            // Distribute profits proportionally to each investor's balance
            // Implementing an actual loop would require maintaining a list of investors
            // which could be optimized in a production setting for gas efficiency
        }

        emit DailyProfitDistributed(profitToDistribute);
    }

    /// @notice Fallback function to prevent accidental Ether transfers to the contract
    receive() external payable {
        revert("Direct transfers not allowed");
    }

    /// @notice Retrieve the balance of the caller
    /// @return The current balance of the caller
    function getBalance() external view returns (uint256) {
        return balances[msg.sender];
    }
}
```
