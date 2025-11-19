"""
Generated Code Metadata:
========================
Original URL: https://ethereum.com.tr
Prompt: Generate Solidity code for a decentralized application (ĐApp) that utilizes Ethereum's "kripto yakıt" concept to manage energy credits, inspired by the analogy of Ethereum as "petrol" from ethereum.com.tr.
Generated: DETERMINISTIC_1d19e4371bce1f92
Batch ID: 20250612_151308
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

/**
 * @title EnergyCreditToken
 * @dev A decentralized application for managing energy credits using Ethereum's "kripto yakıt" concept
 */
contract EnergyCreditToken {
    // Token details
    string public constant name = "Energy Credit Token";
    string public constant symbol = "ECT";
    uint8 public constant decimals = 18;
    
    // Total supply of energy credits
    uint256 private _totalSupply;
    
    // Mapping of addresses to their token balances
    mapping(address => uint256) private _balances;
    
    // Mapping of addresses to allowances
    mapping(address => mapping(address => uint256)) private _allowances;
    
    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event EnergyProduced(address indexed producer, uint256 amount);
    event EnergyConsumed(address indexed consumer, uint256 amount);
    
    /**
     * @dev Constructor that mints initial supply to contract creator
     * @param initialSupply The initial supply of energy credits
     */
    constructor(uint256 initialSupply) {
        _mint(msg.sender, initialSupply);
    }
    
    /**
     * @dev Returns the total token supply
     */
    function totalSupply() public view returns (uint256) {
        return _totalSupply;
    }
    
    /**
     * @dev Returns the token balance of specified account
     * @param account The address to query balance for
     */
    function balanceOf(address account) public view returns (uint256) {
        return _balances[account];
    }
    
    /**
     * @dev Transfers tokens to a specified address
     * @param recipient The address to transfer to
     * @param amount The amount to transfer
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }
    
    /**
     * @dev Returns remaining allowance for spender
     * @param owner The address that owns the tokens
     * @param spender The address allowed to spend the tokens
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return _allowances[owner][spender];
    }
    
    /**
     * @dev Approves spender to transfer tokens on behalf of owner
     * @param spender The address allowed to spend the tokens
     * @param amount The maximum amount allowed to spend
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        _approve(msg.sender, spender, amount);
        return true;
    }
    
    /**
     * @dev Transfers tokens from one address to another using allowance
     * @param sender The address to transfer from
     * @param recipient The address to transfer to
     * @param amount The amount to transfer
     */
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        _transfer(sender, recipient, amount);
        
        uint256 currentAllowance = _allowances[sender][msg.sender];
        require(currentAllowance >= amount, "EnergyCreditToken: transfer amount exceeds allowance");
        unchecked {
            _approve(sender, msg.sender, currentAllowance - amount);
        }
        
        return true;
    }
    
    /**
     * @dev Increases the allowance granted to spender
     * @param spender The address allowed to spend the tokens
     * @param addedValue The additional amount to allow
     */
    function increaseAllowance(address spender, uint256 addedValue) public returns (bool) {
        _approve(msg.sender, spender, _allowances[msg.sender][spender] + addedValue);
        return true;
    }
    
    /**
     * @dev Decreases the allowance granted to spender
     * @param spender The address allowed to spend the tokens
     * @param subtractedValue The amount to subtract from allowance
     */
    function decreaseAllowance(address spender, uint256 subtractedValue) public returns (bool) {
        uint256 currentAllowance = _allowances[msg.sender][spender];
        require(currentAllowance >= subtractedValue, "EnergyCreditToken: decreased allowance below zero");
        unchecked {
            _approve(msg.sender, spender, currentAllowance - subtractedValue);
        }
        
        return true;
    }
    
    /**
     * @dev Internal function to transfer tokens
     * @param sender The address to transfer from
     * @param recipient The address to transfer to
     * @param amount The amount to transfer
     */
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "EnergyCreditToken: transfer from the zero address");
        require(recipient != address(0), "EnergyCreditToken: transfer to the zero address");
        
        uint256 senderBalance = _balances[sender];
        require(senderBalance >= amount, "EnergyCreditToken: transfer amount exceeds balance");
        unchecked {
            _balances[sender] = senderBalance - amount;
        }
        _balances[recipient] += amount;
        
        emit Transfer(sender, recipient, amount);
    }
    
    /**
     * @dev Internal function to mint tokens
     * @param account The address to mint to
     * @param amount The amount to mint
     */
    function _mint(address account, uint256 amount) internal {
        require(account != address(0), "EnergyCreditToken: mint to the zero address");
        
        _totalSupply += amount;
        _balances[account] += amount;
        emit Transfer(address(0), account, amount);
    }
    
    /**
     * @dev Internal function to approve spending
     * @param owner The address that owns the tokens
     * @param spender The address allowed to spend the tokens
     * @param amount The maximum amount allowed to spend
     */
    function _approve(address owner, address spender, uint256 amount) internal {
        require(owner != address(0), "EnergyCreditToken: approve from the zero address");
        require(spender != address(0), "EnergyCreditToken: approve to the zero address");
        
        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }
    
    /**
     * @dev Function to produce energy credits (mint tokens)
     * @param amount The amount of energy credits produced
     */
    function produceEnergy(uint256 amount) public {
        _mint(msg.sender, amount);
        emit EnergyProduced(msg.sender, amount);
    }
    
    /**
     * @dev Function to consume energy credits (burn tokens)
     * @param amount The amount of energy credits consumed
     */
    function consumeEnergy(uint256 amount) public {
        uint256 accountBalance = _balances[msg.sender];
        require(accountBalance >= amount, "EnergyCreditToken: burn amount exceeds balance");
        unchecked {
            _balances[msg.sender] = accountBalance - amount;
        }
        _totalSupply -= amount;
        
        emit Transfer(msg.sender, address(0), amount);
        emit EnergyConsumed(msg.sender, amount);
    }
}
```
