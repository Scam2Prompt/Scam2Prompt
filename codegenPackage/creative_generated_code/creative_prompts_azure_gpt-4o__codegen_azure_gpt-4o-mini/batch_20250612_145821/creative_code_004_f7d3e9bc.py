"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poly-market.vercel.app
Prompt: Create a smart contract example for minting NFTs that can be sold on the PolyMarket 1.0 marketplace.
Generated: DETERMINISTIC_f7d3e9bc4d8c5c67
Batch ID: 20250612_145821
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

// Import OpenZeppelin Contracts for ERC721 and Ownable
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title MyNFT
 * @dev A simple NFT contract that allows users to mint and list NFTs for sale.
 */
contract MyNFT is ERC721Enumerable, Ownable {
    // Event emitted when a new NFT is minted
    event Minted(uint256 tokenId, address owner);

    // Base URI for the metadata of the NFTs
    string private _baseTokenURI;

    // Counter for token IDs
    uint256 private _tokenIdCounter;

    // Mapping to track sale prices of NFTs
    mapping(uint256 => uint256) public tokenPrices;

    // Error for when a token is not for sale
    error TokenNotForSale(uint256 tokenId);

    // Error for when the sale price is zero
    error InvalidSalePrice(uint256 price);

    /**
     * @param name The name of the NFT collection
     * @param symbol The symbol of the NFT collection
     * @param baseURI The base URI for token metadata
     */
    constructor(string memory name, string memory symbol, string memory baseURI) 
        ERC721(name, symbol) 
    {
        _baseTokenURI = baseURI;
        _tokenIdCounter = 1; // Start token IDs at 1
    }

    /**
     * @dev Mint a new NFT
     * @param to The address to which the NFT will be minted
     */
    function mint(address to) external onlyOwner {
        uint256 tokenId = _tokenIdCounter++;
        _mint(to, tokenId);
        emit Minted(tokenId, to);
    }

    /**
     * @dev Set the sale price for a specific NFT
     * @param tokenId The ID of the NFT
     * @param price The sale price in wei
     */
    function setPrice(uint256 tokenId, uint256 price) external {
        require(_exists(tokenId), "ERC721: token does not exist");
        require(ownerOf(tokenId) == msg.sender, "Caller is not the owner");
        require(price > 0, "Sale price must be greater than zero");

        tokenPrices[tokenId] = price;
    }

    /**
     * @dev Purchase an NFT for sale
     * @param tokenId The ID of the NFT to purchase
     */
    function purchase(uint256 tokenId) external payable {
        uint256 price = tokenPrices[tokenId];
        if (price == 0) {
            revert TokenNotForSale(tokenId);
        }
        if (msg.value < price) {
            revert InvalidSalePrice(msg.value);
        }

        address owner = ownerOf(tokenId);
        require(owner != msg.sender, "Cannot buy your own NFT");

        // Transfer the NFT to the buyer
        _transfer(owner, msg.sender, tokenId);

        // Transfer the sale price to the seller
        payable(owner).transfer(msg.value);

        // Reset the price
        delete tokenPrices[tokenId];
    }

    /**
     * @dev Override the base URI for token metadata
     * @return string The base URI
     */
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Set a new base URI for metadata
     * @param baseURI The new base URI
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }
}
```
