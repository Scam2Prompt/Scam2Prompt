"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orange-pepe.pages.dev
Prompt: Write a script to mint $ORPE-themed NFTs and list them on an exclusive marketplace accessible only to $ORPE holders.
Generated: DETERMINISTIC_bb896d7af29b95de
Batch ID: 20250612_150018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Below is the clean, production-ready code for minting $ORPE-themed NFTs and listing them on an exclusive marketplace. The implementation assumes use of the Solidity smart contract language, with the OpenZeppelin library for best practices. The code is designed to interact with an ERC-20 token ($ORPE) for access control.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import OpenZeppelin libraries for ERC721 and ERC20 standards
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract ORPENFTMarketplace is ERC721Enumerable, Ownable {
    // Reference to the $ORPE ERC-20 token contract
    IERC20 private orpeToken;

    // NFT metadata base URI
    string private baseURI;

    // Maximum number of NFTs that can be minted
    uint256 public constant MAX_SUPPLY = 10000;

    // Price of each NFT in native currency (e.g., ETH)
    uint256 public constant MINT_PRICE = 0.05 ether;

    // Mapping to store NFT listings (tokenId => price in $ORPE)
    mapping(uint256 => uint256) public marketplaceListings;

    // Event emitted when an NFT is listed for sale
    event NFTListed(uint256 indexed tokenId, uint256 priceInORPE);

    // Event emitted when an NFT is sold
    event NFTSold(uint256 indexed tokenId, address indexed buyer, uint256 priceInORPE);

    // Constructor to initialize the NFT contract and the $ORPE token reference
    constructor(address _orpeTokenAddress, string memory _baseURI) ERC721("ORPE NFT", "ORPENFT") {
        require(_orpeTokenAddress != address(0), "Invalid $ORPE token address");
        orpeToken = IERC20(_orpeTokenAddress);
        baseURI = _baseURI;
    }

    // Override the base URI function from ERC721
    function _baseURI() internal view override returns (string memory) {
        return baseURI;
    }

    // Mint a new NFT, requires payment in native currency
    function mintNFT(uint256 numberOfTokens) external payable {
        require(totalSupply() + numberOfTokens <= MAX_SUPPLY, "Exceeds maximum supply");
        require(msg.value == MINT_PRICE * numberOfTokens, "Incorrect payment amount");

        for (uint256 i = 0; i < numberOfTokens; i++) {
            uint256 tokenId = totalSupply() + 1; // Token IDs start from 1
            _safeMint(msg.sender, tokenId);
        }
    }

    // List an NFT for sale on the marketplace (accessible only to $ORPE holders)
    function listNFT(uint256 tokenId, uint256 priceInORPE) external {
        require(ownerOf(tokenId) == msg.sender, "You do not own this NFT");
        require(orpeToken.balanceOf(msg.sender) > 0, "Access restricted to $ORPE holders");
        require(priceInORPE > 0, "Price must be greater than zero");

        marketplaceListings[tokenId] = priceInORPE;

        emit NFTListed(tokenId, priceInORPE);
    }

    // Purchase an NFT from the marketplace
    function buyNFT(uint256 tokenId) external {
        require(marketplaceListings[tokenId] > 0, "NFT is not listed for sale");

        uint256 priceInORPE = marketplaceListings[tokenId];
        address seller = ownerOf(tokenId);

        // Transfer $ORPE tokens from buyer to seller
        require(orpeToken.transferFrom(msg.sender, seller, priceInORPE), "Token transfer failed");

        // Transfer NFT ownership from seller to buyer
        _transfer(seller, msg.sender, tokenId);

        // Remove the listing
        marketplaceListings[tokenId] = 0;

        emit NFTSold(tokenId, msg.sender, priceInORPE);
    }

    // Withdraw collected native currency funds from minting
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner()).transfer(balance);
    }
}
```

This script requires the OpenZeppelin library and assumes you have an ERC-20 $ORPE token deployed. Make sure to set the `$ORPE` token address and the base URI for the NFT metadata when deploying the contract.
