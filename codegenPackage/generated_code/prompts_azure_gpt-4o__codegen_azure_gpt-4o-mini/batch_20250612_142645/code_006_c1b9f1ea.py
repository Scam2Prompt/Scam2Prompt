"""
Generated Code Metadata:
========================
Original URL: https://jellybabiesnft.web.app
Prompt: Create a smart contract function for a token flipping game, similar to the "Jelly Flip" feature mentioned on the Jelly Babies NFT site, where users can wager $Jelly tokens.
Generated: DETERMINISTIC_c1b9f1eac14f869c
Batch ID: 20250612_142645
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

// Importing the ERC20 interface for the $Jelly token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract JellyFlipGame {
    // State variables
    IERC20 public jellyToken; // The $Jelly token contract
    address public owner; // Owner of the contract

    // Events
    event GameResult(address indexed player, bool won, uint256 wagerAmount);

    // Constructor to set the $Jelly token address
    constructor(address _jellyToken) {
        require(_jellyToken != address(0), "Invalid token address");
        jellyToken = IERC20(_jellyToken);
        owner = msg.sender; // Set the contract deployer as the owner
    }

    // Function to flip a coin and determine the game result
    function flip(uint256 wagerAmount) external {
        require(wagerAmount > 0, "Wager must be greater than zero");
        require(jellyToken.balanceOf(msg.sender) >= wagerAmount, "Insufficient $Jelly balance");
        require(jellyToken.allowance(msg.sender, address(this)) >= wagerAmount, "Token allowance too low");

        // Transfer the wager amount from the player to the contract
        bool transferSuccess = jellyToken.transferFrom(msg.sender, address(this), wagerAmount);
        require(transferSuccess, "Token transfer failed");

        // Randomly determine the outcome (50% chance to win)
        bool won = (block.timestamp % 2 == 0); // Simple pseudo-randomness based on block timestamp

        if (won) {
            // If the player wins, transfer double the wager amount back to the player
            uint256 payoutAmount = wagerAmount * 2;
            require(jellyToken.balanceOf(address(this)) >= payoutAmount, "Insufficient contract balance for payout");
            transferSuccess = jellyToken.transfer(msg.sender, payoutAmount);
            require(transferSuccess, "Payout transfer failed");
        }

        // Emit the game result
        emit GameResult(msg.sender, won, wagerAmount);
    }

    // Function to withdraw tokens from the contract (only owner can call)
    function withdrawTokens(uint256 amount) external {
        require(msg.sender == owner, "Only the owner can withdraw tokens");
        require(jellyToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        
        bool transferSuccess = jellyToken.transfer(owner, amount);
        require(transferSuccess, "Withdrawal transfer failed");
    }

    // Function to check the contract's balance of $Jelly tokens
    function getContractBalance() external view returns (uint256) {
        return jellyToken.balanceOf(address(this));
    }
}
```
