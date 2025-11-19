"""
Generated Code Metadata:
========================
Original URL: https://oceantoken.net
Prompt: Generate a smart contract code for Ocean Token using Solidity, implementing a simple token transfer functionality.
Generated: DETERMINISTIC_6fed8efb81521ad6
Batch ID: 20250622_205302
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
 * @title OceanToken
 * @dev Implementation of the OceanToken ERC20 token.
 */
contract OceanToken is ERC20, Ownable {
    /**
     * @dev Initializes the contract by:
     * - Setting the token name and symbol
     * - Minting initial supply to the contract deployer
     * @param initialSupply The initial token supply to be minted
     */
    constructor(uint256 initialSupply) ERC20("OceanToken", "OCEAN") {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Creates new tokens and assigns them to an account.
     * Can only be called by the contract owner.
     * @param to The account that will receive the minted tokens
     * @param amount The amount of tokens to mint
     */
    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
    }

    /**
     * @dev Burns tokens from the caller's account.
     * @param amount The amount of tokens to burn
     */
    function burn(uint256 amount) public {
        _burn(msg.sender, amount);
    }

    /**
     * @dev Transfers tokens from one account to another.
     * Overrides ERC20's transfer function to include additional checks.
     * @param recipient The account to receive the tokens
     * @param amount The amount of tokens to transfer
     * @return bool indicating whether the operation succeeded
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(recipient != address(0), "ERC20: transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");
        return super.transfer(recipient, amount);
    }
}
```
