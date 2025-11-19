"""
Generated Code Metadata:
========================
Original URL: https://babygrokai.pages.dev
Prompt: Generate a code snippet in Solidity to implement a burn mechanism for a cryptocurrency token, similar to the one described in the Baby Grok tokenomics.
Generated: DETERMINISTIC_6c73296863040901
Batch ID: 20250622_205016
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

/**
 * @title BurnableToken
 * @dev Implementation of a burn mechanism for an ERC20 token.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract BurnableToken is ERC20, Ownable {
    // Event to log token burns
    event TokensBurned(address indexed burner, uint256 amount);

    /**
     * @dev Constructor to initialize the token with a name, symbol, and initial supply.
     * @param name Token name
     * @param symbol Token symbol
     * @param initialSupply Initial token supply (in smallest units)
     */
    constructor(string memory name, string memory symbol, uint256 initialSupply) ERC20(name, symbol) {
        // Mint the initial supply to the contract deployer
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Function to burn tokens from the caller's balance.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) external {
        require(amount > 0, "Burn amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");

        // Burn the tokens
        _burn(msg.sender, amount);

        // Emit the burn event
        emit TokensBurned(msg.sender, amount);
    }

    /**
     * @dev Function to burn tokens from another account (requires allowance).
     * @param account The account to burn tokens from.
     * @param amount The amount of tokens to burn.
     */
    function burnFrom(address account, uint256 amount) external {
        require(amount > 0, "Burn amount must be greater than zero");
        require(balanceOf(account) >= amount, "Insufficient balance to burn");

        // Check and reduce the allowance
        uint256 currentAllowance = allowance(account, msg.sender);
        require(currentAllowance >= amount, "Burn amount exceeds allowance");
        _approve(account, msg.sender, currentAllowance - amount);

        // Burn the tokens
        _burn(account, amount);

        // Emit the burn event
        emit TokensBurned(account, amount);
    }
}
```
