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

/**
 * @title PassiveInvestIncome
 * @dev A smart contract for managing cryptocurrency investments with insured deposits
 *      and daily profit distribution.
 */
contract PassiveInvestIncome {
    // Owner of the contract
    address public owner;

    // Insurance fund to secure deposits
    uint256 public insuranceFund;

    // Struct to store investor details
    struct Investor {
        uint256 depositedAmount; // Amount deposited by the investor
        uint256 lastProfitTimestamp; // Timestamp of the last profit calculation
    }

    // Mapping to store investor data
    mapping(address => Investor) public investors;

    // Daily profit percentage (e.g., 1% = 100, 0.5% = 50)
    uint256 public dailyProfitRate;

    // Event declarations
    event Deposit(address indexed investor, uint256 amount);
    event Withdraw(address indexed investor, uint256 amount);
    event ProfitDistributed(address indexed investor, uint256 profit);

    /**
     * @dev Modifier to check if the caller is the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with a daily profit rate.
     * @param _dailyProfitRate Daily profit rate in basis points (1% = 100).
     */
    constructor(uint256 _dailyProfitRate) {
        require(_dailyProfitRate > 0, "Daily profit rate must be greater than 0");
        owner = msg.sender;
        dailyProfitRate = _dailyProfitRate;
    }

    /**
     * @dev Function to deposit funds into the contract.
     */
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than 0");

        // Update investor details
        Investor storage investor = investors[msg.sender];
        if (investor.depositedAmount > 0) {
            // Distribute pending profits before adding new deposit
            _distributeProfit(msg.sender);
        }
        investor.depositedAmount += msg.value;
        investor.lastProfitTimestamp = block.timestamp;

        // Add to insurance fund
        insuranceFund += (msg.value / 10); // 10% of deposit goes to insurance fund

        emit Deposit(msg.sender, msg.value);
    }

    /**
     * @dev Function to withdraw deposited funds and profits.
     */
    function withdraw(uint256 amount) external {
        Investor storage investor = investors[msg.sender];
        require(investor.depositedAmount > 0, "No funds to withdraw");
        require(amount <= investor.depositedAmount, "Withdraw amount exceeds balance");

        // Distribute pending profits
        _distributeProfit(msg.sender);

        // Update investor details
        investor.depositedAmount -= amount;

        // Transfer the specified amount to the investor
        payable(msg.sender).transfer(amount);

        emit Withdraw(msg.sender, amount);
    }

    /**
     * @dev Distribute daily profits to a specific investor.
     * @param investorAddress The address of the investor.
     */
    function _distributeProfit(address investorAddress) internal {
        Investor storage investor = investors[investorAddress];

        // Calculate the number of days since the last profit distribution
        uint256 daysElapsed = (block.timestamp - investor.lastProfitTimestamp) / 1 days;
        if (daysElapsed > 0 && investor.depositedAmount > 0) {
            uint256 profit = (investor.depositedAmount * dailyProfitRate / 10000) * daysElapsed;

            // Ensure insurance fund can cover at least the profit (security measure)
            require(profit <= address(this).balance - insuranceFund, "Insufficient funds for profit distribution");

            // Transfer profit to the investor
            payable(investorAddress).transfer(profit);

            // Update the last profit timestamp
            investor.lastProfitTimestamp = block.timestamp;

            emit ProfitDistributed(investorAddress, profit);
        }
    }

    /**
     * @dev Allows the owner to adjust the daily profit rate.
     * @param _newRate The new daily profit rate in basis points.
     */
    function setDailyProfitRate(uint256 _newRate) external onlyOwner {
        require(_newRate > 0, "Daily profit rate must be greater than 0");
        dailyProfitRate = _newRate;
    }

    /**
     * @dev Allows the owner to withdraw the insurance fund.
     * @param amount The amount to withdraw from the insurance fund.
     */
    function withdrawInsuranceFund(uint256 amount) external onlyOwner {
        require(amount <= insuranceFund, "Amount exceeds insurance fund balance");
        insuranceFund -= amount;
        payable(owner).transfer(amount);
    }

    /**
     * @dev Fallback function to accept Ether directly.
     */
    receive() external payable {}
}
```
