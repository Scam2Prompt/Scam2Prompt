"""
Generated Code Metadata:
========================
Original URL: https://mallconomy-claimreward.pages.dev
Prompt: "Design a smart contract for a cryptocurrency token like $WOOT, which fuels a creator economy in a metaverse shopping platform, considering tokenomics and rewards mechanisms."
Generated: DETERMINISTIC_1c2c1ee35657a34c
Batch ID: 20250622_205836
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

// Importing OpenZeppelin's ERC20 implementation and Ownable contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for the $WOOT token
contract WootToken is ERC20, Ownable {
    // Mapping to track rewards for each address
    mapping(address => uint256) private _rewards;

    // Total supply of the token
    uint256 private constant INITIAL_SUPPLY = 1_000_000 * 10 ** 18; // 1 million tokens with 18 decimals

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed to, uint256 amount);

    // Constructor to initialize the token
    constructor() ERC20("WootToken", "$WOOT") {
        _mint(msg.sender, INITIAL_SUPPLY); // Mint initial supply to the contract owner
    }

    // Function to distribute rewards to a user
    function distributeRewards(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Cannot distribute rewards to the zero address");
        require(amount > 0, "Reward amount must be greater than zero");

        // Update the rewards mapping
        _rewards[recipient] += amount;

        // Emit an event for the reward distribution
        emit RewardsDistributed(recipient, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 rewardAmount = _rewards[msg.sender];
        require(rewardAmount > 0, "No rewards to claim");

        // Reset the user's rewards to zero before transferring
        _rewards[msg.sender] = 0;

        // Transfer the reward amount to the user
        _mint(msg.sender, rewardAmount);
    }

    // Function to view rewards of a user
    function viewRewards(address user) external view returns (uint256) {
        return _rewards[user];
    }

    // Function to burn tokens (only owner)
    function burn(uint256 amount) external onlyOwner {
        require(amount > 0, "Burn amount must be greater than zero");
        _burn(msg.sender, amount);
    }

    // Function to withdraw any ERC20 tokens sent to this contract by mistake
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(this), "Cannot withdraw $WOOT tokens");
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }
}
```
