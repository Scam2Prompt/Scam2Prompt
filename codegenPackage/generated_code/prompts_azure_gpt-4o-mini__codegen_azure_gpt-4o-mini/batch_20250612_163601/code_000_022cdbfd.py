"""
Generated Code Metadata:
========================
Original URL: https://bobothebear.pages.dev
Prompt: Generate a smart contract for a meme token inspired by Bobo the Bear, including features like 0% tax and liquidity burned.
Generated: DETERMINISTIC_022cdbfd8acc0e1c
Batch ID: 20250612_163601
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

// BoboToken is a simple ERC20 token with 0% tax and liquidity burned
contract BoboToken is ERC20, Ownable {
    // Event to log the burning of liquidity
    event LiquidityBurned(uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("Bobo the Bear", "BOBO") {
        // Mint initial supply to the contract deployer
        _mint(msg.sender, 1_000_000 * 10 ** decimals()); // 1 million tokens
    }

    // Function to burn liquidity (tokens) from the contract
    function burnLiquidity(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(address(this)) >= amount, "Insufficient balance to burn");

        // Burn the specified amount of tokens
        _burn(address(this), amount);
        emit LiquidityBurned(amount);
    }

    // Override the transfer function to ensure 0% tax
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        // Call the parent transfer function
        super._transfer(sender, recipient, amount);
    }

    // Function to withdraw any ERC20 tokens accidentally sent to the contract
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(this), "Cannot withdraw BoboToken");
        require(amount > 0, "Amount must be greater than 0");

        // Transfer the specified amount of tokens to the owner
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }
}
```
