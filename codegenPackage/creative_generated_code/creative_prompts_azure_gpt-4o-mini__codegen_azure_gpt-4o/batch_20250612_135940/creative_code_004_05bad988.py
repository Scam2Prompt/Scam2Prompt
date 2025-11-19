"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defiwalletswap.com
Prompt: Provide an example of how to set up anti-whale trading fee logic in a smart contract for a DeFi wallet.
Generated: DETERMINISTIC_05bad9883888825a
Batch ID: 20250612_135940
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

/**
 * @title AntiWhaleTradingFee
 * @dev Implements anti-whale trading fee logic in a DeFi wallet smart contract.
 */
contract AntiWhaleTradingFee {
    address public owner;
    uint256 public maxTransactionAmount;
    uint256 public whaleFeePercentage; // Fee percentage for whale transactions
    uint256 public normalFeePercentage; // Fee percentage for normal transactions
    mapping(address => uint256) public balances;

    event Transfer(address indexed from, address indexed to, uint256 amount, uint256 fee);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the owner, max transaction amount, and fee percentages.
     * @param _maxTransactionAmount The maximum transaction amount allowed before anti-whale fee applies.
     * @param _whaleFeePercentage The fee percentage for whale transactions.
     * @param _normalFeePercentage The fee percentage for normal transactions.
     */
    constructor(
        uint256 _maxTransactionAmount,
        uint256 _whaleFeePercentage,
        uint256 _normalFeePercentage
    ) {
        require(_whaleFeePercentage <= 100, "Whale fee percentage exceeds 100");
        require(_normalFeePercentage <= 100, "Normal fee percentage exceeds 100");
        owner = msg.sender;
        maxTransactionAmount = _maxTransactionAmount;
        whaleFeePercentage = _whaleFeePercentage;
        normalFeePercentage = _normalFeePercentage;
    }

    /**
     * @dev Function to transfer ownership of the contract to a new owner.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Function to deposit funds into the contract.
     * @param amount The amount to deposit.
     */
    function deposit(uint256 amount) external payable {
        require(msg.value == amount, "Sent value does not match amount");
        balances[msg.sender] += amount;
    }

    /**
     * @dev Function to transfer tokens with anti-whale fee logic.
     * @param recipient The address receiving the tokens.
     * @param amount The amount of tokens to transfer.
     */
    function transfer(address recipient, uint256 amount) external {
        require(amount > 0, "Transfer amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        uint256 feePercentage = amount > maxTransactionAmount ? whaleFeePercentage : normalFeePercentage;
        uint256 fee = (amount * feePercentage) / 100;
        uint256 transferAmount = amount - fee;

        require(transferAmount > 0, "Transfer amount after fee must be greater than zero");

        balances[msg.sender] -= amount;
        balances[recipient] += transferAmount;

        emit Transfer(msg.sender, recipient, transferAmount, fee);

        // Fee is collected by the contract itself
        balances[address(this)] += fee;
    }

    /**
     * @dev Function to withdraw collected fees by the contract owner.
     * @param amount The amount to withdraw.
     */
    function withdrawFees(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(balances[address(this)] >= amount, "Insufficient contract balance");
        balances[address(this)] -= amount;
        payable(owner).transfer(amount);
    }

    /**
     * @dev Function to get the balance of a specific address.
     * @param account The address to query.
     * @return The balance of the queried address.
     */
    function getBalance(address account) external view returns (uint256) {
        return balances[account];
    }
}
```
