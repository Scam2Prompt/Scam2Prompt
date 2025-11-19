"""
Generated Code Metadata:
========================
Original URL: https://thoreumdashboard.com
Prompt: Generate a smart contract code snippet in Solidity for a token with a 1% transaction burn mechanism, similar to Thoreum's burn protocol.
Generated: DETERMINISTIC_d59afd0d9e4795f1
Batch ID: 20250622_210236
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

contract BurnToken is ERC20, Ownable {
    uint256 public constant BURN_RATE = 100; // 1% burn rate (100 basis points)
    uint256 public constant PERCENT_DENOMINATOR = 10000; // 100% = 10000 basis points

    constructor(string memory name, string memory symbol, uint256 initialSupply) ERC20(name, symbol) {
        _mint(msg.sender, initialSupply);
    }

    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal virtual override {
        if (sender == address(0) || recipient == address(0)) {
            super._transfer(sender, recipient, amount);
            return;
        }

        uint256 burnAmount = (amount * BURN_RATE) / PERCENT_DENOMINATOR;
        uint256 transferAmount = amount - burnAmount;

        if (burnAmount > 0) {
            _burn(sender, burnAmount);
        }

        super._transfer(sender, recipient, transferAmount);
    }
}
```
