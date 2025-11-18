"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zero-815.pages.dev
Prompt: Provide a detailed example of how to calculate and set the relayer fee for LayerZero's cross-chain messaging protocol in a Solidity contract.
Generated: DETERMINISTIC_f9d4db9f36ad8e29
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

/**
 * @title LayerZeroFeeManager
 * @dev This contract calculates and sets the relayer fee for LayerZero's cross-chain messaging protocol.
 * It uses LayerZero's ILayerZeroEndpoint interface for fee estimation.
 */
interface ILayerZeroEndpoint {
    function estimateFees(
        uint16 _dstChainId,
        address _userApplication,
        bytes calldata _payload,
        bool _payInZRO,
        bytes calldata _adapterParams
    ) external view returns (uint256 nativeFee, uint256 zroFee);
}

contract LayerZeroFeeManager {
    // LayerZero Endpoint address (this should be configured based on your environment)
    ILayerZeroEndpoint public immutable layerZeroEndpoint;

    // The address of the contract owner
    address public owner;

    // Mapping to store relayer fees for specific chains
    mapping(uint16 => uint256) public relayerFees;

    // Modifier to restrict certain functions to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the LayerZero endpoint address.
     * @param _layerZeroEndpoint The address of LayerZero's endpoint contract.
     */
    constructor(address _layerZeroEndpoint) {
        require(_layerZeroEndpoint != address(0), "Invalid endpoint address");
        owner = msg.sender;
        layerZeroEndpoint = ILayerZeroEndpoint(_layerZeroEndpoint);
    }

    /**
     * @dev Function to calculate the relayer fee for a specific chain.
     * @param _dstChainId The destination chain ID.
     * @param _payload The payload to be sent to the destination chain.
     * @param _adapterParams Adapter parameters used for messaging.
     * @return nativeFee The calculated native fee.
     */
    function calculateRelayerFee(
        uint16 _dstChainId,
        bytes calldata _payload,
        bytes calldata _adapterParams
    ) external view returns (uint256 nativeFee) {
        // Estimate the fee using LayerZero's endpoint contract
        (uint256 _nativeFee, ) = layerZeroEndpoint.estimateFees(
            _dstChainId,
            address(this),
            _payload,
            false, // payInZRO (false indicates payment in native tokens)
            _adapterParams
        );

        return _nativeFee;
    }

    /**
     * @dev Function to set the relayer fee for a specific destination chain.
     * @param _dstChainId The destination chain ID.
     * @param _payload The payload to be sent to the destination chain.
     * @param _adapterParams Adapter parameters used for messaging.
     */
    function setRelayerFee(
        uint16 _dstChainId,
        bytes calldata _payload,
        bytes calldata _adapterParams
    ) external onlyOwner {
        // Estimate the fee using LayerZero's endpoint contract
        (uint256 _nativeFee, ) = layerZeroEndpoint.estimateFees(
            _dstChainId,
            address(this),
            _payload,
            false, // payInZRO (false indicates payment in native tokens)
            _adapterParams
        );

        // Store the estimated fee in the mapping
        relayerFees[_dstChainId] = _nativeFee;
    }

    /**
     * @dev Function to retrieve the stored relayer fee for a specific chain.
     * @param _dstChainId The destination chain ID.
     * @return fee The stored relayer fee.
     */
    function getRelayerFee(uint16 _dstChainId) external view returns (uint256 fee) {
        return relayerFees[_dstChainId];
    }

    /**
     * @dev Function to change the owner of the contract.
     * @param _newOwner The address of the new owner.
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "New owner is the zero address");
        owner = _newOwner;
    }
}
```
