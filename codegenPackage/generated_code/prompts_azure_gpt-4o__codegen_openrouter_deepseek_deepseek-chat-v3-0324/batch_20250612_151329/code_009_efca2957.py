"""
Generated Code Metadata:
========================
Original URL: https://fffrfh.pages.dev
Prompt: Write a Solidity function that ensures MOR tokens are non-transferable for the first 90 days after fair launch, as described in the Morpheus documentation. Include logic to enable transfers after this period.
Generated: DETERMINISTIC_efca2957c7c720c4
Batch ID: 20250612_151329
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

contract MORToken is ERC20 {
    uint256 public immutable fairLaunchTimestamp;
    uint256 public constant LOCK_DURATION = 90 days;

    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        address initialHolder
    ) ERC20(name, symbol) {
        fairLaunchTimestamp = block.timestamp;
        _mint(initialHolder, initialSupply);
    }

    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal virtual override {
        super._beforeTokenTransfer(from, to, amount);

        // Skip check for minting and burning
        if (from == address(0) || to == address(0)) {
            return;
        }

        require(
            block.timestamp >= fairLaunchTimestamp + LOCK_DURATION,
            "MOR: Transfers are locked for 90 days after fair launch"
        );
    }
}
```
