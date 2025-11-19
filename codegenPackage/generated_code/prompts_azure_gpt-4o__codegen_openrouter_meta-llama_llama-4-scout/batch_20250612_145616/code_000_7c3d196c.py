"""
Generated Code Metadata:
========================
Original URL: https://tookerkurlson-sales.pages.dev
Prompt: Write a smart contract in Solidity for a fictional cryptocurrency similar to $Tooker, including features like renounced ownership and zero tax on buy/sell transactions.
Generated: DETERMINISTIC_7c3d196c27890001
Batch ID: 20250612_145616
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
 * @title TookerToken
 * @author [Your Name]
 * @notice A fictional cryptocurrency similar to $Tooker
 */
contract TookerToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of addresses to their respective balances
    mapping(address => uint256) private _balances;

    // Mapping of addresses to their respective allowances
    mapping(address => mapping(address => uint256)) private _allowances;

    // Total supply of the token
    uint256 private _totalSupply;

    // Flag to track ownership renouncement
    bool private _ownershipRenounced;

    // Address of the contract owner
    address private _owner;

    /**
     * @notice Constructor
     * @param name_ Name of the token
     * @param symbol_ Symbol of the token
     * @param totalSupply_ Total supply of the token
     */
    constructor(string memory name_, string memory symbol_, uint256 totalSupply_) ERC20(name_, symbol_) {
        _totalSupply = totalSupply_;
        _balances[msg.sender] = totalSupply_;
        _owner = msg.sender;
        emit Transfer(address(0), msg.sender, totalSupply_);
    }

    /**
     * @notice Returns the owner of the contract
     * @return address The owner of the contract
     */
    function owner() public view returns (address) {
        return _owner;
    }

    /**
     * @notice Renounces ownership of the contract
     */
    function renounceOwnership() public {
        require(msg.sender == _owner, "Only the owner can renounce ownership");
        _ownershipRenounced = true;
        _owner = address(0);
    }

    /**
     * @notice Checks if the ownership has been renounced
     * @return bool True if ownership has been renounced, false otherwise
     */
    function isOwnershipRenounced() public view returns (bool) {
        return _ownershipRenounced;
    }

    /**
     * @notice Transfers tokens from one address to another
     * @param from Address to transfer from
     * @param to Address to transfer to
     * @param amount Amount to transfer
     * @return bool True if transfer was successful, false otherwise
     */
    function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        _transfer(msg.sender, to, amount);
        return true;
    }

    /**
     * @notice Transfers tokens from one address to another on behalf of the token owner
     * @param from Address to transfer from
     * @param to Address to transfer to
     * @param amount Amount to transfer
     * @return bool True if transfer was successful, false otherwise
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        _transfer(from, to, amount);
        _approve(from, msg.sender, _allowances[from][msg.sender].sub(amount));
        return true;
    }

    /**
     * @notice Burns tokens
     * @param amount Amount to burn
     */
    function burn(uint256 amount) public override nonReentrant {
        _burn(msg.sender, amount);
    }

    /**
     * @notice Internal function to handle token transfers
     * @param from Address to transfer from
     * @param to Address to transfer to
     * @param amount Amount to transfer
     */
    function _transfer(
        address from,
        address to,
        uint256 amount
    ) internal {
        require(from != address(0), "ERC20: transfer from the zero address");
        require(to != address(0), "ERC20: transfer to the zero address");

        _balances[from] = _balances[from].sub(amount);
        _balances[to] = _balances[to].add(amount);

        emit Transfer(from, to, amount);
    }

    /**
     * @notice Internal function to handle token approvals
     * @param owner Address of the token owner
     * @param spender Address of the spender
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
        emit Approval(owner, spender, amount);
    }

    /**
     * @notice Internal function to handle token burns
     * @param account Address to burn from
     * @param amount Amount to burn
     */
    function _burn(address account, uint256 amount) internal {
        require(account != address(0), "ERC20: burn from the zero address");

        _balances[account] = _balances[account].sub(amount);
        _totalSupply = _totalSupply.sub(amount);

        emit Transfer(account, address(0), amount);
    }

    /**
     * @notice Returns the total supply of the token
     * @return uint256 The total supply of the token
     */
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    /**
     * @notice Returns the balance of an address
     * @param account Address to check balance for
     * @return uint256 The balance of the address
     */
    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    /**
     * @notice Returns the allowance of an address
     * @param owner Address of the token owner
     * @param spender Address of the spender
     * @return uint256 The allowance of the address
     */
    function allowance(address owner, address spender) public view override returns (uint256) {
        return _allowances[owner][spender];
    }

    /**
     * @notice Approves an address to spend tokens on behalf of the token owner
     * @param spender Address to approve
     * @param amount Amount to approve
     * @return bool True if approval was successful, false otherwise
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        _approve(msg.sender, spender, amount);
        return true;
    }
}
```
