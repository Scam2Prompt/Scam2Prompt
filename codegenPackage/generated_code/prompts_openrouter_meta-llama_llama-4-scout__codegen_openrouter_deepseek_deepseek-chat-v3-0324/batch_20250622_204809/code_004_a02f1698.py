"""
Generated Code Metadata:
========================
Original URL: https://pablo-defis.web.app
Prompt: Create a Solidity smart contract for an NFT collection, similar to the Pablo Cartel NFT Collection, with functionality for minting, buying, and selling NFTs, and integrating it with the $PABLO token ecosystem.
Generated: DETERMINISTIC_a02f1698a9f0bcf8
Batch ID: 20250622_204809
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract PabloCartelNFT is ERC721, ERC721Enumerable, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    
    Counters.Counter private _tokenIdCounter;
    
    // Token contract address
    IERC20 public pabloToken;
    
    // NFT metadata
    string public baseURI;
    uint256 public maxSupply;
    uint256 public mintPrice;
    uint256 public saleFeePercentage;
    
    // Mapping from token ID to sale price
    mapping(uint256 => uint256) private _tokenPrices;
    
    // Events
    event NFTMinted(address indexed owner, uint256 tokenId, uint256 price);
    event NFTPurchased(address indexed buyer, address indexed seller, uint256 tokenId, uint256 price);
    event NFTPriced(uint256 indexed tokenId, uint256 price);
    
    constructor(
        string memory name,
        string memory symbol,
        string memory _baseURI,
        uint256 _maxSupply,
        uint256 _mintPrice,
        uint256 _saleFeePercentage,
        address _pabloToken
    ) ERC721(name, symbol) {
        baseURI = _baseURI;
        maxSupply = _maxSupply;
        mintPrice = _mintPrice;
        saleFeePercentage = _saleFeePercentage;
        pabloToken = IERC20(_pabloToken);
    }
    
    function _baseURI() internal view override returns (string memory) {
        return baseURI;
    }
    
    function setBaseURI(string memory _baseURI) external onlyOwner {
        baseURI = _baseURI;
    }
    
    function setMintPrice(uint256 _mintPrice) external onlyOwner {
        mintPrice = _mintPrice;
    }
    
    function setSaleFeePercentage(uint256 _saleFeePercentage) external onlyOwner {
        require(_saleFeePercentage <= 100, "Fee percentage cannot exceed 100");
        saleFeePercentage = _saleFeePercentage;
    }
    
    function mintNFT() external nonReentrant {
        require(totalSupply() < maxSupply, "Max supply reached");
        require(pabloToken.transferFrom(msg.sender, address(this), mintPrice), "Token transfer failed");
        
        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();
        _safeMint(msg.sender, tokenId);
        
        emit NFTMinted(msg.sender, tokenId, mintPrice);
    }
    
    function setPrice(uint256 tokenId, uint256 price) external {
        require(_exists(tokenId), "Token does not exist");
        require(ownerOf(tokenId) == msg.sender, "Not the owner");
        _tokenPrices[tokenId] = price;
        
        emit NFTPriced(tokenId, price);
    }
    
    function buyNFT(uint256 tokenId) external nonReentrant {
        require(_exists(tokenId), "Token does not exist");
        uint256 price = _tokenPrices[tokenId];
        require(price > 0, "Token is not for sale");
        
        address seller = ownerOf(tokenId);
        require(seller != msg.sender, "Cannot buy your own NFT");
        
        uint256 feeAmount = (price * saleFeePercentage) / 100;
        uint256 sellerAmount = price - feeAmount;
        
        require(pabloToken.transferFrom(msg.sender, seller, sellerAmount), "Token transfer to seller failed");
        if (feeAmount > 0) {
            require(pabloToken.transferFrom(msg.sender, address(this), feeAmount), "Token transfer fee failed");
        }
        
        _transfer(seller, msg.sender, tokenId);
        _tokenPrices[tokenId] = 0;
        
        emit NFTPurchased(msg.sender, seller, tokenId, price);
    }
    
    function withdrawTokens() external onlyOwner {
        uint256 balance = pabloToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(pabloToken.transfer(msg.sender, balance), "Token transfer failed");
    }
    
    function getPrice(uint256 tokenId) external view returns (uint256) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenPrices[tokenId];
    }
    
    // Override required by Solidity
    function _beforeTokenTransfer(address from, address to, uint256 tokenId)
        internal
        override(ERC721, ERC721Enumerable)
    {
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
