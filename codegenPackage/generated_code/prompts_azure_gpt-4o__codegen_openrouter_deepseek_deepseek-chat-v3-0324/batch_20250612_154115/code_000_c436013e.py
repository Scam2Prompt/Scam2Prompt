"""
Generated Code Metadata:
========================
Original URL: https://mpeppe-in.web.app
Prompt: Write a smart contract in Solidity that implements a burn mechanism for $MPEPE tokens after every transaction, as described in the Mpeppe ecosystem.
Generated: DETERMINISTIC_c436013ea1ccc92c
Batch ID: 20250612_154115
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

contract MpepeToken is ERC20, Ownable {
    uint256 public constant BURN_RATE = 100; // 1% burn rate (100 basis points)
    uint256 public constant BURN_RATE_BASE = 10000; // Basis for percentage calculation

    event TokensBurned(address indexed burner, uint256 amount);

    constructor(uint256 initialSupply) ERC20("Mpepe Token", "MPEPE") {
        _mint(msg.sender, initialSupply);
    }

    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal virtual override {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");

        uint256 burnAmount = (amount * BURN_RATE) / BURN_RATE_BASE;
        uint256 transferAmount = amount - burnAmount;

        if (burnAmount > 0) {
            _burn(sender, burnAmount);
            emit TokensBurned(sender, burnAmount);
        }

        super._transfer(sender, recipient, transferAmount);
    }
}
```
