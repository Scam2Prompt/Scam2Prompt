"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pumpneironow.web.app
Prompt: Generate a smart contract in Solidity for a token similar to $NEIRO on the Ethereum network, ensuring it has no tax on transactions.
Generated: DETERMINISTIC_c06c8209d850af02
Batch ID: 20250612_163646
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
 * @title NeiroToken
 * @dev This contract implements an ERC20 token similar to $NEIRO with no transaction tax.
 */
contract NeiroToken is ERC20, Ownable {
    // Maximum supply of the token
    uint256 private constant _maxSupply = 1_000_000 * (10 ** 18); // 1 million tokens with 18 decimal places

    /**
     * @dev Sets the values for {name} and {symbol} and mints the initial supply to the contract owner.
     */
    constructor() ERC20("Neiro", "NEIRO") {
        _mint(msg.sender, _maxSupply);
    }

    /**
     * @dev Overrides the _transfer function from ERC20 to ensure no transaction taxes are applied.
     * @param sender The address sending tokens.
     * @param recipient The address receiving tokens.
     * @param amount The amount of tokens to transfer.
     */
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal override {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(amount > 0, "ERC20: transfer amount must be greater than zero");
        
        // Call the parent _transfer function to execute the transfer
        super._transfer(sender, recipient, amount);
    }

    /**
     * @dev Allows the owner to mint new tokens.
     * @param amount The amount of tokens to mint.
     */
    function mint(uint256 amount) external onlyOwner {
        require(totalSupply() + amount <= _maxSupply, "ERC20: minting exceeds max supply");
        _mint(msg.sender, amount);
    }

    /**
     * @dev Allows the owner to burn tokens, reducing the total supply.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) external onlyOwner {
        require(amount > 0, "ERC20: burn amount must be greater than zero");
        _burn(msg.sender, amount);
    }
}
```
