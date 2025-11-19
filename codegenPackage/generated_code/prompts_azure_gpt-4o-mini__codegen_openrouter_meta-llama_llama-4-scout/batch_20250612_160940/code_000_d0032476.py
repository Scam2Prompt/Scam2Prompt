"""
Generated Code Metadata:
========================
Original URL: https://supertruimpcoin.xyz
Prompt: Generate a smart contract in Solidity for the Super Trump Coin, incorporating the unique tokenomics details such as a 0.3% tax and 0.8% allocation to the Trump wallet.
Generated: DETERMINISTIC_d0032476599086e5
Batch ID: 20250612_160940
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
 * @title SuperTrumpCoin
 * @author [Your Name]
 * @notice A token with a 0.3% tax and 0.8% allocation to the Trump wallet.
 */
contract SuperTrumpCoin is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Wallet addresses
    address private _trumpWallet;
    address private _owner;

    // Tax and allocation rates
    uint256 private constant _taxRate = 300; // 0.3%
    uint256 private constant _trumpAllocationRate = 800; // 0.8%

    // Mapping of account balances and allowances
    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    /**
     * @notice Constructor.
     * @param trumpWallet The wallet address to receive the Trump allocation.
     */
    constructor(address trumpWallet) ERC20("Super Trump Coin", "STC") {
        _trumpWallet = trumpWallet;
        _owner = msg.sender;
        _balances[msg.sender] = 1000 * 10**18; // Initial supply: 1000 STC
        emit Transfer(address(0), msg.sender, 1000 * 10**18);
    }

    /**
     * @notice Returns the Trump wallet address.
     * @return The Trump wallet address.
     */
    function getTrumpWallet() public view returns (address) {
        return _trumpWallet;
    }

    /**
     * @notice Returns the owner address.
     * @return The owner address.
     */
    function getOwner() public view returns (address) {
        return _owner;
    }

    /**
     * @notice Transfers tokens, applying the tax and Trump allocation.
     * @param recipient The recipient address.
     * @param amount The amount to transfer.
     * @return A boolean indicating success.
     */
    function transfer(address recipient, uint256 amount) public override nonReentrant returns (bool) {
        uint256 tax = amount.mul(_taxRate).div(10000);
        uint256 trumpAllocation = amount.mul(_trumpAllocationRate).div(10000);
        uint256 netAmount = amount.sub(tax).sub(trumpAllocation);

        _balances[msg.sender] = _balances[msg.sender].sub(amount);
        _balances[recipient] = _balances[recipient].add(netAmount);
        _balances[_trumpWallet] = _balances[_trumpWallet].add(trumpAllocation);

        emit Transfer(msg.sender, recipient, netAmount);
        emit Transfer(msg.sender, _trumpWallet, trumpAllocation);

        // Burn the tax amount
        _burn(msg.sender, tax);

        return true;
    }

    /**
     * @notice Approves an allowance, applying the tax and Trump allocation.
     * @param spender The spender address.
     * @param amount The amount to approve.
     * @return A boolean indicating success.
     */
    function approve(address spender, uint256 amount) public override returns (bool) {
        _allowances[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    /**
     * @notice Transfers from an allowance, applying the tax and Trump allocation.
     * @param sender The sender address.
     * @param recipient The recipient address.
     * @param amount The amount to transfer.
     * @return A boolean indicating success.
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        uint256 tax = amount.mul(_taxRate).div(10000);
        uint256 trumpAllocation = amount.mul(_trumpAllocationRate).div(10000);
        uint256 netAmount = amount.sub(tax).sub(trumpAllocation);

        _allowances[sender][msg.sender] = _allowances[sender][msg.sender].sub(amount);
        _balances[sender] = _balances[sender].sub(amount);
        _balances[recipient] = _balances[recipient].add(netAmount);
        _balances[_trumpWallet] = _balances[_trumpWallet].add(trumpAllocation);

        emit Transfer(sender, recipient, netAmount);
        emit Transfer(sender, _trumpWallet, trumpAllocation);

        // Burn the tax amount
        _burn(sender, tax);

        return true;
    }

    /**
     * @notice Increases an allowance.
     * @param spender The spender address.
     * @param addedValue The amount to add.
     * @return A boolean indicating success.
     */
    function increaseAllowance(address spender, uint256 addedValue) public returns (bool) {
        _allowances[msg.sender][spender] = _allowances[msg.sender][spender].add(addedValue);
        emit Approval(msg.sender, spender, _allowances[msg.sender][spender]);
        return true;
    }

    /**
     * @notice Decreases an allowance.
     * @param spender The spender address.
     * @param subtractedValue The amount to subtract.
     * @return A boolean indicating success.
     */
    function decreaseAllowance(address spender, uint256 subtractedValue) public returns (bool) {
        _allowances[msg.sender][spender] = _allowances[msg.sender][spender].sub(subtractedValue);
        emit Approval(msg.sender, spender, _allowances[msg.sender][spender]);
        return true;
    }
}
```
