"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://teacoindappclaim.pages.dev
Prompt: Develop a code example for a DApp that addresses issues related to NFTs minting and transfer, as specified on the Teacoind DApp Claim website.
Generated: DETERMINISTIC_9c103404e1d7cb95
Batch ID: 20250612_160254
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
 * @title NFTDApp
 * @dev A decentralized application for minting and transferring NFTs.
 *      This contract ensures secure minting, ownership management, and transfer of NFTs.
 */
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract NFTDApp is ERC721, Ownable {
    // Counter to keep track of the next tokenId to be minted
    uint256 private _currentTokenId;

    // Mapping to track if an address has claimed an NFT
    mapping(address => bool) private _claimed;

    // Event for minting an NFT
    event NFTMinted(address indexed recipient, uint256 tokenId);

    // Event for transferring an NFT
    event NFTTransferred(address indexed from, address indexed to, uint256 tokenId);

    /**
     * @dev Constructor initializes the ERC721 contract with a name and symbol.
     */
    constructor() ERC721("TeacoindNFT", "TCOIN") {}

    /**
     * @dev Mint a new NFT to the caller's address.
     *      Ensures that each address can claim only one NFT.
     */
    function claimNFT() external {
        require(!_claimed[msg.sender], "You have already claimed your NFT.");
        
        _currentTokenId++;
        _claimed[msg.sender] = true;

        // Mint a new NFT to the caller
        _safeMint(msg.sender, _currentTokenId);
        emit NFTMinted(msg.sender, _currentTokenId);
    }

    /**
     * @dev Transfer an NFT from one address to another.
     *      Only callable by the owner of the NFT.
     * @param to Address to which the NFT will be transferred.
     * @param tokenId ID of the NFT to transfer.
     */
    function transferNFT(address to, uint256 tokenId) external {
        require(ownerOf(tokenId) == msg.sender, "You are not the owner of this NFT.");
        require(to != address(0), "Cannot transfer to the zero address.");

        // Transfers the NFT
        _transfer(msg.sender, to, tokenId);
        emit NFTTransferred(msg.sender, to, tokenId);
    }

    /**
     * @dev Checks if an address has already claimed an NFT.
     * @param account Address to check for claim status.
     * @return bool True if the address has claimed an NFT, false otherwise.
     */
    function hasClaimed(address account) external view returns (bool) {
        return _claimed[account];
    }

    /**
     * @dev Retrieves the current token ID counter.
     * @return uint256 The current token ID.
     */
    function getCurrentTokenId() external view returns (uint256) {
        return _currentTokenId;
    }
}
```
