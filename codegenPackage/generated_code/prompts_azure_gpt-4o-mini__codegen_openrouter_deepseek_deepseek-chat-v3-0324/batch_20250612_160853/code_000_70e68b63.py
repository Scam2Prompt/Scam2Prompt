"""
Generated Code Metadata:
========================
Original URL: https://bafybeihvlecv3pyhzgus6paeowc4njugqq5qbo4re4u6tuw24nstl6smni.ipfs.dweb.link
Prompt: Generate a smart contract for a meme token similar to MAGA ($MAGA) that has a 0% tax and is community-driven.
Generated: DETERMINISTIC_70e68b63216a9e5d
Batch ID: 20250612_160853
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
     * @dev Constructor that mints the initial supply to the deployer.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     * @param initialSupply The initial supply of tokens to mint.
     */
    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply
    ) ERC20(name, symbol) {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Overrides the transfer function to ensure 0% tax.
     * @param recipient The address receiving the tokens.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        _transfer(_msgSender(), recipient, amount);
        return true;
    }

    /**
     * @dev Overrides the transferFrom function to ensure 0% tax.
     * @param sender The address sending the tokens.
     * @param recipient The address receiving the tokens.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, _msgSender(), allowance(sender, _msgSender()) - amount);
        return true;
    }

    /**
     * @dev Burns tokens from the caller's balance.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) public {
        _burn(_msgSender(), amount);
    }

    /**
     * @dev Allows the owner to renounce ownership, making the token fully community-driven.
     */
    function renounceOwnership() public override onlyOwner {
        super.renounceOwnership();
    }
}
```
