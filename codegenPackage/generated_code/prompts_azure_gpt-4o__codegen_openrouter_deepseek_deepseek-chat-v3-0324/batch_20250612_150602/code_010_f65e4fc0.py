"""
Generated Code Metadata:
========================
Original URL: https://kishu.finance
Prompt: Write a Solidity contract that implements a token burning mechanism similar to the one described for $KISHU, where tokens are permanently removed from circulation.
Generated: DETERMINISTIC_f65e4fc084da813f
Batch ID: 20250612_150602
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

/**
 * @title BurnableToken
 * @dev ERC20 token with burn functionality and ownership control
 */
contract BurnableToken is ERC20, Ownable {
    // Total amount of tokens burned
    uint256 private _totalBurned;

    /**
     * @dev Constructor that mints initial supply to contract deployer
     * @param name Token name
     * @param symbol Token symbol
     * @param initialSupply Initial token supply
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply
    ) ERC20(name, symbol) {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Burns a specific amount of tokens from the caller's balance
     * @param amount The amount of tokens to be burned
     */
    function burn(uint256 amount) public {
        _burn(msg.sender, amount);
        _totalBurned += amount;
    }

    /**
     * @dev Burns a specific amount of tokens from a specified account (only owner)
     * @param account The account to burn tokens from
     * @param amount The amount of tokens to be burned
     */
    function burnFrom(address account, uint256 amount) public onlyOwner {
        _spendAllowance(account, msg.sender, amount);
        _burn(account, amount);
        _totalBurned += amount;
    }

    /**
     * @dev Returns the total amount of tokens burned
     * @return uint256 representing the total burned tokens
     */
    function totalBurned() public view returns (uint256) {
        return _totalBurned;
    }

    /**
     * @dev Overrides the ERC20 _burn function to track total burned tokens
     * @param account The account to burn tokens from
     * @param amount The amount of tokens to be burned
     */
    function _burn(address account, uint256 amount) internal override {
        require(amount > 0, "BurnableToken: amount must be greater than 0");
        require(
            balanceOf(account) >= amount,
            "BurnableToken: burn amount exceeds balance"
        );
        super._burn(account, amount);
    }
}
```
