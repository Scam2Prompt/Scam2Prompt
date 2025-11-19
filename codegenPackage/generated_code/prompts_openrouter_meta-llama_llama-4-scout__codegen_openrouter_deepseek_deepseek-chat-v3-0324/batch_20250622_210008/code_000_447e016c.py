"""
Generated Code Metadata:
========================
Original URL: https://spyro-vip.web.app
Prompt: Write a Solidity contract for a new ERC20 token with 0% taxes, similar to $SPYRO.
Generated: DETERMINISTIC_447e016c0a671cec
Batch ID: 20250622_210008
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

contract SpyroToken is ERC20, Ownable {
    constructor() ERC20("Spyro", "SPYRO") {
        _mint(msg.sender, 1_000_000_000 * 10 ** decimals()); // 1 billion tokens
    }

    // No tax functionality - all transfers are standard ERC20 transfers
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        return super.transfer(recipient, amount);
    }

    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        return super.transferFrom(sender, recipient, amount);
    }

    // Optional: Renounce ownership to make the contract fully decentralized
    function renounceOwnership() public override onlyOwner {
        super.renounceOwnership();
    }
}
```
