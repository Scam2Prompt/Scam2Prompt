"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cowonbasenets.pages.dev
Prompt: What are the steps to create a cryptocurrency token with a burned liquidity feature, as seen with $COW?
Generated: DETERMINISTIC_bec61fca7c699b97
Batch ID: 20250612_163840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here's an example of an Ethereum-based ERC-20 token with a burned liquidity feature, written in Solidity:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/*
 * A basic ERC-20 token with a burned liquidity feature.
 * This contract allows for automatic burning of a percentage of every transfer.
 */

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract BurnableToken is ERC20, Ownable {
    // Percentage of the transfer amount to burn. Value in basis points (e.g., 100 = 1%).
    uint256 public burnRate = 100; // Default to 1%
    uint256 public constant BASIS_POINTS = 10000; // 100% = 10,000 basis points.

    // Constructor to initialize the token with name, symbol, and initial supply.
    constructor(uint256 initialSupply) ERC20("BurnableToken", "BTK") {
        // Mint the entire initial supply to the deployer of the contract.
        _mint(msg.sender, initialSupply);
    }

    // Function to set the burn rate. Can only be set by the owner of the contract.
    function setBurnRate(uint256 newBurnRate) external onlyOwner {
        require(newBurnRate <= BASIS_POINTS, "Burn rate must be <= 100%");
        burnRate = newBurnRate;
    }

    // Override the _transfer function to include the burn logic.
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal virtual override {
        // Calculate the amount to burn.
        uint256 burnAmount = (amount * burnRate) / BASIS_POINTS;

        // Calculate the amount to transfer to the recipient.
        uint256 sendAmount = amount - burnAmount;

        // Ensure the total amount is accounted for.
        assert(amount == sendAmount + burnAmount);

        // Burn the tokens (reduce total supply).
        if (burnAmount > 0) {
            _burn(sender, burnAmount);
        }

        // Perform the standard transfer.
        super._transfer(sender, recipient, sendAmount);
    }
}
```

### Notes on Usage:
1. Deploy the contract and specify the initial token supply (e.g., `1000000e18` for 1 million tokens with 18 decimals).
2. The owner of the contract can adjust the burn rate using `setBurnRate` in units of basis points (e.g., `100` for 1% or `500` for 5%).
3. The contract uses OpenZeppelin's standard libraries for secure and well-tested ERC-20 implementation. Install them in your project with `npm install @openzeppelin/contracts` to use this code.

Make sure to test thoroughly in a development environment like Hardhat or Truffle before deploying to a live blockchain.
