"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://substantial-belgium-incalculable.on-fleek.app
Prompt: Write a code snippet using LayerZero V2 to configure an OFT (Omnichain Fungible Token) for cross-chain communication. Reference the LayerZero contract standards and configuration guidelines.
Generated: DETERMINISTIC_7aad1f48d34d61e4
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

// Import LayerZero contracts and interfaces
import "@layerzero/contracts/OmnichainFungibleToken.sol";
import "@layerzero/contracts/interfaces/ILayerZeroEndpoint.sol";

/// @title Omnichain Fungible Token (OFT) Contract Implementation
/// @dev This contract integrates with LayerZero for cross-chain token transfers
contract MyOmnichainToken is OmnichainFungibleToken {
    /// @notice Constructor to initialize the OFT
    /// @param _name Name of the token
    /// @param _symbol Symbol of the token
    /// @param _endpoint Address of the LayerZero endpoint for cross-chain messaging
    constructor(
        string memory _name,
        string memory _symbol,
        address _endpoint
    )
        OmnichainFungibleToken(
            _name,
            _symbol,
            _endpoint // LayerZero endpoint must be set
        )
    {}

    /// @notice Override the _nonblockingLzReceive function for custom logic
    /// @dev Handles incoming cross-chain messages
    /// @param _srcChainId Source chain ID where the message originated
    /// @param _srcAddress Address on the source chain
    /// @param _nonce Unique message nonce
    /// @param _payload Encoded payload data
    function _nonblockingLzReceive(
        uint16 _srcChainId,
        bytes memory _srcAddress,
        uint64 _nonce,
        bytes memory _payload
    ) internal override {
        // Custom logic for processing the payload can be implemented here
        // For example, decoding and transferring tokens
        // payload decoding example: (address recipient, uint256 amount) = abi.decode(_payload, (address, uint256));

        super._nonblockingLzReceive(_srcChainId, _srcAddress, _nonce, _payload);
    }

    /// @notice Override for token transfer functionality
    /// @dev Handles cross-chain token transfer logic
    /// @param _dstChainId Destination chain ID
    /// @param _to Address on the destination chain
    /// @param _amount Amount of tokens to transfer
    /// @param _refundAddress Address for refunding excess gas fees
    /// @param _zroPaymentAddress Address for LayerZero ZRO token payment
    /// @param _adapterParams Additional configuration parameters
    function sendTokens(
        uint16 _dstChainId,
        bytes memory _to,
        uint256 _amount,
        address payable _refundAddress,
        address _zroPaymentAddress,
        bytes memory _adapterParams
    ) external payable {
        require(_amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender) >= _amount, "Insufficient balance");

        // Burn tokens from sender's address before sending
        _burn(msg.sender, _amount);

        // Call LayerZero send function to handle cross-chain messaging
        lzSend(
            _dstChainId,
            abi.encode(_to, _amount), // Encode recipient and amount
            _refundAddress,
            _zroPaymentAddress,
            _adapterParams
        );
    }

    /// @notice Set configuration for LayerZero endpoint
    /// @param _version Version of the configuration
    /// @param _chainId Chain ID for configuration
    /// @param _configType Type of configuration
    /// @param _config Encoded configuration data
    function setLayerZeroConfig(
        uint16 _version,
        uint16 _chainId,
        uint256 _configType,
        bytes memory _config
    ) external onlyOwner {
        // Set LayerZero endpoint configuration
        lzEndpoint.setConfig(_version, _chainId, _configType, _config);
    }

    /// @notice Set the LayerZero send/receive gas fees
    /// @param _chainId Chain ID where fees are being configured
    /// @param _remoteAddress Address on the remote chain
    /// @param _price Encoded gas pricing data
    function setGasFees(
        uint16 _chainId,
        bytes memory _remoteAddress,
        bytes memory _price
    ) external onlyOwner {
        // Set LayerZero remote gas fees
        lzEndpoint.setSendVersion(_chainId, _remoteAddress, _price);
    }

    /// @notice Fallback function to handle unexpected Ether transfers
    receive() external payable {}
}
```
