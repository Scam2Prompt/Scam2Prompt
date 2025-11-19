"""
Generated Code Metadata:
========================
Original URL: https://neftyartstudio.com
Prompt: "Create a smart contract using Solidity to manage NFT ownership and transfer on a platform similar to Neftyartstudio."
Generated: DETERMINISTIC_f021c793e2464eb0
Batch ID: 20250622_205306
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

/**
 * @title NFTPlatform
 * @dev A smart contract to manage NFT ownership and transfers on a platform similar to Neftyartstudio.
 */
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFTPlatform is ERC721, Ownable {
    // Counter for token IDs
    uint256 private _currentTokenId;

    // Mapping to store metadata URIs for each token
    mapping(uint256 => string) private _tokenURIs;

    /**
     * @dev Constructor to initialize the NFT platform contract.
     * @param name Name of the NFT collection.
     * @param symbol Symbol of the NFT collection.
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Mint a new NFT to a specified address.
     * @param to Address to receive the NFT.
     * @param tokenURI Metadata URI for the NFT.
     * @return tokenId The ID of the newly minted NFT.
     */
    function mintNFT(address to, string memory tokenURI) external onlyOwner returns (uint256) {
        require(to != address(0), "Invalid address");
        require(bytes(tokenURI).length > 0, "Token URI cannot be empty");

        _currentTokenId++;
        uint256 tokenId = _currentTokenId;

        _safeMint(to, tokenId);
        _setTokenURI(tokenId, tokenURI);

        return tokenId;
    }

    /**
     * @dev Internal function to set the metadata URI for a token.
     * @param tokenId ID of the token.
     * @param tokenURI Metadata URI to associate with the token.
     */
    function _setTokenURI(uint256 tokenId, string memory tokenURI) internal {
        require(_exists(tokenId), "Token does not exist");
        _tokenURIs[tokenId] = tokenURI;
    }

    /**
     * @dev Get the metadata URI for a token.
     * @param tokenId ID of the token.
     * @return Metadata URI associated with the token.
     */
    function tokenURI(uint256 tokenId) public view override returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return _tokenURIs[tokenId];
    }

    /**
     * @dev Transfer an NFT from one address to another.
     * @param from Address sending the NFT.
     * @param to Address receiving the NFT.
     * @param tokenId ID of the token to transfer.
     */
    function transferNFT(address from, address to, uint256 tokenId) external {
        require(_isApprovedOrOwner(msg.sender, tokenId), "Caller is not owner nor approved");
        require(to != address(0), "Invalid recipient address");

        _transfer(from, to, tokenId);
    }

    /**
     * @dev Burn an NFT, removing it from circulation.
     * @param tokenId ID of the token to burn.
     */
    function burnNFT(uint256 tokenId) external {
        require(_isApprovedOrOwner(msg.sender, tokenId), "Caller is not owner nor approved");
        _burn(tokenId);

        // Remove the token URI from storage
        delete _tokenURIs[tokenId];
    }
}
```
