"""
Generated Code Metadata:
========================
Original URL: https://mixtoearn-migration.pages.dev
Prompt: Write a Solidity contract that enforces wallet and transaction limits, such as a maximum transaction of 1% of the total supply and a maximum wallet size of 2% of the total supply, similar to the $MTE tokenomics.
Generated: DETERMINISTIC_584c2cfe71381eea
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title LimitedERC20Token
 * @author [Your Name]
 * @notice ERC20 token with wallet and transaction limits.
 */
contract LimitedERC20Token is ERC20, ERC20Burnable, ReentrancyGuard {
    // Maximum transaction percentage of total supply
    uint256 public constant MAX_TRANSACTION_PERCENTAGE = 1;
    // Maximum wallet percentage of total supply
    uint256 public constant MAX_WALLET_PERCENTAGE = 2;

    // Mapping of wallet addresses to their current balances
    mapping(address => uint256) public balances;

    /**
     * @notice Constructor for the LimitedERC20Token contract.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     * @param totalSupply The total supply of the token.
     */
    constructor(string memory name, string memory symbol, uint256 totalSupply) ERC20(name, symbol) {
        _mint(msg.sender, totalSupply);
    }

    /**
     * @notice Checks if a transaction is within the allowed limits.
     * @param from The sender's address.
     * @param to The recipient's address.
     * @param amount The amount to be transferred.
     */
    function _checkTransactionLimits(address from, address to, uint256 amount) internal view {
        uint256 totalSupply = totalSupply();
        uint256 maxTransactionAmount = (totalSupply * MAX_TRANSACTION_PERCENTAGE) / 100;

        require(amount <= maxTransactionAmount, "Transaction amount exceeds the maximum allowed");
    }

    /**
     * @notice Checks if a wallet is within the allowed limits.
     * @param account The wallet address to check.
     */
    function _checkWalletLimit(address account) internal view {
        uint256 totalSupply = totalSupply();
        uint256 maxWalletAmount = (totalSupply * MAX_WALLET_PERCENTAGE) / 100;
        uint256 accountBalance = balanceOf(account);

        require(accountBalance <= maxWalletAmount, "Wallet balance exceeds the maximum allowed");
    }

    /**
     * @notice Transfers tokens from one address to another.
     * @param from The sender's address.
     * @param to The recipient's address.
     * @param amount The amount to be transferred.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transfer(address to, uint256 amount) public override nonReentrant returns (bool) {
        _checkTransactionLimits(msg.sender, to, amount);
        _checkWalletLimit(to);

        return super.transfer(to, amount);
    }

    /**
     * @notice Transfers tokens from one address to another on behalf of the owner.
     * @param from The sender's address.
     * @param to The recipient's address.
     * @param amount The amount to be transferred.
     * @return A boolean indicating whether the transfer was successful.
     */
    function transferFrom(
        address from,
        address to,
        uint256 amount
    ) public override nonReentrant returns (bool) {
        _checkTransactionLimits(from, to, amount);
        _checkWalletLimit(to);

        return super.transferFrom(from, to, amount);
    }

    /**
     * @notice Increases the balance of a given account.
     * @param account The account to increase the balance of.
     * @param amount The amount to increase the balance by.
     */
    function _mint(address account, uint256 amount) internal override {
        super._mint(account, amount);
        _checkWalletLimit(account);
    }

    /**
     * @notice Decreases the balance of a given account.
     * @param account The account to decrease the balance of.
     * @param amount The amount to decrease the balance by.
     */
    function _burn(address account, uint256 amount) internal override {
        super._burn(account, amount);
    }
}
```
