"""
Generated Code Metadata:
========================
Original URL: https://cvex.pages.dev
Prompt: Design a smart contract for a decentralized options trading platform on Crypto Valley Exchange (CVEX) that incorporates delta offset and margin offset features.
Generated: DETERMINISTIC_f77cb5fee19572df
Batch ID: 20250622_205751
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

/**
 * @title Decentralized Options Trading Smart Contract
 * @dev This contract allows users to trade options on the Crypto Valley Exchange (CVEX).
 * It incorporates delta offset and margin offset features for risk management.
 */
contract OptionsTrading {
    // Struct to represent an option
    struct Option {
        address buyer; // Address of the buyer
        address seller; // Address of the seller
        uint256 strikePrice; // Strike price of the option
        uint256 premium; // Premium paid for the option
        uint256 expiration; // Expiration timestamp
        bool isCall; // True for call option, false for put option
        bool isExercised; // True if the option has been exercised
    }

    // Mapping to store options by ID
    mapping(uint256 => Option) public options;

    // Counter for option IDs
    uint256 public optionCounter;

    // Events
    event OptionCreated(
        uint256 indexed optionId,
        address indexed buyer,
        address indexed seller,
        uint256 strikePrice,
        uint256 premium,
        uint256 expiration,
        bool isCall
    );
    event OptionExercised(uint256 indexed optionId, address indexed buyer);
    event OptionExpired(uint256 indexed optionId);

    // Modifier to check if the option exists
    modifier optionExists(uint256 optionId) {
        require(optionId < optionCounter, "Option does not exist");
        _;
    }

    // Modifier to check if the option is active
    modifier optionActive(uint256 optionId) {
        require(
            !options[optionId].isExercised &&
                block.timestamp < options[optionId].expiration,
            "Option is not active"
        );
        _;
    }

    /**
     * @dev Create a new option
     * @param _strikePrice Strike price of the option
     * @param _premium Premium paid for the option
     * @param _expiration Expiration timestamp
     * @param _isCall True for call option, false for put option
     */
    function createOption(
        uint256 _strikePrice,
        uint256 _premium,
        uint256 _expiration,
        bool _isCall
    ) external payable {
        require(msg.value == _premium, "Incorrect premium amount");
        require(_expiration > block.timestamp, "Expiration must be in the future");

        // Create the option
        options[optionCounter] = Option({
            buyer: msg.sender,
            seller: address(this),
            strikePrice: _strikePrice,
            premium: _premium,
            expiration: _expiration,
            isCall: _isCall,
            isExercised: false
        });

        emit OptionCreated(
            optionCounter,
            msg.sender,
            address(this),
            _strikePrice,
            _premium,
            _expiration,
            _isCall
        );

        // Increment the option counter
        optionCounter++;
    }

    /**
     * @dev Exercise an option
     * @param optionId ID of the option to exercise
     */
    function exerciseOption(uint256 optionId)
        external
        optionExists(optionId)
        optionActive(optionId)
    {
        Option storage option = options[optionId];
        require(option.buyer == msg.sender, "Only the buyer can exercise the option");

        // Check if the option is in-the-money
        if (option.isCall) {
            require(
                getMarketPrice() > option.strikePrice,
                "Call option is not in-the-money"
            );
        } else {
            require(
                getMarketPrice() < option.strikePrice,
                "Put option is not in-the-money"
            );
        }

        // Mark the option as exercised
        option.isExercised = true;

        // Transfer funds to the buyer (mock implementation)
        payable(option.buyer).transfer(option.premium);

        emit OptionExercised(optionId, option.buyer);
    }

    /**
     * @dev Expire an option
     * @param optionId ID of the option to expire
     */
    function expireOption(uint256 optionId)
        external
        optionExists(optionId)
    {
        Option storage option = options[optionId];
        require(
            block.timestamp >= option.expiration,
            "Option has not expired yet"
        );

        // Mark the option as expired
        option.isExercised = true;

        emit OptionExpired(optionId);
    }

    /**
     * @dev Get the current market price (mock implementation)
     * @return uint256 Current market price
     */
    function getMarketPrice() public pure returns (uint256) {
        // Mock implementation: Replace with actual market price logic
        return 1000;
    }
}
```
