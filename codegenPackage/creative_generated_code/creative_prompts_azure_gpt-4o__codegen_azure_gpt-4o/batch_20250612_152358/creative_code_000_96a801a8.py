"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everllodge-claim.pages.dev
Prompt: Write a smart contract in Solidity for fractional ownership of vacation homes, inspired by the Everlodge platform's co-ownership model on the Ethereum blockchain.
Generated: DETERMINISTIC_96a801a88b27c85f
Batch ID: 20250612_152358
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
 * @title FractionalOwnership
 * @dev A smart contract for fractional ownership of vacation homes. Inspired by the Everlodge platform's co-ownership model.
 */
contract FractionalOwnership {
    // Struct representing a vacation home
    struct VacationHome {
        string name;           // Name of the vacation home
        uint256 price;         // Total price of the home in wei
        uint256 fractionalCost; // Cost per fraction in wei
        uint256 fractionsSold; // Number of fractions sold
        uint256 totalFractions; // Total fractions available
        address[] owners;      // Array of owners (fractional investors)
    }

    // Mapping from home ID to VacationHome struct
    mapping(uint256 => VacationHome) public vacationHomes;

    // Mapping from home ID to owner address to number of fractions owned
    mapping(uint256 => mapping(address => uint256)) public ownership;

    // Event emitted when a new vacation home is added
    event VacationHomeAdded(
        uint256 indexed homeId,
        string name,
        uint256 price,
        uint256 fractionalCost,
        uint256 totalFractions
    );

    // Event emitted when a fraction is purchased
    event FractionPurchased(
        uint256 indexed homeId,
        address indexed buyer,
        uint256 fractionsOwned
    );

    // Modifier to check if the home exists
    modifier homeExists(uint256 homeId) {
        require(vacationHomes[homeId].totalFractions > 0, "Vacation home does not exist");
        _;
    }

    /**
     * @dev Adds a new vacation home to the contract.
     * @param homeId Unique identifier for the vacation home.
     * @param name Name of the vacation home.
     * @param price Total price of the vacation home in wei.
     * @param totalFractions Number of fractions available for ownership.
     */
    function addVacationHome(
        uint256 homeId,
        string memory name,
        uint256 price,
        uint256 totalFractions
    ) public {
        require(vacationHomes[homeId].totalFractions == 0, "Home ID already exists");
        require(totalFractions > 0, "Total fractions must be greater than zero");

        uint256 fractionalCost = price / totalFractions;

        require(fractionalCost > 0, "Fractional cost must be greater than zero");

        vacationHomes[homeId] = VacationHome({
            name: name,
            price: price,
            fractionalCost: fractionalCost,
            fractionsSold: 0,
            totalFractions: totalFractions,
            owners: new address[](0)
        });

        emit VacationHomeAdded(homeId, name, price, fractionalCost, totalFractions);
    }

    /**
     * @dev Allows a user to purchase fractional ownership of a vacation home.
     * @param homeId Unique identifier for the vacation home.
     * @param numberOfFractions Number of fractions the buyer wants to purchase.
     */
    function purchaseFraction(uint256 homeId, uint256 numberOfFractions) public payable homeExists(homeId) {
        VacationHome storage home = vacationHomes[homeId];
        uint256 cost = numberOfFractions * home.fractionalCost;

        require(msg.value == cost, "Incorrect payment amount");
        require(home.fractionsSold + numberOfFractions <= home.totalFractions, "Not enough fractions available");

        // Update ownership
        ownership[homeId][msg.sender] += numberOfFractions;

        // Update fractions sold
        home.fractionsSold += numberOfFractions;

        // Add buyer to owners list if first purchase
        if (ownership[homeId][msg.sender] == numberOfFractions) {
            home.owners.push(msg.sender);
        }

        emit FractionPurchased(homeId, msg.sender, ownership[homeId][msg.sender]);
    }

    /**
     * @dev Returns the owners of a specific vacation home.
     * @param homeId Unique identifier for the vacation home.
     * @return owners Array of owner addresses.
     */
    function getOwners(uint256 homeId) public view homeExists(homeId) returns (address[] memory) {
        return vacationHomes[homeId].owners;
    }

    /**
     * @dev Returns the number of fractions owned by a specific owner for a specific vacation home.
     * @param homeId Unique identifier for the vacation home.
     * @param owner Address of the owner.
     * @return fractionsOwned Number of fractions owned by the owner.
     */
    function getFractionsOwned(uint256 homeId, address owner) public view homeExists(homeId) returns (uint256) {
        return ownership[homeId][owner];
    }
}
```
