"""
Generated Code Metadata:
========================
Original URL: https://wikicat-coin.web.app
Prompt: Create a smart contract in Solidity for a new token that mimics Wiki Cat's tokenomics, including a 2% transaction tax split between a burn wallet and a fee wallet, and ensure the contract includes liquidity locking using Unicrypt.
Generated: DETERMINISTIC_aebfb5ca4f9092c2
Batch ID: 20250612_152326
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
import "./Unicrypt.sol";

contract WikiCatToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of addresses to their respective balances
    mapping(address => uint256) private _balances;

    // Mapping of addresses to their respective allowances
    mapping(address => mapping(address => uint256)) private _allowances;

    // Constants for transaction tax and wallet addresses
    uint256 public constant TRANSACTION_TAX = 200; // 2%
    address public immutable BURN_WALLET;
    address public immutable FEE_WALLET;
    address public immutable UNICRYPT_LOCKING_CONTRACT;

    // Flag to track if liquidity locking is enabled
    bool public liquidityLocked;

    /**
     * @dev Constructor for the WikiCatToken contract
     * @param burnWallet Address of the burn wallet
     * @param feeWallet Address of the fee wallet
     * @param unicryptLockingContract Address of the Unicrypt locking contract
     */
    constructor(address burnWallet, address feeWallet, address unicryptLockingContract) ERC20("Wiki Cat", "WKC") {
        BURN_WALLET = burnWallet;
        FEE_WALLET = feeWallet;
        UNICRYPT_LOCKING_CONTRACT = unicryptLockingContract;

        // Mint initial supply to the contract creator
        _mint(msg.sender, 1000 * 10**18);

        // Approve Unicrypt locking contract to spend tokens on behalf of the contract creator
        _approve(msg.sender, UNICRYPT_LOCKING_CONTRACT, 1000 * 10**18);
    }

    /**
     * @dev Transfers tokens from one address to another, applying transaction tax
     * @param from Address to transfer tokens from
     * @param to Address to transfer tokens to
     * @param amount Amount of tokens to transfer
     * @return bool indicating success of the transfer
     */
    function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        uint256 tax = amount.mul(TRANSACTION_TAX).div(10000);
        uint256 burnAmount = tax.div(2);
        uint256 feeAmount = tax.sub(burnAmount);

        // Burn transaction tax
        _burn(msg.sender, amount.sub(tax));

        // Transfer remaining amount to recipient
        _transfer(msg.sender, to, amount.sub(tax));

        // Transfer burn amount to burn wallet
        _transfer(msg.sender, BURN_WALLET, burnAmount);

        // Transfer fee amount to fee wallet
        _transfer(msg.sender, FEE_WALLET, feeAmount);

        return true;
    }

    /**
     * @dev Transfers tokens from one address to another on behalf of a third party, applying transaction tax
     * @param from Address to transfer tokens from
     * @param to Address to transfer tokens to
     * @param amount Amount of tokens to transfer
     * @return bool indicating success of the transfer
     */
    function transferFrom(address from, address to, uint256 amount) public override nonReentrant returns (bool) {
        uint256 tax = amount.mul(TRANSACTION_TAX).div(10000);
        uint256 burnAmount = tax.div(2);
        uint256 feeAmount = tax.sub(burnAmount);

        // Burn transaction tax
        _burn(from, amount.sub(tax));

        // Transfer remaining amount to recipient
        _transfer(from, to, amount.sub(tax));

        // Transfer burn amount to burn wallet
        _transfer(from, BURN_WALLET, burnAmount);

        // Transfer fee amount to fee wallet
        _transfer(from, FEE_WALLET, feeAmount);

        // Decrease allowance
        _approve(from, msg.sender, _allowances[from][msg.sender].sub(amount));

        return true;
    }

    /**
     * @dev Locks liquidity using Unicrypt
     * @param amount Amount of tokens to lock
     */
    function lockLiquidity(uint256 amount) public {
        require(msg.sender == owner(), "Only the contract owner can lock liquidity");
        require(!liquidityLocked, "Liquidity is already locked");

        // Approve Unicrypt locking contract to spend tokens on behalf of the contract
        _approve(address(this), UNICRYPT_LOCKING_CONTRACT, amount);

        // Lock liquidity using Unicrypt
        Unicrypt(UNICRYPT_LOCKING_CONTRACT).lockLiquidity(amount);

        liquidityLocked = true;
    }

    /**
     * @dev Unlocks liquidity using Unicrypt
     */
    function unlockLiquidity() public {
        require(msg.sender == owner(), "Only the contract owner can unlock liquidity");
        require(liquidityLocked, "Liquidity is not locked");

        // Unlock liquidity using Unicrypt
        Unicrypt(UNICRYPT_LOCKING_CONTRACT).unlockLiquidity();

        liquidityLocked = false;
    }

    // Helper functions
    function _transfer(address sender, address recipient, uint256 amount) internal virtual override {
        require(sender != address(0), "ERC20: transfer from the zero address");
        require(recipient != address(0), "ERC20: transfer to the zero address");

        _balances[sender] = _balances[sender].sub(amount);
        _balances[recipient] = _balances[recipient].add(amount);
        emit Transfer(sender, recipient, amount);
    }

    function _burn(address account, uint256 amount) internal virtual override {
        require(account != address(0), "ERC20: burn from the zero address");

        _balances[account] = _balances[account].sub(amount);
        _totalSupply = _totalSupply.sub(amount);
        emit Transfer(account, address(0), amount);
    }
}
```
