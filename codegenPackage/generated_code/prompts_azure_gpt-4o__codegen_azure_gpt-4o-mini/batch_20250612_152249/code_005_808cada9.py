"""
Generated Code Metadata:
========================
Original URL: https://pushd-ai.pages.dev
Prompt: Generate code for a token burn program in Solidity, ensuring unsold tokens from a presale are burned and implementing a periodic burn every three months for three years.
Generated: DETERMINISTIC_808cada97af62761
Batch ID: 20250612_152249
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title TokenBurn
 * @dev ERC20 Token with burn functionality for unsold tokens and periodic burns.
 */
contract TokenBurn is ERC20, Ownable {
    using SafeMath for uint256;

    // Timestamp for the next scheduled burn
    uint256 public nextBurnTime;
    // Duration between burns (3 months)
    uint256 public constant BURN_INTERVAL = 90 days;
    // Total number of burns scheduled (3 years)
    uint256 public constant TOTAL_BURNS = 12;
    // Counter for the number of burns executed
    uint256 public burnCount;

    // Event emitted when tokens are burned
    event TokensBurned(uint256 amount);

    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        // Initialize the next burn time to 3 months from now
        nextBurnTime = block.timestamp + BURN_INTERVAL;
        burnCount = 0;
    }

    /**
     * @dev Burns unsold tokens from the presale.
     * @param amount The amount of tokens to burn.
     */
    function burnUnsoldTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(address(this)) >= amount, "Insufficient balance to burn");

        _burn(address(this), amount);
        emit TokensBurned(amount);
    }

    /**
     * @dev Executes a periodic burn of tokens every 3 months.
     */
    function periodicBurn() external onlyOwner {
        require(burnCount < TOTAL_BURNS, "All scheduled burns have been executed");
        require(block.timestamp >= nextBurnTime, "Burn interval has not passed");

        uint256 amountToBurn = balanceOf(address(this));
        require(amountToBurn > 0, "No tokens available for burning");

        _burn(address(this), amountToBurn);
        emit TokensBurned(amountToBurn);

        // Update the next burn time and increment the burn count
        nextBurnTime = nextBurnTime.add(BURN_INTERVAL);
        burnCount++;
    }

    /**
     * @dev Allows the owner to withdraw any tokens accidentally sent to the contract.
     * @param token The address of the token to withdraw.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(this), "Cannot withdraw own tokens");
        require(IERC20(token).balanceOf(address(this)) >= amount, "Insufficient balance to withdraw");

        IERC20(token).transfer(owner(), amount);
    }
}
```
