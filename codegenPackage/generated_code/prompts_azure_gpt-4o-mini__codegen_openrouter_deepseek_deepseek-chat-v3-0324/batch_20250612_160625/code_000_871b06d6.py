"""
Generated Code Metadata:
========================
Original URL: https://oddfellowsnft.com
Prompt: Generate a smart contract for an NFT collection based on the Secret Society of Odd Fellows concept.
Generated: DETERMINISTIC_871b06d63bff7f75
Batch ID: 20250612_160625
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

contract OddFellowsSociety is ERC721, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    using Strings for uint256;

    // Constants
    uint256 public constant MAX_SUPPLY = 10000;
    uint256 public constant MAX_PER_MINT = 10;
    uint256 public constant PRICE = 0.08 ether;
    bool public isSaleActive = false;
    string public baseTokenURI;
    string public contractURI;

    Counters.Counter private _tokenIdCounter;

    // Events
    event Minted(address indexed to, uint256 tokenId);
    event BaseURIChanged(string newBaseURI);
    event ContractURIChanged(string newContractURI);
    event SaleStateChanged(bool isActive);

    // Modifiers
    modifier whenSaleActive() {
        require(isSaleActive, "Sale is not active");
        _;
    }

    modifier validMintAmount(uint256 amount) {
        require(amount > 0 && amount <= MAX_PER_MINT, "Invalid mint amount");
        require(_tokenIdCounter.current() + amount <= MAX_SUPPLY, "Exceeds max supply");
        _;
    }

    constructor(
        string memory _name,
        string memory _symbol,
        string memory _initBaseURI,
        string memory _initContractURI
    ) ERC721(_name, _symbol) {
        baseTokenURI = _initBaseURI;
        contractURI = _initContractURI;
    }

    // Minting functions
    function mint(uint256 amount) external payable whenSaleActive validMintAmount(amount) nonReentrant {
        require(msg.value >= PRICE * amount, "Insufficient payment");

        for (uint256 i = 0; i < amount; i++) {
            _safeMint(msg.sender, _tokenIdCounter.current() + 1);
            _tokenIdCounter.increment();
            emit Minted(msg.sender, _tokenIdCounter.current());
        }
    }

    function reserveTokens(address to, uint256 amount) external onlyOwner validMintAmount(amount) {
        for (uint256 i = 0; i < amount; i++) {
            _safeMint(to, _tokenIdCounter.current() + 1);
            _tokenIdCounter.increment();
            emit Minted(to, _tokenIdCounter.current());
        }
    }

    // URI functions
    function _baseURI() internal view override returns (string memory) {
        return baseTokenURI;
    }

    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "ERC721Metadata: URI query for nonexistent token");
        return string(abi.encodePacked(baseTokenURI, tokenId.toString(), ".json"));
    }

    function setBaseURI(string memory newBaseURI) external onlyOwner {
        baseTokenURI = newBaseURI;
        emit BaseURIChanged(newBaseURI);
    }

    function setContractURI(string memory newContractURI) external onlyOwner {
        contractURI = newContractURI;
        emit ContractURIChanged(newContractURI);
    }

    // Sale control
    function toggleSale() external onlyOwner {
        isSaleActive = !isSaleActive;
        emit SaleStateChanged(isSaleActive);
    }

    // Withdraw funds
    function withdraw() external onlyOwner nonReentrant {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        
        (bool success, ) = owner().call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    // Utility functions
    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter.current();
    }

    function exists(uint256 tokenId) external view returns (bool) {
        return _exists(tokenId);
    }
}
```
