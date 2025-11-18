"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://website-9v1.pages.dev
Prompt: Generate code to implement a token burn policy for $PLRT tokens, ensuring organic price growth over time as described in the PLR Tokenomics.
Generated: DETERMINISTIC_14d503a88291394b
Batch ID: 20250612_154520
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title PLRToken
 * @dev Implementation of the PLRT Token with a token burn policy.
 */
contract PLRToken is ERC20, Ownable {
    // Event emitted when tokens are burned
    event TokensBurned(address indexed burner, uint256 amount);

    // Percentage of tokens to burn after each transaction (in basis points, e.g., 100 = 1%)
    uint256 public burnPercentageBasisPoints = 100; // 1%

    // Total supply cap for PLRT tokens
    uint256 public constant SUPPLY_CAP = 1_000_000 * 10 ** decimals(); // 1 million tokens

    /**
     * @dev Constructor that gives msg.sender all of existing tokens.
     */
    constructor() ERC20("PLR Token", "PLRT") {
        _mint(msg.sender, SUPPLY_CAP);
    }

    /**
     * @dev Overrides the _transfer function to implement token burn on transfer.
     * @param from Address from which tokens are transferred.
     * @param to Address to which tokens are transferred.
     * @param amount Amount of tokens to transfer.
     */
    function _transfer(address from, address to, uint256 amount) internal override {
        require(from != address(0), "PLRToken: transfer from the zero address");
        require(to != address(0), "PLRToken: transfer to the zero address");
        require(amount > 0, "PLRToken: transfer amount must be greater than zero");

        // Calculate burn amount based on burn percentage
        uint256 burnAmount = (amount * burnPercentageBasisPoints) / 10_000;
        uint256 transferAmount = amount - burnAmount;

        // Burn the tokens
        if (burnAmount > 0) {
            _burn(from, burnAmount);
            emit TokensBurned(from, burnAmount);
        }

        // Transfer the remaining tokens
        super._transfer(from, to, transferAmount);
    }

    /**
     * @dev Allows the owner to update the burn percentage.
     * @param newBurnPercentageBasisPoints New burn percentage in basis points.
     */
    function setBurnPercentage(uint256 newBurnPercentageBasisPoints) external onlyOwner {
        require(newBurnPercentageBasisPoints <= 1000, "PLRToken: burn percentage too high"); // Max 10%
        burnPercentageBasisPoints = newBurnPercentageBasisPoints;
    }

    /**
     * @dev Returns the current burn percentage.
     * @return Current burn percentage in basis points.
     */
    function getBurnPercentage() external view returns (uint256) {
        return burnPercentageBasisPoints;
    }
}
```
