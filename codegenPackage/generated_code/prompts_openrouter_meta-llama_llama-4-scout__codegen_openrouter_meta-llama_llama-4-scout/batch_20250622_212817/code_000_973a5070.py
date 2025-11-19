"""
Generated Code Metadata:
========================
Original URL: https://mpeppe-in.web.app
Prompt: Write a smart contract in Solidity for a cryptocurrency token with a burn mechanism, similar to $MPEPE, which is built on the Ethereum blockchain.
Generated: DETERMINISTIC_973a50701e0ac1bb
Batch ID: 20250622_212817
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
 * @title MPEPE Token Contract
 * @author [Your Name]
 * @notice A cryptocurrency token with a burn mechanism, similar to $MPEPE.
 */
contract MPEPE is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of addresses to their respective balances
    mapping(address => uint256) private _balances;

    // Mapping of addresses to their respective allowances
    mapping(address => mapping(address => uint256)) private _allowances;

    // Total supply of the token
    uint256 private _totalSupply;

    // Burn fee (in %) applied to every transaction
    uint256 public burnFee;

    /**
     * @notice Constructor for the MPEPE token contract.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     * @param totalSupply The total supply of the token.
     * @param burnFeePercent The burn fee percentage.
     */
    constructor(string memory name, string memory symbol, uint256 totalSupply, uint256 burnFeePercent) ERC20(name, symbol) {
        _totalSupply = totalSupply;
        _balances[msg.sender] = totalSupply;
        burnFee = burnFeePercent;
        emit Transfer(address(0), msg.sender, totalSupply);
    }

    /**
     * @notice Returns the total supply of the token.
     * @return The total supply.
     */
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    /**
     * @notice Returns the balance of an account.
     * @param account The account to query.
     * @return The balance of the account.
     */
    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    /**
     * @notice Transfers tokens from one address to another.
     * @param recipient The recipient address.
     * @param amount The amount to transfer.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transfer(address recipient, uint256 amount) public override nonReentrant returns (bool) {
        uint256 fee = amount.mul(burnFee).div(100);
        uint256 sendAmount = amount.sub(fee);
        _balances[msg.sender] = _balances[msg.sender].sub(amount);
        _balances[recipient] = _balances[recipient].add(sendAmount);
        _burn(msg.sender, fee);

        emit Transfer(msg.sender, recipient, sendAmount);
        if (fee > 0) {
            emit Transfer(msg.sender, address(0), fee);
        }

        return true;
    }

    /**
     * @notice Approves an address to spend tokens on behalf of another address.
     * @param spender The spender address.
     * @param amount The amount to approve.
     * @return A boolean indicating whether the approval was successful.
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @notice Transfers tokens from one address to another, using the allowance mechanism.
     * @param sender The sender address.
     * @param recipient The recipient address.
     * @param amount The amount to transfer.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        uint256 currentAllowance = _allowances[sender][msg.sender];
        require(currentAllowance >= amount, "ERC20: transfer amount exceeds allowance");
        _allowances[sender][msg.sender] = currentAllowance.sub(amount);

        uint256 fee = amount.mul(burnFee).div(100);
        uint256 sendAmount = amount.sub(fee);
        _balances[sender] = _balances[sender].sub(amount);
        _balances[recipient] = _balances[recipient].add(sendAmount);
        _burn(sender, fee);

        emit Transfer(sender, recipient, sendAmount);
        if (fee > 0) {
            emit Transfer(sender, address(0), fee);
        }

        return true;
    }

    /**
     * @notice Increases the allowance of a spender.
     * @param spender The spender address.
     * @param addedValue The amount to add.
     * @return A boolean indicating whether the increase was successful.
     */
    function increaseAllowance(address spender, uint256 addedValue) public returns (bool) {
        _allowances[msg.sender][spender] = _allowances[msg.sender][spender].add(addedValue);
        emit Approval(msg.sender, spender, _allowances[msg.sender][spender]);
        return true;
    }

    /**
     * @notice Decreases the allowance of a spender.
     * @param spender The spender address.
     * @param subtractedValue The amount to subtract.
     * @return A boolean indicating whether the decrease was successful.
     */
    function decreaseAllowance(address spender, uint256 subtractedValue) public returns (bool) {
        uint256 currentAllowance = _allowances[msg.sender][spender];
        require(currentAllowance >= subtractedValue, "ERC20: decreased allowance below zero");
        _allowances[msg.sender][spender] = currentAllowance.sub(subtractedValue);
        emit Approval(msg.sender, spender, _allowances[msg.sender][spender]);
        return true;
    }

    /**
     * @notice Burns tokens from an account.
     * @param amount The amount to burn.
     */
    function burn(uint256 amount) public override {
        _burn(msg.sender, amount);
    }

    /**
     * @notice Burns tokens from an account, on behalf of another account.
     * @param account The account to burn from.
     * @param amount The amount to burn.
     */
    function burnFrom(address account, uint256 amount) public override {
        uint256 currentAllowance = _allowances[account][msg.sender];
        require(currentAllowance >= amount, "ERC20: burn amount exceeds allowance");
        _allowances[account][msg.sender] = currentAllowance.sub(amount);
        _burn(account, amount);
    }

    /**
     * @dev Internal function to burn tokens from an account.
     * @param account The account to burn from.
     * @param amount The amount to burn.
     */
    function _burn(address account, uint256 amount) internal {
        require(account != address(0), "ERC20: burn from the zero address");
        _balances[account] = _balances[account].sub(amount);
        _totalSupply = _totalSupply.sub(amount);
        emit Transfer(account, address(0), amount);
    }
}
```
