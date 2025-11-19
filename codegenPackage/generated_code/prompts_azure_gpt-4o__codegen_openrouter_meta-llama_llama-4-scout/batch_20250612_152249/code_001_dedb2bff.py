"""
Generated Code Metadata:
========================
Original URL: https://bafybeihvlecv3pyhzgus6paeowc4njugqq5qbo4re4u6tuw24nstl6smni.ipfs.dweb.link
Prompt: Generate Solidity code for a smart contract that implements a 0% tax token similar to MAGA ($MAGA), ensuring it is community-driven and includes basic tokenomics features.
Generated: DETERMINISTIC_dedb2bff8fcbb512
Batch ID: 20250612_152249
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
 * @title MAGA Token Contract
 * @author [Your Name]
 * @notice A community-driven 0% tax token with basic tokenomics features.
 */
contract MAGAToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of addresses to their respective balances
    mapping(address => uint256) private _balances;

    // Mapping of addresses to their respective allowances
    mapping(address => mapping(address => uint256)) private _allowances;

    // Total supply of the token
    uint256 private _totalSupply;

    // Maximum supply of the token
    uint256 public immutable MAX_SUPPLY;

    /**
     * @notice Constructor function for the MAGA Token contract.
     * @param name_ The name of the token.
     * @param symbol_ The symbol of the token.
     * @param totalSupply_ The total supply of the token.
     */
    constructor(string memory name_, string memory symbol_, uint256 totalSupply_) ERC20(name_, symbol_) {
        MAX_SUPPLY = totalSupply_;
        _totalSupply = totalSupply_;
        _balances[msg.sender] = totalSupply_;
        emit Transfer(address(0), msg.sender, totalSupply_);
    }

    /**
     * @notice Returns the total supply of the token.
     * @return The total supply of the token.
     */
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    /**
     * @notice Returns the balance of the specified address.
     * @param account The address to query.
     * @return The balance of the specified address.
     */
    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    /**
     * @notice Transfers tokens from the sender's account to the recipient's account.
     * @param recipient The address of the recipient.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transfer(address recipient, uint256 amount) public override nonReentrant returns (bool) {
        require(recipient != address(0), "ERC20: transfer to the zero address");

        uint256 senderBalance = _balances[msg.sender];
        require(senderBalance >= amount, "ERC20: transfer amount exceeds balance");

        _balances[msg.sender] = senderBalance.sub(amount);
        _balances[recipient] = _balances[recipient].add(amount);

        emit Transfer(msg.sender, recipient, amount);
        return true;
    }

    /**
     * @notice Approves the specified address to transfer tokens on behalf of the sender.
     * @param spender The address to approve.
     * @param amount The amount of tokens to approve.
     * @return A boolean indicating whether the approval was successful.
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @notice Returns the allowance of the specified spender for the specified owner.
     * @param owner The address of the owner.
     * @param spender The address of the spender.
     * @return The allowance of the specified spender for the specified owner.
     */
    function allowance(address owner, address spender) public view override returns (uint256) {
        return _allowances[owner][spender];
    }

    /**
     * @notice Transfers tokens from the owner's account to the recipient's account on behalf of the owner.
     * @param sender The address of the owner.
     * @param recipient The address of the recipient.
     * @param amount The amount of tokens to transfer.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");

        uint256 senderBalance = _balances[sender];
        require(senderBalance >= amount, "ERC20: transfer amount exceeds balance");

        uint256 allowance = _allowances[sender][msg.sender];
        require(allowance >= amount, "ERC20: transfer amount exceeds allowance");

        _balances[sender] = senderBalance.sub(amount);
        _balances[recipient] = _balances[recipient].add(amount);
        _allowances[sender][msg.sender] = allowance.sub(amount);

        emit Transfer(sender, recipient, amount);
        return true;
    }

    /**
     * @notice Burns tokens from the sender's account.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) public override nonReentrant {
        require(amount > 0, "ERC20: burn amount is zero");
        require(_balances[msg.sender] >= amount, "ERC20: burn amount exceeds balance");

        _balances[msg.sender] = _balances[msg.sender].sub(amount);
        _totalSupply = _totalSupply.sub(amount);

        emit Transfer(msg.sender, address(0), amount);
    }

    /**
     * @notice Burns tokens from the specified address on behalf of the owner.
     * @param account The address to burn tokens from.
     * @param amount The amount of tokens to burn.
     */
    function burnFrom(address account, uint256 amount) public override nonReentrant {
        require(amount > 0, "ERC20: burn amount is zero");
        require(_balances[account] >= amount, "ERC20: burn amount exceeds balance");

        uint256 allowance = _allowances[account][msg.sender];
        require(allowance >= amount, "ERC20: burn amount exceeds allowance");

        _balances[account] = _balances[account].sub(amount);
        _totalSupply = _totalSupply.sub(amount);
        _allowances[account][msg.sender] = allowance.sub(amount);

        emit Transfer(account, address(0), amount);
    }
}
```
