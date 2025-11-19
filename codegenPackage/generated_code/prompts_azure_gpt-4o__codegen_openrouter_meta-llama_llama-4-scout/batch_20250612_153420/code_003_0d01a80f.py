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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title DeflationaryToken
 * @author [Your Name]
 * @notice A deflationary token model similar to BEEF, where tokens are burned over time to reduce supply.
 */
contract DeflationaryToken is ERC20, ERC20Burnable, ReentrancyGuard {
    // Token burn rate per second (18 decimals for precision)
    uint256 public burnRate;

    // Timestamp of last burn
    uint256 public lastBurnTimestamp;

    /**
     * @notice Constructor for DeflationaryToken
     * @param name Token name
     * @param symbol Token symbol
     * @param initialSupply Initial token supply
     * @param burnRate_ Token burn rate per second (18 decimals for precision)
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        uint256 burnRate_
    ) ERC20(name, symbol) {
        // Mint initial supply to contract deployer
        _mint(msg.sender, initialSupply);

        // Initialize burn rate and last burn timestamp
        burnRate = burnRate_;
        lastBurnTimestamp = block.timestamp;
    }

    /**
     * @notice Burns tokens from the contract's own balance over time
     */
    function burnTokens() public nonReentrant {
        // Calculate time elapsed since last burn
        uint256 timeElapsed = block.timestamp - lastBurnTimestamp;

        // Calculate tokens to burn based on elapsed time and burn rate
        uint256 tokensToBurn = (timeElapsed * burnRate) / 1e18;

        // If tokens to burn is greater than 0, burn tokens and update last burn timestamp
        if (tokensToBurn > 0) {
            // Burn tokens from contract's own balance
            _burn(address(this), tokensToBurn);

            // Update last burn timestamp
            lastBurnTimestamp = block.timestamp;
        }
    }

    /**
     * @notice Transfers tokens and burns a percentage of the transferred amount
     * @param to Recipient address
     * @param amount Amount to transfer
     * @return bool Success status
     */
    function transfer(address to, uint256 amount) public override returns (bool) {
        // Calculate tokens to burn based on transfer amount and burn rate
        uint256 tokensToBurn = (amount * burnRate) / 1e18;

        // Transfer tokens and burn a percentage of the transferred amount
        _transfer(msg.sender, to, amount - tokensToBurn);
        _burn(msg.sender, tokensToBurn);

        return true;
    }

    /**
     * @notice Transfers tokens from one address to another and burns a percentage of the transferred amount
     * @param from Sender address
     * @param to Recipient address
     * @param amount Amount to transfer
     * @return bool Success status
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public override returns (bool) {
        // Calculate tokens to burn based on transfer amount and burn rate
        uint256 tokensToBurn = (amount * burnRate) / 1e18;

        // Transfer tokens and burn a percentage of the transferred amount
        _transfer(from, to, amount - tokensToBurn);
        _burn(from, tokensToBurn);

        // Reduce allowance
        _approve(
            from,
            msg.sender,
            allowance(from, msg.sender) - (amount - tokensToBurn) - tokensToBurn
        );

        return true;
    }
}
```
