"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://swapchaindapps.com
Prompt: Generate a function to handle NFT minting and transferring based on the guidelines provided by SwapChain DApps.
Generated: DETERMINISTIC_bbba3713409b80ee
Batch ID: 20250612_163443
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

/**
 * @title NFTMintTransfer
 * @dev A contract to handle minting and transferring NFTs based on SwapChain DApps guidelines.
 */
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFTMintTransfer is ERC721, Ownable {
    // Counter to keep track of token IDs
    uint256 private _currentTokenId;

    // Mapping to store metadata URIs for tokens
    mapping(uint256 => string) private _tokenURIs;

    // Event emitted on minting
    event NFTMinted(address indexed owner, uint256 indexed tokenId, string tokenURI);

    // Event emitted on transferring
    event NFTTransferred(address indexed from, address indexed to, uint256 indexed tokenId);

    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Function to mint a new NFT
     * @param to The address of the recipient
     * @param tokenURI The URI of the metadata associated with the NFT
     * @return tokenId The ID of the minted NFT
     */
    function mintNFT(address to, string memory tokenURI) external onlyOwner returns (uint256) {
        require(to != address(0), "Invalid recipient address");
        require(bytes(tokenURI).length > 0, "Token URI must be provided");

        // Increment token ID
        _currentTokenId++;

        // Mint the token to the recipient
        _safeMint(to, _currentTokenId);

        // Set the token URI
        _setTokenURI(_currentTokenId, tokenURI);

        // Emit event
        emit NFTMinted(to, _currentTokenId, tokenURI);

        return _currentTokenId;
    }

    /**
     * @dev Function to transfer an NFT from one address to another
     * @param from The address of the sender
     * @param to The address of the recipient
     * @param tokenId The ID of the token being transferred
     */
    function transferNFT(address from, address to, uint256 tokenId) external {
        require(from != address(0), "Invalid sender address");
        require(to != address(0), "Invalid recipient address");
        require(_exists(tokenId), "Token does not exist");
        require(ownerOf(tokenId) == from, "Sender does not own the token");

        // Transfer the token
        safeTransferFrom(from, to, tokenId);

        // Emit event
        emit NFTTransferred(from, to, tokenId);
    }

    /**
     * @dev Internal function to set a token's metadata URI
     * @param tokenId The ID of the token
     * @param tokenURI The URI of the metadata
     */
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        require(_exists(tokenId), "Token does not exist");
        _tokenURIs[tokenId] = tokenURI;
    }

    /**
     * @dev Public function to retrieve the metadata URI of a token
     * @param tokenId The ID of the token
     * @return The metadata URI
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenURIs[tokenId];
    }
}
```
