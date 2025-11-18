"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mong-life-mong.pages.dev
Prompt: Write a smart contract to implement a no-tax policy for a memecoin, inspired by $MONG's no-tax feature.
Generated: DETERMINISTIC_6fcbf06bb47df08e
Batch ID: 20250612_153517
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
 * @title NoTaxMemecoin
 * @dev An ERC20 token with a no-tax policy for transactions.
 */
contract NoTaxMemecoin is ERC20, Ownable {
    
    // Mapping to track allowances
    mapping(address => mapping(address => uint256)) private _allowances;

    // Event for logging transfers
    event Transfer(address indexed from, address indexed to, uint256 value);

    /**
     * @dev Constructor that initializes the token with a name and symbol.
     * @param name Token name
     * @param symbol Token symbol
     * @param initialSupply Initial token supply
     */
    constructor(string memory name, string memory symbol, uint256 initialSupply) 
        ERC20(name, symbol) 
    {
        // Mint initial supply to the contract owner
        _mint(msg.sender, initialSupply * (10 ** decimals()));
    }

    /**
     * @dev Override the _transfer function to ensure no tax is applied.
     * @param sender Address of the sender
     * @param recipient Address of the recipient
     * @param amount Amount to transfer
     */
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        require(sender != address(0), "NoTaxMemecoin: transfer from the zero address");
        require(recipient != address(0), "NoTaxMemecoin: transfer to the zero address");
        require(amount > 0, "NoTaxMemecoin: transfer amount must be greater than zero");
        
        // Call the parent method to perform the transfer without tax
        super._transfer(sender, recipient, amount);

        // Emit the transfer event
        emit Transfer(sender, recipient, amount);
    }

    /**
     * @dev Override the approve function to allow for unlimited allowances.
     * @param owner Address of the token owner
     * @param spender Address of the spender
     * @param amount Amount to allocate
     * @return true if the approval was successful
     */
    function approve(address spender, uint256 amount) public virtual override returns (bool) {
        require(spender != address(0), "NoTaxMemecoin: approve to the zero address");

        _approve(_msgSender(), spender, amount);
        return true;
    }

    /**
     * @dev Internal function to set the allowance for a spender.
     * @param owner Address of the token owner
     * @param spender Address of the spender
     * @param amount Amount to allocate
     */
    function _approve(address owner, address spender, uint256 amount) internal virtual {
        require(owner != address(0), "NoTaxMemecoin: approve from the zero address");
        require(spender != address(0), "NoTaxMemecoin: approve to the zero address");

        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }

    /**
     * @dev Function to check the allowance of a spender.
     * @param owner Address of the token owner
     * @param spender Address of the spender
     * @return The allowance amount
     */
    function allowance(address owner, address spender) public view virtual override returns (uint256) {
        return _allowances[owner][spender];
    }

    /**
     * @dev Function to handle transfers on behalf of the owner.
     * @param sender Address of the token owner
     * @param recipient Address of the recipient
     * @param amount Amount to transfer
     * @return true if the transfer was successful
     */
    function transferFrom(address sender, address recipient, uint256 amount) public virtual override returns (bool) {
        require(amount <= _allowances[sender][_msgSender()], "NoTaxMemecoin: transfer amount exceeds allowance");

        // Decrease the allowance
        _allowances[sender][_msgSender()] -= amount;

        // Perform the transfer
        _transfer(sender, recipient, amount);
        return true;
    }
}
```
