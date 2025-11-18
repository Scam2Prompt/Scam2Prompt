"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pythcall.com
Prompt: Generate code for a smart contract that utilizes Pyth Network's price feed oracles to retrieve and process cryptocurrency price data.
Generated: DETERMINISTIC_8f9f84c2a0dbf9e3
Batch ID: 20250612_155024
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

// Import interfaces from Pyth Network
interface IPyth {
    function getPrice(bytes32 priceId) external view returns (int64 price, uint64 conf, int32 expo);
    function getUpdateFee(uint256 numUpdates) external view returns (uint256);
    function updatePriceFeeds(bytes[] calldata priceUpdateData) external payable;
}

contract CryptoPriceConsumer {
    // Address of the Pyth smart contract on the blockchain.
    address public pythContractAddress;

    // Event to log fetched price data.
    event PriceRetrieved(bytes32 indexed priceId, int64 price, uint64 confidence, int32 exponent);

    // Modifier to ensure a valid address for the Pyth contract.
    modifier validAddress(address _addr) {
        require(_addr != address(0), "Invalid address");
        _;
    }

    /**
     * @notice Constructor to set the Pyth contract address.
     * @param _pythContractAddress Address of the deployed Pyth contract.
     */
    constructor(address _pythContractAddress) validAddress(_pythContractAddress) {
        pythContractAddress = _pythContractAddress;
    }

    /**
     * @notice Fetches and processes the price feed for a given price ID.
     * @param priceId The unique identifier of the price feed.
     */
    function fetchPrice(bytes32 priceId) public {
        IPyth pythContract = IPyth(pythContractAddress);

        // Retrieve price data from Pyth contract
        (int64 price, uint64 confidence, int32 expo) = pythContract.getPrice(priceId);

        // Emit an event with the retrieved price data
        emit PriceRetrieved(priceId, price, confidence, expo);
    }

    /**
     * @notice Updates the price feeds using data provided by the off-chain source.
     * @param priceUpdateData Encoded price update data from off-chain providers.
     */
    function updatePriceFeeds(bytes[] calldata priceUpdateData) external payable {
        IPyth pythContract = IPyth(pythContractAddress);

        // Ensure the transaction includes the correct update fee
        uint256 updateFee = pythContract.getUpdateFee(priceUpdateData.length);
        require(msg.value == updateFee, "Insufficient update fee");

        // Update the price feeds using Pyth contract's function
        pythContract.updatePriceFeeds{value: msg.value}(priceUpdateData);
    }

    /**
     * @notice Allows updating the Pyth contract address by the owner (extendable via Ownable).
     * @param _newPythContractAddress Address of the new Pyth contract.
     */
    function setPythContractAddress(address _newPythContractAddress) external validAddress(_newPythContractAddress) {
        // In production, this function should be restricted to the contract owner.
        pythContractAddress = _newPythContractAddress;
    }

    /**
     * @notice Fallback function to prevent accidental ETH transfers.
     */
    fallback() external payable {
        revert("ETH transfers not allowed");
    }

    /**
     * @notice Receive function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("ETH transfers not allowed");
    }
}
```
