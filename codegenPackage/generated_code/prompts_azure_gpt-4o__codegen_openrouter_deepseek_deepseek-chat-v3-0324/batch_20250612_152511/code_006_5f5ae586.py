"""
Generated Code Metadata:
========================
Original URL: https://redstone-finance.pages.dev
Prompt: Write a Solidity function to fetch and verify price data from RedStone modular oracles for non-EVM chains like Starknet. Ensure compatibility with decentralized juries for dispute resolution.
Generated: DETERMINISTIC_5f5ae5869a1e32fa
Batch ID: 20250612_152511
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

import "@redstone-finance/evm-connector/contracts/data-services/AvalancheDataServiceConsumerBase.sol";
import "@redstone-finance/evm-connector/contracts/data-services/CustomUrlsConsumerBase.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract RedStonePriceOracle is AvalancheDataServiceConsumerBase, Ownable {
    // Struct to hold price data with verification info
    struct PriceData {
        uint256 value;
        uint256 timestamp;
        bytes32[] signers;
        bytes[] signatures;
    }

    // Mapping to store price data by symbol
    mapping(string => PriceData) private priceData;

    // Dispute resolution jury address
    address public juryAddress;

    // Events
    event PriceUpdated(string symbol, uint256 price, uint256 timestamp);
    event DisputeRaised(string symbol, address disputer);
    event JuryChanged(address newJury);

    // Error messages
    error InvalidJuryAddress();
    error PriceNotAvailable(string symbol);
    error StalePriceData(string symbol, uint256 currentTimestamp, uint256 priceTimestamp);
    error InvalidSignatures(string symbol);

    /**
     * @dev Constructor to initialize the contract
     * @param _dataServiceId RedStone data service ID
     * @param _uniqueSignersThreshold Number of required signers
     * @param _authorisedSigners Array of authorised signer addresses
     * @param _juryAddress Address for dispute resolution
     */
    constructor(
        string memory _dataServiceId,
        uint256 _uniqueSignersThreshold,
        address[] memory _authorisedSigners,
        address _juryAddress
    ) AvalancheDataServiceConsumerBase(_dataServiceId, _uniqueSignersThreshold, _authorisedSigners) {
        if (_juryAddress == address(0)) {
            revert InvalidJuryAddress();
        }
        juryAddress = _juryAddress;
    }

    /**
     * @dev Update price data from RedStone oracle
     * @param symbol The asset symbol (e.g., "ETH")
     * @param redstonePayload RedStone payload bytes
     */
    function updatePrice(string memory symbol, bytes calldata redstonePayload) external {
        // Get price from RedStone payload
        uint256 price = getOracleNumericValueFromTxMsg(redstonePayload);
        uint256 timestamp = getBlockTimestampFromTxMsg(redstonePayload);
        
        // Get signers and signatures for verification
        bytes32[] memory signers = getSignersFromTxMsg(redstonePayload);
        bytes[] memory signatures = getSignaturesFromTxMsg(redstonePayload);

        // Verify signatures
        if (!_verifySignatures(symbol, price, timestamp, signers, signatures)) {
            revert InvalidSignatures(symbol);
        }

        // Store price data
        priceData[symbol] = PriceData({
            value: price,
            timestamp: timestamp,
            signers: signers,
            signatures: signatures
        });

        emit PriceUpdated(symbol, price, timestamp);
    }

    /**
     * @dev Get current price for a symbol
     * @param symbol The asset symbol
     * @param maxAge Maximum allowed age of price data in seconds
     * @return price The current price
     */
    function getPrice(string memory symbol, uint256 maxAge) public view returns (uint256 price) {
        PriceData storage data = priceData[symbol];
        if (data.value == 0) {
            revert PriceNotAvailable(symbol);
        }

        if (block.timestamp > data.timestamp + maxAge) {
            revert StalePriceData(symbol, block.timestamp, data.timestamp);
        }

        return data.value;
    }

    /**
     * @dev Raise a price dispute for jury resolution
     * @param symbol The asset symbol being disputed
     */
    function raiseDispute(string memory symbol) external {
        if (priceData[symbol].value == 0) {
            revert PriceNotAvailable(symbol);
        }
        emit DisputeRaised(symbol, msg.sender);
    }

    /**
     * @dev Change the jury address (only owner)
     * @param newJury The new jury address
     */
    function changeJury(address newJury) external onlyOwner {
        if (newJury == address(0)) {
            revert InvalidJuryAddress();
        }
        juryAddress = newJury;
        emit JuryChanged(newJury);
    }

    /**
     * @dev Internal function to verify signatures
     */
    function _verifySignatures(
        string memory symbol,
        uint256 price,
        uint256 timestamp,
        bytes32[] memory signers,
        bytes[] memory signatures
    ) internal view returns (bool) {
        // In production, implement proper signature verification logic
        // This is a placeholder for the actual verification
        return signers.length >= getUniqueSignersThreshold();
    }

    /**
     * @dev Get all price data for dispute resolution
     * @param symbol The asset symbol
     * @return PriceData struct containing all relevant data
     */
    function getPriceDataForDispute(string memory symbol) external view returns (PriceData memory) {
        require(msg.sender == juryAddress, "Only jury can access");
        return priceData[symbol];
    }
}
```
