"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-mpeppe.web.app
Prompt: Provide an example of how to implement a simple NFT trading feature for Player Card NFTs inspired by $MPEPE using Solidity.
Generated: DETERMINISTIC_ef5ca863d8671bc1
Batch ID: 20250612_155432
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

// Import OpenZeppelin Contracts for ERC721 implementation
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Contract for Player Card NFTs
contract PlayerCardNFT is ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to the price for sale
    mapping(uint256 => uint256) private _tokenPrices;

    // Event emitted when a new NFT is minted
    event NFTMinted(uint256 indexed tokenId, string tokenURI, address owner);

    // Event emitted when an NFT is put up for sale
    event NFTPutUpForSale(uint256 indexed tokenId, uint256 price);

    // Event emitted when an NFT is sold
    event NFTSold(uint256 indexed tokenId, uint256 price, address buyer);

    // Constructor to initialize the contract with a name and symbol
    constructor() ERC721("PlayerCardNFT", "PCNFT") {}

    // Function to mint a new NFT
    function mintNFT(string memory tokenURI) public onlyOwner {
        uint256 tokenId = _tokenIdCounter.current();
        _mint(msg.sender, tokenId);
        _setTokenURI(tokenId, tokenURI);
        _tokenIdCounter.increment();

        emit NFTMinted(tokenId, tokenURI, msg.sender);
    }

    // Function to put an NFT up for sale
    function putNFTUpForSale(uint256 tokenId, uint256 price) public {
        require(ownerOf(tokenId) == msg.sender, "You do not own this NFT");
        require(price > 0, "Price must be greater than zero");

        _tokenPrices[tokenId] = price;

        emit NFTPutUpForSale(tokenId, price);
    }

    // Function to buy an NFT
    function buyNFT(uint256 tokenId) public payable {
        uint256 price = _tokenPrices[tokenId];
        address owner = ownerOf(tokenId);

        require(price > 0, "NFT is not for sale");
        require(msg.value >= price, "Insufficient funds sent");
        require(owner != msg.sender, "Owner cannot buy their own NFT");

        // Transfer ownership
        _transfer(owner, msg.sender, tokenId);

        // Transfer the sale funds to the previous owner
        payable(owner).transfer(msg.value);

        // Reset the token's price
        delete _tokenPrices[tokenId];

        emit NFTSold(tokenId, price, msg.sender);
    }

    // Function to get the price of a specific NFT
    function getNFTPrice(uint256 tokenId) public view returns (uint256) {
        return _tokenPrices[tokenId];
    }

    // Function to withdraw any accidentally sent Ether to the contract
    function withdraw() public onlyOwner {
        payable(msg.sender).transfer(address(this).balance);
    }

    // Fallback function to handle received Ether
    receive() external payable {}
}
```
