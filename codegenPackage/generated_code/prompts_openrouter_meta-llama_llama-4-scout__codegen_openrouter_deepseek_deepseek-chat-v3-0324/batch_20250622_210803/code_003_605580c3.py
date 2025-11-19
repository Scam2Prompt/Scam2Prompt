"""
Generated Code Metadata:
========================
Original URL: https://degen-4g1.pages.dev
Prompt: "Create a smart contract on Polygon for a limited edition NFT series, inspired by Highlight's open edition collections like ProFlies Pictures (xBAA) v2."
Generated: DETERMINISTIC_605580c346c1e048
Batch ID: 20250622_210803
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

contract LimitedEditionNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    using Strings for uint256;

    Counters.Counter private _tokenIdCounter;
    
    uint256 public constant MAX_SUPPLY = 1000;
    uint256 public constant PRICE = 0.05 ether;
    string public baseURI;
    bool public saleIsActive = false;
    string public contractURI;

    event Minted(address indexed to, uint256 tokenId);

    constructor(
        string memory name,
        string memory symbol,
        string memory initialBaseURI,
        string memory initialContractURI
    ) ERC721(name, symbol) {
        baseURI = initialBaseURI;
        contractURI = initialContractURI;
    }

    modifier whenSaleIsActive() {
        require(saleIsActive, "Sale is not active");
        _;
    }

    function totalSupply() public view returns (uint256) {
        return _tokenIdCounter.current();
    }

    function setBaseURI(string memory newBaseURI) external onlyOwner {
        baseURI = newBaseURI;
    }

    function setContractURI(string memory newContractURI) external onlyOwner {
        contractURI = newContractURI;
    }

    function toggleSale() external onlyOwner {
        saleIsActive = !saleIsActive;
    }

    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        payable(owner()).transfer(balance);
    }

    function mint(address to, uint256 quantity) external payable whenSaleIsActive {
        require(quantity > 0, "Quantity must be greater than 0");
        require(
            _tokenIdCounter.current() + quantity <= MAX_SUPPLY,
            "Exceeds max supply"
        );
        require(msg.value >= PRICE * quantity, "Insufficient payment");

        for (uint256 i = 0; i < quantity; i++) {
            _tokenIdCounter.increment();
            uint256 tokenId = _tokenIdCounter.current();
            _safeMint(to, tokenId);
            emit Minted(to, tokenId);
        }
    }

    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return string(abi.encodePacked(baseURI, tokenId.toString()));
    }

    function reserveTokens(uint256 quantity) external onlyOwner {
        require(
            _tokenIdCounter.current() + quantity <= MAX_SUPPLY,
            "Exceeds max supply"
        );

        for (uint256 i = 0; i < quantity; i++) {
            _tokenIdCounter.increment();
            uint256 tokenId = _tokenIdCounter.current();
            _safeMint(owner(), tokenId);
            emit Minted(owner(), tokenId);
        }
    }
}
```
