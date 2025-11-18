"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shibasaga-io.web.app
Prompt: Write a Solidity contract that supports NFT minting for Shiba Saga characters, props, and items, ensuring compatibility with the ShiaVerse.
Generated: DETERMINISTIC_415e13d9d3ebf8d4
Batch ID: 20250612_152827
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
 * @title ShibaSagaNFT
 * @dev A contract for minting NFTs representing Shiba Saga characters, props, and items.
 * This contract uses ERC721 standards and allows only the owner to mint new tokens.
 */
contract ShibaSagaNFT is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    
    // Counter for token IDs
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to token metadata URI
    mapping(uint256 => string) private _tokenURIs;

    // Event emitted when a new NFT is minted
    event Minted(uint256 indexed tokenId, address indexed recipient, string tokenURI);

    /**
     * @dev Constructor for the ShibaSagaNFT contract
     * Sets the name and symbol for the ERC721 token.
     * @param name The name of the NFT collection
     * @param symbol The symbol of the NFT collection
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Mint a new NFT
     * Only callable by the contract owner.
     * @param recipient The address to receive the minted NFT
     * @param tokenURI The metadata URI for the token
     */
    function mintNFT(address recipient, string memory tokenURI) external onlyOwner {
        require(recipient != address(0), "Recipient address cannot be zero");
        require(bytes(tokenURI).length > 0, "Token URI cannot be empty");

        // Increment the token ID counter and get the new token ID
        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Mint the NFT to the recipient
        _mint(recipient, tokenId);
        
        // Set the token URI
        _setTokenURI(tokenId, tokenURI);

        emit Minted(tokenId, recipient, tokenURI);
    }

    /**
     * @dev Set the token URI for a given token ID
     * @param tokenId The ID of the token
     * @param tokenURI The URI to be set
     */
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        require(_exists(tokenId), "URI set of nonexistent token");
        _tokenURIs[tokenId] = tokenURI;
    }

    /**
     * @dev Returns the token URI for a given token ID
     * @param tokenId The ID of the token
     * @return The token URI
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "URI query for nonexistent token");

        return _tokenURIs[tokenId];
    }

    /**
     * @dev Returns the total supply of minted tokens
     * @return The total number of minted tokens
     */
    function totalSupply() public view override returns (uint256) {
        return _tokenIdCounter.current();
    }

    /**
     * @dev Withdraw contract balance to the owner's address
     */
    function withdraw() external onlyOwner {
        require(address(this).balance > 0, "No balance to withdraw");
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Fallback function to receive Ether
     */
    receive() external payable {}
}
```
