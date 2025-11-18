"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://layer-1yd.pages.dev
Prompt: Write a Solidity contract that uses LayerZero's `OApp` to implement a generic message-passing interface for decentralized applications.
Generated: DETERMINISTIC_cfeb7bb980dee3e0
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

// Import LayerZero's OApp interface
import "@layerzerolabs/solidity-examples/contracts/interfaces/IOmnichainApplication.sol";
import "@layerzerolabs/solidity-examples/contracts/libraries/BytesLib.sol";
import "@layerzerolabs/solidity-examples/contracts/lzApp/NonblockingLzApp.sol";

/**
 * @title GenericMessagePassing
 * @dev A message-passing contract powered by LayerZero's Omnichain Application Framework
 */
contract GenericMessagePassing is NonblockingLzApp {
    using BytesLib for bytes;

    // Event to log incoming messages
    event MessageReceived(uint16 srcChainId, address srcAddress, bytes payload);

    // Event to log outgoing messages
    event MessageSent(uint16 dstChainId, bytes payload);

    /**
     * @dev Constructor for the contract.
     * @param _layerZeroEndpoint Address of the LayerZero endpoint on the current chain.
     */
    constructor(address _layerZeroEndpoint) NonblockingLzApp(_layerZeroEndpoint) {}

    /**
     * @dev Sends a message to another chain.
     * @param dstChainId The LayerZero chain ID of the destination chain.
     * @param payload The message payload to send.
     * @param refundAddress Address to refund excess gas fees.
     * @param zroPaymentAddress Address to pay for transaction fees in ZRO tokens, or address(0) for ETH.
     * @param adapterParams LayerZero adapter parameters for gas and other settings.
     */
    function sendMessage(
        uint16 dstChainId,
        bytes memory payload,
        address payable refundAddress,
        address zroPaymentAddress,
        bytes memory adapterParams
    ) external payable {
        require(payload.length > 0, "GenericMessagePassing: Payload cannot be empty");

        // Log the outgoing message
        emit MessageSent(dstChainId, payload);

        // Call LayerZero's send function to send the message
        _lzSend(
            dstChainId,
            payload,
            refundAddress,
            zroPaymentAddress,
            adapterParams,
            msg.value
        );
    }

    /**
     * @dev Handles incoming LayerZero messages. Overridden from NonblockingLzApp.
     * @param srcChainId The LayerZero chain ID from which the message originated.
     * @param srcAddress The address of the contract that sent the message on the source chain.
     * @param payload The message payload.
     */
    function _nonblockingLzReceive(
        uint16 srcChainId,
        bytes memory srcAddress,
        uint64, // nonce (unused, but required by the interface)
        bytes memory payload
    ) internal override {
        // Decode the source address
        address senderAddress = srcAddress.toAddress(0);

        // Log the incoming message
        emit MessageReceived(srcChainId, senderAddress, payload);

        // You can add further processing logic for the payload here
    }

    /**
     * @dev Allows the contract owner to withdraw funds accidentally sent to this contract.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "GenericMessagePassing: No funds to withdraw");
        (bool success, ) = msg.sender.call{value: balance}("");
        require(success, "GenericMessagePassing: Withdrawal failed");
    }

    /**
     * @dev Fallback function to accept ETH deposits.
     */
    receive() external payable {}

    /**
     * @dev Modifier to restrict access to contract owner functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner(), "GenericMessagePassing: Caller is not the owner");
        _;
    }

    /**
     * @dev Returns the address of the contract owner.
     */
    function owner() public view returns (address) {
        return address(uint160(uint256(keccak256(abi.encodePacked(blockhash(block.number - 1))))));
    }
}
```
