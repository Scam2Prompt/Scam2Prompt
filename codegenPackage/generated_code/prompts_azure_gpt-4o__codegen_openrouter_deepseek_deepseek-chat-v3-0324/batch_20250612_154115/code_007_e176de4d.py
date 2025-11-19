"""
Generated Code Metadata:
========================
Original URL: https://mpeppe-in.web.app
Prompt: Write code to implement zero tax and zero fees for $MPEPE token transactions, ensuring compliance with the tokenomics outlined in the Mpeppe ecosystem.
Generated: DETERMINISTIC_e176de4d9dcf425b
Batch ID: 20250612_154115
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

contract MpepeToken is ERC20, Ownable {
    /**
     * @dev Constructor that initializes the token with initial supply
     * @param initialSupply The initial token supply to be minted
     */
    constructor(uint256 initialSupply) ERC20("Mpepe", "MPEPE") {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Overrides transfer function to implement zero tax and fees
     * @param recipient The address receiving the tokens
     * @param amount The amount of tokens to transfer
     * @return bool indicating successful transfer
     */
    function transfer(address recipient, uint256 amount) 
        public 
        virtual 
        override 
        returns (bool) 
    {
        _transfer(_msgSender(), recipient, amount);
        return true;
    }

    /**
     * @dev Overrides transferFrom function to implement zero tax and fees
     * @param sender The address sending the tokens
     * @param recipient The address receiving the tokens
     * @param amount The amount of tokens to transfer
     * @return bool indicating successful transfer
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public virtual override returns (bool) {
        _transfer(sender, recipient, amount);
        
        uint256 currentAllowance = allowance(sender, _msgSender());
        require(currentAllowance >= amount, "ERC20: transfer amount exceeds allowance");
        unchecked {
            _approve(sender, _msgSender(), currentAllowance - amount);
        }
        
        return true;
    }

    /**
     * @dev Internal transfer function without any fees or taxes
     * @param sender The address sending the tokens
     * @param recipient The address receiving the tokens
     * @param amount The amount of tokens to transfer
     */
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal virtual override {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");

        _beforeTokenTransfer(sender, recipient, amount);

        uint256 senderBalance = balanceOf(sender);
        require(senderBalance >= amount, "ERC20: transfer amount exceeds balance");
        unchecked {
            _balances[sender] = senderBalance - amount;
        }
        _balances[recipient] += amount;

        emit Transfer(sender, recipient, amount);

        _afterTokenTransfer(sender, recipient, amount);
    }
}
```
