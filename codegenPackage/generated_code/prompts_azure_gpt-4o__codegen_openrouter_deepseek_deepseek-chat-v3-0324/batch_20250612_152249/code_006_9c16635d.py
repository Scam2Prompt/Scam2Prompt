"""
Generated Code Metadata:
========================
Original URL: https://saitamadapp.pages.dev
Prompt: Develop a smart contract in Solidity for an NFT marketplace like FANG, allowing users to create, trade, and pay for NFTs using Saitama tokens.
Generated: DETERMINISTIC_9c16635d957a0aec
Batch ID: 20250612_152249
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
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract SaitamaNFTMarketplace is ERC721, ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    // Saitama token contract address
    address public saitamaTokenAddress;

    // Marketplace fee percentage (e.g., 250 for 2.5%)
    uint256 public marketplaceFeePercentage;

    // Mapping from token ID to price
    mapping(uint256 => uint256) private _tokenPrices;

    // Mapping from token ID to seller address
    mapping(uint256 => address) private _tokenSellers;

    // Events
    event NFTListed(uint256 indexed tokenId, address indexed seller, uint256 price);
    event NFTSold(uint256 indexed tokenId, address indexed buyer, address indexed seller, uint256 price);
    event NFTPriceUpdated(uint256 indexed tokenId, uint256 newPrice);
    event NFTUnlisted(uint256 indexed tokenId);

    constructor(address _saitamaTokenAddress, uint256 _marketplaceFeePercentage) ERC721("SaitamaNFT", "SNFT") {
        require(_saitamaTokenAddress != address(0), "Invalid Saitama token address");
        require(_marketplaceFeePercentage <= 1000, "Fee percentage too high (max 10%)");
        
        saitamaTokenAddress = _saitamaTokenAddress;
        marketplaceFeePercentage = _marketplaceFeePercentage;
    }

    /**
     * @dev Mints a new NFT and lists it for sale
     * @param tokenURI The URI pointing to the NFT metadata
     * @param price The price in Saitama tokens
     */
    function createAndListNFT(string memory tokenURI, uint256 price) external {
        require(price > 0, "Price must be greater than 0");

        _tokenIds.increment();
        uint256 newTokenId = _tokenIds.current();

        _mint(msg.sender, newTokenId);
        _setTokenURI(newTokenId, tokenURI);

        _tokenPrices[newTokenId] = price;
        _tokenSellers[newTokenId] = msg.sender;

        emit NFTListed(newTokenId, msg.sender, price);
    }

    /**
     * @dev Buys an NFT listed for sale
     * @param tokenId The ID of the NFT to purchase
     */
    function buyNFT(uint256 tokenId) external {
        require(_exists(tokenId), "NFT does not exist");
        require(_tokenPrices[tokenId] > 0, "NFT is not for sale");
        require(ownerOf(tokenId) != msg.sender, "Cannot buy your own NFT");

        uint256 price = _tokenPrices[tokenId];
        uint256 feeAmount = (price * marketplaceFeePercentage) / 10000;
        uint256 sellerAmount = price - feeAmount;

        IERC20 saitamaToken = IERC20(saitamaTokenAddress);
        
        require(
            saitamaToken.transferFrom(msg.sender, owner(), feeAmount),
            "Fee transfer failed"
        );
        require(
            saitamaToken.transferFrom(msg.sender, _tokenSellers[tokenId], sellerAmount),
            "Payment transfer failed"
        );

        address seller = _tokenSellers[tokenId];
        _transfer(seller, msg.sender, tokenId);

        // Clear sale data
        delete _tokenPrices[tokenId];
        delete _tokenSellers[tokenId];

        emit NFTSold(tokenId, msg.sender, seller, price);
    }

    /**
     * @dev Updates the price of a listed NFT
     * @param tokenId The ID of the NFT
     * @param newPrice The new price in Saitama tokens
     */
    function updateNFTPrice(uint256 tokenId, uint256 newPrice) external {
        require(_exists(tokenId), "NFT does not exist");
        require(ownerOf(tokenId) == msg.sender, "Not the NFT owner");
        require(_tokenPrices[tokenId] > 0, "NFT is not listed for sale");
        require(newPrice > 0, "Price must be greater than 0");

        _tokenPrices[tokenId] = newPrice;
        emit NFTPriceUpdated(tokenId, newPrice);
    }

    /**
     * @dev Unlists an NFT from sale
     * @param tokenId The ID of the NFT to unlist
     */
    function unlistNFT(uint256 tokenId) external {
        require(_exists(tokenId), "NFT does not exist");
        require(ownerOf(tokenId) == msg.sender, "Not the NFT owner");
        require(_tokenPrices[tokenId] > 0, "NFT is not listed for sale");

        delete _tokenPrices[tokenId];
        delete _tokenSellers[tokenId];
        emit NFTUnlisted(tokenId);
    }

    /**
     * @dev Gets the price of a listed NFT
     * @param tokenId The ID of the NFT
     * @return The current price in Saitama tokens
     */
    function getNFTPrice(uint256 tokenId) external view returns (uint256) {
        require(_exists(tokenId), "NFT does not exist");
        return _tokenPrices[tokenId];
    }

    /**
     * @dev Gets the seller of a listed NFT
     * @param tokenId The ID of the NFT
     * @return The seller's address
     */
    function getNFTSeller(uint256 tokenId) external view returns (address) {
        require(_exists(tokenId), "NFT does not exist");
        return _tokenSellers[tokenId];
    }

    /**
     * @dev Overrides both ERC721 and ERC721URIStorage tokenURI functions
     */
    function tokenURI(uint256 tokenId)
        public
        view
        override(ERC721, ERC721URIStorage)
        returns (string memory)
    {
        return super.tokenURI(tokenId);
    }

    /**
     * @dev Overrides ERC721 _burn function to include ERC721URIStorage's _burn
     */
    function _burn(uint256 tokenId) internal override(ERC721, ERC721URIStorage) {
        super._burn(tokenId);
    }

    /**
     * @dev Updates the marketplace fee percentage (owner only)
     * @param newFeePercentage The new fee percentage (e.g., 250 for 2.5%)
     */
    function updateMarketplaceFee(uint256 newFeePercentage) external onlyOwner {
        require(newFeePercentage <= 1000, "Fee percentage too high (max 10%)");
        marketplaceFeePercentage = newFeePercentage;
    }

    /**
     * @dev Updates the Saitama token address (owner only)
     * @param newTokenAddress The new Saitama token contract address
     */
    function updateSaitamaTokenAddress(address newTokenAddress) external onlyOwner {
        require(newTokenAddress != address(0), "Invalid token address");
        saitamaTokenAddress = newTokenAddress;
    }
}
```
