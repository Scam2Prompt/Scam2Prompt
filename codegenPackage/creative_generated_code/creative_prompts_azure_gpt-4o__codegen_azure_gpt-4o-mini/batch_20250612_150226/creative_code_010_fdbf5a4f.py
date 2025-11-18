"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://layer-1yd.pages.dev
Prompt: Generate a Solidity contract for an omnichain NFT (ONFT) using LayerZero's protocol, ensuring the NFT can be transferred across multiple blockchains.
Generated: DETERMINISTIC_fdbf5a4f59e65e55
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

// Import necessary interfaces from LayerZero
import "@layerzerolabs/solidity-examples/contracts/interfaces/ILayerZeroReceiver.sol";
import "@layerzerolabs/solidity-examples/contracts/interfaces/ILayerZeroEndpoint.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Omnichain NFT contract
contract OmnichainNFT is ERC721, Ownable, ILayerZeroReceiver {
    using Counters for Counters.Counter;
    
    // State variables
    Counters.Counter private _tokenIdCounter;
    ILayerZeroEndpoint public endpoint; // LayerZero endpoint for cross-chain communication
    mapping(uint256 => string) private _tokenURIs; // Mapping from token ID to token URI
    mapping(uint256 => bytes) public remoteChainData; // Store data for remote chains

    // Event emitted on successful NFT transfer across chains
    event NFTTransferred(uint256 indexed tokenId, uint256 indexed destinationChainId, address indexed recipient);

    // Constructor to initialize the contract with the LayerZero endpoint
    constructor(address _endpoint) ERC721("OmnichainNFT", "ONFT") {
        endpoint = ILayerZeroEndpoint(_endpoint);
    }

    // Mint a new NFT to the caller's address
    function mint(string memory tokenURI) external onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        _setTokenURI(tokenId, tokenURI);
        _tokenIdCounter.increment();
    }

    // Function to update token URI
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        require(_exists(tokenId), "ERC721Metadata: URI set of nonexistent token");
        _tokenURIs[tokenId] = tokenURI;
    }

    // Function to get token URI
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "ERC721Metadata: URI query for nonexistent token");
        return _tokenURIs[tokenId];
    }

    // Function to transfer the NFT to another chain
    function transferNFT(uint256 tokenId, uint256 destinationChainId, address recipient) external payable {
        require(ownerOf(tokenId) == msg.sender, "You are not the owner of this NFT");
        require(destinationChainId != block.chainid, "Cannot transfer to the same chain");

        // Prepare data for remote chain, can include extra metadata
        bytes memory data = abi.encode(msg.sender, recipient, tokenId);
        remoteChainData[tokenId] = data;

        // Burn the NFT on the current chain
        _burn(tokenId);

        // Send the message to the LayerZero endpoint
        endpoint.send{value: msg.value}(
            destinationChainId,
            // The address on the destination chain to receive the data
            abi.encodePacked(address(this)),
            data,
            payable(msg.sender), // Refund the gas fee to the sender
            address(0x0), // Call back function (not used here)
            "" // AdapterParams (not used here)
        );

        emit NFTTransferred(tokenId, destinationChainId, recipient);
    }

    // Function to handle incoming messages from LayerZero
    function lzReceive(uint16 _srcChainId, bytes memory _srcAddress, uint64, bytes memory _payload) external override {
        require(msg.sender == address(endpoint), "Unauthorized endpoint");

        // Decode the payload
        (address originalOwner, address recipient, uint256 tokenId) = abi.decode(_payload, (address, address, uint256));

        // Mint the NFT to the recipient on this chain
        _mint(recipient, tokenId);
        // Optionally set the URI for the NFT
        // _setTokenURI(tokenId, remoteChainData[tokenId]);

        // Clear the remote chain data for this tokenId
        delete remoteChainData[tokenId];
    }

    // Receive function to allow the contract to accept ETH
    receive() external payable {}
}
```
