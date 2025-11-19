"""
Generated Code Metadata:
========================
Original URL: https://mansorytoken.xyz
Prompt: Generate a smart contract code in Solidity for a token with a total supply of 1,000,000,000 units, similar to Mansory Token, and describe its utility in a luxury car marketplace.
Generated: DETERMINISTIC_f8284a28f82027ba
Batch ID: 20250622_212015
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title MansoryToken
 * @dev ERC20 token with a total supply of 1,000,000,000 units, designed for a luxury car marketplace.
 * This token can be used for transactions, rewards, and exclusive access within the marketplace.
 */
contract MansoryToken is ERC20, Ownable {
    using SafeMath for uint256;

    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens with 18 decimals

    /**
     * @dev Constructor that mints the total supply to the deployer (owner).
     */
    constructor() ERC20("Mansory Token", "MANSORY") {
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    /**
     * @dev Burns tokens from the caller's balance.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) public {
        _burn(msg.sender, amount);
    }

    /**
     * @dev Transfers tokens to a specified address.
     * Overrides ERC20's transfer to include additional checks.
     * @param recipient The address to transfer to.
     * @param amount The amount to transfer.
     * @return A boolean indicating success.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(recipient != address(0), "MansoryToken: transfer to the zero address");
        require(amount > 0, "MansoryToken: transfer amount must be greater than zero");
        return super.transfer(recipient, amount);
    }

    /**
     * @dev Transfers tokens from one address to another.
     * Overrides ERC20's transferFrom to include additional checks.
     * @param sender The address to transfer from.
     * @param recipient The address to transfer to.
     * @param amount The amount to transfer.
     * @return A boolean indicating success.
     */
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(sender != address(0), "MansoryToken: transfer from the zero address");
        require(recipient != address(0), "MansoryToken: transfer to the zero address");
        require(amount > 0, "MansoryToken: transfer amount must be greater than zero");
        return super.transferFrom(sender, recipient, amount);
    }

    /**
     * @dev Mints new tokens. Only callable by the owner.
     * @param to The address to mint to.
     * @param amount The amount to mint.
     */
    function mint(address to, uint256 amount) public onlyOwner {
        require(to != address(0), "MansoryToken: mint to the zero address");
        _mint(to, amount);
    }
}
```
