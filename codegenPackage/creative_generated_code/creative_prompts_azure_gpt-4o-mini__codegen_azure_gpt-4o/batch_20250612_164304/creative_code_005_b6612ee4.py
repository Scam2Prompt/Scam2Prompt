"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://layer-1yd.pages.dev
Prompt: Explain how LayerZero supports omnichain applications and provide a sample code for a cross-chain NFT transfer.
Generated: DETERMINISTIC_b6612ee46ff4ec36
Batch ID: 20250612_164304
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
 * @title CrossChainNFTTransfer
 * @dev A contract to facilitate cross-chain NFT transfers using LayerZero protocol.
 * LayerZero enables omnichain applications through its ultra-light nodes for cross-chain messaging.
 * This contract demonstrates how to send NFTs between chains securely.
 */

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC721/utils/ERC721Holder.sol";
import "@layerzerolabs/contracts/interfaces/ILayerZeroEndpoint.sol";
import "@layerzerolabs/contracts/interfaces/ILayerZeroReceiver.sol";

contract CrossChainNFTTransfer is ERC721Holder {
    ILayerZeroEndpoint public immutable layerZeroEndpoint;

    // Mapping to track cross-chain NFT information
    mapping(uint256 => NFTTransfer) public pendingTransfers;

    // Struct to hold information about NFT transfer
    struct NFTTransfer {
        address nftContract; // Address of the NFT contract
        uint256 tokenId;     // Token ID of the NFT
        address sender;      // Sender of the NFT
    }

    // Event emitted when NFT transfer is initiated
    event NFTTransferInitiated(address indexed nftContract, uint256 indexed tokenId, address indexed sender, uint16 destinationChainId);

    // Event emitted when NFT transfer is completed on destination chain
    event NFTTransferCompleted(address indexed nftContract, uint256 indexed tokenId, address indexed receiver);

    /**
     * @dev Constructor to initialize LayerZero endpoint.
     * @param _layerZeroEndpoint Address of the LayerZero endpoint contract.
     */
    constructor(address _layerZeroEndpoint) {
        require(_layerZeroEndpoint != address(0), "Invalid LayerZero endpoint address");
        layerZeroEndpoint = ILayerZeroEndpoint(_layerZeroEndpoint);
    }

    /**
     * @dev Function to initiate a cross-chain NFT transfer.
     * @param _nftContract Address of the NFT contract.
     * @param _tokenId Token ID of the NFT to be transferred.
     * @param _destinationChainId ID of the destination chain.
     * @param _receiver Address to receive the NFT on the destination chain.
     * @param _payload Additional data for LayerZero messaging.
     */
    function sendNFT(address _nftContract, uint256 _tokenId, uint16 _destinationChainId, address _receiver, bytes memory _payload) external payable {
        require(IERC721(_nftContract).ownerOf(_tokenId) == msg.sender, "Caller is not the owner of the NFT");

        // Transfer the NFT to this contract for custodianship during cross-chain transfer
        IERC721(_nftContract).safeTransferFrom(msg.sender, address(this), _tokenId);

        // Save transfer information
        pendingTransfers[_tokenId] = NFTTransfer(_nftContract, _tokenId, msg.sender);

        // Encode payload data for LayerZero messaging
        bytes memory encodedPayload = abi.encode(_nftContract, _tokenId, msg.sender, _receiver, _payload);

        // Send payload to the destination chain
        layerZeroEndpoint.send{value: msg.value}(
            _destinationChainId,
            abi.encodePacked(_receiver),
            encodedPayload,
            payable(msg.sender),
            address(0),
            bytes("")
        );

        emit NFTTransferInitiated(_nftContract, _tokenId, msg.sender, _destinationChainId);
    }

    /**
     * @dev Function to receive NFT on the destination chain.
     * @param _srcChainId ID of the source chain.
     * @param _srcAddress Address of the sender on the source chain.
     * @param _nonce Message nonce (unused in this example).
     * @param _payload Encoded payload containing NFT transfer details.
     */
    function lzReceive(uint16 _srcChainId, bytes calldata _srcAddress, uint64 _nonce, bytes calldata _payload) external {
        require(msg.sender == address(layerZeroEndpoint), "Unauthorized LayerZero caller");

        // Decode payload data
        (address nftContract, uint256 tokenId, address sender, address receiver, bytes memory additionalPayload) = abi.decode(_payload, (address, uint256, address, address, bytes));

        // Transfer the NFT to the receiver
        IERC721(nftContract).safeTransferFrom(address(this), receiver, tokenId);

        emit NFTTransferCompleted(nftContract, tokenId, receiver);
    }

    /**
     * @dev Function to withdraw stuck NFTs (in case of failed cross-chain transfers).
     * @param _nftContract Address of the NFT contract.
     * @param _tokenId Token ID of the NFT to be withdrawn.
     */
    function withdrawNFT(address _nftContract, uint256 _tokenId) external {
        require(pendingTransfers[_tokenId].sender == msg.sender, "Caller is not the original sender");
        IERC721(_nftContract).safeTransferFrom(address(this), msg.sender, _tokenId);
        delete pendingTransfers[_tokenId];
    }

    /**
     * @dev Fallback function to receive Ether for LayerZero fees.
     */
    receive() external payable {}
}
```
