"""
Generated Code Metadata:
========================
Original URL: https://layer-1yd.pages.dev
Prompt: Create a LayerZero-based contract that transfers in-game assets between blockchains for a gaming application, referencing the `Heroes of Mavia` use case.
Generated: DETERMINISTIC_42296b98fbf2a930
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

// Importing LayerZero interface for cross-chain communication
import "@layerzero/contracts/interfaces/ILayerZeroEndpoint.sol";
import "@layerzero/contracts/interfaces/ILayerZeroReceiver.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title CrossChainAssetTransfer
 * @dev A contract to transfer in-game assets (ERC721 tokens) between blockchains using LayerZero.
 */
contract CrossChainAssetTransfer is ILayerZeroReceiver, Ownable {
    // LayerZero endpoint for cross-chain communication
    ILayerZeroEndpoint public endpoint;

    // Mapping to track the ownership of assets across chains
    mapping(uint256 => address) public assetOwners;

    // Event emitted when an asset is transferred
    event AssetTransferred(uint256 indexed tokenId, address indexed from, address indexed to, uint16 dstChainId);

    // Constructor to set the LayerZero endpoint
    constructor(address _endpoint) {
        endpoint = ILayerZeroEndpoint(_endpoint);
    }

    /**
     * @dev Transfers an ERC721 asset to another blockchain.
     * @param _tokenId The ID of the token to transfer.
     * @param _dstChainId The destination chain ID.
     * @param _to The address to receive the asset on the destination chain.
     */
    function transferAsset(uint256 _tokenId, uint16 _dstChainId, address _to) external {
        // Ensure the caller is the owner of the asset
        require(assetOwners[_tokenId] == msg.sender, "Not the asset owner");

        // Mark the asset as transferred
        assetOwners[_tokenId] = address(0);

        // Prepare the payload for the destination chain
        bytes memory payload = abi.encode(_tokenId, msg.sender, _to);

        // Send the asset to the destination chain
        endpoint.send{value: msg.value}(
            _dstChainId,
            address(this), // Destination address on the other chain
            payload,
            payable(msg.sender), // Refund address
            address(0), // No extra gas
            "" // No adapter params
        );

        emit AssetTransferred(_tokenId, msg.sender, _to, _dstChainId);
    }

    /**
     * @dev Handles the receipt of assets from another chain.
     * @param _srcChainId The source chain ID.
     * @param _srcAddress The source address.
     * @param _payload The payload containing the asset information.
     */
    function lzReceive(
        uint16 _srcChainId,
        bytes memory _srcAddress,
        uint64, // nonce
        bytes memory _payload
    ) external override {
        // Ensure the call is coming from the LayerZero endpoint
        require(msg.sender == address(endpoint), "Invalid caller");

        // Decode the payload
        (uint256 tokenId, address from, address to) = abi.decode(_payload, (uint256, address, address));

        // Assign the asset to the new owner
        assetOwners[tokenId] = to;

        // Emit an event for the asset reception
        emit AssetTransferred(tokenId, from, to, _srcChainId);
    }

    /**
     * @dev Allows the contract owner to withdraw any Ether sent to the contract.
     */
    function withdrawEther() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {}
}
```
