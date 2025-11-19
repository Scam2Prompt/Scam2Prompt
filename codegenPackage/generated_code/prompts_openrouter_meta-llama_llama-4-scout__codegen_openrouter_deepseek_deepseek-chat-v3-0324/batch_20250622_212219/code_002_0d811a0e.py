"""
Generated Code Metadata:
========================
Original URL: https://unichaincrew.club
Prompt: Generate a smart contract code for an NFT project on Unichain, inspired by the Unichain Crew Club collection.
Generated: DETERMINISTIC_0d811a0ea62a1a2b
Batch ID: 20250622_212219
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract UnichainCrewClub is ERC721, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    using Strings for uint256;

    Counters.Counter private _tokenIdCounter;

    uint256 public constant MAX_SUPPLY = 10000;
    uint256 public constant PRICE = 0.08 ether;
    uint256 public constant MAX_PER_MINT = 5;
    
    string public baseURI;
    string public baseExtension = ".json";
    bool public isPublicSaleActive = false;

    mapping(address => uint256) private _mintedCount;

    constructor(
        string memory _name,
        string memory _symbol,
        string memory _initBaseURI
    ) ERC721(_name, _symbol) {
        baseURI = _initBaseURI;
    }

    modifier whenPublicSaleActive() {
        require(isPublicSaleActive, "Public sale is not active");
        _;
    }

    function mint(uint256 _quantity) external payable nonReentrant whenPublicSaleActive {
        require(_quantity > 0 && _quantity <= MAX_PER_MINT, "Invalid mint quantity");
        require(_tokenIdCounter.current() + _quantity <= MAX_SUPPLY, "Exceeds max supply");
        require(msg.value >= PRICE * _quantity, "Insufficient ETH sent");

        _mintedCount[msg.sender] += _quantity;
        
        for (uint256 i = 0; i < _quantity; i++) {
            _safeMint(msg.sender, _tokenIdCounter.current() + 1);
            _tokenIdCounter.increment();
        }
    }

    function tokenURI(uint256 tokenId) public view virtual override returns (string memory) {
        require(_exists(tokenId), "ERC721Metadata: URI query for nonexistent token");

        string memory currentBaseURI = _baseURI();
        return bytes(currentBaseURI).length > 0
            ? string(abi.encodePacked(currentBaseURI, tokenId.toString(), baseExtension))
            : "";
    }

    function _baseURI() internal view virtual override returns (string memory) {
        return baseURI;
    }

    function setBaseURI(string memory _newBaseURI) external onlyOwner {
        baseURI = _newBaseURI;
    }

    function setBaseExtension(string memory _newBaseExtension) external onlyOwner {
        baseExtension = _newBaseExtension;
    }

    function togglePublicSale() external onlyOwner {
        isPublicSaleActive = !isPublicSaleActive;
    }

    function totalSupply() public view returns (uint256) {
        return _tokenIdCounter.current();
    }

    function withdraw() external onlyOwner nonReentrant {
        (bool success, ) = payable(owner()).call{value: address(this).balance}("");
        require(success, "Withdrawal failed");
    }

    function mintedCount(address _address) public view returns (uint256) {
        return _mintedCount[_address];
    }
}
```
