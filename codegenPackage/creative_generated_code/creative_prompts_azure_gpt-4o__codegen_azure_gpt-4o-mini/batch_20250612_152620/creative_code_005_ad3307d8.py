"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rebelsatoshi-io.web.app
Prompt: Develop a Solidity function for a burn event that reduces the total supply of "$RBLZ" tokens. Ensure the function is secure and can only be executed by authorized accounts.
Generated: DETERMINISTIC_ad3307d810e9ad58
Batch ID: 20250612_152620
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title RBLZToken
 * @dev Implementation of the $RBLZ ERC20 token with a burn function
 */
contract RBLZToken is ERC20, Ownable {
    // Event emitted when tokens are burned
    event TokensBurned(address indexed account, uint256 amount);

    /**
     * @dev Constructor that gives msg.sender all initial tokens.
     * @param initialSupply The initial supply of tokens
     */
    constructor(uint256 initialSupply) ERC20("RBLZ Token", "$RBLZ") {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Function to burn a specific amount of tokens.
     * Can only be called by the owner of the contract.
     * @param amount The amount of tokens to burn
     */
    function burn(uint256 amount) external onlyOwner {
        require(amount > 0, "Burn amount must be greater than zero");
        require(amount <= balanceOf(msg.sender), "Insufficient balance to burn");

        // Burn the specified amount of tokens
        _burn(msg.sender, amount);
        
        // Emit the burn event
        emit TokensBurned(msg.sender, amount);
    }
}
```
