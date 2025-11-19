"""
Generated Code Metadata:
========================
Original URL: https://beefcom.pages.dev
Prompt: Provide a Solidity smart contract example for implementing a deflationary token model similar to BEEF, where tokens are burned over time to reduce supply.
Generated: DETERMINISTIC_0d01a80fba20bb86
Batch ID: 20250612_153420
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

contract DeflationaryToken is ERC20, Ownable {
    uint256 public constant BURN_RATE = 100; // 1% burn rate (100 basis points)
    uint256 public constant BASIS_POINTS = 10000; // 100% in basis points
    address public constant BURN_ADDRESS = address(0x000000000000000000000000000000000000dEaD);

    event TokensBurned(address indexed from, uint256 amount);

    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply
    ) ERC20(name, symbol) {
        _mint(msg.sender, initialSupply);
    }

    function transfer(address recipient, uint256 amount) public override returns (bool) {
        uint256 burnAmount = (amount * BURN_RATE) / BASIS_POINTS;
        uint256 transferAmount = amount - burnAmount;

        _burn(msg.sender, burnAmount);
        _transfer(msg.sender, recipient, transferAmount);

        emit TokensBurned(msg.sender, burnAmount);
        return true;
    }

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override returns (bool) {
        uint256 burnAmount = (amount * BURN_RATE) / BASIS_POINTS;
        uint256 transferAmount = amount - burnAmount;

        _burn(sender, burnAmount);
        _transfer(sender, recipient, transferAmount);

        uint256 currentAllowance = allowance(sender, msg.sender);
        require(currentAllowance >= amount, "ERC20: transfer amount exceeds allowance");
        _approve(sender, msg.sender, currentAllowance - amount);

        emit TokensBurned(sender, burnAmount);
        return true;
    }

    // Owner can mint additional tokens if needed
    function mint(address account, uint256 amount) public onlyOwner {
        _mint(account, amount);
    }
}
```
