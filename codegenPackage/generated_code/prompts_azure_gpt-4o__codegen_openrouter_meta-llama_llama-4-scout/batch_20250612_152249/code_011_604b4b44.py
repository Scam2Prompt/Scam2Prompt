"""
Generated Code Metadata:
========================
Original URL: https://saitamadapp.pages.dev
Prompt: Write a Solidity smart contract that implements a hyperburn mechanism for token supply management, inspired by Saitama's hyperburn feature.
Generated: DETERMINISTIC_604b4b442a63847a
Batch ID: 20250612_152249
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

/**
 * @title HyperburnToken
 * @author [Your Name]
 * @notice A token with a hyperburn mechanism for token supply management.
 */
contract HyperburnToken is ERC20, ERC20Burnable, ReentrancyGuard {
    // Mapping of addresses to their respective burn multipliers
    mapping(address => uint256) public burnMultipliers;

    // Event emitted when a hyperburn occurs
    event Hyperburn(address indexed from, uint256 amount);

    /**
     * @notice Constructor for the HyperburnToken contract.
     * @param name_ The name of the token.
     * @param symbol_ The symbol of the token.
     */
    constructor(string memory name_, string memory symbol_) ERC20(name_, symbol_) {
        // Initialize burn multiplier for the contract creator to 1
        burnMultipliers[msg.sender] = 1;
    }

    /**
     * @notice Sets the burn multiplier for an address.
     * @param account The address for which to set the burn multiplier.
     * @param multiplier The burn multiplier to set.
     */
    function setBurnMultiplier(address account, uint256 multiplier) public onlyOwner {
        require(multiplier > 0, "Burn multiplier must be greater than 0");
        burnMultipliers[account] = multiplier;
    }

    /**
     * @notice Gets the burn multiplier for an address.
     * @param account The address for which to get the burn multiplier.
     * @return The burn multiplier for the given address.
     */
    function getBurnMultiplier(address account) public view returns (uint256) {
        return burnMultipliers[account];
    }

    /**
     * @notice Hyperburn function to burn tokens with a multiplier.
     * @param amount The amount of tokens to burn.
     */
    function hyperburn(uint256 amount) public nonReentrant {
        require(amount > 0, "Amount to burn must be greater than 0");
        uint256 burnAmount = amount * getBurnMultiplier(msg.sender);
        _burn(msg.sender, amount);
        emit Hyperburn(msg.sender, burnAmount);
    }

    /**
     * @notice Overrides the burn function to prevent accidental burns without multiplier.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) public override nonReentrant {
        revert("Use hyperburn function to burn tokens");
    }

    /**
     * @notice Overrides the burnFrom function to prevent accidental burns without multiplier.
     * @param from The address from which to burn tokens.
     * @param amount The amount of tokens to burn.
     */
    function burnFrom(address from, uint256 amount) public override nonReentrant {
        revert("Use hyperburn function to burn tokens");
    }
}
```
