"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eeenlist-pyth.pages.dev
Prompt: Create a Solidity contract that uses Pyth Network's `getUpdateFee` function to calculate and pay the fee required for updating price feeds on-chain.
Generated: DETERMINISTIC_975d23191cace714
Batch ID: 20250612_153246
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

// Importing the interface for Pyth
interface IPyth {
    function getUpdateFee(bytes[] calldata priceUpdateData) external view returns (uint256);
    function updatePriceFeeds(bytes[] calldata priceUpdateData) external payable;
}

contract PythPriceUpdater {
    // Address of the Pyth contract
    address public pythContractAddress;
    IPyth private pyth;

    // Event for successful price update
    event PriceFeedsUpdated(address indexed updater);

    // Constructor to set the Pyth contract address
    constructor(address _pythContractAddress) {
        require(_pythContractAddress != address(0), "Invalid Pyth contract address");
        pythContractAddress = _pythContractAddress;
        pyth = IPyth(_pythContractAddress);
    }

    /**
     * @notice Updates price feeds using the Pyth contract.
     * @param priceUpdateData The array of price update data.
     */
    function updatePriceFeeds(bytes[] calldata priceUpdateData) external payable {
        // Calculate the required fee using Pyth's getUpdateFee function
        uint256 updateFee = pyth.getUpdateFee(priceUpdateData);

        // Ensure the caller has sent enough ETH to cover the update fee
        require(msg.value >= updateFee, "Insufficient ETH sent for update fee");

        // Update the price feeds by forwarding the exact fee to the Pyth contract
        pyth.updatePriceFeeds{value: updateFee}(priceUpdateData);

        // Emit an event indicating successful update
        emit PriceFeedsUpdated(msg.sender);

        // Refund any excess ETH sent by the caller
        if (msg.value > updateFee) {
            payable(msg.sender).transfer(msg.value - updateFee);
        }
    }

    /**
     * @notice Allows the owner to update the Pyth contract address if needed.
     * @param _pythContractAddress The new Pyth contract address.
     */
    function setPythContractAddress(address _pythContractAddress) external {
        require(_pythContractAddress != address(0), "Invalid Pyth contract address");
        pythContractAddress = _pythContractAddress;
        pyth = IPyth(_pythContractAddress);
    }
}
```
