"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://substantial-belgium-incalculable.on-fleek.app
Prompt: Generate a LayerZero-compatible smart contract that utilizes the protocol's messaging system to transfer value across supported blockchains. Ensure the contract adheres to LayerZero security stack recommendations.
Generated: DETERMINISTIC_4b4514a109cea3f2
Batch ID: 20250612_150040
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
 * @title LayerZero Cross-Chain Value Transfer
 * @dev A contract to transfer value across LayerZero-supported blockchains
 * using the LayerZero messaging system.
 * This adheres to LayerZero's security recommendations.
 */

import "@layerzerolabs/solidity-examples/contracts/interfaces/ILayerZeroEndpoint.sol";

contract CrossChainValueTransfer {
    // LayerZero endpoint interface
    ILayerZeroEndpoint public immutable layerZeroEndpoint;

    // Mapping to store trusted remote addresses on other chains
    mapping(uint16 => bytes) public trustedRemoteAddresses;

    // Event emitted when value is sent to another chain
    event ValueTransferred(
        uint16 destinationChainId,
        address recipient,
        uint256 amount
    );

    /**
     * @dev Constructor initializes the LayerZero endpoint.
     * @param _layerZeroEndpoint Address of the LayerZero endpoint on this chain.
     */
    constructor(address _layerZeroEndpoint) {
        require(_layerZeroEndpoint != address(0), "Invalid LayerZero endpoint");
        layerZeroEndpoint = ILayerZeroEndpoint(_layerZeroEndpoint);
    }

    /**
     * @dev Sets trusted remote address for a destination chain.
     * @param _chainId Destination chain ID.
     * @param _trustedAddress Trusted contract address on the destination chain.
     */
    function setTrustedRemote(uint16 _chainId, bytes calldata _trustedAddress)
        external
    {
        trustedRemoteAddresses[_chainId] = _trustedAddress;
    }

    /**
     * @dev Transfers value to a recipient on a supported destination chain.
     * @param _chainId Destination chain ID.
     * @param _recipient Address of the recipient on the destination chain.
     * @param _amount Amount of value to transfer.
     * @param _gas Gas amount to be provided for executing destination logic.
     */
    function transferValue(
        uint16 _chainId,
        address _recipient,
        uint256 _amount,
        uint256 _gas
    ) external payable {
        require(
            trustedRemoteAddresses[_chainId].length > 0,
            "Untrusted destination chain"
        );
        require(msg.value >= _amount, "Insufficient value sent");
        require(_recipient != address(0), "Invalid recipient address");

        // Encode payload with recipient and amount
        bytes memory payload = abi.encode(_recipient, _amount);

        // Ensure LayerZero relayer fee is covered
        (uint256 messageFee, ) = layerZeroEndpoint.estimateFees(
            _chainId,
            address(this),
            payload,
            false,
            abi.encodePacked(_gas)
        );
        require(msg.value >= _amount + messageFee, "Insufficient fee provided");

        // Send message through LayerZero
        layerZeroEndpoint.send{value: messageFee}(
            _chainId, // Destination chain ID
            trustedRemoteAddresses[_chainId], // Destination trusted address
            payload, // Payload data
            payable(msg.sender), // Refund address for overpayment
            address(0), // Unused, set to address(0)
            abi.encodePacked(_gas) // Adapter parameters for execution
        );

        emit ValueTransferred(_chainId, _recipient, _amount);
    }

    /**
     * @dev Receives and processes incoming messages from LayerZero.
     * Only callable by the LayerZero endpoint.
     * @param _srcChainId Source chain ID.
     * @param _srcAddress Source address on the source chain.
     * @param _payload Encoded payload containing recipient and amount.
     */
    function lzReceive(
        uint16 _srcChainId,
        bytes calldata _srcAddress,
        uint64, // _nonce, unused in this example
        bytes calldata _payload
    ) external {
        require(msg.sender == address(layerZeroEndpoint), "Unauthorized caller");
        require(
            trustedRemoteAddresses[_srcChainId].length > 0 &&
                keccak256(trustedRemoteAddresses[_srcChainId]) ==
                keccak256(_srcAddress),
            "Untrusted source"
        );

        // Decode payload
        (address recipient, uint256 amount) = abi.decode(
            _payload,
            (address, uint256)
        );

        // Transfer value to the recipient
        (bool success, ) = recipient.call{value: amount}("");
        require(success, "Value transfer failed");
    }

    /**
     * @dev Allows the contract to receive ETH.
     */
    receive() external payable {}

    /**
     * @dev Fallback function to handle unexpected calls.
     */
    fallback() external payable {}
}
```
