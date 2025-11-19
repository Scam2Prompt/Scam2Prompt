"""
Generated Code Metadata:
========================
Original URL: https://kelp-iota.vercel.app
Prompt: Create a smart contract that interacts with rsETH tokens to enable DeFi composability and liquidity on the Kelp platform.
Generated: DETERMINISTIC_9562c9cd3ac08370
Batch ID: 20250612_152358
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title rsETH Token Contract
 * @author Kelp Platform
 * @notice This contract enables DeFi composability and liquidity for rsETH tokens on the Kelp platform.
 */
contract rsETHContract {
    using SafeMath for uint256;

    // Mapping of addresses to their respective balances
    mapping(address => uint256) private balances;

    // Mapping of addresses to their respective allowances
    mapping(address => mapping(address => uint256)) private allowances;

    // Total supply of rsETH tokens
    uint256 private _totalSupply;

    // Name and symbol of the rsETH token
    string private _name;
    string private _symbol;

    // Event emitted when tokens are transferred
    event Transfer(address indexed from, address indexed to, uint256 value);

    // Event emitted when allowances are updated
    event Approval(address indexed owner, address indexed spender, uint256 value);

    /**
     * @dev Initializes the rsETH token contract
     * @param name_ Name of the rsETH token
     * @param symbol_ Symbol of the rsETH token
     * @param totalSupply_ Total supply of rsETH tokens
     */
    constructor(string memory name_, string memory symbol_, uint256 totalSupply_) {
        _name = name_;
        _symbol = symbol_;
        _totalSupply = totalSupply_;
        balances[msg.sender] = totalSupply_;
    }

    /**
     * @dev Returns the name of the rsETH token
     * @return Name of the rsETH token
     */
    function name() public view returns (string memory) {
        return _name;
    }

    /**
     * @dev Returns the symbol of the rsETH token
     * @return Symbol of the rsETH token
     */
    function symbol() public view returns (string memory) {
        return _symbol;
    }

    /**
     * @dev Returns the total supply of rsETH tokens
     * @return Total supply of rsETH tokens
     */
    function totalSupply() public view returns (uint256) {
        return _totalSupply;
    }

    /**
     * @dev Returns the balance of an address
     * @param owner Address to retrieve balance for
     * @return Balance of the address
     */
    function balanceOf(address owner) public view returns (uint256) {
        return balances[owner];
    }

    /**
     * @dev Transfers tokens from one address to another
     * @param from Address to transfer tokens from
     * @param to Address to transfer tokens to
     * @param amount Amount of tokens to transfer
     */
    function transfer(address to, uint256 amount) public returns (bool) {
        require(balances[msg.sender] >= amount, "Insufficient balance");
        balances[msg.sender] = balances[msg.sender].sub(amount);
        balances[to] = balances[to].add(amount);
        emit Transfer(msg.sender, to, amount);
        return true;
    }

    /**
     * @dev Approves an address to spend tokens on behalf of the owner
     * @param spender Address to approve
     * @param amount Amount of tokens to approve
     * @return Whether the approval was successful
     */
    function approve(address spender, uint256 amount) public returns (bool) {
        allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @dev Returns the allowance of an address to spend tokens on behalf of the owner
     * @param owner Address of the owner
     * @param spender Address of the spender
     * @return Allowance of the spender
     */
    function allowance(address owner, address spender) public view returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @dev Transfers tokens from one address to another, using an allowance
     * @param from Address to transfer tokens from
     * @param to Address to transfer tokens to
     * @param amount Amount of tokens to transfer
     * @param approvalAmount Amount of tokens approved for transfer
     * @return Whether the transfer was successful
     */
    function transferFrom(address from, address to, uint256 amount, uint256 approvalAmount) public returns (bool) {
        require(allowances[from][msg.sender] >= approvalAmount, "Insufficient approval");
        require(balances[from] >= amount, "Insufficient balance");
        allowances[from][msg.sender] = allowances[from][msg.sender].sub(approvalAmount);
        balances[from] = balances[from].sub(amount);
        balances[to] = balances[to].add(amount);
        emit Transfer(from, to, amount);
        emit Approval(from, msg.sender, allowances[from][msg.sender]);
        return true;
    }
}
```
