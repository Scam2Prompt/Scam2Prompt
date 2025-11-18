"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://roostcoinclaim.pages.dev
Prompt: Write a Solidity contract that mimics the presale breakdown of $ROOST, ensuring 50% of the raise goes to LP and 50% to expenses, development, and distribution.
Generated: DETERMINISTIC_90d6d56275fd9e10
Batch ID: 20250612_152710
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

// Importing OpenZeppelin's Ownable contract for ownership management
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for the $ROOST presale
contract RoostPresale is Ownable {
    // Event emitted when funds are raised
    event FundsRaised(address indexed investor, uint256 amount);
    event FundsAllocated(uint256 lpAmount, uint256 expensesAmount);

    // State variables
    uint256 public totalRaised; // Total amount raised during the presale
    uint256 public lpAllocation; // Amount allocated to liquidity pool
    uint256 public expenseAllocation; // Amount allocated to expenses

    // Mapping to track investments
    mapping(address => uint256) public investments;

    // Modifier to ensure the presale is active
    modifier presaleActive() {
        require(totalRaised < hardCap, "Presale has ended");
        _;
    }

    // Hard cap for the presale
    uint256 public hardCap = 100 ether; // Presale hard cap set to 100 ETH

    // Function to invest in the presale
    function invest() external payable presaleActive {
        require(msg.value > 0, "Investment must be greater than zero");
        require(totalRaised + msg.value <= hardCap, "Investment exceeds hard cap");

        // Update total raised amount and individual investment
        totalRaised += msg.value;
        investments[msg.sender] += msg.value;

        emit FundsRaised(msg.sender, msg.value);
    }

    // Function to finalize the presale
    function finalizePresale() external onlyOwner {
        require(totalRaised > 0, "No funds raised");

        // Calculate allocations
        lpAllocation = totalRaised / 2; // 50% to liquidity pool
        expenseAllocation = totalRaised / 2; // 50% to expenses

        // Transfer allocations (note: replace with actual LP address and expense handling)
        payable(owner()).transfer(expenseAllocation); // Send funds to owner for expenses

        // Emit event to signal that funds have been allocated
        emit FundsAllocated(lpAllocation, expenseAllocation);
    }

    // Function to withdraw remaining funds in case of emergency
    function emergencyWithdraw() external onlyOwner {
        require(totalRaised == 0, "Funds already raised, cannot withdraw");

        // Transfer remaining balance to the owner
        payable(owner()).transfer(address(this).balance);
    }

    // Function to check contract balance
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }

    // Fallback function to accept ether
    receive() external payable {
        invest(); // Allow direct investments via the fallback function
    }
}
```
