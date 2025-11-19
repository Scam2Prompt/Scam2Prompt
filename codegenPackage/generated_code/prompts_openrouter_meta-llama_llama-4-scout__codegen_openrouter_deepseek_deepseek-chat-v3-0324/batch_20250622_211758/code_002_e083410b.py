"""
Generated Code Metadata:
========================
Original URL: https://cloneforce.xyz
Prompt: Generate a smart contract code in Solidity to implement a burning utility for digital assets, similar to the one mentioned on the Clone Force website.
Generated: DETERMINISTIC_e083410b087e282c
Batch ID: 20250622_211758
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
 * @dev Implementation of an ERC20 token with burnable functionality.
 * Allows token holders to burn their own tokens or allows an owner to burn tokens on behalf of users.
 */
contract BurnableToken is ERC20, Ownable {
    /**
     * @dev Emitted when tokens are burned.
     * @param burner Address that initiated the burn
     * @param value Amount of tokens burned
     */
    event Burn(address indexed burner, uint256 value);

    /**
     * @dev Constructor that initializes the token with a name and symbol.
     * @param name The name of the token
     * @param symbol The symbol of the token
     * @param initialSupply The initial supply of tokens
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply
    ) ERC20(name, symbol) {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Burns a specific amount of tokens from the caller's balance.
     * @param amount The amount of tokens to burn
     */
    function burn(uint256 amount) public {
        _burn(msg.sender, amount);
        emit Burn(msg.sender, amount);
    }

    /**
     * @dev Burns a specific amount of tokens from a specified address.
     * Only callable by the contract owner.
     * @param from The address to burn tokens from
     * @param amount The amount of tokens to burn
     */
    function burnFrom(address from, uint256 amount) public onlyOwner {
        _burn(from, amount);
        emit Burn(from, amount);
    }

    /**
     * @dev Overrides the ERC20 transfer function to include additional checks.
     * @param recipient The address to transfer tokens to
     * @param amount The amount of tokens to transfer
     * @return bool Whether the transfer was successful
     */
    function transfer(address recipient, uint256 amount) 
        public 
        virtual 
        override 
        returns (bool) 
    {
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(amount > 0, "Amount must be greater than zero");
        return super.transfer(recipient, amount);
    }

    /**
     * @dev Overrides the ERC20 transferFrom function to include additional checks.
     * @param sender The address to transfer tokens from
     * @param recipient The address to transfer tokens to
     * @param amount The amount of tokens to transfer
     * @return bool Whether the transfer was successful
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public virtual override returns (bool) {
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(amount > 0, "Amount must be greater than zero");
        return super.transferFrom(sender, recipient, amount);
    }
}
```
