"""
Generated Code Metadata:
========================
Original URL: https://wagmicoins.web.app
Prompt: Create a smart contract that implements a 0% tax policy for $WAGMI transactions, as described in the tokenomics section.
Generated: DETERMINISTIC_55f278b5dd65fdfb
Batch ID: 20250612_145521
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
 * @title WAGMIToken
 * @dev Implementation of the WAGMI token with 0% tax policy on all transactions
 */
contract WAGMIToken is ERC20, Ownable {
    /**
     * @dev Initializes the contract by:
     * - Setting the token name and symbol
     * - Minting initial supply to the contract deployer
     * @param initialSupply The initial token supply to mint
     */
    constructor(uint256 initialSupply) ERC20("WAGMI", "WAGMI") {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Overrides ERC20 transfer function to implement 0% tax policy
     * @param recipient The address to receive tokens
     * @param amount The amount of tokens to transfer
     * @return true if transfer was successful
     */
    function transfer(address recipient, uint256 amount) public virtual override returns (bool) {
        _transfer(_msgSender(), recipient, amount);
        return true;
    }

    /**
     * @dev Overrides ERC20 transferFrom function to implement 0% tax policy
     * @param sender The address sending tokens
     * @param recipient The address to receive tokens
     * @param amount The amount of tokens to transfer
     * @return true if transfer was successful
     */
    function transferFrom(address sender, address recipient, uint256 amount) public virtual override returns (bool) {
        _transfer(sender, recipient, amount);
        
        uint256 currentAllowance = allowance(sender, _msgSender());
        require(currentAllowance >= amount, "ERC20: transfer amount exceeds allowance");
        unchecked {
            _approve(sender, _msgSender(), currentAllowance - amount);
        }
        
        return true;
    }

    /**
     * @dev Function to mint additional tokens (only callable by owner)
     * @param to The address to receive minted tokens
     * @param amount The amount of tokens to mint
     */
    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
    }
}
```
