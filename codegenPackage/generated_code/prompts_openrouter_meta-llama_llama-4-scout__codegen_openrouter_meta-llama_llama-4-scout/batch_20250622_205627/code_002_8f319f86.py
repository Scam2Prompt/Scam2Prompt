"""
Generated Code Metadata:
========================
Original URL: https://telos-4ji.pages.dev
Prompt: Develop a smart contract on Telos EVM for a simple NFT marketplace, utilizing LayerZero for omnichain interoperability.
Generated: DETERMINISTIC_8f319f86a4cc824a
Batch ID: 20250622_205627
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/LayerZero-Labs/layerzero-solidity/contracts/interfaces/ILayerZeroReceiver.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/LayerZero-Labs/layerzero-solidity/contracts/interfaces/ILayerZeroEndpoint.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

Here is the code for a simple NFT marketplace smart contract on Telos EVM with LayerZero for omnichain interoperability:
```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol";
import "https://github.com/LayerZero-Labs/layerzero-solidity/contracts/interfaces/ILayerZeroEndpoint.sol";
import "https://github.com/LayerZero-Labs/layerzero-solidity/contracts/interfaces/ILayerZeroReceiver.sol";

// Telos EVM NFT Marketplace contract
contract TelosNFMarketplace {
    // Mapping of NFT owners
    mapping(address => mapping(uint256 => uint256)) public nftOwners;

    // Mapping of NFT metadata
    mapping(uint256 => NFT) public nftMetadata;

    // LayerZero endpoint
    ILayerZeroEndpoint public layerZeroEndpoint;

    // Event emitted when an NFT is minted
    event NFTMinted(address indexed owner, uint256 tokenId);

    // Event emitted when an NFT is transferred
    event NFTTransferred(address indexed from, address indexed to, uint256 tokenId);

    // Event emitted when an NFT is sold
    event NFTSold(address indexed seller, address indexed buyer, uint256 tokenId);

    // Struct for NFT metadata
    struct NFT {
        uint256 id;
        string name;
        string description;
        string image;
    }

    // Constructor
    constructor(address _layerZeroEndpoint) public {
        layerZeroEndpoint = ILayerZeroEndpoint(_layerZeroEndpoint);
    }

    // Function to mint a new NFT
    function mintNFT(string memory _name, string memory _description, string memory _image) public {
        // Generate a new token ID
        uint256 tokenId = uint256(keccak256(abi.encodePacked(msg.sender, block.timestamp)));

        // Create a new NFT
        NFT memory nft = NFT(tokenId, _name, _description, _image);

        // Set the NFT owner
        nftOwners[msg.sender][tokenId] = tokenId;

        // Set the NFT metadata
        nftMetadata[tokenId] = nft;

        // Emit the NFTMinted event
        emit NFTMinted(msg.sender, tokenId);
    }

    // Function to transfer an NFT
    function transferNFT(uint256 _tokenId, address _to) public {
        // Check if the sender is the owner
        require(nftOwners[msg.sender][_tokenId] == _tokenId, "Only the owner can transfer");

        // Transfer the NFT
        nftOwners[_to][_tokenId] = _tokenId;
        delete nftOwners[msg.sender][_tokenId];

        // Emit the NFTTransferred event
        emit NFTTransferred(msg.sender, _to, _tokenId);
    }

    // Function to sell an NFT
    function sellNFT(uint256 _tokenId, uint256 _price) public {
        // Check if the sender is the owner
        require(nftOwners[msg.sender][_tokenId] == _tokenId, "Only the owner can sell");

        // Execute the sale
        // ...

        // Emit the NFTSold event
        emit NFTSold(msg.sender, msg.sender, _tokenId);
    }

    // Function to handle incoming cross-chain messages
    function _nonReentrant() internal {
        // LayerZero receiver
        ILayerZeroReceiver receiver = ILayerZeroReceiver(msg.sender);

        // Get the payload
        bytes memory payload = receiver.getPayload();

        // Decode the payload
        (uint256 tokenId, address to) = abi.decode(payload, (uint256, address));

        // Transfer the NFT
        transferNFT(tokenId, to);
    }

    // Fallback function for LayerZero
    fallback() external {
        // Handle incoming cross-chain messages
        _nonReentrant();
    }
}

// Omnichain NFT contract
contract OmnichainNFT is ILayerZeroReceiver {
    // Mapping of NFT owners
    mapping(address => mapping(uint256 => uint256)) public nftOwners;

    // Mapping of NFT metadata
    mapping(uint256 => NFT) public nftMetadata;

    // LayerZero endpoint
    ILayerZeroEndpoint public layerZeroEndpoint;

    // Event emitted when an NFT is minted
    event NFTMinted(address indexed owner, uint256 tokenId);

    // Event emitted when an NFT is transferred
    event NFTTransferred(address indexed from, address indexed to, uint256 tokenId);

    // Struct for NFT metadata
    struct NFT {
        uint256 id;
        string name;
        string description;
        string image;
    }

    // Constructor
    constructor(address _layerZeroEndpoint) public {
        layerZeroEndpoint = ILayerZeroEndpoint(_layerZeroEndpoint);
    }

    // Function to mint a new NFT
    function mintNFT(string memory _name, string memory _description, string memory _image) public {
        // Generate a new token ID
        uint256 tokenId = uint256(keccak256(abi.encodePacked(msg.sender, block.timestamp)));

        // Create a new NFT
        NFT memory nft = NFT(tokenId, _name, _description, _image);

        // Set the NFT owner
        nftOwners[msg.sender][tokenId] = tokenId;

        // Set the NFT metadata
        nftMetadata[tokenId] = nft;

        // Emit the NFTMinted event
        emit NFTMinted(msg.sender, tokenId);
    }

    // Function to handle incoming cross-chain messages
    function receivePayload(uint16 _srcChainId, bytes calldata _payload) external override {
        // Decode the payload
        (uint256 tokenId, address to) = abi.decode(_payload, (uint256, address));

        // Transfer the NFT
        transferNFT(tokenId, to);
    }

    // Function to transfer an NFT
    function transferNFT(uint256 _tokenId, address _to) public {
        // Check if the sender is the owner
        require(nftOwners[msg.sender][_tokenId] == _tokenId, "Only the owner can transfer");

        // Transfer the NFT
        nftOwners[_to][_tokenId] = _tokenId;
        delete nftOwners[msg.sender][_tokenId];

        // Emit the NFTTransferred event
        emit NFTTransferred(msg.sender, _to, _tokenId);
    }

    // Function to send an NFT cross-chain
    function sendNFT(uint256 _tokenId, uint16 _dstChainId, address _to) public {
        // Get the LayerZero endpoint
        ILayerZeroEndpoint endpoint = layerZeroEndpoint;

        // Encode the payload
        bytes memory payload = abi.encode(_tokenId, _to);

        // Send the payload
        endpoint.send{value: 0}(_dstChainId, payload);
    }
}
```
