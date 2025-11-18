"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memes-index.pages.dev
Prompt: Generate a Solidity contract for a decentralized meme coin index fund that tracks the performance of indices like "Meme MidCap Index" and "Meme Frenzy Index."
Generated: DETERMINISTIC_c19719688242bd94
Batch ID: 20250612_145633
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Decentralized Meme Coin Index Fund
 * @dev This contract allows users to invest in a fund that tracks the performance of meme coin indices.
 */
contract MemeCoinIndexFund is Ownable {
    using SafeMath for uint256;

    // Struct to represent an investment
    struct Investment {
        uint256 amount;
        uint256 index;
    }

    // Mapping of investor addresses to their investments
    mapping(address => Investment) private investments;

    // Total funds in the contract
    uint256 public totalFunds;

    // Index performance tracking (mock values for simplicity)
    mapping(uint256 => uint256) public indexPerformance; // index ID => performance value

    // Events
    event Invested(address indexed investor, uint256 amount, uint256 index);
    event Withdrawn(address indexed investor, uint256 amount);
    event IndexUpdated(uint256 index, uint256 performance);

    constructor() {
        // Initialize mock indices performance
        indexPerformance[1] = 100; // Meme MidCap Index
        indexPerformance[2] = 200; // Meme Frenzy Index
    }

    /**
     * @dev Invest in a meme coin index.
     * @param index The index to invest in (1 for Meme MidCap, 2 for Meme Frenzy).
     */
    function invest(uint256 index) external payable {
        require(index == 1 || index == 2, "Invalid index");
        require(msg.value > 0, "Investment amount must be greater than 0");

        // Update investor's investment
        investments[msg.sender] = Investment({
            amount: investments[msg.sender].amount.add(msg.value),
            index: index
        });

        // Update total funds
        totalFunds = totalFunds.add(msg.value);

        emit Invested(msg.sender, msg.value, index);
    }

    /**
     * @dev Withdraw the invested amount.
     */
    function withdraw() external {
        Investment memory investment = investments[msg.sender];
        require(investment.amount > 0, "No investment to withdraw");

        // Calculate the amount to withdraw based on index performance
        uint256 withdrawalAmount = calculateWithdrawalAmount(investment);

        // Reset the investor's investment
        investments[msg.sender] = Investment(0, 0);
        totalFunds = totalFunds.sub(investment.amount);

        // Transfer the funds back to the investor
        (bool success, ) = msg.sender.call{value: withdrawalAmount}("");
        require(success, "Transfer failed");

        emit Withdrawn(msg.sender, withdrawalAmount);
    }

    /**
     * @dev Calculate the withdrawal amount based on index performance.
     * @param investment The investor's investment details.
     * @return The calculated withdrawal amount.
     */
    function calculateWithdrawalAmount(Investment memory investment) internal view returns (uint256) {
        uint256 performance = indexPerformance[investment.index];
        return investment.amount.mul(performance).div(100); // Assume performance is a percentage
    }

    /**
     * @dev Update the performance of an index.
     * @param index The index to update.
     * @param performance The new performance value.
     */
    function updateIndexPerformance(uint256 index, uint256 performance) external onlyOwner {
        require(index == 1 || index == 2, "Invalid index");
        indexPerformance[index] = performance;

        emit IndexUpdated(index, performance);
    }

    /**
     * @dev Retrieve the investment details of an investor.
     * @param investor The address of the investor.
     * @return The amount and index of the investment.
     */
    function getInvestmentDetails(address investor) external view returns (uint256 amount, uint256 index) {
        Investment memory investment = investments[investor];
        return (investment.amount, investment.index);
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {
        revert("Direct Ether transfer not allowed. Use invest function.");
    }
}
```
