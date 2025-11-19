"""
Generated Code Metadata:
========================
Original URL: https://layer-1yd.pages.dev
Prompt: Create a Solidity contract for a LayerZero-based gaming token that supports seamless asset transfers between Ethereum and a custom blockchain network, referencing the `Beam` use case.
Generated: DETERMINISTIC_385132aa0292960b
Batch ID: 20250612_150226
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "../interfaces/ILayerZeroEndpoint.sol";
import "../interfaces/ILayerZeroReceiver.sol";

contract BeamToken is ERC20, ERC20Burnable, ReentrancyGuard, ILayerZeroReceiver {
    // Mapping of supported chains and their respective LayerZero endpoints
    mapping(uint256 => address) public supportedChains;

    // Mapping of message hashes to booleans for message tracking
    mapping(bytes32 => bool) public processedMessages;

    // LayerZero endpoint address
    address public immutable endpoint;

    // Token bridge address
    address public immutable bridge;

    /**
     * @notice Constructor for BeamToken contract
     * @param name_ Name of the token
     * @param symbol_ Symbol of the token
     * @param endpoint_ LayerZero endpoint address
     * @param bridge_ Token bridge address
     */
    constructor(string memory name_, string memory symbol_, address endpoint_, address bridge_) ERC20(name_, symbol_) {
        endpoint = endpoint_;
        bridge = bridge_;
    }

    /**
     * @notice Adds a supported chain and its LayerZero endpoint
     * @param chainId Chain ID of the supported chain
     * @param endpoint_ LayerZero endpoint address of the supported chain
     */
    function addSupportedChain(uint256 chainId, address endpoint_) public onlyOwner {
        supportedChains[chainId] = endpoint_;
    }

    /**
     * @notice Removes a supported chain
     * @param chainId Chain ID of the chain to remove
     */
    function removeSupportedChain(uint256 chainId) public onlyOwner {
        delete supportedChains[chainId];
    }

    /**
     * @notice Transfers tokens to a recipient on a different chain
     * @param recipient Address of the recipient on the destination chain
     * @param amount Amount of tokens to transfer
     * @param destinationChainId Chain ID of the destination chain
     * @param adapterParams Parameters for the adapter (e.g., fees)
     */
    function transferOut(address recipient, uint256 amount, uint256 destinationChainId, bytes memory adapterParams) public nonReentrant {
        require(supportedChains[destinationChainId] != address(0), "Destination chain not supported");

        // Burn tokens on the source chain
        _burn(msg.sender, amount);

        // Send tokens to the LayerZero endpoint
        ILayerZeroEndpoint(endpoint).send{value: 0}(
            destinationChainId,
            abi.encodePacked(msg.sender),
            abi.encode(recipient, amount),
            adapterParams,
            address(this)
        );
    }

    /**
     * @notice Receives tokens from a different chain
     * @param _srcChainId Chain ID of the source chain
     * @param _srcAddress Address of the sender on the source chain
     * @param _payload Payload containing the recipient and amount
     * @param _refundAddress Address to refund excess gas
     * @param _zroPaymentAddress Address to pay for LayerZero fees
     * @param _adapterParams Parameters for the adapter (e.g., fees)
     */
    function _nonReentrantReceive(
        uint256 _srcChainId,
        bytes calldata _srcAddress,
        bytes calldata _payload,
        address _refundAddress,
        address _zroPaymentAddress,
        bytes calldata _adapterParams
    ) internal virtual {
        // Decode the payload
        (address recipient, uint256 amount) = abi.decode(_payload, (address, uint256));

        // Mint tokens on the destination chain
        _mint(recipient, amount);

        // Mark the message as processed
        bytes32 messageHash = ILayerZeroEndpoint(endpoint).hashPayload(_srcChainId, _srcAddress, _payload);
        processedMessages[messageHash] = true;
    }

    /**
     * @notice Receives a message from LayerZero
     * @param _srcChainId Chain ID of the source chain
     * @param _srcAddress Address of the sender on the source chain
     * @param _payload Payload containing the recipient and amount
     * @param _refundAddress Address to refund excess gas
     * @param _zroPaymentAddress Address to pay for LayerZero fees
     * @param _adapterParams Parameters for the adapter (e.g., fees)
     */
    function lzReceive(
        uint256 _srcChainId,
        bytes calldata _srcAddress,
        bytes calldata _payload,
        address _refundAddress,
        address _zroPaymentAddress,
        bytes calldata _adapterParams
    ) external override {
        _nonReentrantReceive(_srcChainId, _srcAddress, _payload, _refundAddress, _zroPaymentAddress, _adapterParams);
    }
}
```
