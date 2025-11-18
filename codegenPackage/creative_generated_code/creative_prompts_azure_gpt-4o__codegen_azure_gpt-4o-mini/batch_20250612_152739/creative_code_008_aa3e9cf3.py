"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://allianceblock-ahz.pages.dev
Prompt: Write a smart contract that enables tokenized financing of art, cars, and collectibles through on-chain options, inspired by Arkefi AG's platform on AllianceBlock.
Generated: DETERMINISTIC_aa3e9cf3d1494ca1
Batch ID: 20250612_152739
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

// Importing OpenZeppelin's ERC20 implementation for token creation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Smart contract for tokenized financing of art, cars, and collectibles
contract TokenizedFinancing is ERC20, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _optionIdCounter;

    // Struct to represent an option
    struct Option {
        uint256 id;            // Unique identifier for the option
        address creator;       // Address of the option creator
        address buyer;         // Address of the buyer (if purchased)
        uint256 tokenAmount;   // Amount of tokens for the option
        uint256 strikePrice;   // Strike price in wei
        uint256 expiry;        // Expiry timestamp for the option
        bool exercised;        // Status of the option (exercised or not)
    }

    // Mapping to store options by their ID
    mapping(uint256 => Option) public options;

    // Event emitted when an option is created
    event OptionCreated(uint256 indexed optionId, address indexed creator, uint256 tokenAmount, uint256 strikePrice, uint256 expiry);
    
    // Event emitted when an option is purchased
    event OptionPurchased(uint256 indexed optionId, address indexed buyer);
    
    // Event emitted when an option is exercised
    event OptionExercised(uint256 indexed optionId, address indexed buyer);

    // Constructor to initialize the token with a name and symbol
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {}

    // Function to create a new financing option
    function createOption(uint256 tokenAmount, uint256 strikePrice, uint256 expiry) external onlyOwner {
        require(expiry > block.timestamp, "Expiry must be in the future");

        // Increment the option ID counter
        uint256 optionId = _optionIdCounter.current();
        _optionIdCounter.increment();

        // Create the new option
        options[optionId] = Option({
            id: optionId,
            creator: msg.sender,
            buyer: address(0),
            tokenAmount: tokenAmount,
            strikePrice: strikePrice,
            expiry: expiry,
            exercised: false
        });

        emit OptionCreated(optionId, msg.sender, tokenAmount, strikePrice, expiry);
    }

    // Function for a buyer to purchase an option
    function purchaseOption(uint256 optionId) external payable {
        Option storage option = options[optionId];

        require(option.id != 0, "Option does not exist");
        require(option.buyer == address(0), "Option already purchased");
        require(msg.value == option.strikePrice, "Incorrect amount sent");
        require(block.timestamp < option.expiry, "Option has expired");

        // Set the buyer and mark option as purchased
        option.buyer = msg.sender;

        emit OptionPurchased(optionId, msg.sender);
    }

    // Function to exercise an option
    function exerciseOption(uint256 optionId) external {
        Option storage option = options[optionId];

        require(option.id != 0, "Option does not exist");
        require(option.buyer == msg.sender, "Only the buyer can exercise");
        require(block.timestamp < option.expiry, "Option has expired");
        require(!option.exercised, "Option already exercised");

        // Transfer tokens to the buyer
        _mint(msg.sender, option.tokenAmount);

        // Mark the option as exercised
        option.exercised = true;

        emit OptionExercised(optionId, msg.sender);
    }

    // Function to withdraw funds made from option purchases
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        
        // Transfer the balance to the owner
        payable(msg.sender).transfer(balance);
    }

    // Function to get the option details by ID
    function getOption(uint256 optionId) external view returns (Option memory) {
        return options[optionId];
    }
}
```
