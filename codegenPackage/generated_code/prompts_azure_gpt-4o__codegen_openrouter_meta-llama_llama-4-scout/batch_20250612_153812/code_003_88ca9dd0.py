"""
Generated Code Metadata:
========================
Original URL: https://cheemspet.web.app
Prompt: Write code to implement a token burning mechanism similar to $Cheems, where users can burn tokens to reduce the circulating supply. Use Solidity for the smart contract.
Generated: DETERMINISTIC_88ca9dd0a43683c8
Batch ID: 20250612_153812
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
 * @title CheemsToken
 * @author [Your Name]
 * @notice A token contract with a burn mechanism.
 */
contract CheemsToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user balances
    mapping(address => uint256) private _balances;

    // Mapping of allowances
    mapping(address => mapping(address => uint256)) private _allowances;

    // Total supply
    uint256 private _totalSupply;

    /**
     * @notice Constructor for the CheemsToken contract.
     * @param name_ Name of the token.
     * @param symbol_ Symbol of the token.
     * @param totalSupply_ Total supply of the token.
     */
    constructor(string memory name_, string memory symbol_, uint256 totalSupply_) ERC20(name_, symbol_) {
        _totalSupply = totalSupply_;
        _balances[msg.sender] = totalSupply_;
    }

    /**
     * @notice Returns the total supply of tokens.
     * @return uint256 Total supply.
     */
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    /**
     * @notice Burns tokens from the specified address.
     * @param amount Amount of tokens to burn.
     */
    function burn(uint256 amount) public override nonReentrant {
        _burn(msg.sender, amount);
    }

    /**
     * @notice Burns tokens from the specified address on behalf of the owner.
     * @param account Account to burn tokens from.
     * @param amount Amount of tokens to burn.
     */
    function burnFrom(address account, uint256 amount) public override nonReentrant {
        uint256 currentAllowance = _allowances[account][msg.sender];
        require(currentAllowance >= amount, "ERC20: burn amount exceeds allowance");
        unchecked {
            _allowances[account][msg.sender] = currentAllowance - amount;
        }
        _burn(account, amount);
    }

    /**
     * @notice Internal function to burn tokens.
     * @param account Account to burn tokens from.
     * @param amount Amount of tokens to burn.
     */
    function _burn(address account, uint256 amount) internal override {
        require(account != address(0), "ERC20: burn from the zero address");
        uint256 accountBalance = _balances[account];
        require(accountBalance >= amount, "ERC20: burn amount exceeds balance");
        unchecked {
            _balances[account] = accountBalance - amount;
        }
        _totalSupply = _totalSupply - amount;
        emit Transfer(account, address(0), amount);
    }

    /**
     * @notice Increases the allowance of a spender.
     * @param spender Spender address.
     * @param addedValue Value to add to the allowance.
     * @return bool Success.
     */
    function increaseAllowance(address spender, uint256 addedValue) public {
        uint256 currentAllowance = _allowances[msg.sender][spender];
        _approve(msg.sender, spender, currentAllowance + addedValue);
    }

    /**
     * @notice Decreases the allowance of a spender.
     * @param spender Spender address.
     * @param subtractedValue Value to subtract from the allowance.
     * @return bool Success.
     */
    function decreaseAllowance(address spender, uint256 subtractedValue) public {
        uint256 currentAllowance = _allowances[msg.sender][spender];
        require(currentAllowance >= subtractedValue, "ERC20: decreased allowance below zero");
        unchecked {
            _allowances[msg.sender][spender] = currentAllowance - subtractedValue;
        }
    }

    /**
     * @notice Approves a spender to spend a certain amount of tokens.
     * @param spender Spender address.
     * @param amount Amount to approve.
     */
    function _approve(address owner, address spender, uint256 amount) internal {
        require(owner != address(0), "ERC20: approve from the zero address");
        require(spender != address(0), "ERC20: approve to the zero address");
        _allowances[owner][spender] = amount;
        emit Approval(owner, spender, amount);
    }

    /**
     * @notice Transfers tokens from one address to another.
     * @param sender Sender address.
     * @param recipient Recipient address.
     * @param amount Amount to transfer.
     * @return bool Success.
     */
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        uint256 senderBalance = _balances[sender];
        require(senderBalance >= amount, "ERC20: transfer amount exceeds balance");
        unchecked {
            _balances[sender] = senderBalance - amount;
        }
        _balances[recipient] = _balances[recipient] + amount;
        emit Transfer(sender, recipient, amount);
    }
}
```
