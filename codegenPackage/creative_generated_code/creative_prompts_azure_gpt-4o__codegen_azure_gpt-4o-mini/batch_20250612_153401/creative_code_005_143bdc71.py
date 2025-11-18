"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://publicsale-mocaverse.pages.dev
Prompt: Develop a smart contract in Solidity for managing token allocation during the $MOCA public sale, ensuring compliance with the total supply and community allocation limits.
Generated: DETERMINISTIC_143bdc71273257ea
Batch ID: 20250612_153401
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

/// @title $MOCA Token Sale Smart Contract
/// @author Your Name
/// @notice This contract manages the public sale of the $MOCA token
/// @dev This contract ensures compliance with total supply and community allocation limits

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MOCA is ERC20, Ownable {
    // Total supply of tokens
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 ether; // 1 billion tokens, assuming 18 decimals
    // Community allocation limit
    uint256 public constant COMMUNITY_ALLOCATION_LIMIT = 200_000_000 ether; // 200 million tokens
    // Amount of tokens allocated for sale
    uint256 public tokensForSale;

    // Address to collect the funds from the sale
    address payable public treasury;

    // Event emitted when tokens are purchased
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Mapping to track the balance of tokens sold
    mapping(address => uint256) public balances;

    /// @dev Constructor function initializes the token and treasury address
    /// @param _treasury Address to receive funds from the sale
    constructor(address payable _treasury) ERC20("MOCA Token", "MOCA") {
        require(_treasury != address(0), "Treasury address cannot be zero");
        treasury = _treasury;
        _mint(address(this), TOTAL_SUPPLY); // Mint total supply to contract itself
        tokensForSale = COMMUNITY_ALLOCATION_LIMIT; // Set tokens available for sale
    }

    /// @dev Purchase tokens during the public sale
    /// @param amount The amount of tokens to purchase
    function purchaseTokens(uint256 amount) external payable {
        require(amount > 0, "Amount must be greater than zero");
        require(msg.value > 0, "Ether value must be greater than zero");
        require(amount <= tokensForSale, "Not enough tokens available for sale");

        uint256 requiredEther = amount / 1000; // Assuming 1 token = 0.001 Ether
        require(msg.value >= requiredEther, "Insufficient Ether sent");

        // Update balances
        balances[msg.sender] += amount;
        tokensForSale -= amount;

        // Transfer the tokens from the contract to the buyer
        _transfer(address(this), msg.sender, amount);

        // Forward the funds to the treasury
        treasury.transfer(msg.value);

        emit TokensPurchased(msg.sender, amount);
    }

    /// @dev Owner function to withdraw unsold tokens after the sale
    function withdrawUnsoldTokens() external onlyOwner {
        uint256 unsoldTokens = balanceOf(address(this));
        require(unsoldTokens > 0, "No unsold tokens available");

        // Transfer unsold tokens back to owner
        _transfer(address(this), owner(), unsoldTokens);
    }

    /// @dev Override the _beforeTokenTransfer function to restrict transfers
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal override {
        super._beforeTokenTransfer(from, to, amount);
        require(from == address(0) || to == address(0) || balances[from] >= amount, "Insufficient balance for transfer");
    }

    /// @dev Fallback function to allow contract to receive Ether
    receive() external payable {
        // Allow receiving ETH directly to the contract
    }

    /// @dev Function to withdraw collected Ether by the owner
    function withdrawEther() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No Ether to withdraw");
        treasury.transfer(balance);
    }
}
```
