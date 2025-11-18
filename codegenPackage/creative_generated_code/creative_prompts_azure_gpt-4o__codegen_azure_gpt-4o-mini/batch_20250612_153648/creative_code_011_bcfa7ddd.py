"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pyth-test.vercel.app
Prompt: Provide code for a decentralized application that uses Pyth Network's price feeds to calculate expiry prices for options contracts on Ethereum.
Generated: DETERMINISTIC_bcfa7ddd5c12d2b5
Batch ID: 20250612_153648
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

// Importing OpenZeppelin's SafeMath library for safe mathematical operations
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for Pyth Network price feed contracts
interface IPyth {
    function getPrice(uint256 assetId) external view returns (int256);
}

// Struct to hold option contract details
struct OptionContract {
    address creator;
    uint256 strikePrice; // The price at which the option can be exercised
    uint256 expiry;      // Expiry time of the option in seconds since epoch
    bool isExercised;    // Flag to check if the option has been exercised
}

// Main contract to manage options
contract OptionsContract {
    using SafeMath for uint256;

    // Mapping to store option contracts by their unique IDs
    mapping(uint256 => OptionContract) public options;
    uint256 public nextOptionId;

    // Address of the Pyth network price feed contract
    IPyth public pyth;

    // Event emitted when an option is created
    event OptionCreated(uint256 indexed optionId, address indexed creator, uint256 strikePrice, uint256 expiry);
    // Event emitted when an option is exercised
    event OptionExercised(uint256 indexed optionId, address indexed exerciser);

    // Constructor to initialize the Pyth price feed contract address
    constructor(address _pythAddress) {
        pyth = IPyth(_pythAddress);
    }

    // Function to create an option contract
    function createOption(uint256 _strikePrice, uint256 _expiry) external returns (uint256) {
        require(_expiry > block.timestamp, "Expiry must be in the future");
        
        options[nextOptionId] = OptionContract({
            creator: msg.sender,
            strikePrice: _strikePrice,
            expiry: _expiry,
            isExercised: false
        });

        emit OptionCreated(nextOptionId, msg.sender, _strikePrice, _expiry);
        nextOptionId++;
        return nextOptionId - 1;
    }

    // Function to exercise an option if conditions are met
    function exerciseOption(uint256 _optionId) external {
        OptionContract storage option = options[_optionId];
        require(!option.isExercised, "Option already exercised");
        require(block.timestamp < option.expiry, "Option has expired");

        // Fetch the current price from Pyth network
        int256 currentPrice = pyth.getPrice(1); // Assuming 1 is the assetId for the price feed
        require(currentPrice > 0, "Invalid price from Pyth");

        uint256 price = uint256(currentPrice);

        // Check if the current price meets the strike price condition
        require(price >= option.strikePrice, "Current price below strike price");

        // Mark the option as exercised
        option.isExercised = true;

        emit OptionExercised(_optionId, msg.sender);
        // Logic to transfer the appropriate tokens can be added here
    }
}
```
