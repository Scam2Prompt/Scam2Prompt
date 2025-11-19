"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kangamoon-claims.pages.dev
Prompt: Generate a code snippet for integrating the $KANG token into a Play-to-Earn game using the ERC-20 standard.
Generated: DETERMINISTIC_779ee8a8cd46cc59
Batch ID: 20250612_163848
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

// Importing the ERC20 interface from OpenZeppelin
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// The KangToken contract is an ERC20 token that can be integrated into a Play-to-Earn game
contract KangToken is ERC20Burnable, Ownable {
    // The total supply of the token
    uint256 public constant INITIAL_SUPPLY = 1_000_000 * 10 ** 18; // 1 million tokens with 18 decimals

    // Mapping to track balances of players for rewards
    mapping(address => uint256) public playerRewards;

    // Events for logging
    event RewardDistributed(address indexed player, uint256 amount);

    // Constructor to mint the initial supply
    constructor() ERC20("Kang Token", "KANG") {
        _mint(msg.sender, INITIAL_SUPPLY); // Mint tokens to the owner's address
    }

    // Function to distribute rewards to players
    function distributeRewards(address player, uint256 amount) external onlyOwner {
        require(player != address(0), "Invalid player address"); // Ensure valid address
        require(amount > 0, "Amount must be greater than zero"); // Ensure reward amount is valid
        
        // Check if the contract has enough tokens to distribute
        require(balanceOf(msg.sender) >= amount, "Insufficient token balance for reward distribution");

        // Transfer tokens to the player
        _transfer(msg.sender, player, amount);
        
        // Update the player's reward balance
        playerRewards[player] += amount;

        // Emit the reward distribution event
        emit RewardDistributed(player, amount);
    }

    // Function to check player rewards
    function checkReward(address player) external view returns (uint256) {
        return playerRewards[player];
    }

    // Function to allow players to redeem their rewards
    function redeemRewards(uint256 amount) external {
        require(playerRewards[msg.sender] >= amount, "Insufficient rewards to redeem"); // Ensure player has enough rewards

        // Deduct the redeemed amount from the player's rewards
        playerRewards[msg.sender] -= amount;

        // Transfer the tokens to the player
        _transfer(owner(), msg.sender, amount); // Tokens should be sent from the owner’s balance
    }

    // Function to withdraw tokens from the contract (only for the owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(balanceOf(address(this)) >= amount, "Insufficient balance in contract");

        // Transfer specified amount to the owner
        _transfer(address(this), msg.sender, amount);
    }
}
```
