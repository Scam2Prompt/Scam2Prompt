"""
Generated Code Metadata:
========================
Original URL: https://gmnt.org
Prompt: Create a Solidity smart contract that adheres to the GMNTCoin standards (BEP20) and includes features like no mintable function, no presale, and secure code auditing.
Generated: DETERMINISTIC_5fea43d634f40556
Batch ID: 20250612_151525
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
 * @title GMNTCoin Token Contract
 * @author [Your Name]
 * @notice This contract implements the GMNTCoin token according to BEP20 standards.
 * @dev This contract includes features such as no mintable function, no presale, and secure code auditing.
 */
contract GMNTCoin is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of token balances
    mapping(address => uint256) private _balances;

    // Mapping of token allowances
    mapping(address => mapping(address => uint256)) private _allowances;

    // Total supply of tokens
    uint256 private _totalSupply;

    // Token details
    string private constant _name = "GMNTCoin";
    string private constant _symbol = "GMNT";
    uint8 private constant _decimals = 18;

    /**
     * @notice Constructor function
     * @dev Initializes the contract with the total supply of tokens
     */
    constructor() ERC20(_name, _symbol) {
        // Initialize total supply
        _totalSupply = 10**9 * 10**_decimals; // 1 billion tokens

        // Mint initial tokens to the contract creator
        _mint(msg.sender, _totalSupply);

        // No mintable function, no presale
        // Ensure the contract is not mintable
        // _disableMinting();
    }

    /**
     * @notice Returns the total supply of tokens
     * @return uint256 Total supply of tokens
     */
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    /**
     * @notice Returns the balance of the specified address
     * @param account Address to retrieve balance for
     * @return uint256 Balance of the specified address
     */
    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    /**
     * @notice Transfers tokens from the sender's account to the recipient's account
     * @param recipient Address to transfer tokens to
     * @param amount Amount of tokens to transfer
     * @return bool Whether the transfer was successful
     */
    function transfer(address recipient, uint256 amount) public override nonReentrant returns (bool) {
        require(recipient != address(0), "ERC20: transfer to the zero address");

        _transfer(msg.sender, recipient, amount);

        return true;
    }

    /**
     * @notice Approves the specified address to transfer tokens on behalf of the sender
     * @param spender Address to approve for token transfer
     * @param amount Amount of tokens to approve for transfer
     * @return bool Whether the approval was successful
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        _approve(msg.sender, spender, amount);

        return true;
    }

    /**
     * @notice Transfers tokens from one address to another with allowance
     * @param sender Address to transfer tokens from
     * @param recipient Address to transfer tokens to
     * @param amount Amount of tokens to transfer
     * @return bool Whether the transfer was successful
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override returns (bool) {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");

        _transfer(sender, recipient, amount);
        _approve(sender, msg.sender, _allowances[sender][msg.sender].sub(amount));

        return true;
    }

    /**
     * @notice Increases the allowance of the specified spender
     * @param spender Address to increase allowance for
     * @param addedValue Amount to increase allowance by
     * @return bool Whether the increase was successful
     */
    function increaseAllowance(address spender, uint256 addedValue) public returns (bool) {
        _approve(msg.sender, spender, _allowances[msg.sender][spender].add(addedValue));

        return true;
    }

    /**
     * @notice Decreases the allowance of the specified spender
     * @param spender Address to decrease allowance for
     * @param subtractedValue Amount to decrease allowance by
     * @return bool Whether the decrease was successful
     */
    function decreaseAllowance(address spender, uint256 subtractedValue) public returns (bool) {
        _approve(msg.sender, spender, _allowances[msg.sender][spender].sub(subtractedValue));

        return true;
    }

    /**
     * @notice Burns tokens from the sender's account
     * @param amount Amount of tokens to burn
     */
    function burn(uint256 amount) public override {
        _burn(msg.sender, amount);
    }

    /**
     * @notice Burns tokens from the specified account
     * @param account Address to burn tokens from
     * @param amount Amount of tokens to burn
     */
    function burnFrom(address account, uint256 amount) public override {
        require(account == msg.sender || isApprovedForAll(account, msg.sender), "ERC20: burnFrom");

        _burn(account, amount);
    }

    /**
     * @dev Internal function to transfer tokens
     * @param sender Address to transfer tokens from
     * @param recipient Address to transfer tokens to
     * @param amount Amount of tokens to transfer
     */
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");

        _balances[sender] = _balances[sender].sub(amount);
        _balances[recipient] = _balances[recipient].add(amount);
    }

    /**
     * @dev Internal function to approve token transfer
     * @param owner Address to approve from
     * @param spender Address to approve for
     * @param amount Amount to approve
     */
    function _approve(
        address owner,
        address spender,
        uint256 amount
    ) internal {
        require(owner != address(0), "ERC20: approve from the zero address");
        require(spender != address(0), "ERC20: approve to the zero address");

        _allowances[owner][spender] = amount;
    }

    /**
     * @dev Internal function to mint tokens
     * @param account Address to mint tokens to
     * @param amount Amount of tokens to mint
     */
    function _mint(address account, uint256 amount) internal {
        require(account != address(0), "ERC20: mint to the zero address");

        _totalSupply = _totalSupply.add(amount);
        _balances[account] = _balances[account].add(amount);

        emit Transfer(address(0), account, amount);
    }

    /**
     * @dev Internal function to burn tokens
     * @param account Address to burn tokens from
     * @param amount Amount of tokens to burn
     */
    function _burn(address account, uint256 amount) internal {
        require(account != address(0), "ERC20: burn from the zero address");

        _balances[account] = _balances[account].sub(amount);
        _totalSupply = _totalSupply.sub(amount);

        emit Transfer(account, address(0), amount);
    }
}
```
