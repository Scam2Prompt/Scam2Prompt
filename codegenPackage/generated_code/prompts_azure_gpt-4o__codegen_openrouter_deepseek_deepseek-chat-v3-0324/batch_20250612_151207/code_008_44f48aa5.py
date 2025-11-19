"""
Generated Code Metadata:
========================
Original URL: https://blockchainbetsclub-ai.pages.dev
Prompt: Write a function in Solidity to burn tokens and update the circulating supply, similar to the tokenomics described for Blockchain Bets.
Generated: DETERMINISTIC_44f48aa52c57b1fd
Batch ID: 20250612_151207
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

contract BlockchainBetsToken is ERC20, Ownable {
    uint256 private _circulatingSupply;
    uint256 private _totalBurned;

    event TokensBurned(address indexed burner, uint256 amount);

    constructor(uint256 initialSupply) ERC20("Blockchain Bets Token", "BBT") {
        _mint(msg.sender, initialSupply);
        _circulatingSupply = initialSupply;
    }

    /**
     * @dev Returns the circulating supply of tokens.
     */
    function circulatingSupply() public view returns (uint256) {
        return _circulatingSupply;
    }

    /**
     * @dev Returns the total amount of tokens burned.
     */
    function totalBurned() public view returns (uint256) {
        return _totalBurned;
    }

    /**
     * @dev Burns a specific amount of tokens and updates the circulating supply.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) public {
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to burn");
        
        _burn(msg.sender, amount);
        _circulatingSupply -= amount;
        _totalBurned += amount;
        
        emit TokensBurned(msg.sender, amount);
    }

    /**
     * @dev Burns a specific amount of tokens from a specified address.
     * @param account The address to burn tokens from.
     * @param amount The amount of tokens to burn.
     */
    function burnFrom(address account, uint256 amount) public {
        uint256 currentAllowance = allowance(account, msg.sender);
        require(currentAllowance >= amount, "ERC20: burn amount exceeds allowance");
        
        _approve(account, msg.sender, currentAllowance - amount);
        _burn(account, amount);
        _circulatingSupply -= amount;
        _totalBurned += amount;
        
        emit TokensBurned(account, amount);
    }
}
```
