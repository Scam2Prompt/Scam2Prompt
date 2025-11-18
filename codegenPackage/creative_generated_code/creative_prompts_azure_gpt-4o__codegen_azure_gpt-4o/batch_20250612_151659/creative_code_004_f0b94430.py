"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://embersft.costhentic.com
Prompt: Write a function in Solidity to limit the number of Ember NFTs a user can mint during the Fire Sale (1 per user) and Public Sale (2 per transaction).
Generated: DETERMINISTIC_f0b9443064092001
Batch ID: 20250612_151659
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
 * @title EmberNFT
 * @dev A contract for limiting NFT minting during Fire Sale and Public Sale.
 */
contract EmberNFT {
    // State variables
    address public owner; // Contract owner
    uint256 public fireSaleMax = 1; // Max NFTs per user in Fire Sale
    uint256 public publicSaleMax = 2; // Max NFTs per transaction in Public Sale
    enum SaleState { None, FireSale, PublicSale }
    SaleState public currentSaleState;

    mapping(address => uint256) private fireSaleMints; // Tracks Fire Sale mints per user

    // Events
    event Mint(address indexed user, uint256 quantity);

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor to set the contract owner
    constructor() {
        owner = msg.sender;
    }

    // Function to update the sale state (Owner only)
    function setSaleState(SaleState state) external onlyOwner {
        currentSaleState = state;
    }

    /**
     * @dev Mint NFTs during the active sale phase
     * @param quantity Number of NFTs to mint
     */
    function mint(uint256 quantity) external {
        require(currentSaleState != SaleState.None, "No active sale");

        if (currentSaleState == SaleState.FireSale) {
            // Fire Sale: Limit minting to 1 NFT per user
            require(quantity == 1, "Only 1 NFT can be minted during Fire Sale");
            require(fireSaleMints[msg.sender] == 0, "User has already minted during Fire Sale");

            // Record Fire Sale mint for the user
            fireSaleMints[msg.sender] = 1;
        } else if (currentSaleState == SaleState.PublicSale) {
            // Public Sale: Limit minting to 2 NFTs per transaction
            require(quantity > 0 && quantity <= publicSaleMax, "Invalid quantity for Public Sale");
        }

        // Logic for minting NFTs goes here
        // Example: _mint(msg.sender, quantity);

        emit Mint(msg.sender, quantity);
    }
}
```
