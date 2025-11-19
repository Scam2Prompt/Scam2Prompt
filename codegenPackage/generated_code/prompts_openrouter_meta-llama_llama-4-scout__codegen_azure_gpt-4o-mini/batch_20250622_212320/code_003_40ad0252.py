"""
Generated Code Metadata:
========================
Original URL: https://gorodshansona.ru
Prompt: "Generate a smart contract using Solidity that utilizes Immutable X for instant and fee-less NFT trading on Ethereum."
Generated: DETERMINISTIC_40ad0252ba936116
Batch ID: 20250622_212320
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

// Importing the OpenZeppelin ERC721 implementation for NFT standards
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the Immutable X protocol
interface IImmutableX {
    function mint(
        address to,
        uint256 tokenId,
        string memory uri
    ) external;

    function transfer(
        address from,
        address to,
        uint256 tokenId
    ) external;
}

// Smart contract for NFT minting and trading using Immutable X
contract ImmutableXNFT is ERC721, Ownable {
    // Immutable X contract address
    IImmutableX public immutable immutableX;

    // Mapping from token ID to token URI
    mapping(uint256 => string) private _tokenURIs;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed to, uint256 indexed tokenId, string uri);

    // Constructor to initialize the contract with the Immutable X address
    constructor(address _immutableXAddress) ERC721("ImmutableXNFT", "IMXNFT") {
        require(_immutableXAddress != address(0), "Invalid Immutable X address");
        immutableX = IImmutableX(_immutableXAddress);
    }

    // Function to mint a new NFT
    function mintNFT(address to, uint256 tokenId, string memory uri) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(!_exists(tokenId), "Token ID already exists");

        // Mint the NFT using Immutable X
        immutableX.mint(to, tokenId, uri);

        // Set the token URI
        _tokenURIs[tokenId] = uri;

        // Emit the NFTMinted event
        emit NFTMinted(to, tokenId, uri);
    }

    // Function to get the token URI for a given token ID
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenURIs[tokenId];
    }

    // Function to transfer an NFT to another address
    function transferNFT(address from, address to, uint256 tokenId) external {
        require(from != address(0), "Invalid from address");
        require(to != address(0), "Invalid to address");
        require(_exists(tokenId), "Token does not exist");

        // Transfer the NFT using Immutable X
        immutableX.transfer(from, to, tokenId);
    }

    // Function to check if a token exists
    function _exists(uint256 tokenId) internal view returns (bool) {
        return bytes(_tokenURIs[tokenId]).length > 0;
    }
}
```
