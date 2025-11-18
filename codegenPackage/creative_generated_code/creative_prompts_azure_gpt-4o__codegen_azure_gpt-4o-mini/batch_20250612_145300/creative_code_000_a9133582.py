"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mpeppe-is.web.app
Prompt: Write a smart contract in Solidity for an ERC20 token with a burn mechanism similar to $MPEPE, where tokens are automatically burned after every transaction.
Generated: DETERMINISTIC_a91335827e3d7714
Batch ID: 20250612_145300
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
 * @title ERC20TokenWithBurn
 * @dev This contract implements an ERC20 token with an automatic burn mechanism
 */
contract ERC20TokenWithBurn is ERC20, Ownable {
    // Burn percentage (in basis points, e.g., 100 = 1%)
    uint256 public burnPercentage;

    /**
     * @dev Sets the values for {name} and {symbol}, and initializes the burn percentage.
     * @param name Name of the token.
     * @param symbol Symbol of the token.
     * @param initialSupply Initial supply of tokens to be minted.
     * @param _burnPercentage Burn percentage for each transaction.
     */
    constructor(string memory name, string memory symbol, uint256 initialSupply, uint256 _burnPercentage) ERC20(name, symbol) {
        require(_burnPercentage <= 10000, "Burn percentage cannot exceed 100%.");
        burnPercentage = _burnPercentage;
        _mint(msg.sender, initialSupply * (10 ** decimals()));
    }

    /**
     * @dev Overrides the _transfer function to include the burn mechanism.
     * @param sender The address sending the tokens.
     * @param recipient The address receiving the tokens.
     * @param amount The amount of tokens to transfer.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        // Calculate the amount to burn based on the burn percentage
        uint256 burnAmount = (amount * burnPercentage) / 10000;
        uint256 transferAmount = amount - burnAmount;

        // Ensure that the sender has enough balance to cover the transaction
        require(balanceOf(sender) >= amount, "Insufficient balance.");

        // Transfer the tokens to the recipient
        super._transfer(sender, recipient, transferAmount);

        // Burn the tokens
        if (burnAmount > 0) {
            _burn(sender, burnAmount);
        }
    }

    /**
     * @dev Allows the owner to update the burn percentage.
     * @param newBurnPercentage New burn percentage for the token transactions.
     */
    function setBurnPercentage(uint256 newBurnPercentage) external onlyOwner {
        require(newBurnPercentage <= 10000, "Burn percentage cannot exceed 100%.");
        burnPercentage = newBurnPercentage;
    }
}
```
