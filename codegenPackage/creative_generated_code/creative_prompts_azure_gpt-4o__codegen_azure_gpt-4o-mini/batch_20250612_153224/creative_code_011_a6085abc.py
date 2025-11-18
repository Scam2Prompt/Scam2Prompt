"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://venoms-1zv.pages.dev
Prompt: Create a deployment script for a VEP-1155 tokenized asset collection, ensuring compliance with Venom's mainnet standards and hackathon requirements.
Generated: DETERMINISTIC_a6085abc4860d1a0
Batch ID: 20250612_153224
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC1155/ERC1155.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title VEP-1155 Tokenized Asset Collection
 * @dev This contract implements an ERC1155 token for VEP-1155 compliant asset collections.
 */
contract VEP1155TokenCollection is ERC1155, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Mapping from token ID to token metadata URI
    mapping(uint256 => string) private _tokenURIs;

    // Event emitted when a new token is minted
    event TokenMinted(uint256 indexed tokenId, address indexed owner, uint256 amount);

    /**
     * @dev Constructor to set the initial URI.
     * @param uri The URI for metadata.
     */
    constructor(string memory uri) ERC1155(uri) {
        // Initializing the contract with the base URI
    }

    /**
     * @dev Mint new tokens.
     * @param amount The quantity of tokens to mint.
     * @param metadataURI The URI for the token's metadata.
     */
    function mint(uint256 amount, string memory metadataURI) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        
        // Incrementing the token ID counter and getting the new tokenId
        uint256 newTokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();

        // Minting the tokens
        _mint(msg.sender, newTokenId, amount, "");

        // Setting the token URI
        _setTokenURI(newTokenId, metadataURI);

        // Emitting the TokenMinted event
        emit TokenMinted(newTokenId, msg.sender, amount);
    }

    /**
     * @dev Internal function to set the token URI.
     * @param tokenId The ID of the token.
     * @param uri The URI for the token's metadata.
     */
    function _setTokenURI(uint256 tokenId, string memory uri) internal {
        require(bytes(uri).length > 0, "URI must not be empty");
        _tokenURIs[tokenId] = uri;
    }

    /**
     * @dev Returns the URI for a specific token ID.
     * @param tokenId The ID of the token.
     * @return The URI string.
     */
    function uri(uint256 tokenId) public view override returns (string memory) {
        return _tokenURIs[tokenId];
    }

    /**
     * @dev Allows the owner to update the base URI for all tokens.
     * @param newUri The new base URI for tokens.
     */
    function setBaseURI(string memory newUri) external onlyOwner {
        _setURI(newUri);
    }

    /**
     * @dev Function to withdraw Ether from the contract (if applicable).
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");

        // Transfer the balance to the owner
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Fallback function to receive Ether.
     */
    receive() external payable {}

    /**
     * @dev Function to get the total number of minted tokens.
     * @return The total count of minted token IDs.
     */
    function totalSupply() external view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
