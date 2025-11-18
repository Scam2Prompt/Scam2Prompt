"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://abc-abracadabra.web.app
Prompt: Explain how to implement a "0% royalties" policy in an NFT smart contract, referencing the ABC - Abracadabra project as an example.
Generated: DETERMINISTIC_98cea4028e7fbebd
Batch ID: 20250612_151415
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

// Importing OpenZeppelin's ERC721 implementation for NFTs
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title ABCNFT
 * @dev Implementation of a non-fungible token (NFT) with a 0% royalties policy.
 */
contract ABCNFT is ERC721Enumerable, Ownable {
    // Mapping from token ID to the token's metadata
    mapping(uint256 => string) private _tokenURIs;
    
    // Counter for token IDs
    uint256 private _tokenIdCounter;

    // Event emitted when a new NFT is minted
    event Minted(address indexed to, uint256 indexed tokenId, string tokenURI);

    /**
     * @dev Constructor that sets the name and symbol of the NFT collection.
     */
    constructor() ERC721("ABCNFT", "ABCNFT") {}

    /**
     * @dev Mint a new NFT to the specified address with the given tokenURI.
     * @param to The address receiving the minted NFT.
     * @param tokenURI The URI for the NFT metadata.
     */
    function mint(address to, string memory tokenURI) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");
        require(bytes(tokenURI).length > 0, "Token URI cannot be empty");

        // Increment token ID counter and assign to new token
        uint256 tokenId = _tokenIdCounter++;
        _mint(to, tokenId);
        _setTokenURI(tokenId, tokenURI);

        emit Minted(to, tokenId, tokenURI);
    }

    /**
     * @dev Set the token URI for a given token ID.
     * @param tokenId The ID of the token.
     * @param tokenURI The URI for the token metadata.
     */
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        require(_exists(tokenId), "Token does not exist");
        _tokenURIs[tokenId] = tokenURI;
    }

    /**
     * @dev Retrieve the metadata URI for a given token ID.
     * @param tokenId The ID of the token.
     * @return The token URI.
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenURIs[tokenId];
    }

    /**
     * @dev Override the default function to ensure no royalties are sent.
     * This function is intentionally left empty to enforce a 0% royalties policy.
     */
    function royaltyInfo(uint256, uint256) external pure returns (address, uint256) {
        return (address(0), 0);
    }
}
```
