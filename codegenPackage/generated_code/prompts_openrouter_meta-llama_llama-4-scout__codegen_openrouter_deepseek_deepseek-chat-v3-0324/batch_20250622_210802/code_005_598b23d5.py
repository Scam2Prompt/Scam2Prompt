"""
Generated Code Metadata:
========================
Original URL: https://venom-dh8.pages.dev
Prompt: "Design a basic smart contract for a security token on the Venom network, following the guidelines and requirements of the TokenForge hackathon."
Generated: DETERMINISTIC_598b23d52bd1796d
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// SPDX-License-Identifier: MIT
pragma ton-solidity >= 0.57.0;

import "@broxus/contracts/contracts/access/Ownable.sol";
import "@broxus/contracts/contracts/utils/RandomNonce.sol";
import "@broxus/contracts/contracts/utils/CheckPubKey.sol";

/**
 * @title SecurityToken
 * @dev Implementation of a security token compliant with Venom network standards
 */
contract SecurityToken is Ownable, RandomNonce, CheckPubKey {
    string public name;
    string public symbol;
    uint8 public decimals;
    uint128 public totalSupply;
    
    mapping(address => uint128) private _balances;
    mapping(address => mapping(address => uint128)) private _allowances;
    
    event Transfer(address indexed from, address indexed to, uint128 value);
    event Approval(address indexed owner, address indexed spender, uint128 value);
    
    modifier validAddress(address _addr) {
        require(_addr != address(0), "SecurityToken: Invalid address");
        _;
    }
    
    /**
     * @dev Constructor that initializes the token contract
     * @param _name Token name
     * @param _symbol Token symbol
     * @param _decimals Number of decimals
     * @param _initialSupply Initial token supply
     * @param _owner Address of the token owner
     */
    constructor(
        string _name,
        string _symbol,
        uint8 _decimals,
        uint128 _initialSupply,
        address _owner
    ) public {
        tvm.accept();
        name = _name;
        symbol = _symbol;
        decimals = _decimals;
        totalSupply = _initialSupply;
        _balances[_owner] = _initialSupply;
        _transferOwnership(_owner);
        
        emit Transfer(address(0), _owner, _initialSupply);
    }
    
    /**
     * @dev Returns the balance of the specified address
     * @param _owner The address to query the balance of
     * @return balance The balance amount
     */
    function balanceOf(address _owner) external view returns (uint128 balance) {
        return _balances[_owner];
    }
    
    /**
     * @dev Transfer tokens to a specified address
     * @param _to The address to transfer to
     * @param _value The amount to be transferred
     */
    function transfer(address _to, uint128 _value) external validAddress(_to) {
        require(_balances[msg.sender] >= _value, "SecurityToken: Insufficient balance");
        
        _balances[msg.sender] -= _value;
        _balances[_to] += _value;
        
        emit Transfer(msg.sender, _to, _value);
    }
    
    /**
     * @dev Transfer tokens from one address to another
     * @param _from The address to transfer from
     * @param _to The address to transfer to
     * @param _value The amount to be transferred
     */
    function transferFrom(address _from, address _to, uint128 _value) external validAddress(_to) {
        require(_balances[_from] >= _value, "SecurityToken: Insufficient balance");
        require(_allowances[_from][msg.sender] >= _value, "SecurityToken: Insufficient allowance");
        
        _balances[_from] -= _value;
        _balances[_to] += _value;
        _allowances[_from][msg.sender] -= _value;
        
        emit Transfer(_from, _to, _value);
    }
    
    /**
     * @dev Approve the passed address to spend the specified amount of tokens
     * @param _spender The address which will spend the funds
     * @param _value The amount of tokens to be spent
     */
    function approve(address _spender, uint128 _value) external {
        _allowances[msg.sender][_spender] = _value;
        emit Approval(msg.sender, _spender, _value);
    }
    
    /**
     * @dev Function to check the amount of tokens that an owner allowed to a spender
     * @param _owner The address which owns the funds
     * @param _spender The address which will spend the funds
     * @return remaining Amount of tokens still available for the spender
     */
    function allowance(address _owner, address _spender) external view returns (uint128 remaining) {
        return _allowances[_owner][_spender];
    }
    
    /**
     * @dev Mint new tokens (only owner)
     * @param _amount The amount of tokens to mint
     */
    function mint(uint128 _amount) external onlyOwner {
        totalSupply += _amount;
        _balances[owner()] += _amount;
        emit Transfer(address(0), owner(), _amount);
    }
    
    /**
     * @dev Burn tokens (only owner)
     * @param _amount The amount of tokens to burn
     */
    function burn(uint128 _amount) external onlyOwner {
        require(_balances[owner()] >= _amount, "SecurityToken: Burn amount exceeds balance");
        
        totalSupply -= _amount;
        _balances[owner()] -= _amount;
        emit Transfer(owner(), address(0), _amount);
    }
    
    /**
     * @dev Freeze tokens (only owner)
     * @param _from The address to freeze tokens from
     * @param _amount The amount of tokens to freeze
     */
    function freeze(address _from, uint128 _amount) external onlyOwner validAddress(_from) {
        require(_balances[_from] >= _amount, "SecurityToken: Insufficient balance to freeze");
        
        _balances[_from] -= _amount;
        emit Transfer(_from, address(0), _amount);
    }
    
    /**
     * @dev Unfreeze tokens (only owner)
     * @param _to The address to unfreeze tokens to
     * @param _amount The amount of tokens to unfreeze
     */
    function unfreeze(address _to, uint128 _amount) external onlyOwner validAddress(_to) {
        _balances[_to] += _amount;
        emit Transfer(address(0), _to, _amount);
    }
    
    /**
     * @dev Override ownership transfer to include token balance transfer
     * @param newOwner The address to transfer ownership to
     */
    function transferOwnership(address newOwner) public override onlyOwner validAddress(newOwner) {
        uint128 ownerBalance = _balances[owner()];
        if (ownerBalance > 0) {
            _balances[newOwner] += ownerBalance;
            _balances[owner()] = 0;
            emit Transfer(owner(), newOwner, ownerBalance);
        }
        _transferOwnership(newOwner);
    }
}
```
