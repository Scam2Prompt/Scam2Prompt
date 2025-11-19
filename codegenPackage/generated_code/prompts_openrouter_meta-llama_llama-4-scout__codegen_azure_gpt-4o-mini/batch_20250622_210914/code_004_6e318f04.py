"""
Generated Code Metadata:
========================
Original URL: https://mogcoin-xyz.pages.dev
Prompt: Develop a smart contract code in Solidity to create a new token on the Ethereum blockchain, similar to Mog Coin ($MOG), with tokenized winning features.
Generated: DETERMINISTIC_6e318f04372f0ff9
Batch ID: 20250622_210914
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

// Importing OpenZeppelin's ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// MogCoin contract inherits from ERC20 and Ownable
contract MogCoin is ERC20, Ownable {
    // Event to log the winning feature activation
    event WinningFeatureActivated(address indexed winner, uint256 amount);

    // Mapping to track winners
    mapping(address => bool) public winners;

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("Mog Coin", "MOG") {
        // Mint an initial supply of tokens to the contract deployer
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1 million tokens
    }

    // Function to activate the winning feature for a specific address
    function activateWinningFeature(address winner, uint256 amount) external onlyOwner {
        require(!winners[winner], "Winner has already been activated.");
        require(amount > 0, "Amount must be greater than zero.");
        
        // Mark the address as a winner
        winners[winner] = true;

        // Transfer the specified amount of tokens to the winner
        _transfer(owner(), winner, amount);

        // Emit an event for the activation
        emit WinningFeatureActivated(winner, amount);
    }

    // Function to check if an address is a winner
    function isWinner(address account) external view returns (bool) {
        return winners[account];
    }

    // Override the _beforeTokenTransfer hook to implement custom logic
    function _beforeTokenTransfer(address from, address to, uint256 amount) internal override {
        super._beforeTokenTransfer(from, to, amount);
        // Additional logic can be added here if needed
    }
}
```
