"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pantherappai.pages.dev
Prompt: Develop a Solidity smart contract for PantherAI token burning mechanism, ensuring compliance with BEP20 standards. Include functionality for tracking the total supply reduction.
Generated: DETERMINISTIC_bc872208a4092635
Batch ID: 20250612_145510
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

// Importing the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title PantherAIToken
 * @dev Implementation of the PantherAI token with burning functionality
 */
contract PantherAIToken is ERC20Burnable, Ownable {
    // Total supply of the token
    uint256 private _totalSupply;

    // Event emitted when tokens are burned
    event TokensBurned(address indexed from, uint256 value);

    /**
     * @dev Constructor that gives the deployer all existing tokens.
     * @param initialSupply Initial supply of the PantherAI token
     */
    constructor(uint256 initialSupply) ERC20("PantherAI", "PAI") {
        require(initialSupply > 0, "Initial supply must be greater than zero");
        _totalSupply = initialSupply * (10 ** decimals());
        _mint(msg.sender, _totalSupply);
    }

    /**
     * @dev Override the burn function to include event logging
     * @param amount The amount of tokens to be burned
     */
    function burn(uint256 amount) public override {
        super.burn(amount);
        _totalSupply -= amount;
        emit TokensBurned(msg.sender, amount);
    }

    /**
     * @dev Get the current total supply of the token
     * @return uint256 Current total supply of the token
     */
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    /**
     * @dev Function to burn tokens on behalf of another address
     * @param account The address of the token holder
     * @param amount The amount of tokens to burn
     */
    function burnFrom(address account, uint256 amount) public override {
        super.burnFrom(account, amount);
        _totalSupply -= amount;
        emit TokensBurned(account, amount);
    }

    /**
     * @dev Function to get the current total supply reduction
     * @return uint256 Total supply reduction since the contract deployment
     */
    function totalSupplyReduction() public view returns (uint256) {
        return _totalSupply - totalSupply();
    }
}
```
