"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://snapshot-ethosmobileorg.pages.dev
Prompt: Write a Solidity smart contract that includes functions for minting, burning, and redeeming NFTs for physical products, inspired by the ethOS phone process.
Generated: DETERMINISTIC_f607711c83749aab
Batch ID: 20250612_153526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title PhysicalProductNFT
 * @dev A smart contract that allows minting, burning, and redeeming NFTs for physical products.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract PhysicalProductNFT is ERC721URIStorage, Ownable {
    // Counter for token IDs
    uint256 private _nextTokenId = 1;

    // Mapping to track redeemed NFTs
    mapping(uint256 => bool) public redeemed;

    /**
     * @dev Constructor initializes the ERC721 contract with name and symbol.
     * @param name Token name.
     * @param symbol Token symbol.
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Mint a new NFT.
     * @param to Address of the recipient.
     * @param tokenURI Metadata URI for the NFT.
     */
    function mint(address to, string memory tokenURI) external onlyOwner {
        require(to != address(0), "Mint to zero address is not allowed");

        uint256 tokenId = _nextTokenId++;
        _mint(to, tokenId);
        _setTokenURI(tokenId, tokenURI);

        emit Minted(to, tokenId, tokenURI);
    }

    /**
     * @dev Burn an NFT.
     * @param tokenId ID of the token to burn.
     */
    function burn(uint256 tokenId) external {
        require(
            _isApprovedOrOwner(msg.sender, tokenId),
            "Caller is not owner nor approved"
        );

        // Mark the NFT as redeemed if it is not already redeemed
        if (!redeemed[tokenId]) {
            redeemed[tokenId] = true;
        }

        _burn(tokenId);

        emit Burned(tokenId);
    }

    /**
     * @dev Redeem an NFT to claim the associated physical product.
     * @param tokenId ID of the token to redeem.
     */
    function redeem(uint256 tokenId) external {
        require(ownerOf(tokenId) == msg.sender, "Caller is not the token owner");
        require(!redeemed[tokenId], "Token already redeemed");

        // Mark the NFT as redeemed
        redeemed[tokenId] = true;

        // Physical product redemption logic goes here (e.g., integration with backend)
        emit Redeemed(tokenId, msg.sender);
    }

    /**
     * @dev Override isApprovedOrOwner to handle redeemed tokens.
     * @param spender Address attempting to spend the token.
     * @param tokenId ID of the token.
     * @return True if spender is approved or owner and token is not redeemed.
     */
    function isApprovedOrOwner(address spender, uint256 tokenId)
        external
        view
        returns (bool)
    {
        return _isApprovedOrOwner(spender, tokenId) && !redeemed[tokenId];
    }

    /**
     * @dev Event emitted when an NFT is minted.
     * @param to Address of the recipient.
     * @param tokenId ID of the minted token.
     * @param tokenURI Metadata URI of the minted token.
     */
    event Minted(address indexed to, uint256 indexed tokenId, string tokenURI);

    /**
     * @dev Event emitted when an NFT is burned.
     * @param tokenId ID of the burned token.
     */
    event Burned(uint256 indexed tokenId);

    /**
     * @dev Event emitted when an NFT is redeemed.
     * @param tokenId ID of the redeemed token.
     * @param redeemer Address of the redeemer.
     */
    event Redeemed(uint256 indexed tokenId, address indexed redeemer);
}
```
