"""
Generated Code Metadata:
========================
Original URL: https://oraclememe-sale.pages.dev
Prompt: Write a smart contract for a layer-2 scaling solution on Binance Smart Chain that supports fast and low-cost transactions for meme-related assets, as described in the Oracle Meme roadmap.
Generated: DETERMINISTIC_e03f912402f48bcb
Batch ID: 20250612_150552
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Oracle Meme Token Contract
 * @author [Your Name]
 * @notice A meme-related asset token contract for layer-2 scaling solution on Binance Smart Chain
 */
contract OracleMemeToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user balances and allowances
    mapping(address => uint256) private balances;
    mapping(address => mapping(address => uint256)) private allowances;

    // Token parameters
    string private constant _name = "Oracle Meme Token";
    string private constant _symbol = "OMT";
    uint256 private _totalSupply;
    uint256 private _initialSupply;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
    event Mint(address indexed to, uint256 amount);
    event Burn(address indexed from, uint256 amount);

    /**
     * @notice Constructor
     * @param initialSupply Initial supply of tokens
     */
    constructor(uint256 initialSupply) ERC20(_name, _symbol) {
        _initialSupply = initialSupply;
        _totalSupply = initialSupply;
        balances[msg.sender] = initialSupply;
        emit Transfer(address(0), msg.sender, initialSupply);
    }

    /**
     * @notice Returns the name of the token
     * @return string Memory address of the name
     */
    function name() public view override returns (string memory) {
        return _name;
    }

    /**
     * @notice Returns the symbol of the token
     * @return string Memory address of the symbol
     */
    function symbol() public view override returns (string memory) {
        return _symbol;
    }

    /**
     * @notice Returns the total supply of tokens
     * @return uint256 Total supply
     */
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    /**
     * @notice Returns the balance of a user
     * @param account User account
     * @return uint256 User balance
     */
    function balanceOf(address account) public view override returns (uint256) {
        return balances[account];
    }

    /**
     * @notice Transfers tokens from one user to another
     * @param recipient Recipient address
     * @param amount Amount of tokens to transfer
     * @return bool Success status
     */
    function transfer(address recipient, uint256 amount) public override nonReentrant returns (bool) {
        require(recipient != address(0), "OracleMemeToken: transfer to the zero address");
        require(amount > 0, "OracleMemeToken: transfer amount must be greater than zero");
        require(balances[msg.sender] >= amount, "OracleMemeToken: transfer amount exceeds balance");

        balances[msg.sender] = balances[msg.sender].sub(amount);
        balances[recipient] = balances[recipient].add(amount);

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @notice Approves a spender to transfer tokens on behalf of the owner
     * @param spender Spender address
     * @param amount Amount of tokens to approve
     * @return bool Success status
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        require(spender != address(0), "OracleMemeToken: approve to the zero address");

        allowances[msg.sender][spender] = amount;

        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @notice Returns the allowance of a spender for a user
     * @param owner Owner address
     * @param spender Spender address
     * @return uint256 Allowance amount
     */
    function allowance(address owner, address spender) public view override returns (uint256) {
        return allowances[owner][spender];
    }

    /**
     * @notice Transfers tokens from one user to another with allowance
     * @param sender Sender address
     * @param recipient Recipient address
     * @param amount Amount of tokens to transfer
     * @return bool Success status
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        require(sender != address(0), "OracleMemeToken: transfer from the zero address");
        require(recipient != address(0), "OracleMemeToken: transfer to the zero address");
        require(amount > 0, "OracleMemeToken: transfer amount must be greater than zero");
        require(
            allowances[sender][msg.sender] >= amount,
            "OracleMemeToken: transfer amount exceeds allowance"
        );
        require(balances[sender] >= amount, "OracleMemeToken: transfer amount exceeds balance");

        allowances[sender][msg.sender] = allowances[sender][msg.sender].sub(amount);
        balances[sender] = balances[sender].sub(amount);
        balances[recipient] = balances[recipient].add(amount);

        emit Transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @notice Mints new tokens
     * @param amount Amount of tokens to mint
     */
    function mint(uint256 amount) public nonReentrant {
        require(amount > 0, "OracleMemeToken: mint amount must be greater than zero");

        _totalSupply = _totalSupply.add(amount);
        balances[msg.sender] = balances[msg.sender].add(amount);

        emit Mint(msg.sender, amount);
        emit Transfer(address(0), msg.sender, amount);
    }

    /**
     * @notice Burns tokens
     * @param amount Amount of tokens to burn
     */
    function burn(uint256 amount) public override nonReentrant {
        require(amount > 0, "OracleMemeToken: burn amount must be greater than zero");
        require(balances[msg.sender] >= amount, "OracleMemeToken: burn amount exceeds balance");

        balances[msg.sender] = balances[msg.sender].sub(amount);
        _totalSupply = _totalSupply.sub(amount);

        emit Burn(msg.sender, amount);
        emit Transfer(msg.sender, address(0), amount);
    }
}
```
