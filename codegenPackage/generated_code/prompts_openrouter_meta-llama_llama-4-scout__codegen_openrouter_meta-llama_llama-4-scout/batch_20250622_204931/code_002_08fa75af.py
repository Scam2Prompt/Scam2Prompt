"""
Generated Code Metadata:
========================
Original URL: https://galaxyfox-en.pages.dev
Prompt: Generate a smart contract code in Solidity for a token burn mechanism similar to Galaxy Fox's $GFOX token.
Generated: DETERMINISTIC_08fa75af3a1d6a45
Batch ID: 20250622_204931
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title GFOXToken
 * @author [Your Name]
 * @notice A token with burn mechanism similar to Galaxy Fox's $GFOX token.
 */
contract GFOXToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of addresses to their respective burn allowances
    mapping(address => uint256) private _burnAllowances;

    /**
     * @notice Constructor for the GFOXToken contract.
     * @param name_ The name of the token.
     * @param symbol_ The symbol of the token.
     * @param totalSupply_ The total supply of the token.
     */
    constructor(string memory name_, string memory symbol_, uint256 totalSupply_) ERC20(name_, symbol_) {
        _mint(msg.sender, totalSupply_);
    }

    /**
     * @notice Sets the burn allowance for an address.
     * @param spender The address to set the burn allowance for.
     * @param amount The amount to set the burn allowance to.
     */
    function setBurnAllowance(address spender, uint256 amount) public {
        require(msg.sender == owner(), "Only the owner can set burn allowances");
        _burnAllowances[spender] = amount;
    }

    /**
     * @notice Gets the burn allowance for an address.
     * @param owner The address to get the burn allowance for.
     * @return The burn allowance for the given address.
     */
    function getBurnAllowance(address owner) public view returns (uint256) {
        return _burnAllowances[owner];
    }

    /**
     * @notice Burns tokens from an address and deducts from the burn allowance.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) public override nonReentrant {
        uint256 currentAllowance = _burnAllowances[msg.sender];
        if (currentAllowance != 0) {
            require(currentAllowance >= amount, "Burn amount exceeds allowance");
            _burnAllowances[msg.sender] = currentAllowance.sub(amount);
        }
        super.burn(amount);
    }

    /**
     * @notice Burns tokens from an address on behalf of another address and deducts from the burn allowance.
     * @param account The address to burn tokens from.
     * @param amount The amount of tokens to burn.
     */
    function burnFrom(address account, uint256 amount) public override nonReentrant {
        uint256 currentAllowance = _burnAllowances[account];
        if (currentAllowance != 0) {
            require(currentAllowance >= amount, "Burn amount exceeds allowance");
            _burnAllowances[account] = currentAllowance.sub(amount);
        }
        super.burnFrom(account, amount);
    }
}
```
