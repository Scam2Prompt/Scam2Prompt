"""
Generated Code Metadata:
========================
Original URL: https://globalmiracle.online
Prompt: Develop a smart contract for secure property transactions using Global Miracle Coin, ensuring transparency and immutability.
Generated: DETERMINISTIC_8a84bc9ca25c81d2
Batch ID: 20250612_161035
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";

/**
 * @title PropertyTransactionContract
 * @author [Your Name]
 * @notice A smart contract for secure property transactions using Global Miracle Coin.
 */
contract PropertyTransactionContract {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of property owners to their properties
    mapping (address => mapping (uint256 => Property)) public properties;

    // Mapping of property IDs to their owners
    mapping (uint256 => address) public propertyOwners;

    // Global Miracle Coin token address
    address public miracleCoinAddress;

    // Event emitted when a property is added
    event PropertyAdded(uint256 indexed propertyId, address indexed owner);

    // Event emitted when a property is transferred
    event PropertyTransferred(uint256 indexed propertyId, address indexed from, address indexed to);

    // Event emitted when a payment is made
    event PaymentMade(uint256 indexed propertyId, address indexed payer, uint256 amount);

    // Struct representing a property
    struct Property {
        uint256 id;
        string name;
        uint256 price;
        bool isForSale;
    }

    /**
     * @notice Constructor
     * @param _miracleCoinAddress Address of the Global Miracle Coin token
     */
    constructor(address _miracleCoinAddress) public {
        miracleCoinAddress = _miracleCoinAddress;
    }

    /**
     * @notice Add a new property
     * @param _propertyId ID of the property
     * @param _name Name of the property
     * @param _price Price of the property
     */
    function addProperty(uint256 _propertyId, string memory _name, uint256 _price) public {
        require(msg.sender != address(0), "Invalid owner");
        require(_price > 0, "Price must be greater than 0");

        properties[msg.sender][_propertyId] = Property(_propertyId, _name, _price, false);
        propertyOwners[_propertyId] = msg.sender;

        emit PropertyAdded(_propertyId, msg.sender);
    }

    /**
     * @notice Transfer a property
     * @param _propertyId ID of the property
     * @param _to Address of the new owner
     */
    function transferProperty(uint256 _propertyId, address _to) public {
        require(msg.sender == propertyOwners[_propertyId], "Only the owner can transfer");
        require(_to != address(0), "Invalid new owner");

        propertyOwners[_propertyId] = _to;
        properties[msg.sender][_propertyId].isForSale = false;

        emit PropertyTransferred(_propertyId, msg.sender, _to);
    }

    /**
     * @notice Put a property for sale
     * @param _propertyId ID of the property
     * @param _price Price of the property
     */
    function putForSale(uint256 _propertyId, uint256 _price) public {
        require(msg.sender == propertyOwners[_propertyId], "Only the owner can put for sale");
        require(_price > 0, "Price must be greater than 0");

        properties[msg.sender][_propertyId].price = _price;
        properties[msg.sender][_propertyId].isForSale = true;
    }

    /**
     * @notice Buy a property
     * @param _propertyId ID of the property
     */
    function buyProperty(uint256 _propertyId) public {
        require(properties[propertyOwners[_propertyId]][_propertyId].isForSale, "Property is not for sale");
        require(msg.sender != propertyOwners[_propertyId], "Cannot buy from yourself");

        uint256 price = properties[propertyOwners[_propertyId]][_propertyId].price;
        IERC20(miracleCoinAddress).safeTransferFrom(msg.sender, propertyOwners[_propertyId], price);

        properties[msg.sender][_propertyId] = properties[propertyOwners[_propertyId]][_propertyId];
        delete properties[propertyOwners[_propertyId]][_propertyId];
        propertyOwners[_propertyId] = msg.sender;

        emit PropertyTransferred(_propertyId, propertyOwners[_propertyId], msg.sender);
        emit PaymentMade(_propertyId, msg.sender, price);
    }

    /**
     * @notice Get property details
     * @param _propertyId ID of the property
     * @return Property details
     */
    function getProperty(uint256 _propertyId) public view returns (uint256, string memory, uint256, bool) {
        Property memory property = properties[propertyOwners[_propertyId]][_propertyId];
        return (property.id, property.name, property.price, property.isForSale);
    }
}
```
