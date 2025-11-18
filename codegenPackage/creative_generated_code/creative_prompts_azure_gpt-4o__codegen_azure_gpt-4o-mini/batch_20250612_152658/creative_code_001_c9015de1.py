"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://thoreumdashboard.com
Prompt: Create a smart contract in Solidity that implements a token burning mechanism similar to Thoreum, where 1% of the supply is burned daily and 1% is burned on each transaction.
Generated: DETERMINISTIC_c9015de1756d6405
Batch ID: 20250612_152658
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
 * @title BurnableToken
 * @dev ERC20 Token with a burning mechanism that burns 1% of total supply daily 
 * and 1% of the transaction amount on every transfer.
 */
contract BurnableToken is ERC20, Ownable {
    // Last timestamp when burns were executed
    uint256 public lastBurnTimestamp;

    // Burn interval in seconds (1 day = 86400 seconds)
    uint256 public constant BURN_INTERVAL = 86400;

    // Event emitted when tokens are burned
    event TokensBurned(uint256 amount);

    constructor(uint256 initialSupply) ERC20("BurnableToken", "BTK") {
        require(initialSupply > 0, "Initial supply must be greater than 0");
        _mint(msg.sender, initialSupply * (10 ** decimals()));
        lastBurnTimestamp = block.timestamp;
    }

    /**
     * @dev Overrides the _transfer function to implement the burning mechanism.
     * @param sender The address sending tokens
     * @param recipient The address receiving tokens
     * @param amount The amount of tokens to be transferred
     */
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        // Require transfer amount to be greater than 0
        require(amount > 0, "Transfer amount must be greater than 0");
        
        // Perform the daily burn if the interval has elapsed
        _burnDaily();

        // Calculate the burn amount for this transaction (1% of transfer amount)
        uint256 burnAmount = amount / 100;

        // Calculate the actual amount to transfer after burning
        uint256 transferAmount = amount - burnAmount;

        // Call the parent contract's transfer function
        super._transfer(sender, recipient, transferAmount);

        // Burn the calculated amount
        _burn(sender, burnAmount);
        
        // Emit an event for the tokens burned
        emit TokensBurned(burnAmount);
    }

    /**
     * @dev Burns 1% of the total supply daily if the burn interval has elapsed.
     */
    function _burnDaily() internal {
        // Check if 24 hours have passed since the last burn
        if (block.timestamp >= lastBurnTimestamp + BURN_INTERVAL) {
            // Calculate 1% of total supply to burn
            uint256 totalSupply = totalSupply();
            uint256 dailyBurnAmount = totalSupply / 100;

            // Update last burn timestamp
            lastBurnTimestamp = block.timestamp;

            // Perform the burn
            _burn(address(this), dailyBurnAmount);
            
            // Emit event for the daily burn
            emit TokensBurned(dailyBurnAmount);
        }
    }

    /**
     * @dev Allows the owner to withdraw any ERC20 tokens accidentally sent to this contract.
     * @param tokenAddress The address of the ERC20 token contract.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(this), "Cannot withdraw native tokens");
        require(amount > 0, "Amount must be greater than 0");
        
        // Get the token contract
        ERC20 token = ERC20(tokenAddress);
        require(token.balanceOf(address(this)) >= amount, "Insufficient token balance");

        // Transfer tokens to the owner
        token.transfer(msg.sender, amount);
    }
}
```
