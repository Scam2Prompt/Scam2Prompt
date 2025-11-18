"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mixtoearn-migration.pages.dev
Prompt: Write a Solidity contract that enforces wallet and transaction limits, such as a maximum transaction of 1% of the total supply and a maximum wallet size of 2% of the total supply, similar to the $MTE tokenomics.
Generated: DETERMINISTIC_584c2cfe71381eea
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import necessary OpenZeppelin contracts for safe math and access control
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Custom ERC20 token contract with wallet and transaction limits
contract LimitedToken is ERC20, Ownable {
    // Maximum transaction amount as a percentage of total supply
    uint256 public maxTransactionAmount;
    // Maximum wallet size as a percentage of total supply
    uint256 public maxWalletSize;
    // Total supply of the token
    uint256 private _totalSupply;

    // Mapping to store balances
    mapping(address => uint256) private _balances;

    // Emits when the transaction limits are updated
    event TransactionLimitsUpdated(uint256 maxTransactionAmount, uint256 maxWalletSize);

    // Constructor to initialize the token and set limits
    constructor(uint256 totalSupply) ERC20("LimitedToken", "LMT") {
        _totalSupply = totalSupply * (10 ** decimals());
        _mint(msg.sender, _totalSupply);
        
        // Set initial limits to 1% and 2% of the total supply
        maxTransactionAmount = _totalSupply / 100; // 1%
        maxWalletSize = (_totalSupply * 2) / 100; // 2%
    }

    // Override the _transfer function to enforce limits
    function _transfer(address sender, address recipient, uint256 amount) internal override {
        require(sender != address(0), "Transfer from the zero address");
        require(recipient != address(0), "Transfer to the zero address");
        require(amount > 0, "Transfer amount must be greater than zero");

        // Check for maximum transaction limit
        require(amount <= maxTransactionAmount, "Transaction amount exceeds the max limit");

        // Check for maximum wallet size limit
        uint256 recipientBalance = balanceOf(recipient);
        require(recipientBalance + amount <= maxWalletSize, "Wallet size exceeds the max limit");

        // Call the parent _transfer function
        super._transfer(sender, recipient, amount);
    }

    // Function to update transaction limits - onlyOwner can call
    function updateTransactionLimits(uint256 newMaxTransactionAmount, uint256 newMaxWalletSize) external onlyOwner {
        require(newMaxTransactionAmount > 0, "New transaction limit must be greater than zero");
        require(newMaxWalletSize > 0, "New wallet size limit must be greater than zero");

        maxTransactionAmount = newMaxTransactionAmount;
        maxWalletSize = newMaxWalletSize;

        emit TransactionLimitsUpdated(maxTransactionAmount, maxWalletSize);
    }

    // Function to get the total supply of the token
    function totalSupply() public view override returns (uint256) {
        return _totalSupply;
    }
}
```
