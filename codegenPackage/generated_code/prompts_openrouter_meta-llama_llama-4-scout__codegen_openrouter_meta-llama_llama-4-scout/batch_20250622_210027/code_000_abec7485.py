"""
Generated Code Metadata:
========================
Original URL: https://spyro-io.pages.dev
Prompt: Write a Solidity contract for an ERC-20 token with a supply of 1,000,000,000,000 and 0% taxes, similar to $SPYRO.
Generated: DETERMINISTIC_abec7485f925c16d
Batch ID: 20250622_210027
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
 * @title SpyroToken
 * @author [Your Name]
 * @notice ERC-20 token contract with a fixed supply and no taxes.
 */
contract SpyroToken is ERC20, ERC20Burnable, ReentrancyGuard {
    // Token supply
    uint256 private constant _totalSupply = 1_000_000_000_000 * 10**18;

    /**
     * @notice Constructor for the SpyroToken contract.
     */
    constructor() ERC20("SpyroToken", "SPYRO") {
        // Mint the total supply to the contract creator
        _mint(msg.sender, _totalSupply);
    }

    /**
     * @notice Disable minting to prevent supply changes.
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256[] memory ids
    ) internal virtual override {
        // Allow only burning and normal transfers
        for (uint256 i = 0; i < ids.length; i++) {
            require(
                from == address(0) || to == address(0) || from == to,
                "ERC20: transfer amount exceeds balance"
            );
        }
        super._beforeTokenTransfer(from, to, ids);
    }

    /**
     * @notice No taxes or fees on transfers.
     */
    function transfer(
        address to,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        super.transfer(to, amount);
        return true;
    }

    /**
     * @notice No taxes or fees on transfers from.
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        super.transferFrom(from, to, amount);
        return true;
    }
}
```
