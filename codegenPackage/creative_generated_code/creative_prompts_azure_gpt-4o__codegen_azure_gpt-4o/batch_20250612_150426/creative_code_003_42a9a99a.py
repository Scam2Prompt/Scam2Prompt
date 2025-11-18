"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://finveracapitals.com
Prompt: Create a smart contract in Solidity for managing instant withdrawals and profit distributions for investment plans like those offered by Finvera Capitals.
Generated: DETERMINISTIC_42a9a99ad3da25c3
Batch ID: 20250612_150426
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
 * @title InvestmentManager
 * @dev A smart contract for managing investment plans with instant withdrawals
 *      and profit distributions for investors.
 */
contract InvestmentManager {
    // Owner of the contract
    address public owner;

    // Total funds available in the contract
    uint256 public totalFunds;

    // Struct to represent an investor
    struct Investor {
        uint256 balance; // Invested balance
        uint256 profit;  // Accumulated profit
    }

    // Mapping to track investors' data
    mapping(address => Investor) public investors;

    // Events for transparency
    event InvestmentMade(address indexed investor, uint256 amount);
    event Withdrawal(address indexed investor, uint256 amount);
    event ProfitDistributed(uint256 totalProfit);

    /**
     * @dev Modifier to restrict access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the contract and set the owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to allow users to invest in the plan.
     * @notice The value sent with this function will be added to the investor's balance.
     */
    function invest() external payable {
        require(msg.value > 0, "Investment amount must be greater than zero");

        // Update the investor's balance
        investors[msg.sender].balance += msg.value;

        // Update the total funds in the contract
        totalFunds += msg.value;

        emit InvestmentMade(msg.sender, msg.value);
    }

    /**
     * @dev Function to allow investors to withdraw their profits instantly.
     */
    function withdrawProfit() external {
        // Check if the investor has any profit to withdraw
        Investor storage investor = investors[msg.sender];
        uint256 profit = investor.profit;
        require(profit > 0, "No profit available to withdraw");

        // Update the investor's profit balance
        investor.profit = 0;

        // Send the profit to the investor
        (bool success, ) = msg.sender.call{value: profit}("");
        require(success, "Transfer failed");

        emit Withdrawal(msg.sender, profit);
    }

    /**
     * @dev Function to distribute profits among all investors.
     * @param totalProfit The total amount of profit to be distributed.
     * @notice This function can only be called by the owner.
     */
    function distributeProfits(uint256 totalProfit) external onlyOwner {
        require(totalProfit > 0, "Profit amount must be greater than zero");
        require(totalProfit <= address(this).balance - totalFunds, "Insufficient balance for profit distribution");

        // Distribute profits proportionally based on the investor's balance
        for (address addr : _getAllInvestors()) {
            Investor storage investor = investors[addr];
            uint256 share = (investor.balance * totalProfit) / totalFunds;
            investor.profit += share;
        }

        emit ProfitDistributed(totalProfit);
    }

    /**
     * @dev Function to get a list of all investors.
     * @notice This function is private and used only internally.
     */
    function _getAllInvestors() private view returns (address[] memory) {
        // Implementation for dynamically tracking all investor addresses is omitted for simplicity.
        // In an actual implementation, you would need to maintain a list of all investor addresses.
        revert("Not implemented");
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {
        totalFunds += msg.value;
    }
}
```
