"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeicrx6mxjdmgvh7372dgpwudwaunxrrcmmzyotodztwlzppzgiu5xm.ipfs.dweb.link
Prompt: Generate a smart contract in Solidity for a meme token similar to ANDY, using the contract address 0x18A8BD1fe17A1BB9FFB39eCD83E9489cfD17a022 as a reference.
Generated: DETERMINISTIC_114c9ee04055b899
Batch ID: 20250612_164305
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

// Importing the ERC20 interface and OpenZeppelin's Ownable contract
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// MemeToken is an ERC20 token contract resembling a meme token
contract MemeToken is IERC20, Ownable {
    using SafeMath for uint256;

    // Token parameters
    string public name = "MemeToken";      // Name of the token
    string public symbol = "MEME";          // Symbol of the token
    uint8 public decimals = 18;              // Decimals for the token
    uint256 private _totalSupply;            // Total supply of the token

    // Mapping from addresses to their balances
    mapping(address => uint256) private _balances;

    // Mapping from addresses to their allowances
    mapping(address => mapping(address => uint256)) private _allowances;

    // Events for Transfer and Approval
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Constructor to set the total supply of the token
    constructor(uint256 initialSupply) {
        _totalSupply = initialSupply * 10 ** uint256(decimals);
        _balances[msg.sender] = _totalSupply; // Assign the total supply to the contract's creator
        emit Transfer(address(0), msg.sender, _totalSupply); // Emit transfer event for the initial supply
    }

    // Returns the total supply of the token
    function totalSupply() external view override returns (uint256) {
        return _totalSupply;
    }

    // Returns the balance of the specified address
    function balanceOf(address account) external view override returns (uint256) {
        return _balances[account];
    }

    // Transfers tokens to the specified address
    function transfer(address recipient, uint256 amount) external override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(amount <= _balances[msg.sender], "Insufficient balance");

        _balances[msg.sender] = _balances[msg.sender].sub(amount); // Deduct tokens from sender
        _balances[recipient] = _balances[recipient].add(amount); // Add tokens to recipient
        emit Transfer(msg.sender, recipient, amount); // Emit transfer event
        return true;
    }

    // Allows an address to spend a specified amount of tokens on behalf of the caller
    function approve(address spender, uint256 amount) external override returns (bool) {
        require(spender != address(0), "Approval to the zero address is not allowed");

        _allowances[msg.sender][spender] = amount; // Set allowance
        emit Approval(msg.sender, spender, amount); // Emit approval event
        return true;
    }

    // Returns the allowance of a spender for a specified owner
    function allowance(address owner, address spender) external view override returns (uint256) {
        return _allowances[owner][spender];
    }

    // Transfers tokens from one address to another on behalf of a third-party spender
    function transferFrom(address sender, address recipient, uint256 amount) external override returns (bool) {
        require(sender != address(0), "Transfer from the zero address is not allowed");
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(amount <= _balances[sender], "Insufficient balance");
        require(amount <= _allowances[sender][msg.sender], "Transfer amount exceeds allowance");

        _balances[sender] = _balances[sender].sub(amount); // Deduct tokens from sender
        _balances[recipient] = _balances[recipient].add(amount); // Add tokens to recipient
        _allowances[sender][msg.sender] = _allowances[sender][msg.sender].sub(amount); // Deduct allowance
        emit Transfer(sender, recipient, amount); // Emit transfer event
        return true;
    }
}
```
