"""
Generated Code Metadata:
========================
Original URL: https://defihalal.org
Prompt: Write a smart contract that integrates halal-compliant financial principles for use in a DeFi application.
Generated: DETERMINISTIC_d800c3556916add2
Batch ID: 20250612_145117
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
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title HalalCompliantFinancialContract
 * @author [Your Name]
 * @notice A smart contract that integrates halal-compliant financial principles for use in a DeFi application.
 */
contract HalalCompliantFinancialContract is Ownable {
    using SafeMath for uint256;

    // Mapping of users to their account balances
    mapping (address => uint256) private balances;

    // Mapping of users to their account transaction counts
    mapping (address => uint256) private transactionCounts;

    // Maximum allowed transaction count per user
    uint256 public maxTransactionCount;

    // Minimum and maximum allowed investment amounts
    uint256 public minInvestmentAmount;
    uint256 public maxInvestmentAmount;

    // List of approved investment assets (ERC20 tokens)
    mapping (address => bool) public approvedAssets;

    // Event emitted when a user invests
    event InvestmentMade(address indexed user, address indexed asset, uint256 amount);

    // Event emitted when a user withdraws
    event WithdrawalMade(address indexed user, address indexed asset, uint256 amount);

    /**
     * @dev Constructor function
     * @param _maxTransactionCount Maximum allowed transaction count per user
     * @param _minInvestmentAmount Minimum allowed investment amount
     * @param _maxInvestmentAmount Maximum allowed investment amount
     */
    constructor(uint256 _maxTransactionCount, uint256 _minInvestmentAmount, uint256 _maxInvestmentAmount) public {
        maxTransactionCount = _maxTransactionCount;
        minInvestmentAmount = _minInvestmentAmount;
        maxInvestmentAmount = _maxInvestmentAmount;
    }

    /**
     * @dev Adds an asset to the list of approved investment assets
     * @param _asset Address of the ERC20 token to approve
     */
    function addApprovedAsset(address _asset) public onlyOwner {
        require(ERC20(_asset).totalSupply() > 0, "Invalid asset");
        approvedAssets[_asset] = true;
    }

    /**
     * @dev Removes an asset from the list of approved investment assets
     * @param _asset Address of the ERC20 token to remove
     */
    function removeApprovedAsset(address _asset) public onlyOwner {
        approvedAssets[_asset] = false;
    }

    /**
     * @dev Invests in an approved asset
     * @param _asset Address of the ERC20 token to invest in
     * @param _amount Amount to invest
     */
    function invest(address _asset, uint256 _amount) public {
        require(approvedAssets[_asset], "Asset not approved");
        require(_amount >= minInvestmentAmount && _amount <= maxInvestmentAmount, "Invalid investment amount");
        require(transactionCounts[msg.sender] < maxTransactionCount, "Transaction count exceeded");

        // Transfer investment amount from user's wallet to contract
        require(ERC20(_asset).transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        // Update user's balance and transaction count
        balances[msg.sender] = balances[msg.sender].add(_amount);
        transactionCounts[msg.sender]++;

        emit InvestmentMade(msg.sender, _asset, _amount);
    }

    /**
     * @dev Withdraws from an approved asset
     * @param _asset Address of the ERC20 token to withdraw from
     * @param _amount Amount to withdraw
     */
    function withdraw(address _asset, uint256 _amount) public {
        require(approvedAssets[_asset], "Asset not approved");
        require(balances[msg.sender] >= _amount, "Insufficient balance");

        // Update user's balance
        balances[msg.sender] = balances[msg.sender].sub(_amount);

        // Transfer withdrawal amount from contract to user's wallet
        require(ERC20(_asset).transfer(msg.sender, _amount), "Transfer failed");

        emit WithdrawalMade(msg.sender, _asset, _amount);
    }

    /**
     * @dev Gets a user's balance
     * @param _user Address of the user
     * @return User's balance
     */
    function getBalance(address _user) public view returns (uint256) {
        return balances[_user];
    }
}
```
