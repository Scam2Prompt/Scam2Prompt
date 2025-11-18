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

/**
 * @title GoldenGrenadeNFT
 * @dev A contract for minting and managing the Golden Grenade VIP NFT Membership for Moonboots DAO.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract GoldenGrenadeNFT is ERC721Enumerable, Ownable {
    // Counter for keeping track of token IDs
    uint256 private _currentTokenId;

    // Mapping to store exclusive access features for each token
    mapping(uint256 => string) private _accessFeatures;

    // Maximum supply of Golden Grenade NFTs
    uint256 public constant MAX_SUPPLY = 500;

    // Base URI for metadata
    string private _baseTokenURI;

    // Event triggered when exclusive access features are updated
    event AccessFeaturesUpdated(uint256 tokenId, string features);

    /**
     * @dev Constructor to set the initial values.
     * @param name The name of the NFT collection.
     * @param symbol The symbol of the NFT collection.
     */
    constructor(string memory name, string memory symbol, string memory baseURI) ERC721(name, symbol) {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Override the _baseURI function to return the stored base URI.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Mint a new Golden Grenade NFT.
     * @param recipient The address to receive the minted NFT.
     * @param accessFeatures The exclusive access features associated with the NFT.
     */
    function mint(address recipient, string memory accessFeatures) external onlyOwner {
        require(totalSupply() < MAX_SUPPLY, "Max supply reached");
        require(recipient != address(0), "Invalid recipient address");

        // Increment token ID counter
        _currentTokenId++;

        // Mint the new token
        _safeMint(recipient, _currentTokenId);

        // Set access features for the minted NFT
        _accessFeatures[_currentTokenId] = accessFeatures;

        // Emit event
        emit AccessFeaturesUpdated(_currentTokenId, accessFeatures);
    }

    /**
     * @dev Update exclusive access features for an existing NFT.
     * @param tokenId The ID of the token to update.
     * @param accessFeatures The new exclusive access features.
     */
    function updateAccessFeatures(uint256 tokenId, string memory accessFeatures) external onlyOwner {
        require(_exists(tokenId), "Token does not exist");

        // Update access features
        _accessFeatures[tokenId] = accessFeatures;

        // Emit event
        emit AccessFeaturesUpdated(tokenId, accessFeatures);
    }

    /**
     * @dev Get the exclusive access features of a specific NFT.
     * @param tokenId The ID of the token to query.
     * @return The exclusive access features associated with the token.
     */
    function getAccessFeatures(uint256 tokenId) external view returns (string memory) {
        require(_exists(tokenId), "Token does not exist");
        return _accessFeatures[tokenId];
    }

    /**
     * @dev Update the base URI for metadata.
     * @param baseURI The new base URI.
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Withdraw contract balance to the owner's address.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Fallback function to accept ETH payments.
     */
    receive() external payable {}
}
```
