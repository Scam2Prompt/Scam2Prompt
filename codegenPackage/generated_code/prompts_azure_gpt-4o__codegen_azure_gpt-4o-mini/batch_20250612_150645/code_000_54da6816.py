"""
Generated Code Metadata:
========================
Original URL: https://claim-pandoshi.web.app
Prompt: Write a smart contract in Solidity for a deflationary token with a buy-and-burn mechanism, similar to the PAMBO token described in the Pandoshi ecosystem.
Generated: DETERMINISTIC_54da6816a0793bf1
Batch ID: 20250612_150645
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
 * @title DeflationaryToken
 * @dev A deflationary ERC20 token with a buy-and-burn mechanism.
 */
contract DeflationaryToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Burn rate in percentage (e.g., 2 means 2%)
    uint256 public burnRate;
    // Total tokens burned
    uint256 public totalBurned;

    // Events
    event TokensBurned(address indexed burner, uint256 amount);
    
    /**
     * @dev Constructor to initialize the token with a name, symbol, and initial supply.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     * @param initialSupply The initial supply of the token.
     * @param _burnRate The burn rate in percentage.
     */
    constructor(string memory name, string memory symbol, uint256 initialSupply, uint256 _burnRate) 
        ERC20(name, symbol) 
    {
        require(_burnRate <= 100, "Burn rate must be between 0 and 100");
        _mint(msg.sender, initialSupply * (10 ** decimals()));
        burnRate = _burnRate;
    }

    /**
     * @dev Override the _transfer function to implement the buy-and-burn mechanism.
     * @param sender The address sending the tokens.
     * @param recipient The address receiving the tokens.
     * @param amount The amount of tokens to transfer.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");
        
        // Calculate burn amount
        uint256 burnAmount = amount.mul(burnRate).div(100);
        uint256 transferAmount = amount.sub(burnAmount);

        // Update total burned tokens
        totalBurned = totalBurned.add(burnAmount);

        // Burn the tokens
        _burn(sender, burnAmount);
        emit TokensBurned(sender, burnAmount);

        // Transfer the remaining tokens
        super._transfer(sender, recipient, transferAmount);
    }

    /**
     * @dev Function to update the burn rate.
     * @param newBurnRate The new burn rate in percentage.
     */
    function setBurnRate(uint256 newBurnRate) external onlyOwner {
        require(newBurnRate <= 100, "Burn rate must be between 0 and 100");
        burnRate = newBurnRate;
    }

    /**
     * @dev Function to retrieve the total amount of tokens burned.
     * @return The total amount of tokens burned.
     */
    function getTotalBurned() external view returns (uint256) {
        return totalBurned;
    }
}
```
