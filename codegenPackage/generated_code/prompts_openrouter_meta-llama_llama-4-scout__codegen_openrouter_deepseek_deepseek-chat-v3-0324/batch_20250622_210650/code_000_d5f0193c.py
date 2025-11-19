"""
Generated Code Metadata:
========================
Original URL: https://powag.ch
Prompt: "Write a smart contract for a blockchain-based solution using Solidity, incorporating the concepts of proof-of-concept and full stack development."
Generated: DETERMINISTIC_d5f0193c99f11641
Batch ID: 20250622_210650
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
 * @title ProofOfConceptToken
 * @dev A simple ERC20 token implementation with additional features
 *      demonstrating blockchain proof-of-concept and full stack integration
 */
contract ProofOfConceptToken {
    // Token metadata
    string public constant name = "ProofOfConceptToken";
    string public constant symbol = "POC";
    uint8 public constant decimals = 18;
    
    // Total supply
    uint256 private _totalSupply;
    
    // Balances mapping
    mapping(address => uint256) private _balances;
    
    // Allowances mapping
    mapping(address => mapping(address => uint256)) private _allowances;
    
    // Owner address
    address private _owner;
    
    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);
    
    /**
     * @dev Throws if called by any account other than the owner.
     */
    modifier onlyOwner() {
        require(msg.sender == _owner, "Ownable: caller is not the owner");
        _;
    }
    
    /**
     * @dev Constructor that mints initial supply to the contract creator
     */
    constructor(uint256 initialSupply) {
        _owner = msg.sender;
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
     */
    function balanceOf(address account) public view returns (uint256) {
        return _balances[account];
    }
    
    /**
     * @dev Transfers tokens to a specified address
     */
    function transfer(address recipient, uint256 amount) public returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }
    
    /**
     * @dev Returns the allowance granted to spender by owner
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return _allowances[owner][spender];
    }
    
    /**
     * @dev Approves the specified address to spend the specified amount of tokens
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        _approve(msg.sender, spender, amount);
        return true;
    }
    
    /**
     * @dev Transfers tokens from one address to another using allowance
     */
    function transferFrom(address sender, address recipient, uint256 amount) public returns (bool) {
        _transfer(sender, recipient, amount);
        
        uint256 currentAllowance = _allowances[sender][msg.sender];
        require(currentAllowance >= amount, "ERC20: transfer amount exceeds allowance");
        unchecked {
            _approve(sender, msg.sender, currentAllowance - amount);
        }
        
        return true;
    }
    
    /**
     * @dev Increases the allowance granted to spender by owner
     */
    function increaseAllowance(address spender, uint256 addedValue) public returns (bool) {
        _approve(msg.sender, spender, _allowances[msg.sender][spender] + addedValue);
        return true;
    }
    
    /**
     * @dev Decreases the allowance granted to spender by owner
     */
    function decreaseAllowance(address spender, uint256 subtractedValue) public returns (bool) {
        uint256 currentAllowance = _allowances[msg.sender][spender];
        require(currentAllowance >= subtractedValue, "ERC20: decreased allowance below zero");
        unchecked {
            _approve(msg.sender, spender, currentAllowance - subtractedValue);
        }
        
        return true;
    }
    
    /**
     * @dev Mints new tokens to the specified address
     * Only callable by owner
     */
    function mint(address account, uint256 amount) public onlyOwner {
        _mint(account, amount);
    }
    
    /**
     * @dev Burns tokens from the specified address
     */
    function burn(address account, uint256 amount) public {
        require(account == msg.sender || _allowances[account][msg.sender] >= amount, "ERC20: burn amount exceeds allowance");
        
        uint256 accountBalance = _balances[account];
        require(accountBalance >= amount, "ERC20: burn amount exceeds balance");
        unchecked {
            _balances[account] = accountBalance - amount;
        }
        _totalSupply -= amount;
        
        emit Transfer(account, address(0), amount);
    }
    
    /**
     * @dev Transfers ownership to a new account
     * Only callable by owner
     */
    function transferOwnership(address newOwner) public onlyOwner {
        require(newOwner != address(0), "Ownable: new owner is the zero address");
        emit OwnershipTransferred(_owner, newOwner);
        _owner = newOwner;
    }
    
    /**
     * @dev Returns the address of the current owner
     */
    function owner() public view returns (address) {
        return _owner;
    }
    
    /**
     * @dev Internal function to transfer tokens
     */
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");
        
        uint256 senderBalance = _balances[sender];
        require(senderBalance >= amount, "ERC20: transfer amount exceeds balance");
        unchecked {
            _balances[sender] = senderBalance - amount;
        }
        _balances[recipient] += amount;
        
        emit Transfer(sender, recipient, amount);
    }
    
    /**
     * @dev Internal function to mint tokens
     */
    function _mint(address account, uint256 amount) internal {
        require(account != address(0), "ERC20: mint to the zero address");
        
        _totalSupply += amount;
        _balances[account] += amount;
        emit Transfer(address(0), account, amount);
    }
    
    /**
     * @dev Internal function to approve allowance
     */
    function _approve(address owner, address spender, uint256 amount) internal {
        require(owner != address(0), "ERC20: approve from the zero address");
        require(spender != address(0), "ERC20: approve to the zero address");
        
        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }
}
```
