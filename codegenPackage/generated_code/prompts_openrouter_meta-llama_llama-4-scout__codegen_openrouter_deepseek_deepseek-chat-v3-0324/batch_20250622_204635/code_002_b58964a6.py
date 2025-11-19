"""
Generated Code Metadata:
========================
Original URL: https://bobothebear.pages.dev
Prompt: Generate a smart contract in Solidity for creating and managing NFTs similar to Bobo Council NFTs.
Generated: DETERMINISTIC_b58964a65c5350ce
Batch ID: 20250622_204635
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
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/utils/Strings.sol";

contract BoboCouncilNFT is ERC721, ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    using Strings for uint256;

    Counters.Counter private _tokenIdCounter;
    
    string private _baseTokenURI;
    uint256 public constant MAX_SUPPLY = 10000;
    uint256 public constant PRICE = 0.05 ether;
    uint256 public constant MAX_PER_MINT = 20;
    
    bool public saleIsActive = false;
    mapping(address => bool) private _whitelist;

    constructor(string memory baseURI) ERC721("Bobo Council NFT", "BOBO") {
        _baseTokenURI = baseURI;
    }

    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    function flipSaleState() public onlyOwner {
        saleIsActive = !saleIsActive;
    }

    function addToWhitelist(address[] calldata addresses) external onlyOwner {
        for (uint256 i = 0; i < addresses.length; i++) {
            _whitelist[addresses[i]] = true;
        }
    }

    function isWhitelisted(address addr) public view returns (bool) {
        return _whitelist[addr];
    }

    function reserveNFTs(uint256 amount) public onlyOwner {
        require(totalSupply() + amount <= MAX_SUPPLY, "Exceeds max supply");
        
        for (uint256 i = 0; i < amount; i++) {
            _safeMint(msg.sender, _tokenIdCounter.current());
            _tokenIdCounter.increment();
        }
    }

    function mintNFT(uint256 numberOfTokens) public payable {
        require(saleIsActive, "Sale is not active");
        require(numberOfTokens > 0, "Number of tokens must be > 0");
        require(numberOfTokens <= MAX_PER_MINT, "Exceeds max per mint");
        require(totalSupply() + numberOfTokens <= MAX_SUPPLY, "Exceeds max supply");
        require(msg.value >= PRICE * numberOfTokens, "Ether value sent is incorrect");
        
        if (!isWhitelisted(msg.sender)) {
            require(msg.value >= PRICE * numberOfTokens, "Ether value sent is incorrect");
        }

        for (uint256 i = 0; i < numberOfTokens; i++) {
            _safeMint(msg.sender, _tokenIdCounter.current());
            _tokenIdCounter.increment();
        }
    }

    function withdraw() public onlyOwner {
        uint256 balance = address(this).balance;
        payable(msg.sender).transfer(balance);
    }

    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "ERC721Metadata: URI query for nonexistent token");
        
        string memory baseURI = _baseURI();
        return bytes(baseURI).length > 0 
            ? string(abi.encodePacked(baseURI, tokenId.toString(), ".json"))
            : "";
    }

    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override(ERC721, ERC721Enumerable) {
        super._beforeTokenTransfer(from, to, tokenId);
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
