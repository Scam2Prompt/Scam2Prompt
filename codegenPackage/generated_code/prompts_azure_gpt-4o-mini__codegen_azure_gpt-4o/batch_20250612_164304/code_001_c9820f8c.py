"""
Generated Code Metadata:
========================
Original URL: https://layer-1yd.pages.dev
Prompt: Write a Solidity contract that utilizes LayerZero's OFT standard to transfer fungible tokens across multiple blockchains without using liquidity pools.
Generated: DETERMINISTIC_c9820f8c3f8ead29
Batch ID: 20250612_164304
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

// Import LayerZero's OFT standard
import "@layerzerolabs/oft/contracts/NonblockingLzApp.sol";
import "@layerzerolabs/oft/contracts/token/oft/OFT.sol";

/**
 * @title CrossChainToken
 * @dev A contract that implements LayerZero's OFT standard for transferring fungible tokens across multiple blockchains.
 */
contract CrossChainToken is OFT {
    /**
     * @dev Constructor to initialize the token with name, symbol, and LayerZero endpoint.
     * @param _name The name of the token.
     * @param _symbol The symbol of the token.
     * @param _lzEndpoint The LayerZero endpoint address.
     */
    constructor(
        string memory _name,
        string memory _symbol,
        address _lzEndpoint
    ) OFT(_name, _symbol, _lzEndpoint) {
        // Token initialized with LayerZero endpoint
    }

    /**
     * @dev Override the _nonblockingLzReceive function to handle incoming cross-chain messages.
     * @param _srcChainId The source chain ID.
     * @param _srcAddress The source address.
     * @param _nonce The message nonce.
     * @param _payload The message payload.
     */
    function _nonblockingLzReceive(
        uint16 _srcChainId,
        bytes memory _srcAddress,
        uint64 _nonce,
        bytes memory _payload
    ) internal override {
        // Handle incoming cross-chain messages
        // Decode the payload and process the message
        // Example: Transfer tokens to the recipient
    }

    /**
     * @dev Sends tokens to another chain.
     * @param _dstChainId The destination chain ID.
     * @param _toAddress The recipient address on the destination chain.
     * @param _amount The amount of tokens to send.
     * @param _refundAddress The address to refund excess fees.
     * @param _zroPaymentAddress The address to pay for LayerZero fees in ZRO tokens.
     * @param _adapterParams Additional parameters for LayerZero adapter.
     */
    function sendTokens(
        uint16 _dstChainId,
        bytes memory _toAddress,
        uint256 _amount,
        address payable _refundAddress,
        address _zroPaymentAddress,
        bytes memory _adapterParams
    ) external payable {
        // Ensure the sender has enough tokens
        require(balanceOf(msg.sender) >= _amount, "Insufficient balance");

        // Burn tokens on the source chain
        _burn(msg.sender, _amount);

        // Send the message to the destination chain
        _lzSend(
            _dstChainId,
            abi.encode(_toAddress, _amount),
            _refundAddress,
            _zroPaymentAddress,
            _adapterParams
        );
    }

    /**
     * @dev Handles incoming token transfers from other chains.
     * @param _toAddress The recipient address on the current chain.
     * @param _amount The amount of tokens to mint.
     */
    function _handleIncomingTransfer(bytes memory _toAddress, uint256 _amount) internal {
        // Decode the recipient address
        address recipient = abi.decode(_toAddress, (address));

        // Mint tokens to the recipient
        _mint(recipient, _amount);
    }
}
```
