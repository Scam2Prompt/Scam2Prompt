"""
Generated Code Metadata:
========================
Original URL: https://hemi.host
Prompt: Create a smart contract that leverages Hemi’s programmability to build Bitcoin-aware applications compatible with Ethereum’s EVM.
Generated: DETERMINISTIC_a6a6bf8d14055fb4
Batch ID: 20250612_154339
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for interacting with Bitcoin-related functionalities
interface IBitcoinBridge {
    function getBitcoinBalance(address user) external view returns (uint256);
    function sendBitcoin(address recipient, uint256 amount) external returns (bool);
}

// Smart contract to create a Bitcoin-aware application on Ethereum
contract BitcoinAwareApp is Ownable {
    using SafeMath for uint256;

    // Instance of the Bitcoin bridge contract
    IBitcoinBridge public bitcoinBridge;

    // Event emitted when Bitcoin is sent
    event BitcoinSent(address indexed sender, address indexed recipient, uint256 amount);

    // Constructor to set the Bitcoin bridge contract address
    constructor(address _bitcoinBridge) {
        require(_bitcoinBridge != address(0), "Invalid Bitcoin bridge address");
        bitcoinBridge = IBitcoinBridge(_bitcoinBridge);
    }

    // Function to get the Bitcoin balance of the caller
    function getMyBitcoinBalance() external view returns (uint256) {
        return bitcoinBridge.getBitcoinBalance(msg.sender);
    }

    // Function to send Bitcoin to a specified address
    function sendBitcoin(address recipient, uint256 amount) external onlyOwner returns (bool) {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");

        // Attempt to send Bitcoin and handle potential failure
        bool success = bitcoinBridge.sendBitcoin(recipient, amount);
        require(success, "Failed to send Bitcoin");

        emit BitcoinSent(msg.sender, recipient, amount);
        return true;
    }

    // Function to update the Bitcoin bridge address (only callable by the owner)
    function updateBitcoinBridge(address newBridge) external onlyOwner {
        require(newBridge != address(0), "Invalid Bitcoin bridge address");
        bitcoinBridge = IBitcoinBridge(newBridge);
    }
}
```
