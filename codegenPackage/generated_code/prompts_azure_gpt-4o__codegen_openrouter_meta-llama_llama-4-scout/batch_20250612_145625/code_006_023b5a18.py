"""
Generated Code Metadata:
========================
Original URL: https://popofrog-io.web.app
Prompt: Provide a Solidity implementation for a fixed total supply token like $FROP, with allocations for presale, staking, marketing, rewards, and liquidity as described in the tokenomics.
Generated: DETERMINISTIC_023b5a180e3c9726
Batch ID: 20250612_145625
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
 * @title FROP Token Contract
 * @author [Your Name]
 * @notice Implementation of the FROP token with fixed total supply and allocations for presale, staking, marketing, rewards, and liquidity.
 */
contract FROPToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of address to balance
    mapping(address => uint256) private _balances;

    // Mapping of address to allowance
    mapping(address => mapping(address => uint256)) private _allowances;

    // Total supply of the token
    uint256 private _totalSupply;

    // Presale allocation
    uint256 public presaleAllocation;

    // Staking allocation
    uint256 public stakingAllocation;

    // Marketing allocation
    uint256 public marketingAllocation;

    // Rewards allocation
    uint256 public rewardsAllocation;

    // Liquidity allocation
    uint256 public liquidityAllocation;

    // Presale address
    address public presaleAddress;

    // Staking address
    address public stakingAddress;

    // Marketing address
    address public marketingAddress;

    // Rewards address
    address public rewardsAddress;

    // Liquidity address
    address public liquidityAddress;

    /**
     * @notice Constructor for the FROP token contract.
     * @param presaleAddr Presale address.
     * @param stakingAddr Staking address.
     * @param marketingAddr Marketing address.
     * @param rewardsAddr Rewards address.
     * @param liquidityAddr Liquidity address.
     */
    constructor(
        address presaleAddr,
        address stakingAddr,
        address marketingAddr,
        address rewardsAddr,
        address liquidityAddr
    ) ERC20("FROP", "FROP") {
        // Total supply of 100,000,000 tokens
        _totalSupply = 100_000_000 * 10**18;

        // Allocation percentages
        presaleAllocation = _totalSupply.mul(15).div(100); // 15%
        stakingAllocation = _totalSupply.mul(20).div(100); // 20%
        marketingAllocation = _totalSupply.mul(10).div(100); // 10%
        rewardsAllocation = _totalSupply.mul(30).div(100); // 30%
        liquidityAllocation = _totalSupply.mul(25).div(100); // 25%

        // Set allocation addresses
        presaleAddress = presaleAddr;
        stakingAddress = stakingAddr;
        marketingAddress = marketingAddr;
        rewardsAddress = rewardsAddr;
        liquidityAddress = liquidityAddr;

        // Mint tokens to allocation addresses
        _mint(presaleAddress, presaleAllocation);
        _mint(stakingAddress, stakingAllocation);
        _mint(marketingAddress, marketingAllocation);
        _mint(rewardsAddress, rewardsAllocation);
        _mint(liquidityAddress, liquidityAllocation);
    }

    /**
     * @notice Returns the total supply of the token.
     * @return Total supply of the token.
     */
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }

    /**
     * @notice Transfers tokens from one address to another.
     * @param sender Sender address.
     * @param recipient Recipient address.
     * @param amount Amount of tokens to transfer.
     * @return bool Whether the transfer was successful.
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
     * @notice Approves an address to spend a certain amount of tokens on behalf of the owner.
     * @param spender Spender address.
     * @param amount Amount of tokens to approve.
     * @return bool Whether the approval was successful.
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        _allowances[msg.sender][spender] = amount;

        emit Approval(msg.sender, spender, amount);

        return true;
    }

    /**
     * @notice Transfers tokens from one address to another on behalf of the owner.
     * @param sender Sender address.
     * @param recipient Recipient address.
     * @param amount Amount of tokens to transfer.
     * @return bool Whether the transfer was successful.
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
     * @notice Increases the allowance of a spender.
     * @param spender Spender address.
     * @param addedValue Amount to add to the allowance.
     * @return bool Whether the increase was successful.
     */
    function increaseAllowance(address spender, uint256 addedValue) public returns (bool) {
        _allowances[msg.sender][spender] = _allowances[msg.sender][spender].add(addedValue);

        emit Approval(msg.sender, spender, _allowances[msg.sender][spender]);

        return true;
    }

    /**
     * @notice Decreases the allowance of a spender.
     * @param spender Spender address.
     * @param subtractedValue Amount to subtract from the allowance.
     * @return bool Whether the decrease was successful.
     */
    function decreaseAllowance(address spender, uint256 subtractedValue) public returns (bool) {
        uint256 currentAllowance = _allowances[msg.sender][spender];
        require(currentAllowance >= subtractedValue, "ERC20: decreased allowance below zero");

        _allowances[msg.sender][spender] = currentAllowance.sub(subtractedValue);

        emit Approval(msg.sender, spender, _allowances[msg.sender][spender]);

        return true;
    }
}
```
