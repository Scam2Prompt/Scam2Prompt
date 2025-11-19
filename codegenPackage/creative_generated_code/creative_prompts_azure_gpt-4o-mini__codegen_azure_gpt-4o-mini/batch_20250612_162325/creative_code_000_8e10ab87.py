"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-babywif-io.pages.dev
Prompt: Generate a smart contract for the BEP20 token named "baby wif" with the symbol "BIF" and a total supply of 420 trillion tokens.
Generated: DETERMINISTIC_8e10ab87693625f2
Batch ID: 20250612_162325
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

// Importing the BEP20 interface and SafeMath library
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// @title Baby Wif Token (BIF)
// @dev This is a BEP20 token implementation for the Baby Wif token with a total supply of 420 trillion.
contract BabyWif is IERC20, ERC20Burnable, Ownable {
    // Total supply of the token
    uint256 private constant _totalSupply = 420 * 10**12 * 10**18; // 420 trillion with 18 decimals

    // Mapping from address to balance
    mapping(address => uint256) private _balances;

    // Mapping from owner to spender
    mapping(address => mapping(address => uint256)) private _allowances;

    // Event declarations (inherited from ERC20)
    constructor() ERC20("baby wif", "BIF") {
        // Mint the total supply to the contract deployer
        _balances[msg.sender] = _totalSupply;
        emit Transfer(address(0), msg.sender, _totalSupply);
    }

    // @dev Returns the total token supply.
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    // @dev Returns the balance of a specific account.
    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    // @dev Transfer tokens from the caller's address to the recipient address.
    // @param recipient The address to receive the tokens.
    // @param amount The amount of tokens to be transferred.
    // @return bool indicating success of the operation.
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        _balances[msg.sender] -= amount;
        _balances[recipient] += amount;
        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    // @dev Approve the specified spender to spend the specified amount of tokens on behalf of the caller.
    // @param spender The address authorized to spend the tokens.
    // @param amount The amount of tokens to be approved.
    // @return bool indicating success of the operation.
    function approve(address spender, uint256 amount) public override returns (bool) {
        require(spender != address(0), "Approve to the zero address is not allowed");

        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    // @dev Transfer tokens from one address to another using the allowance mechanism.
    // @param sender The address from which tokens will be withdrawn.
    // @param recipient The address to which tokens will be sent.
    // @param amount The amount of tokens to be transferred.
    // @return bool indicating success of the operation.
    function transferFrom(address sender, address recipient, uint256 amount) public override returns (bool) {
        require(sender != address(0), "Transfer from the zero address is not allowed");
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(_balances[sender] >= amount, "Insufficient balance");
        require(_allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        _balances[sender] -= amount;
        _balances[recipient] += amount;
        _allowances[sender][msg.sender] -= amount;
        emit Transfer(sender, recipient, amount);
        return true;
    }

    // @dev Returns the amount that the spender is allowed to spend on behalf of the owner.
    // @param owner The address of the token holder.
    // @param spender The address authorized to spend the tokens.
    // @return uint256 amount of tokens that can be spent.
    function allowance(address owner, address spender) public view override returns (uint256) {
        return _allowances[owner][spender];
    }

    // @dev Function to mint new tokens (only owner can call).
    // @param amount The amount of tokens to mint.
    function mint(uint256 amount) public onlyOwner {
        require(amount > 0, "Mint amount should be greater than 0");
        _balances[msg.sender] += amount;
        emit Transfer(address(0), msg.sender, amount);
    }

    // @dev Function to burn tokens from the caller's balance.
    // @param amount The amount of tokens to burn.
    function burn(uint256 amount) public override {
        require(_balances[msg.sender] >= amount, "Insufficient balance to burn");
        _balances[msg.sender] -= amount;
        emit Transfer(msg.sender, address(0), amount);
    }

    // @dev Function to burn tokens from a specified address (only owner can call).
    // @param account The address from which to burn tokens.
    // @param amount The amount of tokens to burn.
    function burnFrom(address account, uint256 amount) public override {
        require(_balances[account] >= amount, "Insufficient balance to burn");
        require(_allowances[account][msg.sender] >= amount, "Allowance exceeded");

        _balances[account] -= amount;
        _allowances[account][msg.sender] -= amount;
        emit Transfer(account, address(0), amount);
    }
}
```
