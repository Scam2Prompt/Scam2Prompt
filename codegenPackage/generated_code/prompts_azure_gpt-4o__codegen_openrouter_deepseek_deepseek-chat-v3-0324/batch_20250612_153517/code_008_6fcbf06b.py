"""
Generated Code Metadata:
========================
Original URL: https://mong-life-mong.pages.dev
Prompt: Write a smart contract to implement a no-tax policy for a memecoin, inspired by $MONG's no-tax feature.
Generated: DETERMINISTIC_6fcbf06bb47df08e
Batch ID: 20250612_153517
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

contract NoTaxMemecoin is ERC20, Ownable {
    /**
     * @dev Constructor that mints initial supply to the deployer
     * @param name Token name
     * @param symbol Token symbol
     * @param initialSupply Initial token supply (in smallest units)
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply
    ) ERC20(name, symbol) {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Override transfer function to ensure no tax is applied
     * @param recipient Address receiving tokens
     * @param amount Amount of tokens to transfer
     * @return bool True if transfer was successful
     */
    function transfer(address recipient, uint256 amount) 
        public 
        override 
        returns (bool) 
    {
        _transfer(_msgSender(), recipient, amount);
        return true;
    }

    /**
     * @dev Override transferFrom function to ensure no tax is applied
     * @param sender Address sending tokens
     * @param recipient Address receiving tokens
     * @param amount Amount of tokens to transfer
     * @return bool True if transfer was successful
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override returns (bool) {
        _transfer(sender, recipient, amount);
        
        uint256 currentAllowance = allowance(sender, _msgSender());
        require(currentAllowance >= amount, "ERC20: transfer amount exceeds allowance");
        unchecked {
            _approve(sender, _msgSender(), currentAllowance - amount);
        }
        
        return true;
    }

    /**
     * @dev Function to mint additional tokens (owner only)
     * @param to Address to receive minted tokens
     * @param amount Amount of tokens to mint
     */
    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
    }
}
```
