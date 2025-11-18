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
// SPDX-License-Identifier: Apache-2.0
pragma solidity ^0.8.17;

// Import Pyth interfaces
import "@pythnetwork/pyth-sdk-solidity/IPyth.sol";

/// @title Decentralized Options Contract using Pyth Network
/// @notice This smart contract interacts with the Pyth Network to fetch price feeds for calculating expiry prices of options contracts.
contract OptionsContract {

    // Address of the Pyth contract on the Ethereum network
    IPyth public pyth;

    // Mapping to store options data: optionId -> OptionDetails
    mapping(uint256 => OptionDetails) public options;

    // Counter for generating unique option IDs
    uint256 private optionIdCounter;

    // Struct to store details of an option
    struct OptionDetails {
        address creator;   // Address of the option creator
        string assetId;    // Pyth price feed ID for the asset
        uint256 strikePrice; // Strike price of the option
        uint256 expiry;      // Expiry timestamp
        uint256 premium;     // Premium paid in wei
        uint256 settledPrice; // Price at settlement (if available)
        bool isSettled;       // Settlement flag
    }

    /// @param _pythAddress Address of the Pyth contract
    constructor(address _pythAddress) {
        require(_pythAddress != address(0), "Invalid Pyth address");
        pyth = IPyth(_pythAddress);
    }

    /// @notice Creates a new options contract
    /// @param assetId Pyth price feed ID for the underlying asset
    /// @param strikePrice Strike price of the option
    /// @param expiry Expiry timestamp of the option
    /// @return optionId The ID of the created option
    function createOption(
        string memory assetId,
        uint256 strikePrice,
        uint256 expiry
    ) external payable returns (uint256 optionId) {
        require(expiry > block.timestamp, "Expiry must be in the future");
        require(msg.value > 0, "Premium must be greater than 0");

        optionId = optionIdCounter++;
        options[optionId] = OptionDetails({
            creator: msg.sender,
            assetId: assetId,
            strikePrice: strikePrice,
            expiry: expiry,
            premium: msg.value,
            settledPrice: 0,
            isSettled: false
        });

        emit OptionCreated(optionId, msg.sender, assetId, strikePrice, expiry, msg.value);
    }

    /// @notice Settles an expired option and fetches the expiry price from the Pyth Network
    /// @param optionId ID of the option to settle
    /// @param priceUpdateData Array of price update data from Pyth (off-chain signed price data)
    function settleOption(uint256 optionId, bytes[] calldata priceUpdateData) external {
        OptionDetails storage option = options[optionId];

        require(block.timestamp >= option.expiry, "Option has not expired yet");
        require(!option.isSettled, "Option is already settled");

        // Update the Pyth price feeds with signed data
        pyth.updatePriceFeeds(priceUpdateData);

        // Fetch the price for the asset from Pyth
        int64 price;
        uint64 conf;
        (price, conf) = pyth.getPrice(option.assetId);

        // Settle the option
        option.settledPrice = uint256(price);
        option.isSettled = true;

        emit OptionSettled(optionId, uint256(price), msg.sender);
    }

    /// @notice Retrieves details of an option
    /// @param optionId ID of the option
    /// @return Option details
    function getOption(uint256 optionId) external view returns (OptionDetails memory) {
        return options[optionId];
    }

    /// @notice Event emitted when an option is created
    event OptionCreated(uint256 optionId, address indexed creator, string assetId, uint256 strikePrice, uint256 expiry, uint256 premium);

    /// @notice Event emitted when an option is settled
    event OptionSettled(uint256 optionId, uint256 settledPrice, address indexed settler);
}
```

### Notes:
- This code assumes the Pyth smart contract interface (`IPyth`) is correctly implemented and available as part of the imported package. Be sure to configure your environment to include Pyth’s SDK and deploy this contract to Ethereum.
- The function `settleOption` expects signed price update data from Pyth Network as input. You need off-chain infrastructure to fetch these price updates and pass them to this function when settling options.
