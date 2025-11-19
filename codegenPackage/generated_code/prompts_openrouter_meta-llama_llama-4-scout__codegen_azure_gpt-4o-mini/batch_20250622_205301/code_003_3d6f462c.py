"""
Generated Code Metadata:
========================
Original URL: https://taiyoil.web.app
Prompt: Design a simple smart contract using Solidity to manage the minting and distribution of Taiyo Oil, including the logic for rewarding Taiyo Pilots based on oil purchased.
Generated: DETERMINISTIC_3d6f462cc407f9d4
Batch ID: 20250622_205301
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// TaiyoOil is an ERC20 token representing Taiyo Oil
contract TaiyoOil is ERC20, Ownable {
    // Mapping to track the rewards for each Taiyo Pilot
    mapping(address => uint256) public pilotRewards;

    // Event emitted when oil is purchased
    event OilPurchased(address indexed buyer, uint256 amount, uint256 reward);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("Taiyo Oil", "TAIYO") {
        // Mint an initial supply of Taiyo Oil to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1 million tokens
    }

    // Function to purchase oil and reward the pilot
    function purchaseOil(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(owner()) >= amount, "Not enough Taiyo Oil available");

        // Transfer the oil to the buyer
        _transfer(owner(), msg.sender, amount);

        // Calculate the reward (1% of the purchased amount)
        uint256 reward = amount / 100;

        // Update the pilot's reward balance
        pilotRewards[msg.sender] += reward;

        // Emit an event for the purchase
        emit OilPurchased(msg.sender, amount, reward);
    }

    // Function to allow pilots to claim their rewards
    function claimRewards() external {
        uint256 reward = pilotRewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        // Reset the pilot's reward balance
        pilotRewards[msg.sender] = 0;

        // Mint new tokens as rewards
        _mint(msg.sender, reward);
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(address(this)) >= amount, "Not enough tokens in the contract");

        // Transfer tokens to the owner
        _transfer(address(this), msg.sender, amount);
    }

    // Function to check the contract's balance of Taiyo Oil
    function contractBalance() external view returns (uint256) {
        return balanceOf(address(this));
    }
}
```
