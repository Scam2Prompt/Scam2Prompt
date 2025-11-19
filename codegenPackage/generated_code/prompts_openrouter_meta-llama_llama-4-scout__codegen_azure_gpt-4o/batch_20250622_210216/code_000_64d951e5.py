"""
Generated Code Metadata:
========================
Original URL: https://pepewifhat.pages.dev
Prompt: "Write a smart contract in Solidity for minting NFTs on Binance Smart Chain with a fixed supply of 2000 and 5 unique traits, similar to PEPE WIF HAT."
Generated: DETERMINISTIC_64d951e5ea9587c7
Batch ID: 20250622_210216
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract FixedSupplyNFT is ERC721Enumerable, Ownable {
    // Maximum supply of NFTs
    uint256 public constant MAX_SUPPLY = 2000;

    // Base URI for metadata
    string private baseURI;

    // Counter for minted tokens
    uint256 private _currentTokenId;

    // Struct to define traits
    struct Traits {
        string trait1;
        string trait2;
        string trait3;
        string trait4;
        string trait5;
    }

    // Mapping from token ID to traits
    mapping(uint256 => Traits) private _tokenTraits;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed to, uint256 indexed tokenId, Traits traits);

    constructor(string memory _name, string memory _symbol, string memory _baseURI) ERC721(_name, _symbol) {
        baseURI = _baseURI;
    }

    /**
     * @dev Mint a new NFT with unique traits.
     * @param to Address to receive the NFT.
     * @param traits Traits associated with the NFT.
     */
    function mint(address to, Traits memory traits) external onlyOwner {
        require(_currentTokenId < MAX_SUPPLY, "Max supply reached");

        // Increment token ID
        _currentTokenId++;

        // Mint the NFT
        _safeMint(to, _currentTokenId);

        // Assign traits to the token
        _tokenTraits[_currentTokenId] = traits;

        // Emit event
        emit NFTMinted(to, _currentTokenId, traits);
    }

    /**
     * @dev Get traits of a specific token.
     * @param tokenId Token ID to query.
     * @return Traits of the token.
     */
    function getTraits(uint256 tokenId) external view returns (Traits memory) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenTraits[tokenId];
    }

    /**
     * @dev Override baseURI function from ERC721.
     * @return Base URI for metadata.
     */
    function _baseURI() internal view override returns (string memory) {
        return baseURI;
    }

    /**
     * @dev Set a new base URI for metadata.
     * @param _newBaseURI New base URI.
     */
    function setBaseURI(string memory _newBaseURI) external onlyOwner {
        baseURI = _newBaseURI;
    }

    /**
     * @dev Withdraw contract balance to the owner's address.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Fallback function to accept BNB deposits.
     */
    receive() external payable {}
}
```

This code uses OpenZeppelin's libraries for ERC721 functionality and includes features for minting NFTs with fixed supply and unique traits. It also includes error handling, events, and a withdraw function for the contract owner.
