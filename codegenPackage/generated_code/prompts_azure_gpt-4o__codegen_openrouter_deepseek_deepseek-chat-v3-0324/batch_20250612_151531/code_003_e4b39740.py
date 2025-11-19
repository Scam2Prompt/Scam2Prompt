"""
Generated Code Metadata:
========================
Original URL: https://ziber.io
Prompt: Write code in Solidity to freeze 10% of Ziber tokens for one year, ensuring they cannot be withdrawn or sold during this period. Include logic to demonstrate long-range goals to ICO investors.
Generated: DETERMINISTIC_e4b3974014314a9c
Batch ID: 20250612_151531
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

contract ZiberToken is ERC20, Ownable {
    uint256 public constant TOTAL_SUPPLY = 1000000000 * 10**18; // 1 billion tokens
    uint256 public constant FROZEN_PERCENTAGE = 10; // 10% of total supply
    uint256 public constant FREEZE_PERIOD = 365 days; // 1 year
    
    uint256 public frozenAmount;
    uint256 public freezeStartTime;
    bool public frozen;

    mapping(address => bool) private _frozenAccounts;

    event TokensFrozen(uint256 amount, uint256 duration);
    event TokensUnfrozen(uint256 amount);
    event LongTermGoals(string message);

    constructor() ERC20("Ziber Token", "ZIBER") {
        _mint(msg.sender, TOTAL_SUPPLY);
        frozenAmount = (TOTAL_SUPPLY * FROZEN_PERCENTAGE) / 100;
    }

    function freezeTokens() external onlyOwner {
        require(!frozen, "Tokens already frozen");
        freezeStartTime = block.timestamp;
        frozen = true;
        _frozenAccounts[msg.sender] = true;
        
        emit TokensFrozen(frozenAmount, FREEZE_PERIOD);
        emit LongTermGoals("10% of tokens frozen for 1 year to demonstrate long-term commitment to project stability and growth");
    }

    function unfreezeTokens() external onlyOwner {
        require(frozen, "Tokens not frozen");
        require(block.timestamp >= freezeStartTime + FREEZE_PERIOD, "Freeze period not ended");
        
        frozen = false;
        _frozenAccounts[msg.sender] = false;
        
        emit TokensUnfrozen(frozenAmount);
    }

    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal virtual override {
        super._beforeTokenTransfer(from, to, amount);
        
        if (frozen) {
            require(!_frozenAccounts[from], "Sender's tokens are frozen");
        }
    }

    function showLongTermGoals() external onlyOwner {
        emit LongTermGoals("Project roadmap includes: 1) Ecosystem expansion, 2) Partnerships, 3) Platform development, 4) Community growth");
    }
}
```
