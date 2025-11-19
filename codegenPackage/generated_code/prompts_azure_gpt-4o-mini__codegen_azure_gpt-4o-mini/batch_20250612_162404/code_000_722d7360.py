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

// Importing the ERC721 interface for NFT functionality
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// ERC404 Token Standard Implementation
contract ERC404Token is ERC721, Ownable {
    // Mapping from token ID to owner address
    mapping(uint256 => address) private _owners;

    // Mapping from owner address to token count
    mapping(address => uint256) private _balances;

    // Event emitted when an NFT is minted
    event Minted(address indexed to, uint256 indexed tokenId);

    // Event emitted when an NFT is burned
    event Burned(address indexed owner, uint256 indexed tokenId);

    // Counter for token IDs
    uint256 private _tokenIdCounter;

    // Constructor to initialize the token with a name and symbol
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {
        _tokenIdCounter = 1; // Start token IDs from 1
    }

    // Function to mint a new NFT
    function mint(address to) external onlyOwner {
        require(to != address(0), "Cannot mint to the zero address");

        uint256 tokenId = _tokenIdCounter;
        _mint(to, tokenId);
        _tokenIdCounter++;

        emit Minted(to, tokenId);
    }

    // Function to burn an NFT
    function burn(uint256 tokenId) external {
        address owner = ownerOf(tokenId);
        require(msg.sender == owner, "Caller is not the owner");

        _burn(tokenId);
        emit Burned(owner, tokenId);
    }

    // Function to automatically mint NFTs based on balance changes
    function updateBalanceAndMint(address account, uint256 newBalance) external onlyOwner {
        require(account != address(0), "Cannot update balance for the zero address");

        uint256 currentBalance = _balances[account];

        // If the new balance is greater than the current balance, mint NFTs
        if (newBalance > currentBalance) {
            for (uint256 i = currentBalance; i < newBalance; i++) {
                mint(account);
            }
        } 
        // If the new balance is less than the current balance, burn NFTs
        else if (newBalance < currentBalance) {
            for (uint256 i = newBalance; i < currentBalance; i++) {
                burn(tokenIdForIndex(account, i));
            }
        }

        // Update the balance
        _balances[account] = newBalance;
    }

    // Helper function to get the token ID for a specific index
    function tokenIdForIndex(address owner, uint256 index) internal view returns (uint256) {
        require(index < _balances[owner], "Index out of bounds");
        return index + 1; // Assuming token IDs are sequentially assigned
    }

    // Override the _beforeTokenTransfer hook to update balances
    function _beforeTokenTransfer(address from, address to, uint256 tokenId) internal override {
        super._beforeTokenTransfer(from, to, tokenId);

        if (from != address(0)) {
            _balances[from]--;
        }
        if (to != address(0)) {
            _balances[to]++;
        }
    }
}
```
