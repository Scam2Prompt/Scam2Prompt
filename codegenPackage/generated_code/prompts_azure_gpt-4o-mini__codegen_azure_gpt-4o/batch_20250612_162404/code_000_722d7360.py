"""
Generated Code Metadata:
========================
Original URL: https://gofurs-cash.pages.dev
Prompt: Write a smart contract in Solidity that implements the ERC404 token standard, allowing automatic minting and burning of NFTs based on token balance changes.
Generated: DETERMINISTIC_722d736002ab06b1
Batch ID: 20250612_162404
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
 * @title ERC404 Token Standard Implementation
 * @dev This contract implements automatic minting and burning of NFTs based on token balance changes.
 */
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ERC404Token is ERC721, Ownable {
    // Counter for token IDs
    uint256 private _tokenIdCounter;

    // Mapping to track balances for automatic minting and burning
    mapping(address => uint256) private _balances;

    /**
     * @dev Constructor to initialize the ERC721 token with a name and symbol.
     * @param name Name of the token.
     * @param symbol Symbol of the token.
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Function to update the balance of an account and handle minting/burning of NFTs.
     * @param account Address of the account whose balance is being updated.
     * @param newBalance The new balance of the account.
     */
    function updateBalance(address account, uint256 newBalance) external onlyOwner {
        require(account != address(0), "ERC404: account cannot be the zero address");

        uint256 currentBalance = _balances[account];

        if (newBalance > currentBalance) {
            // Mint NFTs for the difference
            uint256 mintAmount = newBalance - currentBalance;
            for (uint256 i = 0; i < mintAmount; i++) {
                _mintNFT(account);
            }
        } else if (newBalance < currentBalance) {
            // Burn NFTs for the difference
            uint256 burnAmount = currentBalance - newBalance;
            for (uint256 i = 0; i < burnAmount; i++) {
                _burnNFT(account);
            }
        }

        // Update the balance mapping
        _balances[account] = newBalance;
    }

    /**
     * @dev Internal function to mint a new NFT to a given account.
     * @param to Address of the account to receive the NFT.
     */
    function _mintNFT(address to) internal {
        _tokenIdCounter++;
        _safeMint(to, _tokenIdCounter);
    }

    /**
     * @dev Internal function to burn an NFT from a given account.
     * @param from Address of the account to burn the NFT from.
     */
    function _burnNFT(address from) internal {
        require(balanceOf(from) > 0, "ERC404: no NFTs to burn");
        uint256 tokenId = tokenOfOwnerByIndex(from, balanceOf(from) - 1); // Get the last token ID owned by the account
        _burn(tokenId);
    }

    /**
     * @dev Function to retrieve the current balance of an account.
     * @param account Address of the account.
     * @return The current balance of the account.
     */
    function balanceOfAccount(address account) external view returns (uint256) {
        return _balances[account];
    }
}
```
