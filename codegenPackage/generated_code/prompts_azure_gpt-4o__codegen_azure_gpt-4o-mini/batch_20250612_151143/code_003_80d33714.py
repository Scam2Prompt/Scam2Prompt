"""
Generated Code Metadata:
========================
Original URL: https://buy-dogepreneur.pages.dev
Prompt: Write a smart contract in Solidity for tokenizing rental properties on the BNB Smart Chain, ensuring it includes functionality for distributing rental income to token holders.
Generated: DETERMINISTIC_80d33714a240a8bd
Batch ID: 20250612_151143
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

// Importing OpenZeppelin's ERC20 implementation for token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// RentalPropertyToken is an ERC20 token that represents ownership in rental properties
contract RentalPropertyToken is ERC20, Ownable {
    // Mapping to track rental income distribution
    mapping(address => uint256) public rentalIncome;

    // Total rental income collected
    uint256 public totalRentalIncome;

    // Event emitted when rental income is distributed
    event RentalIncomeDistributed(uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1 million tokens
    }

    // Function to distribute rental income to token holders
    function distributeRentalIncome() external payable onlyOwner {
        require(msg.value > 0, "No rental income to distribute");

        // Calculate the rental income per token
        uint256 incomePerToken = msg.value / totalSupply();

        // Distribute rental income to each token holder
        for (uint256 i = 0; i < totalSupply(); i++) {
            address holder = address(uint160(i)); // Convert index to address
            uint256 holderBalance = balanceOf(holder);
            if (holderBalance > 0) {
                rentalIncome[holder] += holderBalance * incomePerToken;
            }
        }

        totalRentalIncome += msg.value;
        emit RentalIncomeDistributed(msg.value);
    }

    // Function for token holders to claim their rental income
    function claimRentalIncome() external {
        uint256 income = rentalIncome[msg.sender];
        require(income > 0, "No rental income to claim");

        // Reset the rental income for the caller
        rentalIncome[msg.sender] = 0;

        // Transfer the rental income to the caller
        (bool success, ) = msg.sender.call{value: income}("");
        require(success, "Transfer failed");
    }

    // Function to withdraw any accidental Ether sent to the contract
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");

        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
