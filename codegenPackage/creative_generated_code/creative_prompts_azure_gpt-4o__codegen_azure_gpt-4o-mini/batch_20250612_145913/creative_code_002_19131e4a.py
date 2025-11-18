"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tenderize.xyz
Prompt: Generate code to implement a token burn mechanism for deflationary purposes, similar to Tenderize's approach of burning tokens from platform fees.
Generated: DETERMINISTIC_19131e4acf444a80
Batch ID: 20250612_145913
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

// Importing OpenZeppelin's ERC20 interface and Ownable contract for access control
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title DeflationaryToken
 * @dev Implementation of a deflationary token with a token burn mechanism.
 */
contract DeflationaryToken is IERC20, Ownable {
    string public name; // Token name
    string public symbol; // Token symbol
    uint8 public decimals; // Number of decimal places
    uint256 private _totalSupply; // Total supply of tokens

    // Mapping from address to balance and allowances
    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    // Event emitted when tokens are burned
    event TokensBurned(address indexed from, uint256 amount);

    /**
     * @dev Constructor that initializes the token's name, symbol, and total supply.
     * @param _name The name of the token.
     * @param _symbol The symbol of the token.
     * @param _initialSupply The initial supply of the token.
     */
    constructor(string memory _name, string memory _symbol, uint256 _initialSupply) {
        name = _name;
        symbol = _symbol;
        decimals = 18; // Standard for ERC20 tokens
        _totalSupply = _initialSupply * 10**uint256(decimals);
        _balances[msg.sender] = _totalSupply; // Assign initial supply to the contract owner
    }

    // ERC20 functions
    function totalSupply() external view override returns (uint256) {
        return _totalSupply;
    }

    function balanceOf(address account) external view override returns (uint256) {
        return _balances[account];
    }

    function transfer(address recipient, uint256 amount) external override returns (bool) {
        _transfer(msg.sender, recipient, amount);
        return true;
    }

    function allowance(address owner, address spender) external view override returns (uint256) {
        return _allowances[owner][spender];
    }

    function approve(address spender, uint256 amount) external override returns (bool) {
        _approve(msg.sender, spender, amount);
        return true;
    }

    function transferFrom(address sender, address recipient, uint256 amount) external override returns (bool) {
        _transfer(sender, recipient, amount);
        _approve(sender, msg.sender, _allowances[sender][msg.sender] - amount);
        return true;
    }

    // Internal functions
    function _transfer(address sender, address recipient, uint256 amount) internal {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(_balances[sender] >= amount, "Transfer amount exceeds balance");

        // Burn a percentage of the transaction amount (e.g., 2%)
        uint256 burnAmount = (amount * 2) / 100;
        uint256 sendAmount = amount - burnAmount;

        _balances[sender] -= amount;
        _balances[recipient] += sendAmount;
        _totalSupply -= burnAmount; // Reduce total supply
        emit TokensBurned(sender, burnAmount);

        emit Transfer(sender, recipient, sendAmount);
    }

    function _approve(address owner, address spender, uint256 amount) internal {
        require(owner != address(0), "Approve from the zero address");
        require(spender != address(0), "Approve to the zero address");

        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }

    /**
     * @dev Allows the owner to burn tokens directly from the contract.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) external onlyOwner {
        require(amount > 0, "Burn amount must be greater than zero");
        require(_balances[msg.sender] >= amount, "Burn amount exceeds balance");

        _balances[msg.sender] -= amount;
        _totalSupply -= amount; // Reduce total supply

        emit TokensBurned(msg.sender, amount);
    }
}
```
