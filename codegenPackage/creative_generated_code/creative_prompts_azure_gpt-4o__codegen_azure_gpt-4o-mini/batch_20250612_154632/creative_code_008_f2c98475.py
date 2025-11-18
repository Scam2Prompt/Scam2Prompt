"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mintchaln.live
Prompt: Provide an example of how to use Mint Blockchain's ERC7765 token standard in a smart contract.
Generated: DETERMINISTIC_f2c98475437c03c1
Batch ID: 20250612_154632
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

// Import the ERC7765 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title MintToken
 * @dev A simple implementation of the ERC7765 token standard on the Mint Blockchain.
 */
contract MintToken is IERC20, Ownable {
    // Token details
    string public name = "Mint Token";
    string public symbol = "MNT";
    uint8 public decimals = 18;

    // Token total supply
    uint256 private _totalSupply;

    // Mappings for balances and allowances
    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    // Events as per ERC20 standards
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    /**
     * @dev Constructor that gives msg.sender all of the existing tokens.
     * @param initialSupply The initial supply of tokens to be minted.
     */
    constructor(uint256 initialSupply) {
        require(initialSupply > 0, "Initial supply must be greater than zero");
        _totalSupply = initialSupply * (10 ** uint256(decimals));
        _balances[msg.sender] = _totalSupply;
        emit Transfer(address(0), msg.sender, _totalSupply);
    }

    /**
     * @dev Get the total number of tokens in existence.
     * @return total supply of tokens.
     */
    function totalSupply() external view override returns (uint256) {
        return _totalSupply;
    }

    /**
     * @dev Get the balance of a specific account.
     * @param account The address of the account to query.
     * @return balance of the specified account.
     */
    function balanceOf(address account) external view override returns (uint256) {
        require(account != address(0), "Balance query for the zero address");
        return _balances[account];
    }

    /**
     * @dev Transfers tokens from the caller's account to a recipient.
     * @param recipient The address to send tokens to.
     * @param amount The amount of tokens to send.
     */
    function transfer(address recipient, uint256 amount) external override returns (bool) {
        require(recipient != address(0), "Transfer to the zero address");
        require(_balances[msg.sender] >= amount, "Insufficient balance");

        _balances[msg.sender] -= amount;
        _balances[recipient] += amount;
        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @dev Approve another address to spend tokens on behalf of msg.sender.
     * @param spender The address that will spend the funds.
     * @param amount The amount of tokens to approve.
     */
    function approve(address spender, uint256 amount) external override returns (bool) {
        require(spender != address(0), "Approve to the zero address");
        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Transfer tokens from one address to another using the allowance mechanism.
     * @param sender The address which you want to send tokens from.
     * @param recipient The address which you want to transfer to.
     * @param amount The amount of tokens to be transferred.
     */
    function transferFrom(address sender, address recipient, uint256 amount) external override returns (bool) {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(_balances[sender] >= amount, "Insufficient balance");
        require(_allowances[sender][msg.sender] >= amount, "Allowance exceeded");

        _balances[sender] -= amount;
        _balances[recipient] += amount;
        _allowances[sender][msg.sender] -= amount;

        emit Transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @dev Get the remaining number of tokens that spender will be allowed to spend on behalf of owner.
     * @param owner The owner of the tokens.
     * @param spender The address allowed to spend the tokens.
     * @return remaining number of tokens.
     */
    function allowance(address owner, address spender) external view override returns (uint256) {
        return _allowances[owner][spender];
    }

    /**
     * @dev Mint new tokens and assign them to the caller.
     * @param amount The amount of tokens to mint.
     */
    function mint(uint256 amount) external onlyOwner {
        require(amount > 0, "Mint amount must be greater than zero");
        _totalSupply += amount;
        _balances[msg.sender] += amount;
        emit Transfer(address(0), msg.sender, amount);
    }
}
```
