"""
Generated Code Metadata:
========================
Original URL: https://dogepreneur-io.pages.dev
Prompt: "Write a smart contract in Solidity to facilitate the buying and selling of tokenized real estate assets on the BNB Smart Chain, similar to Dogepreneur."
Generated: DETERMINISTIC_82cfd185dcb9f481
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
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title RealEstateToken
 * @author [Your Name]
 * @notice A smart contract for buying and selling tokenized real estate assets on the BNB Smart Chain.
 */
contract RealEstateToken is ERC721URIStorage, ReentrancyGuard {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    // Mapping of token ID to its current owner and price
    mapping(uint256 => TokenInfo) public tokenInfos;

    // Event emitted when a new token is minted
    event NewToken(address indexed owner, uint256 tokenId);

    // Event emitted when a token is transferred
    event TokenTransferred(address indexed from, address indexed to, uint256 tokenId);

    // Event emitted when a token's price is updated
    event TokenPriceUpdated(uint256 tokenId, uint256 newPrice);

    // Struct to hold token information
    struct TokenInfo {
        address owner;
        uint256 price;
    }

    /**
     * @dev Constructor for the RealEstateToken contract.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Mint a new token with the given URI and price.
     * @param recipient The address of the recipient.
     * @param tokenURI The URI of the token.
     * @param price The initial price of the token.
     * @return The ID of the newly minted token.
     */
    function mint(address recipient, string memory tokenURI, uint256 price) public returns (uint256) {
        _tokenIds.increment();

        uint256 newTokenId = _tokenIds.current();
        _mint(recipient, newTokenId);
        _setTokenURI(newTokenId, tokenURI);
        tokenInfos[newTokenId] = TokenInfo(recipient, price);

        emit NewToken(recipient, newTokenId);
        return newTokenId;
    }

    /**
     * @dev Transfer a token to a new owner.
     * @param from The current owner of the token.
     * @param to The new owner of the token.
     * @param tokenId The ID of the token to transfer.
     */
    function transfer(address from, address to, uint256 tokenId) public {
        require(msg.sender == tokenInfos[tokenId].owner, "Only the owner can transfer the token");
        _transfer(from, to);
        tokenInfos[tokenId].owner = to;

        emit TokenTransferred(from, to, tokenId);
    }

    /**
     * @dev Update the price of a token.
     * @param tokenId The ID of the token to update.
     * @param newPrice The new price of the token.
     */
    function updatePrice(uint256 tokenId, uint256 newPrice) public {
        require(msg.sender == tokenInfos[tokenId].owner, "Only the owner can update the price");
        tokenInfos[tokenId].price = newPrice;

        emit TokenPriceUpdated(tokenId, newPrice);
    }

    /**
     * @dev Buy a token.
     * @param tokenId The ID of the token to buy.
     */
    function buy(uint256 tokenId) public payable {
        require(msg.value >= tokenInfos[tokenId].price, "Insufficient payment");
        address seller = tokenInfos[tokenId].owner;
        _transfer(seller, msg.sender);
        tokenInfos[tokenId].owner = msg.sender;
        payable(seller).transfer(msg.value);

        emit TokenTransferred(seller, msg.sender, tokenId);
    }

    /**
     * @dev Get the information of a token.
     * @param tokenId The ID of the token to query.
     * @return The owner and price of the token.
     */
    function getTokenInfo(uint256 tokenId) public view returns (address, uint256) {
        return (tokenInfos[tokenId].owner, tokenInfos[tokenId].price);
    }
}
```
