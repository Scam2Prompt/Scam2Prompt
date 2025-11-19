"""
Generated Code Metadata:
========================
Original URL: https://zero-815.pages.dev
Prompt: Provide a detailed example of how to calculate and set the relayer fee for LayerZero's cross-chain messaging protocol in a Solidity contract.
Generated: DETERMINISTIC_f9d4db9f36ad8e29
Batch ID: 20250612_153517
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

import "@layerzerolabs/solidity-examples/contracts/lzApp/NonblockingLzApp.sol";

contract LayerZeroRelayerFeeExample is NonblockingLzApp {
    // Chain IDs for reference
    uint16 public constant DESTINATION_CHAIN_ID = 101; // Example: Ethereum Mainnet
    uint16 public constant SOURCE_CHAIN_ID = 102; // Example: BSC

    // Message types
    uint16 public constant MESSAGE_TYPE = 1;

    // Estimated gas amount for the destination chain execution
    uint256 public constant DESTINATION_GAS = 200000;

    constructor(address _lzEndpoint) NonblockingLzApp(_lzEndpoint) {}

    /**
     * @notice Calculates the relayer fee for sending a message to another chain
     * @param _destinationChainId The chain ID of the destination
     * @param _messageType The type of message being sent
     * @param _gasAmount The gas amount needed for execution on destination
     * @param _payload The message payload
     * @return fee The estimated relayer fee in native tokens
     */
    function estimateRelayerFee(
        uint16 _destinationChainId,
        uint16 _messageType,
        uint256 _gasAmount,
        bytes memory _payload
    ) public view returns (uint256 fee) {
        (fee, ) = lzEndpoint.estimateFees(
            _destinationChainId,
            address(this),
            _payload,
            false,
            _getAdapterParams(_gasAmount)
        );
        return fee;
    }

    /**
     * @notice Sends a cross-chain message with proper relayer fee
     * @param _destinationChainId The chain ID of the destination
     * @param _message The message to send
     * @param _gasAmount The gas amount needed for execution on destination
     */
    function sendCrossChainMessage(
        uint16 _destinationChainId,
        bytes memory _message,
        uint256 _gasAmount
    ) external payable {
        require(msg.value > 0, "LayerZeroRelayerFeeExample: msg.value must be > 0");

        bytes memory adapterParams = _getAdapterParams(_gasAmount);

        (uint256 fee, ) = lzEndpoint.estimateFees(
            _destinationChainId,
            address(this),
            _message,
            false,
            adapterParams
        );

        require(msg.value >= fee, "LayerZeroRelayerFeeExample: Insufficient fee");

        _lzSend(
            _destinationChainId,
            _message,
            payable(msg.sender),
            address(0x0),
            adapterParams,
            fee
        );
    }

    /**
     * @notice Internal function to create adapter parameters
     * @param _gasAmount The gas amount needed for execution on destination
     * @return The encoded adapter parameters
     */
    function _getAdapterParams(uint256 _gasAmount) internal pure returns (bytes memory) {
        return abi.encodePacked(uint16(1), _gasAmount);
    }

    /**
     * @notice Override the _nonblockingLzReceive function from NonblockingLzApp
     * @param _srcChainId The source chain ID
     * @param _srcAddress The source address
     * @param _nonce The message nonce
     * @param _payload The message payload
     */
    function _nonblockingLzReceive(
        uint16 _srcChainId,
        bytes memory _srcAddress,
        uint64 _nonce,
        bytes memory _payload
    ) internal override {
        // Handle the received message here
        // This is where you would implement your cross-chain message processing logic
    }

    /**
     * @notice Withdraws native tokens from the contract
     * @param _to The address to withdraw to
     * @param _amount The amount to withdraw
     */
    function withdraw(address payable _to, uint256 _amount) external onlyOwner {
        require(_amount <= address(this).balance, "LayerZeroRelayerFeeExample: Insufficient balance");
        _to.transfer(_amount);
    }
}
```
