"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://saitachaincoin.live
Prompt: Write a smart contract for minting interoperable NFTs on SaitaChain that can be used across multiple platforms.
Generated: DETERMINISTIC_a9afeeed109c874e
Batch ID: 20250612_153809
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

// Import required interfaces from OpenZeppelin for ERC721 implementation
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title InteroperableNFT
 * @dev A smart contract for minting interoperable NFTs on SaitaChain.
 * This contract extends the ERC721 standard and allows the owner to mint new tokens.
 */
contract InteroperableNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to a unique token URI
    mapping(uint256 => string) private _tokenURIs;

    // Event emitted when a new token is minted
    event TokenMinted(address indexed owner, uint256 tokenId, string tokenURI);

    constructor() ERC721("InteroperableNFT", "iNFT") {}

    /**
     * @dev Mint a new token with a given URI.
     * @param to The address that will own the minted token.
     * @param uri The URI pointing to the token's metadata.
     */
    function mint(string memory uri) external onlyOwner {
        require(bytes(uri).length > 0, "Token URI cannot be empty");

        // Increment the token ID counter
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the new token
        _mint(msg.sender, tokenId);
        _setTokenURI(tokenId, uri);

        emit TokenMinted(msg.sender, tokenId, uri);
    }

    /**
     * @dev Set the token URI for a specific token ID.
     * @param tokenId The ID of the token to set the URI for.
     * @param uri The URI to assign to the token.
     */
    function _setTokenURI(uint256 tokenId, string memory uri) internal {
        require(_exists(tokenId), "URI set of nonexistent token");
        _tokenURIs[tokenId] = uri;
    }

    /**
     * @dev Retrieve the token URI for a specific token ID.
     * @param tokenId The ID of the token to retrieve the URI for.
     * @return The token URI as a string.
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "URI query for nonexistent token");

        return _tokenURIs[tokenId];
    }

    /**
     * @dev Withdraw contract's balance to the owner's address.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");

        // Transfer the balance to the owner
        (bool success, ) = owner().call{value: balance}("");
        require(success, "Transfer failed");
    }

    // Fallback function to receive Ether
    receive() external payable {}
}
```
