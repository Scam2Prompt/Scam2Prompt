"""
Generated Code Metadata:
========================
Original URL: https://eeryy5e4y5e4rey5r.pages.dev
Prompt: Create a smart contract in Solidity that facilitates clean energy transactions, inspired by the Nebra project in the Dione Protocol ecosystem.
Generated: DETERMINISTIC_31e87a147455ba00
Batch ID: 20250612_152000
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

/// @title Clean Energy Transaction Smart Contract
/// @author Your Name
/// @notice This contract facilitates transactions for clean energy credits
/// @dev The contract allows users to buy and sell clean energy credits securely

contract CleanEnergyMarket {
    // Struct to represent a clean energy credit
    struct EnergyCredit {
        uint256 id; // Unique identifier for the credit
        address owner; // Current owner of the credit
        uint256 amount; // Amount of energy represented by the credit (in kWh)
        bool isForSale; // Indicates if the credit is available for sale
        uint256 price; // Sale price of the credit in wei
    }

    // Mapping from credit ID to EnergyCredit
    mapping(uint256 => EnergyCredit) public energyCredits;
    // Counter for generating unique credit IDs
    uint256 public creditCounter;

    // Event emitted when a credit is created
    event CreditCreated(uint256 indexed creditId, address indexed owner, uint256 amount);
    // Event emitted when a credit is put up for sale
    event CreditForSale(uint256 indexed creditId, uint256 price);
    // Event emitted when a credit is sold
    event CreditSold(uint256 indexed creditId, address indexed buyer, uint256 price);

    /// @notice Creates a new clean energy credit
    /// @param _amount The amount of energy represented by the credit
    function createCredit(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        creditCounter++;
        energyCredits[creditCounter] = EnergyCredit({
            id: creditCounter,
            owner: msg.sender,
            amount: _amount,
            isForSale: false,
            price: 0
        });

        emit CreditCreated(creditCounter, msg.sender, _amount);
    }

    /// @notice Puts a clean energy credit up for sale
    /// @param _creditId The ID of the credit to sell
    /// @param _price The sale price in wei
    function putCreditForSale(uint256 _creditId, uint256 _price) external {
        EnergyCredit storage credit = energyCredits[_creditId];
        require(credit.owner == msg.sender, "Only the owner can sell the credit");
        require(!credit.isForSale, "Credit is already for sale");
        require(_price > 0, "Price must be greater than zero");

        credit.isForSale = true;
        credit.price = _price;

        emit CreditForSale(_creditId, _price);
    }

    /// @notice Purchases a clean energy credit
    /// @param _creditId The ID of the credit to purchase
    function purchaseCredit(uint256 _creditId) external payable {
        EnergyCredit storage credit = energyCredits[_creditId];
        require(credit.isForSale, "Credit is not for sale");
        require(msg.value >= credit.price, "Insufficient funds sent");

        // Transfer ownership of the credit
        address previousOwner = credit.owner;
        credit.owner = msg.sender;
        credit.isForSale = false;
        credit.price = 0;

        // Transfer funds to the previous owner
        payable(previousOwner).transfer(msg.value);

        emit CreditSold(_creditId, msg.sender, msg.value);
    }

    /// @notice Retrieves the details of a clean energy credit
    /// @param _creditId The ID of the credit to retrieve
    /// @return The details of the energy credit
    function getCreditDetails(uint256 _creditId) external view returns (EnergyCredit memory) {
        return energyCredits[_creditId];
    }
}
```
