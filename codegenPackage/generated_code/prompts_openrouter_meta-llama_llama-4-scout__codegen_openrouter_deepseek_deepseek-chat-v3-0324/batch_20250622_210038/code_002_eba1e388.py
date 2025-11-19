"""
Generated Code Metadata:
========================
Original URL: https://artyfact-game-6gr.pages.dev
Prompt: "Generate a smart contract in Solidity for managing $ARTY token transactions and NFT ownership within the Artyfact ecosystem."
Generated: DETERMINISTIC_eba1e388c81e3cb5
Batch ID: 20250622_210038
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Snapshot.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract ArtyfactToken is ERC20, ERC20Burnable, ERC20Snapshot, Ownable {
    using Counters for Counters.Counter;

    constructor() ERC20("Artyfact Token", "ARTY") {
        _mint(msg.sender, 1000000000 * 10 ** decimals());
    }

    function snapshot() public onlyOwner {
        _snapshot();
    }

    function _beforeTokenTransfer(address from, address to, uint256 amount)
        internal
        override(ERC20, ERC20Snapshot)
    {
        super._beforeTokenTransfer(from, to, amount);
    }
}

contract ArtyfactNFT is ERC721, ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    string private _baseTokenURI;

    constructor(string memory baseURI) ERC721("Artyfact NFT", "ARTYNFT") {
        _baseTokenURI = baseURI;
    }

    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    function setBaseURI(string memory baseURI) public onlyOwner {
        _baseTokenURI = baseURI;
    }

    function mint(address to) public onlyOwner returns (uint256) {
        require(to != address(0), "Cannot mint to zero address");
        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();
        _safeMint(to, tokenId);
        return tokenId;
    }

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

contract ArtyfactMarketplace is Ownable {
    ArtyfactToken public artyToken;
    ArtyfactNFT public artyNFT;

    struct Listing {
        address seller;
        uint256 price;
        bool isActive;
    }

    mapping(uint256 => Listing) public nftListings;
    mapping(address => uint256) public artistRoyalties;

    event NFTListed(uint256 indexed tokenId, address seller, uint256 price);
    event NFTSold(uint256 indexed tokenId, address buyer, uint256 price);
    event RoyaltyPaid(address indexed artist, uint256 amount);

    constructor(address tokenAddress, address nftAddress) {
        artyToken = ArtyfactToken(tokenAddress);
        artyNFT = ArtyfactNFT(nftAddress);
    }

    function listNFT(uint256 tokenId, uint256 price) external {
        require(artyNFT.ownerOf(tokenId) == msg.sender, "Not the owner");
        require(price > 0, "Price must be greater than zero");
        
        nftListings[tokenId] = Listing({
            seller: msg.sender,
            price: price,
            isActive: true
        });

        emit NFTListed(tokenId, msg.sender, price);
    }

    function buyNFT(uint256 tokenId) external {
        Listing memory listing = nftListings[tokenId];
        require(listing.isActive, "NFT not for sale");
        require(artyToken.balanceOf(msg.sender) >= listing.price, "Insufficient balance");

        uint256 royaltyFee = listing.price * 10 / 100; // 10% royalty
        uint256 sellerAmount = listing.price - royaltyFee;

        artyToken.transferFrom(msg.sender, listing.seller, sellerAmount);
        artyToken.transferFrom(msg.sender, owner(), royaltyFee);

        artyNFT.safeTransferFrom(listing.seller, msg.sender, tokenId);

        artistRoyalties[listing.seller] += royaltyFee;
        nftListings[tokenId].isActive = false;

        emit NFTSold(tokenId, msg.sender, listing.price);
        emit RoyaltyPaid(listing.seller, royaltyFee);
    }

    function cancelListing(uint256 tokenId) external {
        require(nftListings[tokenId].seller == msg.sender, "Not the seller");
        require(nftListings[tokenId].isActive, "Listing not active");

        nftListings[tokenId].isActive = false;
    }

    function withdrawRoyalties() external {
        uint256 amount = artistRoyalties[msg.sender];
        require(amount > 0, "No royalties to withdraw");

        artistRoyalties[msg.sender] = 0;
        artyToken.transfer(msg.sender, amount);
    }
}
```
