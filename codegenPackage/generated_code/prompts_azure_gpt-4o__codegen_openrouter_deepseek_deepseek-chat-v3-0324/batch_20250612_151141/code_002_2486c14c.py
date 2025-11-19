"""
Generated Code Metadata:
========================
Original URL: https://neirocoin.pages.dev
Prompt: Generate Solidity code for creating a token similar to $NEIRO on the Ethereum blockchain, ensuring it has no tax (0/0) and a fixed supply of 1 billion tokens, as specified in the NEIRO tokenomics.
Generated: DETERMINISTIC_2486c14c15020d0b
Batch ID: 20250612_151141
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

contract NeiroToken is ERC20, Ownable {
    uint256 private constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens with 18 decimals
    
    constructor() ERC20("Neiro Token", "NEIRO") {
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    // Override transfer functions to ensure no tax (0/0)
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        _transfer(_msgSender(), recipient, amount);
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, _msgSender(), allowance(sender, _msgSender()) - amount);
        return true;
    }

    // Disable minting function to maintain fixed supply
    function mint(address /* to */, uint256 /* amount */) public pure {
        revert("NeiroToken: Minting is disabled");
    }

    // Disable burn function to maintain fixed supply
    function burn(uint256 /* amount */) public pure {
        revert("NeiroToken: Burning is disabled");
    }
}
```
