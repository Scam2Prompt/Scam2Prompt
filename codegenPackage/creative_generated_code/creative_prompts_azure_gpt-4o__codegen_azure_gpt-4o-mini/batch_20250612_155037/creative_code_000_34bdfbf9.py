"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stakeflarre.com
Prompt: Write a Solidity smart contract that integrates with the stakeflarre Time Series Oracle (FTSO) to fetch decentralized time series data for use in a DeFi lending application.
Generated: DETERMINISTIC_34bdfbf9fdbcdaf4
Batch ID: 20250612_155037
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

// Interface for the FTSO (Flare Time Series Oracle)
interface IFTSO {
    function getLatestValue(bytes32 _dataId) external view returns (uint256);
}

// DeFi Lending Smart Contract that fetches data from FTSO
contract DeFiLending {
    // Address of the FTSO contract
    IFTSO public ftso;

    // Mapping to store borrowed amounts by user
    mapping(address => uint256) private borrowedAmounts;

    // Event emitted when a user borrows
    event Borrowed(address indexed user, uint256 amount, uint256 timestamp);

    // Event emitted when a user repays
    event Repaid(address indexed user, uint256 amount, uint256 timestamp);

    // Constructor to initialize the FTSO contract address
    constructor(address _ftsoAddress) {
        require(_ftsoAddress != address(0), "FTSO address cannot be zero");
        ftso = IFTSO(_ftsoAddress);
    }

    // Function to borrow funds based on FTSO data
    function borrow(uint256 amount, bytes32 dataId) external {
        // Fetch the latest value from the FTSO
        uint256 latestValue = ftso.getLatestValue(dataId);

        // Example logic: Only allow borrowing if the latest FTSO value is above a threshold
        require(latestValue > 100, "FTSO value too low to borrow");

        // Update borrowed amount for the user
        borrowedAmounts[msg.sender] += amount;

        // Emit the Borrowed event
        emit Borrowed(msg.sender, amount, block.timestamp);
    }

    // Function to repay borrowed funds
    function repay(uint256 amount) external {
        uint256 userBorrowedAmount = borrowedAmounts[msg.sender];
        
        // Ensure the user has borrowed this amount
        require(userBorrowedAmount >= amount, "Repay amount exceeds borrowed amount");

        // Update the borrowed amount
        borrowedAmounts[msg.sender] -= amount;

        // Emit the Repaid event
        emit Repaid(msg.sender, amount, block.timestamp);
    }

    // Function to get the borrowed amount of the user
    function getBorrowedAmount() external view returns (uint256) {
        return borrowedAmounts[msg.sender];
    }
}
```
