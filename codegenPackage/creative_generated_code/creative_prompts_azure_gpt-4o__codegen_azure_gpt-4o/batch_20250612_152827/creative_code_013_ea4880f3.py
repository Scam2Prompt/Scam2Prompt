"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pulsechain-app.pages.dev
Prompt: Generate code to bridge PLS from PulseChain to Ethereum using the ETHbridge contract, ensuring a 1:1 ratio issuance of "PLS from PulseChain."
Generated: DETERMINISTIC_ea4880f3d9391b1e
Batch ID: 20250612_152827
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
 * @title PLSBridge
 * @dev A contract to bridge PLS from PulseChain to Ethereum
 * using a 1:1 issuance mechanism via the ETHbridge contract.
 */
contract PLSBridge {
    // Address of the Ethereum bridge contract
    address public ethBridgeContract;

    // Event emitted when PLS is bridged
    event PLSBridged(address indexed from, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the ETH bridge address.
     * @param _ethBridgeContract Address of the Ethereum bridge contract.
     */
    constructor(address _ethBridgeContract) {
        require(_ethBridgeContract != address(0), "ETH bridge address cannot be zero");
        ethBridgeContract = _ethBridgeContract;
    }

    /**
     * @dev Function to bridge PLS to Ethereum.
     * @param amount Amount of PLS to bridge (1:1 issuance).
     */
    function bridgePLS(uint256 amount) external payable {
        // Validate that the amount is greater than zero
        require(amount > 0, "Amount must be greater than zero");
        
        // Validate that the sender has sent the correct amount of PLS
        require(msg.value == amount, "Sent value must match the specified amount");

        // Emit the event to notify bridging
        emit PLSBridged(msg.sender, amount);

        // Forward PLS to the Ethereum bridge contract
        (bool success, ) = ethBridgeContract.call{value: amount}("");
        require(success, "Failed to transfer PLS to ETH bridge contract");
    }

    /**
     * @dev Fallback function to receive ETH (in case needed for bridge interaction).
     */
    fallback() external payable {}

    /**
     * @dev Receive function to handle direct transfers to the contract.
     */
    receive() external payable {}
}
```
