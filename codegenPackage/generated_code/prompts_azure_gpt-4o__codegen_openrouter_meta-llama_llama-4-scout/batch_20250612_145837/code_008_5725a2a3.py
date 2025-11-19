"""
Generated Code Metadata:
========================
Original URL: https://mpeppe-live.web.app
Prompt: Generate Solidity code for a tokenomics model resembling `$MPEPE`, including allocations for presale, treasury, gaming, and liquidity, with zero buy/sell tax.
Generated: DETERMINISTIC_5725a2a3087aea35
Batch ID: 20250612_145837
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
 * @notice Tokenomics model resembling $MPEPE with allocations for presale, treasury, gaming, and liquidity.
 */
contract MPEPE is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of addresses to their respective balances
    mapping(address => uint256) private _balances;

    // Mapping of addresses to their respective allowances
    mapping(address => mapping(address => uint256)) private _allowances;

    // Total supply of the token
    uint256 private _totalSupply;

    // Presale, treasury, gaming, and liquidity allocations
    uint256 public constant PRESALE_ALLOCATION = 20 * 10**6 * 10**18; // 20 million
    uint256 public constant TREASURY_ALLOCATION = 30 * 10**6 * 10**18; // 30 million
    uint256 public constant GAMING_ALLOCATION = 15 * 10**6 * 10**18; // 15 million
    uint256 public constant LIQUIDITY_ALLOCATION = 35 * 10**6 * 10**18; // 35 million

    // Address for presale, treasury, gaming, and liquidity
    address public presaleAddress;
    address public treasuryAddress;
    address public gamingAddress;
    address public liquidityAddress;

    /**
     * @notice Constructor for MPEPE token contract
     * @param _presaleAddress Address for presale allocation
     * @param _treasuryAddress Address for treasury allocation
     * @param _gamingAddress Address for gaming allocation
     * @param _liquidityAddress Address for liquidity allocation
     */
    constructor(
        address _presaleAddress,
        address _treasuryAddress,
        address _gamingAddress,
        address _liquidityAddress
    ) ERC20("MPEPE", "MPEPE") {
        _totalSupply = 100 * 10**6 * 10**18; // 100 million

        presaleAddress = _presaleAddress;
        treasuryAddress = _treasuryAddress;
        gamingAddress = _gamingAddress;
        liquidityAddress = _liquidityAddress;

        // Mint tokens for presale, treasury, gaming, and liquidity allocations
        _mint(presaleAddress, PRESALE_ALLOCATION);
        _mint(treasuryAddress, TREASURY_ALLOCATION);
        _mint(gamingAddress, GAMING_ALLOCATION);
        _mint(liquidityAddress, LIQUIDITY_ALLOCATION);
    }

    /**
     * @notice No buy/sell tax, override to ensure no fees are applied
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override {
        super._beforeTokenTransfer(from, to, amount);
    }

    /**
     * @notice Get the total supply of the token
     * @return uint256 Total supply
     */
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    /**
     * @notice Get the balance of an address
     * @param account Address to get balance for
     * @return uint256 Balance
     */
    function balanceOf(address account) public view override returns (uint256) {
        return _balances[account];
    }

    /**
     * @notice Transfer tokens from one address to another
     * @param from Address to transfer from
     * @param to Address to transfer to
     * @param amount Amount to transfer
     * @return bool Success
     */
    function transfer(address to, uint256 amount) public override returns (bool) {
        _transfer(msg.sender, to, amount);
        return true;
    }

    /**
     * @notice Approve an address to spend tokens on behalf of another
     * @param spender Address to approve
     * @param amount Amount to approve
     * @return bool Success
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        _approve(msg.sender, spender, amount);
        return true;
    }

    /**
     * @notice Transfer tokens from one address to another on behalf of another
     * @param from Address to transfer from
     * @param to Address to transfer to
     * @param amount Amount to transfer
     * @return bool Success
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public override returns (bool) {
        _transfer(from, to, amount);
        _approve(from, msg.sender, _allowances[from][msg.sender].sub(amount, "ERC20: transfer amount exceeds allowance"));
        return true;
    }

    /**
     * @notice Increase allowance of an address to spend tokens
     * @param spender Address to increase allowance for
     * @param addedValue Amount to increase allowance by
     * @return bool Success
     */
    function increaseAllowance(address spender, uint256 addedValue) public override returns (bool) {
        _approve(msg.sender, spender, _allowances[msg.sender][spender].add(addedValue));
        return true;
    }

    /**
     * @notice Decrease allowance of an address to spend tokens
     * @param spender Address to decrease allowance for
     * @param subtractedValue Amount to decrease allowance by
     * @return bool Success
     */
    function decreaseAllowance(address spender, uint256 subtractedValue) public override returns (bool) {
        _approve(msg.sender, spender, _allowances[msg.sender][spender].sub(subtractedValue, "ERC20: decreased allowance below zero"));
        return true;
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

        _balances[from] = _balances[from].sub(amount, "ERC20: transfer amount exceeds balance");
        _balances[to] = _balances[to].add(amount);
        emit Transfer(from, to, amount);
    }

    /**
     * @notice Internal function to handle approvals
     * @param owner Address to approve from
     * @param spender Address to approve
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
     * @notice Internal function to mint tokens
     * @param account Address to mint to
     * @param amount Amount to mint
     */
    function _mint(address account, uint256 amount) internal {
        require(account != address(0), "ERC20: mint to the zero address");

        _totalSupply = _totalSupply.add(amount);
        _balances[account] = _balances[account].add(amount);
        emit Transfer(address(0), account, amount);
    }
}
```
