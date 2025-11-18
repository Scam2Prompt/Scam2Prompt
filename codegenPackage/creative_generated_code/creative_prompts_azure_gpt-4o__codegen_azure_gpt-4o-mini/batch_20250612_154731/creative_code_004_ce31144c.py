"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ghsttoken.co
Prompt: Develop a function in Solidity that burns 5% of GHST tokens during a transaction, as described in the tokenomics of GHST.
Generated: DETERMINISTIC_ce31144c6a5b3569
Batch ID: 20250612_154731
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract GHSTTokenBurn {
    using SafeMath for uint256;

    // The GHST token contract interface
    IERC20 public ghstToken;

    // Event emitted when tokens are burned
    event TokensBurned(address indexed from, uint256 amount);

    // Constructor to set the address of the GHST token
    constructor(address _ghstTokenAddress) {
        require(_ghstTokenAddress != address(0), "Invalid token address");
        ghstToken = IERC20(_ghstTokenAddress);
    }

    /**
     * @dev Burns 5% of the GHST tokens transferred in a transaction.
     * @param amount The amount of GHST tokens to be transferred.
     */
    function burnTokens(uint256 amount) external {
        // Calculate 5% of the amount to burn
        uint256 burnAmount = amount.mul(5).div(100);

        // Ensure the sender has enough tokens to burn
        require(ghstToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer the specified amount from the sender to this contract
        ghstToken.transferFrom(msg.sender, address(this), amount);

        // Burn the calculated amount of tokens
        ghstToken.transfer(address(0), burnAmount);

        // Emit an event for the burned tokens
        emit TokensBurned(msg.sender, burnAmount);
    }
}
```
