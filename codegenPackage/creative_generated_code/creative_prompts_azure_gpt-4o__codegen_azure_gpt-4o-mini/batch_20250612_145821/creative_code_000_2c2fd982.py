"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mpeppeiosite.web.app
Prompt: Write a smart contract in Solidity for an ERC20 token with burn functionality, similar to $MPEPE's design, where tokens are automatically burned after every transaction.
Generated: DETERMINISTIC_2c2fd9822c87149d
Batch ID: 20250612_145821
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

// Importing the OpenZeppelin ERC20 implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title BurnableERC20Token
 * @dev Implementation of an ERC20 token with automatic burn functionality.
 */
contract BurnableERC20Token is ERC20, Ownable {
    // Percentage of tokens to burn from each transaction
    uint256 public burnPercentage;

    // Event to log burn actions
    event TokensBurned(address indexed from, uint256 amount);

    /**
     * @dev Constructor that initializes the token with a name, symbol, and burn percentage.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     * @param initialSupply The initial supply of the token.
     * @param _burnPercentage The percentage of tokens to burn on each transaction (in basis points).
     */
    constructor(string memory name, string memory symbol, uint256 initialSupply, uint256 _burnPercentage) 
        ERC20(name, symbol) 
    {
        // Ensure burn percentage is valid (0-10000 basis points -> 0%-100%)
        require(_burnPercentage <= 10000, "Burn percentage must be between 0 and 10000 basis points");
        
        _mint(msg.sender, initialSupply);
        burnPercentage = _burnPercentage;
    }

    /**
     * @dev Overrides the _transfer function to include burn functionality.
     * @param sender The address sending tokens.
     * @param recipient The address receiving tokens.
     * @param amount The amount of tokens to transfer.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        // Calculate the amount to burn
        uint256 burnAmount = (amount * burnPercentage) / 10000;
        uint256 amountAfterBurn = amount - burnAmount;

        // Ensure sender has enough balance after burning
        require(balanceOf(sender) >= amount, "Insufficient balance");

        // Call the standard transfer function
        super._transfer(sender, recipient, amountAfterBurn);

        // Burn the tokens
        if (burnAmount > 0) {
            _burn(sender, burnAmount);
            emit TokensBurned(sender, burnAmount);
        }
    }

    /**
     * @dev Allows the owner to update the burn percentage.
     * @param newBurnPercentage The new burn percentage (in basis points).
     */
    function setBurnPercentage(uint256 newBurnPercentage) external onlyOwner {
        require(newBurnPercentage <= 10000, "Burn percentage must be between 0 and 10000 basis points");
        burnPercentage = newBurnPercentage;
    }
}
```
