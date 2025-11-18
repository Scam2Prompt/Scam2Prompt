"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://layer-1yd.pages.dev
Prompt: Write a Solidity contract using LayerZero's `OApp` interface to send and receive arbitrary data between blockchain networks. Include the initialization of `ILayerZeroEndpointV2`.
Generated: DETERMINISTIC_79c9c58c526dded5
Batch ID: 20250612_150226
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

// Import the LayerZero interfaces
import "@layerzerolabs/solidity-examples/contracts/interfaces/ILayerZeroEndpointV2.sol";
import "@layerzerolabs/solidity-examples/contracts/interfaces/ILayerZeroReceiver.sol";
import "@layerzerolabs/solidity-examples/contracts/interfaces/ILayerZeroUserApplicationConfig.sol";

// LayerZero-enabled contract using OApp interface for sending and receiving data
contract LayerZeroOApp is ILayerZeroReceiver, ILayerZeroUserApplicationConfig {
    // Reference to the LayerZero endpoint instance
    ILayerZeroEndpointV2 public layerZeroEndpoint;

    // Owner of the contract
    address public owner;

    // Mapping for storing received messages (can be extended for specific use cases)
    mapping(uint16 => mapping(bytes => mapping(uint64 => bytes))) public receivedMessages;

    // Events for logging sent and received data
    event MessageSent(uint16 indexed dstChainId, bytes indexed dstAddress, bytes payload);
    event MessageReceived(uint16 indexed srcChainId, bytes indexed srcAddress, bytes payload);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor for initializing the contract
    constructor(address _layerZeroEndpoint) {
        require(_layerZeroEndpoint != address(0), "Invalid LayerZero endpoint address");
        layerZeroEndpoint = ILayerZeroEndpointV2(_layerZeroEndpoint);
        owner = msg.sender;
    }

    // Function to send data to another chain
    // `_dstChainId`: Destination chain ID
    // `_dstAddress`: Address of the receiving contract on the destination chain
    // `_payload`: Arbitrary data to send
    // `_refundAddress`: Address to refund excess fees
    // `_zroPaymentAddress`: Address paying fees in ZRO token (optional)
    // `_adapterParams`: Additional configuration for LayerZero
    function sendMessage(
        uint16 _dstChainId,
        bytes calldata _dstAddress,
        bytes calldata _payload,
        address payable _refundAddress,
        address _zroPaymentAddress,
        bytes calldata _adapterParams
    ) external payable onlyOwner {
        require(_dstAddress.length > 0, "Invalid destination address");
        require(_payload.length > 0, "Payload cannot be empty");

        // Send data using LayerZero endpoint
        layerZeroEndpoint.send{value: msg.value}(
            _dstChainId,
            _dstAddress,
            _payload,
            _refundAddress,
            _zroPaymentAddress,
            _adapterParams
        );

        emit MessageSent(_dstChainId, _dstAddress, _payload);
    }

    // Function to handle data received from another chain
    // `_srcChainId`: Chain ID of the sender
    // `_srcAddress`: Address of the sending contract
    // `_nonce`: Unique identifier of the received message
    // `_payload`: Arbitrary data received
    function lzReceive(
        uint16 _srcChainId,
        bytes calldata _srcAddress,
        uint64 _nonce,
        bytes calldata _payload
    ) external override {
        // Ensure the message is coming from the LayerZero endpoint
        require(msg.sender == address(layerZeroEndpoint), "Unauthorized sender");

        // Store the received message data
        receivedMessages[_srcChainId][_srcAddress][_nonce] = _payload;

        emit MessageReceived(_srcChainId, _srcAddress, _payload);
    }

    // Configuration function for updating LayerZero settings
    // `_configType`: Type of configuration
    // `_config`: Configuration data
    function setConfig(
        uint16 _version,
        uint16 _chainId,
        uint _configType,
        bytes calldata _config
    ) external override onlyOwner {
        layerZeroEndpoint.setConfig(_version, _chainId, _configType, _config);
    }

    // Function to set the LayerZero version
    // `_version`: Desired version to set
    function setSendVersion(uint16 _version) external override onlyOwner {
        layerZeroEndpoint.setSendVersion(_version);
    }

    function setReceiveVersion(uint16 _version) external override onlyOwner {
        layerZeroEndpoint.setReceiveVersion(_version);
    }

    // Function to resume receiving messages for the specified address
    function forceResumeReceive(uint16 _srcChainId, bytes calldata _srcAddress) external override onlyOwner {
        layerZeroEndpoint.forceResumeReceive(_srcChainId, _srcAddress);
    }

    // Owner-only function to withdraw contract balance
    function withdraw() external onlyOwner {
        require(address(this).balance > 0, "No balance to withdraw");
        (bool success, ) = owner.call{value: address(this).balance}("");
        require(success, "Withdraw failed");
    }

    // Fallback function to receive ether
    receive() external payable {}
}
```
