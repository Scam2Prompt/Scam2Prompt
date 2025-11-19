"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gofurs-cash.pages.dev
Prompt: Write a smart contract in Solidity that implements the ERC404 token standard, allowing automatic minting and burning of NFTs based on token balance changes.
Generated: DETERMINISTIC_722d736002ab06b1
Batch ID: 20250612_162404
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
 * @title ERC404Token
 * @dev Implements the ERC404 token standard, allowing automatic minting and burning of NFTs 
 * based on token balance changes.
 */
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ERC404Token is ERC721Enumerable, Ownable {
    // Counter for token IDs
    uint256 private _currentTokenId;

    // Mapping to track balances for mint/burn logic
    mapping(address => uint256) private _trackedBalances;

    /**
     * @dev Constructor to initialize the contract.
     * @param name Name of the token.
     * @param symbol Symbol of the token.
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Function to update the tracked balance and adjust NFTs accordingly.
     * @param account Address of the account whose balance has changed.
     * @param newBalance Updated balance of the account.
     */
    function updateBalance(address account, uint256 newBalance) external onlyOwner {
        require(account != address(0), "ERC404Token: account cannot be the zero address");

        uint256 oldBalance = _trackedBalances[account];
        _trackedBalances[account] = newBalance;

        if (newBalance > oldBalance) {
            // Mint NFTs for the difference in balance
            for (uint256 i = oldBalance; i < newBalance; i++) {
                _mintNFT(account);
            }
        } else if (newBalance < oldBalance) {
            // Burn NFTs for the difference in balance
            for (uint256 i = newBalance; i < oldBalance; i++) {
                _burnNFT(account);
            }
        }
    }

    /**
     * @dev Internal function to mint a new NFT to the specified account.
     * @param to Address to receive the minted NFT.
     */
    function _mintNFT(address to) internal {
        _currentTokenId++;
        _safeMint(to, _currentTokenId);
    }

    /**
     * @dev Internal function to burn an NFT from the specified account.
     * @param from Address from which the NFT will be burned.
     */
    function _burnNFT(address from) internal {
        require(balanceOf(from) > 0, "ERC404Token: no NFTs to burn");

        // Burn the last token owned by the account
        uint256 tokenIdToBurn = tokenOfOwnerByIndex(from, balanceOf(from) - 1);
        _burn(tokenIdToBurn);
    }

    /**
     * @dev Override supportsInterface to include ERC721Enumerable interface.
     * @param interfaceId Interface ID to check.
     * @return bool Whether the interface is supported.
     */
    function supportsInterface(bytes4 interfaceId) public view virtual override(ERC721Enumerable) returns (bool) {
        return super.supportsInterface(interfaceId);
    }
}
```
