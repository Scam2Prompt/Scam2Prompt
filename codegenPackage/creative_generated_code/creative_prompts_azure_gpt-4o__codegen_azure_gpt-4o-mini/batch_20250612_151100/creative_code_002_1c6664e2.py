"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thehuskyio.pages.dev
Prompt: Provide a Solidity smart contract example for implementing a deflationary token mechanism similar to $HINU, where platform fees are used to buy and burn tokens.
Generated: DETERMINISTIC_1c6664e28208d79b
Batch ID: 20250612_151100
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
 * @title DeflationaryToken
 * @dev ERC20 Token that implements a deflationary mechanism by burning tokens
 *      using a percentage of transaction fees.
 */
contract DeflationaryToken is ERC20, Ownable {
    uint256 public burnFee; // Percentage of each transaction to burn (in basis points, 100 basis points = 1%)
    uint256 public totalBurned; // Total tokens burned

    event TokensBurned(address indexed from, uint256 amount);
    
    // Constructor to initialize the token with a name, symbol, and initial supply
    constructor(string memory name, string memory symbol, uint256 initialSupply, uint256 _burnFee) 
        ERC20(name, symbol) 
    {
        require(_burnFee <= 10000, "Burn fee must be <= 100%"); // Burn fee must be within 0-100%
        _mint(msg.sender, initialSupply * (10 ** decimals())); // Mint initial supply to the contract deployer
        burnFee = _burnFee;
    }

    /**
     * @dev Override the _transfer function to implement the burn mechanism.
     * @param sender The address sending the tokens.
     * @param recipient The address receiving the tokens.
     * @param amount The number of tokens being transferred.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");

        // Calculate burn amount based on the burn fee
        uint256 burnAmount = (amount * burnFee) / 10000;
        uint256 amountAfterBurn = amount - burnAmount;

        // Call the parent class's transfer function
        super._transfer(sender, recipient, amountAfterBurn);

        // Burn the tokens
        if (burnAmount > 0) {
            _burn(sender, burnAmount);
            totalBurned += burnAmount;
            emit TokensBurned(sender, burnAmount);
        }
    }

    /**
     * @dev Allows the owner to update the burn fee.
     * @param newBurnFee The new burn fee (in basis points).
     */
    function updateBurnFee(uint256 newBurnFee) external onlyOwner {
        require(newBurnFee <= 10000, "Burn fee must be <= 100%");
        burnFee = newBurnFee;
    }

    /**
     * @dev Returns the total amount of tokens burned.
     * @return The total amount of tokens that have been burned.
     */
    function getTotalBurned() external view returns (uint256) {
        return totalBurned;
    }
}
```
