"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mpeppe-live.web.app
Prompt: Generate code to create an NFT minting contract inspired by `$MPEPE`'s Player Card NFTs, ensuring a fixed supply of 420 NFTs and incorporating metadata for iconic soccer player imagery.
Generated: DETERMINISTIC_3afdff36d4dab01d
Batch ID: 20250612_145837
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
 * @title PlayerCardNFT
 * @dev An ERC721 contract to mint Player Card NFTs with a fixed supply and metadata for iconic soccer players.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract PlayerCardNFT is ERC721URIStorage, Ownable {
    // Fixed supply of NFTs
    uint256 public constant MAX_SUPPLY = 420;

    // Counter for minted NFTs
    uint256 public totalMinted;

    // Base URI for metadata
    string private baseTokenURI;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed to, uint256 tokenId, string tokenURI);

    /**
     * @dev Constructor to initialize contract with name and symbol of NFT.
     * @param _name Name of the NFT collection.
     * @param _symbol Symbol of the NFT collection.
     * @param _baseTokenURI Base URI for metadata.
     */
    constructor(string memory _name, string memory _symbol, string memory _baseTokenURI) 
        ERC721(_name, _symbol) 
    {
        baseTokenURI = _baseTokenURI;
    }

    /**
     * @dev Mint a new Player Card NFT.
     * @param _to Address to receive the NFT.
     * @param _tokenId Unique identifier for the NFT.
     * @param _tokenURI Metadata URI for the NFT.
     */
    function mintNFT(address _to, uint256 _tokenId, string memory _tokenURI) external onlyOwner {
        require(totalMinted < MAX_SUPPLY, "All NFTs have been minted");
        require(_tokenId > 0 && _tokenId <= MAX_SUPPLY, "Invalid tokenId");
        require(!_exists(_tokenId), "Token ID already exists");

        // Mint the NFT
        _safeMint(_to, _tokenId);
        _setTokenURI(_tokenId, _tokenURI);

        // Increment total mint count
        totalMinted++;

        // Emit minting event
        emit NFTMinted(_to, _tokenId, _tokenURI);
    }

    /**
     * @dev Set a new base URI.
     * @param _newBaseTokenURI New base URI for metadata.
     */
    function setBaseURI(string memory _newBaseTokenURI) external onlyOwner {
        baseTokenURI = _newBaseTokenURI;
    }

    /**
     * @dev Override baseURI function to return baseTokenURI.
     */
    function _baseURI() internal view override returns (string memory) {
        return baseTokenURI;
    }

    /**
     * @dev Withdraw funds from the contract (if applicable).
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds available");
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Fallback function to accept ETH.
     */
    receive() external payable {}
}
```

Note: You will need to configure metadata for each NFT such as `tokenURI`, which should point to a backend or IPFS containing metadata for the soccer player imagery. The `mintNFT()` function is restricted to the owner for security and supply control.
