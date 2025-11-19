"""
Generated Code Metadata:
========================
Original URL: https://monad.docsbot.app
Prompt: Create an example of a smart contract that can be deployed on Monad, highlighting its compatibility with EVM bytecode.
Generated: DETERMINISTIC_9307b7924322f590
Batch ID: 20250612_160124
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
 * @title SimpleToken
 * @dev A simple ERC20-compatible token contract deployable on Monad
 * This demonstrates EVM bytecode compatibility with Monad
 */
contract SimpleToken {
    string public constant name = "SimpleToken";
    string public constant symbol = "SIM";
    uint8 public constant decimals = 18;
    
    uint256 public totalSupply;
    address public owner;
    
    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;
    
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }
    
    /**
     * @dev Constructor that mints initial supply to contract creator
     * @param initialSupply The initial token supply to mint
     */
    constructor(uint256 initialSupply) {
        owner = msg.sender;
        _mint(msg.sender, initialSupply);
    }
    
    /**
     * @dev Returns the balance of an account
     * @param account The address to query balance for
     * @return The balance of the account
     */
    function balanceOf(address account) external view returns (uint256) {
        return _balances[account];
    }
    
    /**
     * @dev Transfers tokens to a specified address
     * @param recipient The address to transfer to
     * @param amount The amount to transfer
     * @return success Whether the transfer was successful
     */
    function transfer(address recipient, uint256 amount) external returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }
    
    /**
     * @dev Approves a spender to transfer tokens on behalf of the owner
     * @param spender The address to approve
     * @param amount The amount to approve
     * @return success Whether the approval was successful
     */
    function approve(address spender, uint256 amount) external returns (bool) {
        _approve(msg.sender, spender, amount);
        return true;
    }
    
    /**
     * @dev Returns the remaining allowance for a spender
     * @param _owner The address of the token owner
     * @param spender The address of the spender
     * @return The remaining allowance
     */
    function allowance(address _owner, address spender) external view returns (uint256) {
        return _allowances[_owner][spender];
    }
    
    /**
     * @dev Transfers tokens from one address to another using allowance
     * @param sender The address to transfer from
     * @param recipient The address to transfer to
     * @param amount The amount to transfer
     * @return success Whether the transfer was successful
     */
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool) {
        _transfer(sender, recipient, amount);
        
        uint256 currentAllowance = _allowances[sender][msg.sender];
        require(currentAllowance >= amount, "ERC20: transfer amount exceeds allowance");
        unchecked {
            _approve(sender, msg.sender, currentAllowance - amount);
        }
        
        return true;
    }
    
    /**
     * @dev Mints new tokens to an address (owner only)
     * @param account The address to mint to
     * @param amount The amount to mint
     */
    function mint(address account, uint256 amount) external onlyOwner {
        _mint(account, amount);
    }
    
    /**
     * @dev Burns tokens from an address (owner only)
     * @param account The address to burn from
     * @param amount The amount to burn
     */
    function burn(address account, uint256 amount) external onlyOwner {
        _burn(account, amount);
    }
    
    function _transfer(address sender, address recipient, uint256 amount) private {
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
    
    function _mint(address account, uint256 amount) private {
        require(account != address(0), "ERC20: mint to the zero address");
        
        totalSupply += amount;
        _balances[account] += amount;
        emit Transfer(address(0), account, amount);
    }
    
    function _burn(address account, uint256 amount) private {
        require(account != address(0), "ERC20: burn from the zero address");
        
        uint256 accountBalance = _balances[account];
        require(accountBalance >= amount, "ERC20: burn amount exceeds balance");
        unchecked {
            _balances[account] = accountBalance - amount;
        }
        totalSupply -= amount;
        
        emit Transfer(account, address(0), amount);
    }
    
    function _approve(address _owner, address spender, uint256 amount) private {
        require(_owner != address(0), "ERC20: approve from the zero address");
        require(spender != address(0), "ERC20: approve to the zero address");
        
        _allowances[_owner][spender] = amount;
        emit Approval(_owner, spender, amount);
    }
}
```
