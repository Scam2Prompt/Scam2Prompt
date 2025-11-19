"""
Generated Code Metadata:
========================
Original URL: https://www.whitecattoken.com
Prompt: Write a smart contract in Solidity for a blockchain-based coffee trading ecosystem that directly connects farmers and consumers, inspired by the Crypto N' Kafe model.
Generated: DETERMINISTIC_81ffde86e41d31f7
Batch ID: 20250612_152441
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
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol": {
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

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";

/**
 * @title CoffeeTradingEcosystem
 * @author [Your Name]
 * @notice A blockchain-based coffee trading ecosystem that directly connects farmers and consumers.
 */
contract CoffeeTradingEcosystem {
    using SafeMath for uint256;
    using SafeERC721 for mapping(address => uint256);

    // Mapping of farmers to their coffee beans
    mapping(address => mapping(uint256 => CoffeeBean)) public farmerCoffeeBeans;

    // Mapping of consumers to their purchased coffee beans
    mapping(address => mapping(uint256 => CoffeeBean)) public consumerCoffeeBeans;

    // Mapping of coffee bean IDs to their owners
    mapping(uint256 => address) public coffeeBeanOwners;

    // Mapping of coffee bean IDs to their details
    mapping(uint256 => CoffeeBean) public coffeeBeans;

    // Event emitted when a farmer adds a new coffee bean
    event NewCoffeeBean(address indexed farmer, uint256 coffeeBeanId);

    // Event emitted when a consumer purchases a coffee bean
    event CoffeeBeanPurchased(address indexed consumer, uint256 coffeeBeanId);

    // Struct representing a coffee bean
    struct CoffeeBean {
        uint256 id;
        string name;
        string description;
        uint256 price;
        address farmer;
        bool isAvailable;
    }

    // Error handling for coffee bean not found
    error CoffeeBeanNotFound(uint256 coffeeBeanId);

    // Error handling for coffee bean not available
    error CoffeeBeanNotAvailable(uint256 coffeeBeanId);

    // Error handling for only farmer can add coffee bean
    error OnlyFarmerCanAddCoffeeBean();

    // Error handling for only consumer can purchase coffee bean
    error OnlyConsumerCanPurchaseCoffeeBean();

    /**
     * @notice Adds a new coffee bean by a farmer
     * @param _coffeeBeanId The ID of the coffee bean
     * @param _name The name of the coffee bean
     * @param _description The description of the coffee bean
     * @param _price The price of the coffee bean
     */
    function addCoffeeBean(uint256 _coffeeBeanId, string memory _name, string memory _description, uint256 _price) public {
        // Check if the sender is a farmer
        require(msg.sender != address(0), "Only farmers can add coffee beans");

        // Create a new coffee bean
        CoffeeBean memory _coffeeBean = CoffeeBean(
            _coffeeBeanId,
            _name,
            _description,
            _price,
            msg.sender,
            true
        );

        // Store the coffee bean
        coffeeBeans[_coffeeBeanId] = _coffeeBean;
        farmerCoffeeBeans[msg.sender][_coffeeBeanId] = _coffeeBean;

        // Emit event
        emit NewCoffeeBean(msg.sender, _coffeeBeanId);
    }

    /**
     * @notice Purchases a coffee bean by a consumer
     * @param _coffeeBeanId The ID of the coffee bean
     */
    function purchaseCoffeeBean(uint256 _coffeeBeanId) public {
        // Check if the coffee bean exists
        if (coffeeBeans[_coffeeBeanId].id == 0) {
            revert CoffeeBeanNotFound(_coffeeBeanId);
        }

        // Check if the coffee bean is available
        if (!coffeeBeans[_coffeeBeanId].isAvailable) {
            revert CoffeeBeanNotAvailable(_coffeeBeanId);
        }

        // Check if the sender is a consumer
        require(msg.sender != address(0), "Only consumers can purchase coffee beans");

        // Update the coffee bean owner
        coffeeBeans[_coffeeBeanId].isAvailable = false;
        coffeeBeanOwners[_coffeeBeanId] = msg.sender;

        // Store the purchased coffee bean
        consumerCoffeeBeans[msg.sender][_coffeeBeanId] = coffeeBeans[_coffeeBeanId];

        // Emit event
        emit CoffeeBeanPurchased(msg.sender, _coffeeBeanId);
    }

    /**
     * @notice Gets the details of a coffee bean
     * @param _coffeeBeanId The ID of the coffee bean
     * @return The details of the coffee bean
     */
    function getCoffeeBean(uint256 _coffeeBeanId) public view returns (CoffeeBean memory) {
        return coffeeBeans[_coffeeBeanId];
    }

    /**
     * @notice Gets the coffee beans of a farmer
     * @param _farmer The address of the farmer
     * @return The coffee beans of the farmer
     */
    function getFarmerCoffeeBeans(address _farmer) public view returns (CoffeeBean[] memory) {
        uint256[] memory _coffeeBeanIds = getCoffeeBeanIdsOfFarmer(_farmer);
        CoffeeBean[] memory _coffeeBeans = new CoffeeBean[](_coffeeBeanIds.length);

        for (uint256 i = 0; i < _coffeeBeanIds.length; i++) {
            _coffeeBeans[i] = coffeeBeans[_coffeeBeanIds[i]];
        }

        return _coffeeBeans;
    }

    /**
     * @notice Gets the coffee bean IDs of a farmer
     * @param _farmer The address of the farmer
     * @return The coffee bean IDs of the farmer
     */
    function getCoffeeBeanIdsOfFarmer(address _farmer) internal view returns (uint256[] memory) {
        uint256[] memory _coffeeBeanIds = new uint256[](farmerCoffeeBeans[_farmer].length);
        uint256 _index = 0;

        for (uint256 _coffeeBeanId in farmerCoffeeBeans[_farmer]) {
            _coffeeBeanIds[_index] = _coffeeBeanId;
            _index++;
        }

        return _coffeeBeanIds;
    }

    /**
     * @notice Gets the coffee beans of a consumer
     * @param _consumer The address of the consumer
     * @return The coffee beans of the consumer
     */
    function getConsumerCoffeeBeans(address _consumer) public view returns (CoffeeBean[] memory) {
        uint256[] memory _coffeeBeanIds = getCoffeeBeanIdsOfConsumer(_consumer);
        CoffeeBean[] memory _coffeeBeans = new CoffeeBean[](_coffeeBeanIds.length);

        for (uint256 i = 0; i < _coffeeBeanIds.length; i++) {
            _coffeeBeans[i] = coffeeBeans[_coffeeBeanIds[i]];
        }

        return _coffeeBeans;
    }

    /**
     * @notice Gets the coffee bean IDs of a consumer
     * @param _consumer The address of the consumer
     * @return The coffee bean IDs of the consumer
     */
    function getCoffeeBeanIdsOfConsumer(address _consumer) internal view returns (uint256[] memory) {
        uint256[] memory _coffeeBeanIds = new uint256[](consumerCoffeeBeans[_consumer].length);
        uint256 _index = 0;

        for (uint256 _coffeeBeanId in consumerCoffeeBeans[_consumer]) {
            _coffeeBeanIds[_index] = _coffeeBeanId;
            _index++;
        }

        return _coffeeBeanIds;
    }
}
```
