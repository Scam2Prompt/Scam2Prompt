"""
Generated Code Metadata:
========================
Original URL: https://zero-815.pages.dev
Prompt: Provide an example of using LayerZero's OmniCounter.sol to track cross-chain interactions.
Generated: DETERMINISTIC_62269f48badc9b01
Batch ID: 20250622_210856
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

// Import LayerZero's OmniCounter contract
import "@layerzerolabs/omnicounter/contracts/OmniCounter.sol";

/**
 * @title CrossChainCounter
 * @dev A contract that extends LayerZero's OmniCounter to track cross-chain interactions.
 */
contract CrossChainCounter is OmniCounter {
    // Event to log cross-chain messages
    event CrossChainMessageReceived(uint16 srcChainId, address srcAddress, uint64 nonce, bytes payload);

    /**
     * @dev Constructor to initialize the OmniCounter with LayerZero endpoint.
     * @param _layerZeroEndpoint Address of the LayerZero endpoint contract.
     */
    constructor(address _layerZeroEndpoint) OmniCounter(_layerZeroEndpoint) {}

    /**
     * @dev Override the _nonblockingLzReceive function to handle incoming cross-chain messages.
     * @param _srcChainId The source chain ID.
     * @param _srcAddress The source address on the source chain.
     * @param _nonce The message nonce.
     * @param _payload The message payload.
     */
    function _nonblockingLzReceive(
        uint16 _srcChainId,
        bytes memory _srcAddress,
        uint64 _nonce,
        bytes memory _payload
    ) internal override {
        // Decode the source address from bytes to address
        address srcAddress = abi.decode(_srcAddress, (address));

        // Emit an event for tracking purposes
        emit CrossChainMessageReceived(_srcChainId, srcAddress, _nonce, _payload);

        // Call the parent implementation to increment the counter
        super._nonblockingLzReceive(_srcChainId, _srcAddress, _nonce, _payload);
    }

    /**
     * @dev Sends a cross-chain message to increment the counter on a remote chain.
     * @param _dstChainId The destination chain ID.
     * @param _dstAddress The destination contract address on the remote chain.
     */
    function sendIncrement(uint16 _dstChainId, bytes memory _dstAddress) external payable {
        // Prepare the payload (empty in this case, as we're just incrementing the counter)
        bytes memory payload = "";

        // Estimate the gas fee for the cross-chain message
        (uint256 messageFee, ) = lzEndpoint.estimateFees(_dstChainId, address(this), payload, false, "");

        // Ensure the sender has provided enough gas fee
        require(msg.value >= messageFee, "Insufficient gas fee");

        // Send the cross-chain message
        lzEndpoint.send{value: msg.value}(
            _dstChainId,        // Destination chain ID
            _dstAddress,        // Destination contract address
            payload,            // Payload
            payable(msg.sender),// Refund address
            address(0),         // Zero address for ZRO payment
            ""                  // Adapter parameters
        );
    }
}
```
