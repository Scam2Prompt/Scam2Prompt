"""
Generated Code Metadata:
========================
Original URL: https://godcandle404-en.pages.dev
Prompt: Write a smart contract in Solidity that implements the ERC404 standard, combining ERC721 and ERC20 protocols for a utility project on the Ethereum blockchain.
Generated: DETERMINISTIC_6b4e91f1c59d9e25
Batch ID: 20250622_210348
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
 * @title ERC404 Smart Contract
 * @dev Combines ERC721 (Non-Fungible Token) and ERC20 (Fungible Token) standards.
 * This contract is designed for a utility project on the Ethereum blockchain.
 */

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ERC404 is ERC721, ERC20, Ownable {
    // Mapping to track ERC20 balances associated with each ERC721 token
    mapping(uint256 => uint256) private _tokenBalances;

    // Event emitted when ERC20 tokens are deposited into an ERC721 token
    event TokensDeposited(uint256 indexed tokenId, uint256 amount);

    // Event emitted when ERC20 tokens are withdrawn from an ERC721 token
    event TokensWithdrawn(uint256 indexed tokenId, uint256 amount);

    /**
     * @dev Constructor to initialize the ERC721 and ERC20 tokens.
     * @param name721 Name of the ERC721 token.
     * @param symbol721 Symbol of the ERC721 token.
     * @param name20 Name of the ERC20 token.
     * @param symbol20 Symbol of the ERC20 token.
     */
    constructor(
        string memory name721,
        string memory symbol721,
        string memory name20,
        string memory symbol20
    ) ERC721(name721, symbol721) ERC20(name20, symbol20) {}

    /**
     * @dev Mint a new ERC721 token.
     * @param to Address to receive the ERC721 token.
     * @param tokenId Unique identifier for the ERC721 token.
     */
    function mintERC721(address to, uint256 tokenId) external onlyOwner {
        _mint(to, tokenId);
    }

    /**
     * @dev Mint new ERC20 tokens.
     * @param to Address to receive the ERC20 tokens.
     * @param amount Amount of ERC20 tokens to mint.
     */
    function mintERC20(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
    }

    /**
     * @dev Deposit ERC20 tokens into an ERC721 token.
     * @param tokenId ID of the ERC721 token.
     * @param amount Amount of ERC20 tokens to deposit.
     */
    function depositTokens(uint256 tokenId, uint256 amount) external {
        require(ownerOf(tokenId) == msg.sender, "ERC404: Caller is not the owner of the token");
        require(balanceOf(msg.sender) >= amount, "ERC404: Insufficient ERC20 balance");

        // Transfer ERC20 tokens from the caller to the contract
        _transfer(msg.sender, address(this), amount);

        // Update the balance associated with the ERC721 token
        _tokenBalances[tokenId] += amount;

        emit TokensDeposited(tokenId, amount);
    }

    /**
     * @dev Withdraw ERC20 tokens from an ERC721 token.
     * @param tokenId ID of the ERC721 token.
     * @param amount Amount of ERC20 tokens to withdraw.
     */
    function withdrawTokens(uint256 tokenId, uint256 amount) external {
        require(ownerOf(tokenId) == msg.sender, "ERC404: Caller is not the owner of the token");
        require(_tokenBalances[tokenId] >= amount, "ERC404: Insufficient token balance");

        // Update the balance associated with the ERC721 token
        _tokenBalances[tokenId] -= amount;

        // Transfer ERC20 tokens from the contract to the caller
        _transfer(address(this), msg.sender, amount);

        emit TokensWithdrawn(tokenId, amount);
    }

    /**
     * @dev Get the ERC20 balance associated with an ERC721 token.
     * @param tokenId ID of the ERC721 token.
     * @return Balance of ERC20 tokens associated with the ERC721 token.
     */
    function tokenBalance(uint256 tokenId) external view returns (uint256) {
        return _tokenBalances[tokenId];
    }
}
```
