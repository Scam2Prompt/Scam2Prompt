"""
Generated Code Metadata:
========================
Original URL: https://superrare.fr
Prompt: Provide a step-by-step guide on how to program royalties into an NFT smart contract, referencing the functionality discussed on SuperRare.fr.
Generated: DETERMINISTIC_fdc7c202322238fe
Batch ID: 20250612_155037
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

/**
 * @title RoyaltyNFT
 * @dev ERC721 token with royalty functionality
 */
contract RoyaltyNFT is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    // Struct to store royalty information
    struct RoyaltyInfo {
        address recipient;
        uint256 percentage; // Basis points (10000 = 100%)
    }

    // Mapping from token ID to royalty info
    mapping(uint256 => RoyaltyInfo) private _royalties;

    // Events
    event RoyaltySet(uint256 tokenId, address recipient, uint256 percentage);
    event RoyaltyPaid(uint256 tokenId, address recipient, uint256 amount);

    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Mint a new NFT with royalty information
     * @param to The address to mint the NFT to
     * @param tokenURI The URI of the NFT metadata
     * @param royaltyRecipient The address to receive royalties
     * @param royaltyPercentage The royalty percentage in basis points (10000 = 100%)
     */
    function mintWithRoyalty(
        address to,
        string memory tokenURI,
        address royaltyRecipient,
        uint256 royaltyPercentage
    ) public onlyOwner returns (uint256) {
        require(royaltyPercentage <= 10000, "Royalty percentage too high");

        _tokenIds.increment();
        uint256 newTokenId = _tokenIds.current();

        _mint(to, newTokenId);
        _setTokenURI(newTokenId, tokenURI);

        _royalties[newTokenId] = RoyaltyInfo(royaltyRecipient, royaltyPercentage);
        emit RoyaltySet(newTokenId, royaltyRecipient, royaltyPercentage);

        return newTokenId;
    }

    /**
     * @dev Get royalty information for a token
     * @param tokenId The token ID to query
     * @return recipient The address to receive royalties
     * @return percentage The royalty percentage in basis points
     */
    function getRoyaltyInfo(uint256 tokenId) public view returns (address recipient, uint256 percentage) {
        require(_exists(tokenId), "Token does not exist");
        RoyaltyInfo memory royalty = _royalties[tokenId];
        return (royalty.recipient, royalty.percentage);
    }

    /**
     * @dev Calculate royalty amount for a given sale price
     * @param tokenId The token ID to calculate royalty for
     * @param salePrice The sale price of the NFT
     * @return recipient The address to receive royalties
     * @return amount The royalty amount
     */
    function royaltyInfo(uint256 tokenId, uint256 salePrice) 
        public 
        view 
        returns (address recipient, uint256 amount) 
    {
        require(_exists(tokenId), "Token does not exist");
        RoyaltyInfo memory royalty = _royalties[tokenId];
        amount = (salePrice * royalty.percentage) / 10000;
        return (royalty.recipient, amount);
    }

    /**
     * @dev Update royalty information for a token
     * @param tokenId The token ID to update
     * @param recipient The new royalty recipient
     * @param percentage The new royalty percentage in basis points
     */
    function setRoyaltyInfo(
        uint256 tokenId,
        address recipient,
        uint256 percentage
    ) public onlyOwner {
        require(_exists(tokenId), "Token does not exist");
        require(percentage <= 10000, "Royalty percentage too high");
        
        _royalties[tokenId] = RoyaltyInfo(recipient, percentage);
        emit RoyaltySet(tokenId, recipient, percentage);
    }

    /**
     * @dev Internal function to handle royalty payments during transfers
     * @param from The sender address
     * @param to The recipient address
     * @param tokenId The token ID being transferred
     * @param value The transaction value (if any)
     */
    function _transferWithRoyalty(
        address from,
        address to,
        uint256 tokenId,
        uint256 value
    ) internal {
        (address royaltyRecipient, uint256 royaltyAmount) = royaltyInfo(tokenId, value);
        
        if (royaltyAmount > 0 && royaltyRecipient != address(0)) {
            payable(royaltyRecipient).transfer(royaltyAmount);
            emit RoyaltyPaid(tokenId, royaltyRecipient, royaltyAmount);
        }

        _transfer(from, to, tokenId);
    }

    /**
     * @dev Override transfer function to include royalty payments
     */
    function transferFrom(
        address from,
        address to,
        uint256 tokenId
    ) public payable override {
        _transferWithRoyalty(from, to, tokenId, msg.value);
    }

    /**
     * @dev Override safeTransfer function to include royalty payments
     */
    function safeTransferFrom(
        address from,
        address to,
        uint256 tokenId,
        bytes memory _data
    ) public payable override {
        _transferWithRoyalty(from, to, tokenId, msg.value);
        _checkOnERC721Received(from, to, tokenId, _data);
    }
}
```
