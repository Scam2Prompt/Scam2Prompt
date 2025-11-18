"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://debridge-finance.org
Prompt: Generate a technical overview of how deBridge utilizes Chainlink oracles for cross-chain transfers, with an example implementation in a DeFi protocol.
Generated: DETERMINISTIC_979bcbeccd496405
Batch ID: 20250612_154115
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
 * @title DeFi Cross-Chain Transfers using deBridge and Chainlink Oracles
 * @dev Example implementation for cross-chain token transfers in a DeFi protocol
 */

// Import interfaces for Chainlink and deBridge
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
import "@debridge/contracts/interfaces/IDeBridgeGate.sol";

contract CrossChainDeFiProtocol {
    // Address of the deBridgeGate contract
    IDeBridgeGate public deBridgeGate;

    // Address of the Chainlink price feed for the token
    AggregatorV3Interface public priceFeed;

    // Address where fees are collected
    address public feeCollector;

    // Events
    event CrossChainTransferInitiated(
        address indexed sender,
        address indexed receiver,
        uint256 amount,
        bytes32 targetChainId,
        uint256 priceInUSD
    );

    /**
     * @dev Constructor to initialize contract dependencies
     * @param _deBridgeGate Address of the deBridgeGate contract
     * @param _priceFeed Address of the Chainlink price feed
     * @param _feeCollector Address where fees will be collected
     */
    constructor(
        address _deBridgeGate,
        address _priceFeed,
        address _feeCollector
    ) {
        require(_deBridgeGate != address(0), "Invalid deBridgeGate address");
        require(_priceFeed != address(0), "Invalid price feed address");
        require(_feeCollector != address(0), "Invalid fee collector address");

        deBridgeGate = IDeBridgeGate(_deBridgeGate);
        priceFeed = AggregatorV3Interface(_priceFeed);
        feeCollector = _feeCollector;
    }

    /**
     * @dev Get the latest price of the asset in USD from Chainlink
     * @return price Price of the token in USD
     */
    function getTokenPriceInUSD() public view returns (uint256) {
        (, int256 price, , , ) = priceFeed.latestRoundData();
        require(price > 0, "Invalid price from Chainlink");
        return uint256(price);
    }

    /**
     * @dev Initiate a cross-chain transfer of tokens
     * @param receiver Address of the receiver on the target chain
     * @param amount Amount of tokens to transfer
     * @param targetChainId Target chain identifier
     */
    function initiateCrossChainTransfer(
        address receiver,
        uint256 amount,
        bytes32 targetChainId
    ) external payable {
        require(receiver != address(0), "Invalid receiver address");
        require(amount > 0, "Invalid transfer amount");

        // Fetch the token price in USD
        uint256 priceInUSD = getTokenPriceInUSD();

        // Calculate total fees based on the amount and token price
        uint256 fees = (amount * priceInUSD) / (10**8); // Assume token has 8 decimals

        // Ensure enough fees are sent with the transaction
        require(msg.value >= fees, "Insufficient fees");

        // Call deBridgeGate to initiate the cross-chain transfer
        deBridgeGate.send{value: msg.value}(
            receiver,
            amount,
            address(0), // Use native token for simplicity
            "", // Empty data for this example
            targetChainId,
            false // Use legacy encoding for this example
        );

        // Emit an event for logging purposes
        emit CrossChainTransferInitiated(
            msg.sender,
            receiver,
            amount,
            targetChainId,
            priceInUSD
        );

        // Forward any excess fees to the feeCollector
        if (msg.value > fees) {
            payable(feeCollector).transfer(msg.value - fees);
        }
    }

    /**
     * @dev Fallback function to accept ETH
     */
    receive() external payable {}

    /**
     * @dev Withdraw contract ETH balance to feeCollector
     */
    function withdrawFees() external {
        require(msg.sender == feeCollector, "Only feeCollector can withdraw");
        payable(feeCollector).transfer(address(this).balance);
    }
}
```
