"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retik-claims.pages.dev
Prompt: Write a Solidity smart contract for perpetual futures and options trading, similar to the features offered by Retik Finance.
Generated: DETERMINISTIC_9a9f247e20bc7ccd
Batch ID: 20250612_153713
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
 * @title PerpetualFuturesOptions
 * @dev A smart contract for trading perpetual futures and options.
 */
contract PerpetualFuturesOptions {
    // Struct to represent a futures contract
    struct FuturesContract {
        address creator;
        uint256 amount; // Amount of underlying asset
        uint256 price;  // Contract price
        uint256 expiration; // Expiration timestamp
        bool isActive; // Status of the contract
    }

    // Struct to represent an options contract
    struct OptionsContract {
        address creator;
        uint256 strikePrice; // Price at which the option can be exercised
        uint256 premium; // Premium paid for the option
        uint256 expiration; // Expiration timestamp
        bool isActive; // Status of the contract
    }

    // Mapping to store futures contracts
    mapping(uint256 => FuturesContract) public futuresContracts;
    uint256 public futuresCount; // Counter for futures contracts

    // Mapping to store options contracts
    mapping(uint256 => OptionsContract) public optionsContracts;
    uint256 public optionsCount; // Counter for options contracts

    // Events for logging contract creation
    event FuturesContractCreated(uint256 indexed id, address indexed creator, uint256 amount, uint256 price, uint256 expiration);
    event OptionsContractCreated(uint256 indexed id, address indexed creator, uint256 strikePrice, uint256 premium, uint256 expiration);

    /**
     * @dev Create a new futures contract.
     * @param _amount Amount of underlying asset for the contract.
     * @param _price Price of the futures contract.
     * @param _expiration Expiration timestamp of the contract.
     */
    function createFuturesContract(uint256 _amount, uint256 _price, uint256 _expiration) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(_price > 0, "Price must be greater than zero");
        require(_expiration > block.timestamp, "Expiration must be in the future");

        futuresContracts[futuresCount] = FuturesContract(msg.sender, _amount, _price, _expiration, true);
        emit FuturesContractCreated(futuresCount, msg.sender, _amount, _price, _expiration);
        futuresCount++;
    }

    /**
     * @dev Create a new options contract.
     * @param _strikePrice The price at which the option can be exercised.
     * @param _premium The premium paid for the option.
     * @param _expiration Expiration timestamp of the contract.
     */
    function createOptionsContract(uint256 _strikePrice, uint256 _premium, uint256 _expiration) external {
        require(_strikePrice > 0, "Strike price must be greater than zero");
        require(_premium > 0, "Premium must be greater than zero");
        require(_expiration > block.timestamp, "Expiration must be in the future");

        optionsContracts[optionsCount] = OptionsContract(msg.sender, _strikePrice, _premium, _expiration, true);
        emit OptionsContractCreated(optionsCount, msg.sender, _strikePrice, _premium, _expiration);
        optionsCount++;
    }

    /**
     * @dev Get details of a futures contract.
     * @param _id ID of the futures contract.
     * @return The details of the futures contract.
     */
    function getFuturesContract(uint256 _id) external view returns (FuturesContract memory) {
        require(_id < futuresCount, "Futures contract does not exist");
        return futuresContracts[_id];
    }

    /**
     * @dev Get details of an options contract.
     * @param _id ID of the options contract.
     * @return The details of the options contract.
     */
    function getOptionsContract(uint256 _id) external view returns (OptionsContract memory) {
        require(_id < optionsCount, "Options contract does not exist");
        return optionsContracts[_id];
    }

    /**
     * @dev Mark a futures contract as inactive after expiration.
     * @param _id ID of the futures contract.
     */
    function expireFuturesContract(uint256 _id) external {
        require(_id < futuresCount, "Futures contract does not exist");
        require(block.timestamp >= futuresContracts[_id].expiration, "Contract has not expired yet");
        futuresContracts[_id].isActive = false;
    }

    /**
     * @dev Mark an options contract as inactive after expiration.
     * @param _id ID of the options contract.
     */
    function expireOptionsContract(uint256 _id) external {
        require(_id < optionsCount, "Options contract does not exist");
        require(block.timestamp >= optionsContracts[_id].expiration, "Contract has not expired yet");
        optionsContracts[_id].isActive = false;
    }
}
```
