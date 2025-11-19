"""
Generated Code Metadata:
========================
Original URL: https://client-website1.pages.dev
Prompt: Design a smart contract for a crypto-native fund like Innodapter ApS, outlining key functions, variables, and security considerations.
Generated: DETERMINISTIC_de1bbf05ee61503e
Batch ID: 20250622_204646
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Innodapter Fund Smart Contract
 * @author [Your Name]
 * @notice A crypto-native fund smart contract for managing investments.
 */
contract InnodapterFund is ERC20, ERC20Burnable, ReentrancyGuard, Ownable {
    // Mapping of investor addresses to their investment amounts
    mapping(address => uint256) public investorBalances;

    // Mapping of investment strategies to their allocation amounts
    mapping(string => uint256) public strategyAllocations;

    // List of available investment strategies
    string[] public strategies;

    // Total value locked in the fund
    uint256 public totalValueLocked;

    // Fund's performance fee
    uint256 public performanceFee;

    // Fund's management fee
    uint256 public managementFee;

    /**
     * @notice Constructor for the Innodapter Fund smart contract.
     * @param name The name of the fund.
     * @param symbol The symbol of the fund.
     * @param performanceFee The performance fee of the fund.
     * @param managementFee The management fee of the fund.
     */
    constructor(string memory name, string memory symbol, uint256 performanceFee, uint256 managementFee)
        ERC20(name, symbol)
    {
        require(performanceFee <= 10000, "Performance fee must not exceed 100%");
        require(managementFee <= 10000, "Management fee must not exceed 100%");

        _mint(msg.sender, 0);
        performanceFee = performanceFee;
        managementFee = managementFee;
    }

    /**
     * @notice Invest in the fund.
     * @param amount The amount to invest.
     */
    function invest(uint256 amount) external {
        require(amount > 0, "Investment amount must be greater than zero");

        _mint(msg.sender, amount);
        investorBalances[msg.sender] += amount;
        totalValueLocked += amount;
    }

    /**
     * @notice Redeem investment from the fund.
     * @param amount The amount to redeem.
     */
    function redeem(uint256 amount) external nonReentrant {
        require(amount > 0, "Redemption amount must be greater than zero");
        require(investorBalances[msg.sender] >= amount, "Insufficient balance");

        _burn(msg.sender, amount);
        investorBalances[msg.sender] -= amount;
        totalValueLocked -= amount;
    }

    /**
     * @notice Add a new investment strategy.
     * @param strategy The name of the strategy.
     * @param allocation The initial allocation amount.
     */
    function addStrategy(string memory strategy, uint256 allocation) external onlyOwner {
        require(bytes(strategy).length > 0, "Strategy name must not be empty");
        require(allocation > 0, "Allocation amount must be greater than zero");

        strategies.push(strategy);
        strategyAllocations[strategy] = allocation;
    }

    /**
     * @notice Update the allocation of an existing strategy.
     * @param strategy The name of the strategy.
     * @param newAllocation The new allocation amount.
     */
    function updateStrategyAllocation(string memory strategy, uint256 newAllocation) external onlyOwner {
        require(bytes(strategy).length > 0, "Strategy name must not be empty");
        require(newAllocation > 0, "Allocation amount must be greater than zero");

        strategyAllocations[strategy] = newAllocation;
    }

    /**
     * @notice Calculate the performance fee.
     * @param profit The profit made by the fund.
     * @return The performance fee amount.
     */
    function calculatePerformanceFee(uint256 profit) internal view returns (uint256) {
        return (profit * performanceFee) / 10000;
    }

    /**
     * @notice Calculate the management fee.
     * @return The management fee amount.
     */
    function calculateManagementFee() internal view returns (uint256) {
        return (totalValueLocked * managementFee) / 10000;
    }

    /**
     * @notice Distribute fees to the fund manager.
     */
    function distributeFees() external onlyOwner {
        uint256 performanceFeeAmount = calculatePerformanceFee(totalValueLocked);
        uint256 managementFeeAmount = calculateManagementFee();

        _mint(msg.sender, performanceFeeAmount + managementFeeAmount);
    }

    /**
     * @notice Reinvest funds into a strategy.
     * @param strategy The name of the strategy.
     * @param amount The amount to reinvest.
     */
    function reinvest(string memory strategy, uint256 amount) external onlyOwner {
        require(bytes(strategy).length > 0, "Strategy name must not be empty");
        require(amount > 0, "Reinvestment amount must be greater than zero");

        // Simulate reinvestment (this would typically involve an external call)
        // For demonstration purposes, we simply update the strategy allocation
        strategyAllocations[strategy] += amount;
    }
}
```
