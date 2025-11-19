"""
Generated Code Metadata:
========================
Original URL: https://dao-nftt.web.app
Prompt: Develop a smart contract in Solidity (or equivalent) for creating and managing NFT collections on Solana, inspired by the features of this platform.
Generated: DETERMINISTIC_4d8b944a9abb7b19
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract SolanaNFTCollection is ERC721, ERC721Enumerable, ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Collection metadata
    string private _collectionName;
    string private _collectionSymbol;
    string private _baseURI;

    // Royalty information
    address private _royaltyRecipient;
    uint256 private _royaltyPercentage; // Basis points (100 = 1%)

    // Collection configuration
    uint256 public maxSupply;
    uint256 public mintPrice;
    bool public isPublicMintEnabled;

    // Events
    event Minted(address indexed to, uint256 indexed tokenId, string tokenURI);
    event RoyaltyInfoUpdated(address recipient, uint256 percentage);
    event BaseURIUpdated(string newBaseURI);
    event PublicMintToggled(bool enabled);

    constructor(
        string memory name_,
        string memory symbol_,
        string memory baseURI_,
        uint256 maxSupply_,
        uint256 mintPrice_,
        address royaltyRecipient_,
        uint256 royaltyPercentage_
    ) ERC721(name_, symbol_) {
        _collectionName = name_;
        _collectionSymbol = symbol_;
        _baseURI = baseURI_;
        maxSupply = maxSupply_;
        mintPrice = mintPrice_;
        _royaltyRecipient = royaltyRecipient_;
        _royaltyPercentage = royaltyPercentage_;
        isPublicMintEnabled = false;
    }

    // Mint function for public
    function mint(address to, string memory tokenURI) public payable {
        require(isPublicMintEnabled, "Public minting is disabled");
        require(msg.value >= mintPrice, "Insufficient payment");
        require(_tokenIdCounter.current() < maxSupply, "Max supply reached");
        
        _safeMint(to, _tokenIdCounter.current());
        _setTokenURI(_tokenIdCounter.current(), tokenURI);
        
        emit Minted(to, _tokenIdCounter.current(), tokenURI);
        _tokenIdCounter.increment();
    }

    // Admin mint function
    function adminMint(address to, string memory tokenURI) public onlyOwner {
        require(_tokenIdCounter.current() < maxSupply, "Max supply reached");
        
        _safeMint(to, _tokenIdCounter.current());
        _setTokenURI(_tokenIdCounter.current(), tokenURI);
        
        emit Minted(to, _tokenIdCounter.current(), tokenURI);
        _tokenIdCounter.increment();
    }

    // Set royalty information
    function setRoyaltyInfo(address recipient, uint256 percentage) public onlyOwner {
        require(percentage <= 10000, "Royalty percentage too high");
        _royaltyRecipient = recipient;
        _royaltyPercentage = percentage;
        emit RoyaltyInfoUpdated(recipient, percentage);
    }

    // Get royalty information
    function getRoyaltyInfo() public view returns (address, uint256) {
        return (_royaltyRecipient, _royaltyPercentage);
    }

    // Update base URI
    function setBaseURI(string memory newBaseURI) public onlyOwner {
        _baseURI = newBaseURI;
        emit BaseURIUpdated(newBaseURI);
    }

    // Toggle public mint
    function togglePublicMint() public onlyOwner {
        isPublicMintEnabled = !isPublicMintEnabled;
        emit PublicMintToggled(isPublicMintEnabled);
    }

    // Withdraw funds
    function withdraw() public onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Override functions
    function _baseURI() internal view override returns (string memory) {
        return _baseURI;
    }

    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override(ERC721, ERC721Enumerable) {
        super._beforeTokenTransfer(from, to, tokenId);
    }

    function _burn(uint256 tokenId) internal override(ERC721, ERC721URIStorage) {
        super._burn(tokenId);
    }

    function tokenURI(uint256 tokenId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (string memory)
    {
        return super.tokenURI(tokenId);
    }

    function supportsInterface(bytes4 interfaceId)
        public
        view
        override(ERC721, ERC721Enumerable)
        returns (bool)
    {
        return super.supportsInterface(interfaceId);
    }
}
```
