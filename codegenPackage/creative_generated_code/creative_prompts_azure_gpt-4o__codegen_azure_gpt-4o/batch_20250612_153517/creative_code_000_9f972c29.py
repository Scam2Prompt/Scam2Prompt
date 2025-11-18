"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zero-815.pages.dev
Prompt: Write a Solidity smart contract that uses LayerZero's `OmniCounter.sol` example to implement a cross-chain counter. Include code for sending and receiving messages between chains.
Generated: DETERMINISTIC_9f972c2963e5c8c5
Batch ID: 20250612_153517
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

// Import LayerZero interfaces and libraries
import "@layerzerolabs/solidity-examples/contracts/lzApp/NonblockingLzApp.sol";

/// @title CrossChainCounter
/// @dev This contract extends the OmniCounter example from LayerZero to implement a cross-chain counter
contract CrossChainCounter is NonblockingLzApp {
    // Counter value
    uint256 public counter;

    /// @dev Mapping to track the number of messages received from specific source chains
    mapping(uint16 => uint256) public messageCountFromChain;

    /// @param _lzEndpoint The LayerZero endpoint contract address
    constructor(address _lzEndpoint) NonblockingLzApp(_lzEndpoint) {}

    /// @notice Increment the counter and send a message to another chain
    /// @param _dstChainId The destination chain ID
    /// @param _payload Data to send (in this case, increment instruction)
    function sendIncrement(uint16 _dstChainId, bytes calldata _payload) external payable {
        // Ensure enough native token value is sent for LayerZero message fees
        require(msg.value > 0, "Insufficient value for LayerZero fees");

        // Send the increment message to the destination chain
        _lzSend(
            _dstChainId,   // Destination chain id
            _payload,      // Payload containing the increment instruction
            payable(msg.sender), // Refund address for excess fees
            address(0),    // No ZRO payment (LayerZero Relayer)
            bytes("")      // Empty adapter parameters
        );
    }

    /// @dev Handles incoming messages and increments the counter
    /// @param _srcChainId The chain ID of the source chain
    /// @param _srcAddress The address of the sender on the source chain
    /// @param _payload The message payload
    function _nonblockingLzReceive(
        uint16 _srcChainId,
        bytes memory _srcAddress,
        uint64 /*_nonce*/,
        bytes memory _payload
    ) internal override {
        // Decode the payload (assume it's an increment instruction)
        uint256 incrementValue = abi.decode(_payload, (uint256));

        // Increment the local counter
        counter += incrementValue;

        // Track the number of messages received from this chain
        messageCountFromChain[_srcChainId] += 1;

        emit CounterUpdated(_srcChainId, incrementValue, counter);
    }

    /// @notice Returns the estimated fees to send a message
    /// @param _dstChainId The destination chain ID
    /// @param _payload The payload to send
    /// @return nativeFee The native fee
    /// @return zroFee The ZRO fee (always zero in this implementation)
    function estimateSendFee(uint16 _dstChainId, bytes calldata _payload) external view returns (uint nativeFee, uint zroFee) {
        return lzEndpoint.estimateFees(
            _dstChainId,
            address(this),
            _payload,
            false, // Assume no ZRO payment
            bytes("") // Empty adapter parameters
        );
    }

    /// @dev Event emitted when the counter is updated
    /// @param srcChainId The chain ID of the source chain
    /// @param incrementValue The value added to the counter
    /// @param newCounterValue The new value of the counter
    event CounterUpdated(uint16 srcChainId, uint256 incrementValue, uint256 newCounterValue);

    /// @notice Fallback function to allow contract to receive ETH
    receive() external payable {}
}
```
