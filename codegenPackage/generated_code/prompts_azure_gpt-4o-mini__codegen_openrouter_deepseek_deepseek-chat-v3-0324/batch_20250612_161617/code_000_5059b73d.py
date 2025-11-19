"""
Generated Code Metadata:
========================
Original URL: https://kevinland.pages.dev
Prompt: Generate a smart contract in Solidity for minting NFTs on the Ethereum network, specifically for a project like KevinLand where users can adopt multiple NFTs at once.
Generated: DETERMINISTIC_5059b73d92ab3bc3
Batch ID: 20250612_161617
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/utils/Strings.sol";

contract KevinLand is ERC721, Ownable {
    using Counters for Counters.Counter;
    using Strings for uint256;

    Counters.Counter private _tokenIdCounter;

    string private _baseTokenURI;
    uint256 public constant MAX_SUPPLY = 10000;
    uint256 public constant MAX_BATCH_MINT = 20;
    uint256 public mintPrice = 0.05 ether;

    event NFTMinted(address indexed owner, uint256 tokenId);
    event BatchNFTMinted(address indexed owner, uint256[] tokenIds);

    constructor(string memory baseURI) ERC721("KevinLand", "KVL") {
        _baseTokenURI = baseURI;
    }

    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    function setMintPrice(uint256 newPrice) external onlyOwner {
        mintPrice = newPrice;
    }

    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }

    function mintNFT() external payable {
        require(msg.value >= mintPrice, "Insufficient payment");
        require(_tokenIdCounter.current() < MAX_SUPPLY, "Max supply reached");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(msg.sender, tokenId);

        emit NFTMinted(msg.sender, tokenId);
    }

    function batchMintNFT(uint256 quantity) external payable {
        require(quantity > 0 && quantity <= MAX_BATCH_MINT, "Invalid quantity");
        require(msg.value >= mintPrice * quantity, "Insufficient payment");
        require(_tokenIdCounter.current() + quantity <= MAX_SUPPLY, "Exceeds max supply");

        uint256[] memory tokenIds = new uint256[](quantity);
        
        for (uint256 i = 0; i < quantity; i++) {
            uint256 tokenId = _tokenIdCounter.current();
            _tokenIdCounter.increment();
            _safeMint(msg.sender, tokenId);
            tokenIds[i] = tokenId;
        }

        emit BatchNFTMinted(msg.sender, tokenIds);
    }

    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter.current();
    }

    function tokenURI(uint256 tokenId) public view virtual override returns (string memory) {
        require(_exists(tokenId), "ERC721Metadata: URI query for nonexistent token");
        return string(abi.encodePacked(_baseURI(), tokenId.toString(), ".json"));
    }
}
```
