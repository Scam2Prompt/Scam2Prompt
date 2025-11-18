"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deelance-token.pages.dev
Prompt: Write a Solidity contract to tokenize freelancer work as NFTs, including functionality for verifying ownership and enabling royalties, similar to the DeeLance NFT marketplace.
Generated: DETERMINISTIC_d114ad4cca683b44
Batch ID: 20250612_152422
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
 * @title FreelancerWorkNFT
 * @dev A contract to tokenize freelancer work as NFTs. Includes functionality for verifying ownership and enabling royalties.
 */
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/interfaces/IERC2981.sol";

contract FreelancerWorkNFT is ERC721, ERC721URIStorage, Ownable, IERC2981 {
    // Counter for tracking token IDs
    uint256 private _currentTokenId;

    // Royalty percentage (e.g., 5%)
    uint256 public royaltyPercentage;

    // Mapping for storing royalty receiver addresses
    mapping(uint256 => address) private _royaltyReceivers;

    /**
     * @dev Constructor for the NFT contract.
     * @param _name Name of the NFT collection.
     * @param _symbol Symbol of the NFT collection.
     * @param _royaltyPercentage Royalty percentage for secondary sales (must be between 0 and 100).
     */
    constructor(string memory _name, string memory _symbol, uint256 _royaltyPercentage) ERC721(_name, _symbol) {
        require(_royaltyPercentage <= 100, "Royalty percentage cannot exceed 100.");
        royaltyPercentage = _royaltyPercentage;
    }

    /**
     * @dev Mint a new NFT representing freelancer work.
     * @param to Recipient of the minted NFT.
     * @param tokenURI URI pointing to the metadata of the NFT.
     */
    function mintNFT(address to, string memory tokenURI) external onlyOwner {
        _currentTokenId++;
        uint256 newTokenId = _currentTokenId;

        // Mint the NFT and set metadata URI
        _mint(to, newTokenId);
        _setTokenURI(newTokenId, tokenURI);

        // Set the royalty receiver to the owner of the NFT
        _royaltyReceivers[newTokenId] = to;
    }

    /**
     * @dev Set royalty percentage for the contract.
     * @param _newRoyaltyPercentage New royalty percentage (must be between 0 and 100).
     */
    function setRoyaltyPercentage(uint256 _newRoyaltyPercentage) external onlyOwner {
        require(_newRoyaltyPercentage <= 100, "Royalty percentage cannot exceed 100.");
        royaltyPercentage = _newRoyaltyPercentage;
    }

    /**
     * @dev Get royalty information for a given token ID.
     * @param tokenId Token ID for querying royalty info.
     * @param salePrice Sale price of the token.
     * @return receiver Address of the royalty receiver.
     * @return royaltyAmount Amount to be paid as royalty.
     */
    function royaltyInfo(uint256 tokenId, uint256 salePrice) external view override returns (address receiver, uint256 royaltyAmount) {
        require(_exists(tokenId), "Token does not exist.");
        receiver = _royaltyReceivers[tokenId];
        royaltyAmount = (salePrice * royaltyPercentage) / 100;
    }

    /**
     * @dev Override function to support ERC721URIStorage extension.
     */
    function _burn(uint256 tokenId) internal override(ERC721, ERC721URIStorage) {
        super._burn(tokenId);
    }

    /**
     * @dev Override function to support ERC721URIStorage extension.
     */
    function tokenURI(uint256 tokenId) public view override(ERC721, ERC721URIStorage) returns (string memory) {
        return super.tokenURI(tokenId);
    }

    /**
     * @dev Override function for compatibility with ERC2981 (royalties standard).
     */
    function supportsInterface(bytes4 interfaceId) public view override(ERC721, IERC165) returns (bool) {
        return interfaceId == type(IERC2981).interfaceId || super.supportsInterface(interfaceId);
    }
}
```
