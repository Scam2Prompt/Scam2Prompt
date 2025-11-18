"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hikeshi-nft-olive.vercel.app
Prompt: Write a smart contract in Solidity for minting NFTs that incorporates the Hikeshi project's mission of connecting past, present, and future.
Generated: DETERMINISTIC_6a1b2a2db65ffb16
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
pragma solidity ^0.8.17;

/**
 * @title HikeshiNFT
 * @dev A smart contract for minting NFTs that embodies the mission of the Hikeshi project:
 *      connecting the past, present, and future through blockchain technology.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract HikeshiNFT is ERC721Enumerable, Ownable {
    // Base URI for metadata
    string private _baseTokenURI;

    // Max supply of NFTs (to preserve scarcity and legacy)
    uint256 public constant MAX_SUPPLY = 10000;

    // Mint price per NFT (adjusted to reflect the mission's value)
    uint256 public constant MINT_PRICE = 0.05 ether;

    // Mapping to track original mint timestamps (connecting past, present, future)
    mapping(uint256 => uint256) public mintTimestamps;

    // Event emitted when a new NFT is minted
    event NFTMinted(address indexed to, uint256 indexed tokenId, uint256 timestamp);

    /**
     * @dev Constructor to initialize the contract with a name and symbol.
     * @param name Name of the NFT collection.
     * @param symbol Symbol of the NFT collection.
     * @param baseTokenURI Base URI for NFT metadata.
     */
    constructor(string memory name, string memory symbol, string memory baseTokenURI) ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Mint a new NFT.
     * @param to Address to mint the NFT to.
     * Requirements:
     * - The total supply must not exceed MAX_SUPPLY.
     * - The caller must send enough Ether to cover the mint price.
     */
    function mint(address to) external payable {
        require(totalSupply() < MAX_SUPPLY, "HikeshiNFT: Max supply reached");
        require(msg.value >= MINT_PRICE, "HikeshiNFT: Insufficient funds to mint");

        // Generate the new token ID based on the current supply
        uint256 tokenId = totalSupply() + 1;

        // Mint the token
        _safeMint(to, tokenId);

        // Record the mint timestamp
        mintTimestamps[tokenId] = block.timestamp;

        emit NFTMinted(to, tokenId, block.timestamp);
    }

    /**
     * @dev Set the base URI for metadata.
     * @param baseTokenURI New base URI for metadata.
     * Only callable by the contract owner.
     */
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Override the base URI getter from ERC721.
     * @return Base URI string.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Withdraw the contract balance to the owner's address.
     * Only callable by the contract owner.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "HikeshiNFT: No balance to withdraw");
        payable(owner()).transfer(balance);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    receive() external payable {
        revert("HikeshiNFT: Direct payments not supported");
    }
}
```
