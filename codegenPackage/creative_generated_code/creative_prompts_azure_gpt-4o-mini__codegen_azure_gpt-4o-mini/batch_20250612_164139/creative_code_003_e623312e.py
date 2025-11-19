"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://babygrokai.pages.dev
Prompt: Develop a Solidity contract that implements a burn mechanism for BABYGROK tokens, ensuring a percentage of each transaction is burned.
Generated: DETERMINISTIC_e623312e8c3970f7
Batch ID: 20250612_164139
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title BABYGROK Token Contract
 * @dev ERC20 Token with a burn mechanism for a percentage of each transaction.
 */
contract BABYGROK is ERC20, Ownable {
    // Percentage of tokens to be burned from each transaction (in basis points)
    uint256 public burnPercentage;
    // Basis points constant for calculation (100% = 10000 basis points)
    uint256 private constant BASIS_POINTS = 10000;

    // Event emitted when the burn percentage is updated
    event BurnPercentageUpdated(uint256 oldPercentage, uint256 newPercentage);

    /**
     * @dev Constructor to initialize the token with a name and symbol.
     * @param _name The name of the token.
     * @param _symbol The symbol of the token.
     * @param _burnPercentage The initial burn percentage (in basis points).
     */
    constructor(string memory _name, string memory _symbol, uint256 _burnPercentage) 
        ERC20(_name, _symbol) 
    {
        require(_burnPercentage <= 10000, "Invalid burn percentage");
        burnPercentage = _burnPercentage;
        _mint(msg.sender, 1000000 * 10 ** decimals()); // Mint initial supply to owner
    }

    /**
     * @dev Update the burn percentage for transactions.
     * @param _newBurnPercentage The new burn percentage (in basis points).
     */
    function updateBurnPercentage(uint256 _newBurnPercentage) external onlyOwner {
        require(_newBurnPercentage <= 10000, "Invalid burn percentage");
        uint256 oldPercentage = burnPercentage;
        burnPercentage = _newBurnPercentage;
        emit BurnPercentageUpdated(oldPercentage, burnPercentage);
    }

    /**
     * @dev Override the transfer function to implement the burn mechanism.
     * @param recipient The address to receive the tokens.
     * @param amount The amount of tokens to transfer.
     * @return success Indicates whether the transfer was successful.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool success) {
        // Calculate burn amount
        uint256 burnAmount = (amount * burnPercentage) / BASIS_POINTS;
        uint256 transferAmount = amount - burnAmount;

        // Ensure transfer amount does not exceed the sender's balance
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Burn the tokens
        _burn(msg.sender, burnAmount);
        // Transfer the remaining tokens to the recipient
        _transfer(msg.sender, recipient, transferAmount);

        return true;
    }

    /**
     * @dev Override the transferFrom function to implement the burn mechanism.
     * @param sender The address from which to transfer tokens.
     * @param recipient The address to receive the tokens.
     * @param amount The amount of tokens to transfer.
     * @return success Indicates whether the transfer was successful.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool success) {
        // Calculate burn amount
        uint256 burnAmount = (amount * burnPercentage) / BASIS_POINTS;
        uint256 transferAmount = amount - burnAmount;

        // Ensure transfer amount does not exceed the sender's balance
        require(balanceOf(sender) >= amount, "Insufficient balance");
        require(allowance(sender, msg.sender) >= amount, "Allowance exceeded");

        // Burn the tokens
        _burn(sender, burnAmount);
        // Transfer the remaining tokens to the recipient
        _transfer(sender, recipient, transferAmount);
        // Update the allowance
        _approve(sender, msg.sender, allowance(sender, msg.sender) - amount);

        return true;
    }
}
```
