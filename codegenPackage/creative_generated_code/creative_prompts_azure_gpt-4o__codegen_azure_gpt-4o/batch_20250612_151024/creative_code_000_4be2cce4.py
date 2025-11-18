"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gen-da6.pages.dev
Prompt: Write a smart contract in Solidity for a cryptocurrency token similar to "$ENTS," including functionality for tokenomics and rewards distribution.
Generated: DETERMINISTIC_4be2cce457ff2382
Batch ID: 20250612_151024
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
 * @title ENTS Token Smart Contract
 * @dev ERC20-compliant token contract with tokenomics and rewards distribution.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ENTS is ERC20, Ownable {
    // Tokenomics variables
    uint256 public constant INITIAL_SUPPLY = 1_000_000 * 10**18; // 1 million tokens
    uint256 public rewardsPoolBalance; // Balance reserved for rewards distribution

    // Event to log reward distribution
    event RewardsDistributed(address indexed recipient, uint256 amount);

    /**
     * @dev Constructor that initializes the token with a name and symbol.
     * Mints the initial supply to the contract owner.
     */
    constructor() ERC20("ENTS Token", "ENTS") {
        _mint(msg.sender, INITIAL_SUPPLY);
    }

    /**
     * @dev Function to distribute rewards to a given address from the rewards pool.
     * Requires the caller to be the contract owner.
     * @param recipient The address receiving the rewards.
     * @param amount The amount of tokens to distribute.
     */
    function distributeRewards(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");
        require(rewardsPoolBalance >= amount, "Insufficient rewards pool balance");

        // Transfer tokens from the rewards pool
        rewardsPoolBalance -= amount;
        _transfer(address(this), recipient, amount);

        emit RewardsDistributed(recipient, amount);
    }

    /**
     * @dev Function to deposit tokens into the rewards pool.
     * @param amount The amount of tokens to deposit.
     */
    function depositToRewardsPool(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer tokens to the contract address
        _transfer(msg.sender, address(this), amount);
        rewardsPoolBalance += amount;
    }

    /**
     * @dev Function to withdraw tokens from the rewards pool back to the owner.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawFromRewardsPool(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(rewardsPoolBalance >= amount, "Insufficient rewards pool balance");

        // Transfer tokens back to the owner
        rewardsPoolBalance -= amount;
        _transfer(address(this), msg.sender, amount);
    }

    /**
     * @dev Override `_transfer` to include tokenomics logic if needed (e.g., fees or burns).
     * For simplicity, no modifications are made in this example.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        super._transfer(sender, recipient, amount);
    }
}
```
