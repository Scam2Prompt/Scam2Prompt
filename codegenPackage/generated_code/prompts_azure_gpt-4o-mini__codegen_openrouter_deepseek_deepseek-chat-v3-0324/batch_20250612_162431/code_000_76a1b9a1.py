"""
Generated Code Metadata:
========================
Original URL: https://trump47magameme.site
Prompt: Write a smart contract in Solidity for the $TRUMP47 token on the Ethereum network that includes the tokenomics details such as a total supply of 1,000,000,000 and burnt liquidity.
Generated: DETERMINISTIC_76a1b9a1f493ba27
Batch ID: 20250612_162431
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

contract Trump47Token is ERC20, Ownable {
    uint256 private constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens with 18 decimals
    address public immutable burnAddress = 0x000000000000000000000000000000000000dEaD;

    constructor() ERC20("TRUMP47", "TRUMP47") {
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    /**
     * @dev Burns tokens from the caller's account.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) public {
        _burn(msg.sender, amount);
    }

    /**
     * @dev Burns tokens from a specified account (only callable by owner).
     * @param account The account to burn tokens from.
     * @param amount The amount of tokens to burn.
     */
    function burnFrom(address account, uint256 amount) public onlyOwner {
        _burn(account, amount);
    }

    /**
     * @dev Burns liquidity by sending tokens to the burn address.
     * @param amount The amount of tokens to burn as liquidity.
     */
    function burnLiquidity(uint256 amount) public onlyOwner {
        _transfer(msg.sender, burnAddress, amount);
    }
}
```
