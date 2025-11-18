"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://godcandle404-en.web.app
Prompt: Write a Solidity contract that integrates both ERC-721 and ERC-404 standards, ensuring compatibility with the God Candle ecosystem's innovative features like trading tools and WL airdrops.
Generated: DETERMINISTIC_f445f8b20624a015
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.9;

// Importing OpenZeppelin's ERC721 implementation
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// God Candle NFT Contract integrating ERC-721 and ERC-404 standards.
contract GodCandleNFT is ERC721Enumerable, Ownable {
    // Metadata base URI
    string private _baseTokenURI;

    // Mapping to store whitelist status for WL airdrops
    mapping(address => bool) private _whitelist;

    // ERC-404 trading tools integration mapping
    mapping(uint256 => bool) private _tradeLocked;

    // Event emitted when an address is added/removed from the whitelist
    event WhitelistUpdated(address indexed user, bool status);

    // Event emitted when a token is trade-locked/unlocked
    event TradeLockUpdated(uint256 indexed tokenId, bool locked);

    // Constructor to initialize the NFT contract
    constructor(string memory name, string memory symbol, string memory baseTokenURI) ERC721(name, symbol) {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Override function to set the base URI for token metadata.
     * @return The base URI string.
     */
    function _baseURI() internal view override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Set the base URI for token metadata. Only owner can call this function.
     * @param baseTokenURI New base URI for token metadata.
     */
    function setBaseURI(string memory baseTokenURI) external onlyOwner {
        _baseTokenURI = baseTokenURI;
    }

    /**
     * @dev Mint a new token to a specific address.
     * @param to Address receiving the newly minted token.
     * @param tokenId Unique ID for the token to be minted.
     */
    function mint(address to, uint256 tokenId) external onlyOwner {
        require(!_exists(tokenId), "Token already exists");
        _mint(to, tokenId);
    }

    /**
     * @dev Add an address to the whitelist for WL airdrops.
     * @param user Address to be added to the whitelist.
     */
    function addToWhitelist(address user) external onlyOwner {
        _whitelist[user] = true;
        emit WhitelistUpdated(user, true);
    }

    /**
     * @dev Remove an address from the whitelist for WL airdrops.
     * @param user Address to be removed from the whitelist.
     */
    function removeFromWhitelist(address user) external onlyOwner {
        _whitelist[user] = false;
        emit WhitelistUpdated(user, false);
    }

    /**
     * @dev Check if an address is whitelisted.
     * @param user Address to check.
     * @return True if the address is whitelisted, false otherwise.
     */
    function isWhitelisted(address user) external view returns (bool) {
        return _whitelist[user];
    }

    /**
     * @dev Enable or disable trade lock for a specific token. Only owner can call this function.
     * @param tokenId ID of the token to lock/unlock.
     * @param locked Set true to lock, false to unlock.
     */
    function setTradeLock(uint256 tokenId, bool locked) external onlyOwner {
        require(_exists(tokenId), "Token does not exist");
        _tradeLocked[tokenId] = locked;
        emit TradeLockUpdated(tokenId, locked);
    }

    /**
     * @dev Check if a token is trade-locked.
     * @param tokenId ID of the token to check.
     * @return True if the token is locked, false otherwise.
     */
    function isTradeLocked(uint256 tokenId) external view returns (bool) {
        require(_exists(tokenId), "Token does not exist");
        return _tradeLocked[tokenId];
    }

    /**
     * @dev Override transfer functions to enforce trade lock.
     * @param from Sender address.
     * @param to Receiver address.
     * @param tokenId ID of the token being transferred.
     */
    function _beforeTokenTransfer(address from, address to, uint256 tokenId) internal override {
        super._beforeTokenTransfer(from, to, tokenId);
        require(!_tradeLocked[tokenId], "Token transfer is locked");
    }
}
```
