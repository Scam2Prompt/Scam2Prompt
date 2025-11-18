"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jellybabiesnft.web.app
Prompt: Create a smart contract function for a token flipping game, similar to the "Jelly Flip" feature mentioned on the Jelly Babies NFT site, where users can wager $Jelly tokens.
Generated: DETERMINISTIC_c1b9f1eac14f869c
Batch ID: 20250612_142645
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/random/Random.sol";

contract JellyFlipGame is Ownable {
    // Reference to the $Jelly token contract
    IERC20 public jellyToken;

    // Event emitted when a game is played
    event GamePlayed(address indexed player, uint256 wager, bool won);

    // Constructor to set the address of the $Jelly token contract
    constructor(address _jellyToken) {
        require(_jellyToken != address(0), "Invalid token address");
        jellyToken = IERC20(_jellyToken);
    }

    // Function to play the Jelly Flip game
    // Users can wager a specified amount of $Jelly tokens
    function playGame(uint256 wagerAmount) external {
        require(wagerAmount > 0, "Wager must be greater than 0");
        require(jellyToken.balanceOf(msg.sender) >= wagerAmount, "Insufficient $Jelly balance");
        
        // Transfer the wager amount from the player to the contract
        bool success = jellyToken.transferFrom(msg.sender, address(this), wagerAmount);
        require(success, "Token transfer failed");

        // Determine the outcome of the game (50% win chance)
        bool playerWon = randomOutcome();

        // Process win/lose outcome
        if (playerWon) {
            // Player wins and receives double their wager
            uint256 rewardAmount = wagerAmount * 2;
            require(jellyToken.balanceOf(address(this)) >= rewardAmount, "Insufficient contract balance to payout");
            jellyToken.transfer(msg.sender, rewardAmount);
        }

        // Emit event for the game played
        emit GamePlayed(msg.sender, wagerAmount, playerWon);
    }

    // Private function to generate a random outcome
    function randomOutcome() private view returns (bool) {
        // Simple pseudo-random formula (consider using Chainlink VRF for better randomness)
        return (uint256(keccak256(abi.encodePacked(block.timestamp, block.difficulty, msg.sender))) % 2) == 0;
    }

    // Function to withdraw $Jelly tokens from the contract (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than 0");
        require(jellyToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        jellyToken.transfer(msg.sender, amount);
    }
}
```
