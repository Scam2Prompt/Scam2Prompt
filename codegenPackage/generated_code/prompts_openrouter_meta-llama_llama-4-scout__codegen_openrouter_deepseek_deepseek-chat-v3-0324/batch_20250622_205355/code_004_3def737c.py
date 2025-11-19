"""
Generated Code Metadata:
========================
Original URL: https://arbidoge.pages.dev
Prompt: Design a simple buy, sell, and transfer contract for a meme token with no taxes, inspired by Arbidoge's contract structure.
Generated: DETERMINISTIC_3def737c1bf8df91
Batch ID: 20250622_205355
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

contract MemeToken is ERC20, Ownable {
    /**
     * @dev Constructor that mints initial supply to the deployer
     * @param name Token name
     * @param symbol Token symbol
     * @param initialSupply Initial token supply (in wei)
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply
    ) ERC20(name, symbol) {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Allows owner to mint new tokens
     * @param to Address to receive the minted tokens
     * @param amount Amount of tokens to mint (in wei)
     */
    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
    }

    /**
     * @dev Overrides transfer function to ensure no taxes/fees
     * @param recipient Address receiving tokens
     * @param amount Amount of tokens to transfer (in wei)
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
     * @dev Overrides transferFrom function to ensure no taxes/fees
     * @param sender Address sending tokens
     * @param recipient Address receiving tokens
     * @param amount Amount of tokens to transfer (in wei)
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(
            sender,
            _msgSender(),
            allowance(sender, _msgSender()) - amount
        );
        return true;
    }
}
```
