"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rebelsatoshi-en.web.app
Prompt: Generate a smart contract for the $RBLZ token on the Ethereum blockchain, ensuring it has no buy or sell tax as described on the Rebel Satoshi website.
Generated: DETERMINISTIC_6a90863093b9ad4e
Batch ID: 20250612_161616
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
 * @title RBLZToken
 * @dev ERC20 Token with no buy/sell taxes
 */
contract RBLZToken is ERC20, Ownable {

    // Events for Transfer and Approval
    event TaxFreeTransfer(address indexed from, address indexed to, uint256 value);

    // Constructor to initialize the token with specific name and symbol
    constructor() ERC20("Rebel Satoshi Token", "$RBLZ") {
        // Mint an initial supply of tokens to the contract owner
        _mint(msg.sender, 1_000_000 * 10 ** decimals()); // 1 million tokens with decimals
    }

    /**
     * @dev Overrides the _transfer function to ensure no taxes are applied.
     * @param sender Address of the sender
     * @param recipient Address of the recipient
     * @param amount Amount of tokens to transfer
     */
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");

        // Call the parent _transfer function to execute the transaction
        super._transfer(sender, recipient, amount);

        emit TaxFreeTransfer(sender, recipient, amount);
    }

    /**
     * @dev Allows the owner to mint new tokens. Can be restricted to avoid inflation.
     * @param account Address to mint tokens to
     * @param amount Amount of tokens to mint
     */
    function mint(address account, uint256 amount) external onlyOwner {
        require(account != address(0), "ERC20: mint to the zero address");
        require(amount > 0, "Mint amount must be greater than zero");

        _mint(account, amount);
    }

    /**
     * @dev Allows the owner to burn tokens from a specified account.
     * @param account Address from which to burn tokens
     * @param amount Amount of tokens to burn
     */
    function burn(address account, uint256 amount) external onlyOwner {
        require(account != address(0), "ERC20: burn from the zero address");
        require(amount > 0, "Burn amount must be greater than zero");
        require(balanceOf(account) >= amount, "ERC20: burn amount exceeds balance");

        _burn(account, amount);
    }
}
```
