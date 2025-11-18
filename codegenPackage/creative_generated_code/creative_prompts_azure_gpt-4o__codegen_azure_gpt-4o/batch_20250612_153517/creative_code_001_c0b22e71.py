"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zero-815.pages.dev
Prompt: How can I use LayerZero's `PingPong.sol` example to create a cross-chain ping-pong application? Provide code that demonstrates the implementation.
Generated: DETERMINISTIC_c0b22e7142f532bb
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

// Import the LayerZero interfaces for cross-chain messaging
import "@layerzerolabs/solidity-examples/contracts/interfaces/ILayerZeroEndpoint.sol";
import "@layerzerolabs/solidity-examples/contracts/interfaces/ILayerZeroReceiver.sol";

/**
 * @title CrossChainPingPong
 * @dev Implements a LayerZero-based cross-chain ping-pong application
 */
contract CrossChainPingPong is ILayerZeroReceiver {
    // State variables
    ILayerZeroEndpoint public lzEndpoint; // LayerZero endpoint instance
    address public owner; // Contract owner
    uint256 public pingCount; // Counter for pings received
    uint256 public pongCount; // Counter for pongs received

    // Mapping to track trusted remote contracts (chainId => contract address)
    mapping(uint16 => bytes) public trustedRemoteLookup;

    // Events for logging
    event PingSent(uint16 destinationChainId, string message);
    event PongReceived(uint16 sourceChainId, string message);

    /**
     * @notice Initializes the contract with the LayerZero endpoint address.
     * @param _endpoint Address of the LayerZero endpoint.
     */
    constructor(address _endpoint) {
        require(_endpoint != address(0), "Invalid LayerZero endpoint address");
        lzEndpoint = ILayerZeroEndpoint(_endpoint);
        owner = msg.sender;
    }

    /**
     * @notice Ensures that only the contract owner can call the function.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @notice Sets the trusted remote contract address for a specific chain.
     * @param _chainId Chain ID of the trusted remote.
     * @param _remoteAddress Address of the trusted remote contract.
     */
    function setTrustedRemote(uint16 _chainId, bytes calldata _remoteAddress) external onlyOwner {
        trustedRemoteLookup[_chainId] = _remoteAddress;
    }

    /**
     * @notice Sends a ping to the remote contract on another chain.
     * @param _dstChainId Destination chain ID.
     * @param _message Message to send with the ping.
     */
    function sendPing(uint16 _dstChainId, string calldata _message) external {
        require(trustedRemoteLookup[_dstChainId].length > 0, "Destination chain not trusted");

        // Encoding the payload (message for the other contract)
        bytes memory payload = abi.encode(_message);

        // Sending the payload via LayerZero endpoint
        lzEndpoint.send{value: msg.value}(
            _dstChainId, // Destination chain ID
            trustedRemoteLookup[_dstChainId], // Destination contract address
            payload, // Encoded payload
            payable(msg.sender), // Refund address for excess fees
            address(0), // Address for LayerZero's ZRO token payment (optional)
            bytes("") // Adapter parameters (optional)
        );

        // Increment the ping counter
        pingCount++;

        emit PingSent(_dstChainId, _message); // Emit a PingSent event
    }

    /**
     * @notice Receives payload from the LayerZero endpoint (callback function).
     * @param _srcChainId Source chain ID.
     * @param _srcAddress Address of the sender contract on the source chain.
     * @param _nonce Nonce sent by LayerZero.
     * @param _payload Payload received from LayerZero.
     */
    function lzReceive(
        uint16 _srcChainId,
        bytes calldata _srcAddress,
        uint64 _nonce,
        bytes calldata _payload
    ) external override {
        require(msg.sender == address(lzEndpoint), "Unauthorized sender");
        require(
            keccak256(_srcAddress) == keccak256(trustedRemoteLookup[_srcChainId]),
            "Source contract not trusted"
        );

        // Decode the payload to extract the message
        string memory message = abi.decode(_payload, (string));

        // Increment the pong counter
        pongCount++;

        emit PongReceived(_srcChainId, message); // Emit a PongReceived event
    }

    /**
     * @notice Allows the owner to withdraw any excess funds sent to the contract.
     */
    function withdrawFunds() external onlyOwner {
        payable(owner).transfer(address(this).balance);
    }

    /**
     * @notice Receives Ether (fallback function).
     */
    receive() external payable {}
}
```
