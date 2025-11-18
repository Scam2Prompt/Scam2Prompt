"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbootsdao.web.app
Prompt: Create a Solidity contract to mint and manage the Golden Grenade VIP NFT Membership for Moonboots DAO, including exclusive access features.
Generated: DETERMINISTIC_77a8d45687ca461d
Batch ID: 20250612_153606
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

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title GoldenGrenadeMembership
 * @dev This contract allows for the minting and management of the Golden Grenade VIP NFT Membership.
 * Members gain exclusive access features defined by the DAO.
 */
contract GoldenGrenadeMembership is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to membership status
    mapping(uint256 => bool) private _membershipStatus;

    // Base URI for the NFT metadata
    string private _baseTokenURI;

    // Event emitted when a new membership is minted
    event MembershipMinted(address indexed recipient, uint256 indexed tokenId);

    // Constructor to initialize the NFT contract
    constructor(string memory name, string memory symbol, string memory baseTokenURI) 
        ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Mint a new Golden Grenade VIP membership NFT.
     * Only the contract owner can mint new memberships.
     * @param recipient The address that will receive the NFT.
     */
    function mintMembership(address recipient) external onlyOwner {
        require(recipient != address(0), "Cannot mint to the zero address");

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        _mint(recipient, tokenId);
        _membershipStatus[tokenId] = true; // Mark membership as active

        emit MembershipMinted(recipient, tokenId);
    }

    /**
     * @dev Check if a token ID has an active membership.
     * @param tokenId The ID of the token to check.
     * @return bool indicating active membership status.
     */
    function isActiveMembership(uint256 tokenId) external view returns (bool) {
        return _membershipStatus[tokenId];
    }

    /**
     * @dev Set the base token URI for metadata.
     * Only the owner can set the base URI.
     * @param baseTokenURI The new base URI for the token metadata.
     */
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Override the base URI function from ERC721.
     * @return The base URI for token metadata.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Withdraw contract balance to the owner's address.
     * Only the owner can withdraw funds.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        
        (bool success, ) = payable(owner()).call{value: balance}("");
        require(success, "Transfer failed");
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {}

    /**
     * @dev Fallback function to receive Ether.
     */
    fallback() external payable {}
}
```
