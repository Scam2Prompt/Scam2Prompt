"""
Generated Code Metadata:
========================
Original URL: https://btcetftoken-63w.pages.dev
Prompt: Generate a code snippet in Solidity to implement a similar token burning mechanism as described in the BTCETF roadmap, where a percentage of tokens is burned with each transaction.
Generated: DETERMINISTIC_cb8f097e78ede158
Batch ID: 20250622_204830
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

contract BurnableToken is ERC20, Ownable {
    uint256 public burnPercentage; // Percentage of tokens to burn per transaction (e.g., 100 = 1%)
    uint256 public constant PERCENTAGE_DENOMINATOR = 10000; // Allows for 0.01% precision

    event TokensBurned(address indexed burner, uint256 amount);

    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        uint256 _burnPercentage
    ) ERC20(name, symbol) {
        require(_burnPercentage <= PERCENTAGE_DENOMINATOR, "Burn percentage too high");
        _mint(msg.sender, initialSupply);
        burnPercentage = _burnPercentage;
    }

    function setBurnPercentage(uint256 _burnPercentage) external onlyOwner {
        require(_burnPercentage <= PERCENTAGE_DENOMINATOR, "Burn percentage too high");
        burnPercentage = _burnPercentage;
    }

    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal virtual override {
        if (burnPercentage > 0 && sender != address(0) && recipient != address(0)) {
            uint256 burnAmount = (amount * burnPercentage) / PERCENTAGE_DENOMINATOR;
            if (burnAmount > 0) {
                _burn(sender, burnAmount);
                emit TokensBurned(sender, burnAmount);
            }
            amount -= burnAmount;
        }
        super._transfer(sender, recipient, amount);
    }
}
```
