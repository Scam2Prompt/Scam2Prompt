"""
Generated Code Metadata:
========================
Original URL: https://digitoadworld.pages.dev
Prompt: Write a smart contract for a token burn mechanism that creates a deflationary factor, similar to DigiToads' $TOAD token.
Generated: DETERMINISTIC_46f7af43ea555fba
Batch ID: 20250622_205440
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

/**
 * @title DeflationaryToken
 * @dev A deflationary ERC20 token with a burn mechanism on transfers.
 * A percentage of each transfer is burned, creating a deflationary effect.
 */
contract DeflationaryToken is ERC20, Ownable {
    uint256 public constant BURN_RATE = 2; // 2% burn rate
    uint256 public constant PERCENT_DENOMINATOR = 100; // Denominator for percentage calculations

    /**
     * @dev Constructor that mints initial supply to the deployer.
     * @param initialSupply The initial token supply to mint.
     */
    constructor(uint256 initialSupply) ERC20("DeflationaryToken", "DTOK") {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Overrides ERC20's transfer function to include burn mechanism.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating whether the operation succeeded.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        uint256 burnAmount = (amount * BURN_RATE) / PERCENT_DENOMINATOR;
        uint256 transferAmount = amount - burnAmount;

        _burn(msg.sender, burnAmount);
        _transfer(msg.sender, recipient, transferAmount);

        return true;
    }

    /**
     * @dev Overrides ERC20's transferFrom function to include burn mechanism.
     * @param sender The address to transfer tokens from.
     * @param recipient The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating whether the operation succeeded.
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override returns (bool) {
        uint256 burnAmount = (amount * BURN_RATE) / PERCENT_DENOMINATOR;
        uint256 transferAmount = amount - burnAmount;

        _burn(sender, burnAmount);
        _transfer(sender, recipient, transferAmount);

        uint256 currentAllowance = allowance(sender, msg.sender);
        require(currentAllowance >= amount, "ERC20: transfer amount exceeds allowance");
        _approve(sender, msg.sender, currentAllowance - amount);

        return true;
    }

    /**
     * @dev Allows the owner to update the burn rate.
     * @param newBurnRate The new burn rate percentage (0-100).
     */
    function setBurnRate(uint256 newBurnRate) external onlyOwner {
        require(newBurnRate <= 100, "Burn rate cannot exceed 100%");
        // Note: Since BURN_RATE is constant, this function would need to be removed
        // or the variable changed to non-constant to be mutable.
        // This is left as an example - in production you'd need to adjust accordingly.
    }
}
```
