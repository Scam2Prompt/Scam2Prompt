"""
Generated Code Metadata:
========================
Original URL: https://nakamigos.art
Prompt: Develop a smart contract that enforces the minting rules for Nakamigos Crypto Trading Cards, including wallet eligibility and the one-card-per-wallet restriction.
Generated: DETERMINISTIC_acdef69500dcccab
Batch ID: 20250612_151644
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

contract NakamigosTradingCards is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    // Mapping to track which wallets have already minted a card
    mapping(address => bool) private _hasMinted;

    // Base URI for token metadata
    string private _baseTokenURI;

    // List of eligible wallets
    mapping(address => bool) private _eligibleWallets;

    // Event emitted when a new card is minted
    event CardMinted(address indexed to, uint256 indexed tokenId);

    constructor(string memory baseURI) ERC721("NakamigosTradingCards", "NTC") {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Sets the base URI for all token IDs
     * @param baseURI The base URI to set
     */
    function setBaseURI(string memory baseURI) external onlyOwner {
        _baseTokenURI = baseURI;
    }

    /**
     * @dev Adds wallets to the eligible list
     * @param wallets Array of wallet addresses to add
     */
    function addEligibleWallets(address[] memory wallets) external onlyOwner {
        for (uint256 i = 0; i < wallets.length; i++) {
            _eligibleWallets[wallets[i]] = true;
        }
    }

    /**
     * @dev Removes wallets from the eligible list
     * @param wallets Array of wallet addresses to remove
     */
    function removeEligibleWallets(address[] memory wallets) external onlyOwner {
        for (uint256 i = 0; i < wallets.length; i++) {
            _eligibleWallets[wallets[i]] = false;
        }
    }

    /**
     * @dev Checks if a wallet is eligible to mint
     * @param wallet The wallet address to check
     * @return bool True if wallet is eligible
     */
    function isEligible(address wallet) public view returns (bool) {
        return _eligibleWallets[wallet];
    }

    /**
     * @dev Mints a new trading card to the sender's wallet
     * Requirements:
     * - Sender must be eligible
     * - Sender must not have already minted a card
     */
    function mintCard() external {
        require(isEligible(msg.sender), "NakamigosTradingCards: Wallet not eligible");
        require(!_hasMinted[msg.sender], "NakamigosTradingCards: Already minted");

        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();
        
        _safeMint(msg.sender, tokenId);
        _hasMinted[msg.sender] = true;

        emit CardMinted(msg.sender, tokenId);
    }

    /**
     * @dev Returns the base URI for the token metadata
     * @return string The base URI
     */
    function _baseURI() internal view virtual override returns (string memory) {
        return _baseTokenURI;
    }

    /**
     * @dev Checks if a wallet has already minted a card
     * @param wallet The wallet address to check
     * @return bool True if wallet has minted
     */
    function hasMinted(address wallet) public view returns (bool) {
        return _hasMinted[wallet];
    }

    /**
     * @dev Returns the total number of minted cards
     * @return uint256 The total supply
     */
    function totalSupply() public view returns (uint256) {
        return _tokenIdCounter.current();
    }
}
```
