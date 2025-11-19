"""
Generated Code Metadata:
========================
Original URL: https://buy-dogepreneur.pages.dev
Prompt: Generate a smart contract code in Solidity that enables the creation and management of RWA Tokens, like Dogepreneur, for real estate investment and rental income generation on a blockchain platform.
Generated: DETERMINISTIC_9436f1ee2293700b
Batch ID: 20250622_204615
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// RWA Token Contract for Real Estate Investment
contract RWAToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Mapping to track rental income for each property
    mapping(uint256 => uint256) private rentalIncome;
    // Mapping to track property ownership
    mapping(uint256 => address) private propertyOwners;

    // Event emitted when rental income is distributed
    event RentalIncomeDistributed(uint256 propertyId, uint256 amount);

    // Constructor to initialize the token
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals());
    }

    // Function to create a new property and assign ownership
    function createProperty(uint256 propertyId) external onlyOwner {
        require(propertyOwners[propertyId] == address(0), "Property already exists");
        propertyOwners[propertyId] = msg.sender;
    }

    // Function to distribute rental income to property owners
    function distributeRentalIncome(uint256 propertyId, uint256 amount) external onlyOwner {
        require(propertyOwners[propertyId] != address(0), "Property does not exist");
        require(amount > 0, "Amount must be greater than zero");

        // Update rental income for the property
        rentalIncome[propertyId] = rentalIncome[propertyId].add(amount);
        emit RentalIncomeDistributed(propertyId, amount);
    }

    // Function for property owners to claim their rental income
    function claimRentalIncome(uint256 propertyId) external {
        require(propertyOwners[propertyId] == msg.sender, "You are not the owner of this property");
        
        uint256 income = rentalIncome[propertyId];
        require(income > 0, "No rental income available");

        // Reset rental income after claiming
        rentalIncome[propertyId] = 0;

        // Transfer rental income to the property owner
        payable(msg.sender).transfer(income);
    }

    // Function to receive Ether (for rental income distribution)
    receive() external payable {}

    // Function to withdraw contract balance (only owner)
    function withdraw(uint256 amount) external onlyOwner {
        require(amount <= address(this).balance, "Insufficient balance");
        payable(msg.sender).transfer(amount);
    }

    // Function to get rental income for a property
    function getRentalIncome(uint256 propertyId) external view returns (uint256) {
        return rentalIncome[propertyId];
    }

    // Function to get property owner
    function getPropertyOwner(uint256 propertyId) external view returns (address) {
        return propertyOwners[propertyId];
    }
}
```
