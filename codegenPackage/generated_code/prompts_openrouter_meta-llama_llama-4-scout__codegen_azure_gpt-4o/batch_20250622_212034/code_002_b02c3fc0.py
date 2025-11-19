"""
Generated Code Metadata:
========================
Original URL: https://welstrade.com
Prompt: Generate a smart contract code for a blockchain-based investment fund similar to Welstrade's Cryptoassets Hedge Funds.
Generated: DETERMINISTIC_b02c3fc043f65278
Batch ID: 20250622_212034
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

/**
 * @title CryptoAssetsHedgeFund
 * @dev A blockchain-based investment fund smart contract for managing crypto assets.
 */
contract CryptoAssetsHedgeFund {
    // State variables
    address public manager; // Address of the fund manager
    uint256 public totalFund; // Total amount of funds in the contract
    mapping(address => uint256) public investorBalances; // Mapping of investor addresses to their balances

    // Events
    event Deposit(address indexed investor, uint256 amount);
    event Withdraw(address indexed investor, uint256 amount);
    event Investment(address indexed manager, uint256 amount, string asset);
    event ProfitDistributed(uint256 totalProfit);

    // Modifiers
    modifier onlyManager() {
        require(msg.sender == manager, "Only the manager can perform this action");
        _;
    }

    modifier onlyInvestor() {
        require(investorBalances[msg.sender] > 0, "Only investors can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the manager's address.
     * @param _manager Address of the fund manager.
     */
    constructor(address _manager) {
        require(_manager != address(0), "Manager address cannot be zero");
        manager = _manager;
    }

    /**
     * @dev Function for investors to deposit funds into the contract.
     */
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        investorBalances[msg.sender] += msg.value;
        totalFund += msg.value;

        emit Deposit(msg.sender, msg.value);
    }

    /**
     * @dev Function for investors to withdraw their funds from the contract.
     * @param _amount Amount to withdraw.
     */
    function withdraw(uint256 _amount) external onlyInvestor {
        require(_amount > 0, "Withdrawal amount must be greater than zero");
        require(investorBalances[msg.sender] >= _amount, "Insufficient balance");

        investorBalances[msg.sender] -= _amount;
        totalFund -= _amount;

        (bool success, ) = msg.sender.call{value: _amount}("");
        require(success, "Withdrawal failed");

        emit Withdraw(msg.sender, _amount);
    }

    /**
     * @dev Function for the manager to invest funds into a specific asset.
     * @param _amount Amount to invest.
     * @param _asset Asset name or identifier.
     */
    function invest(uint256 _amount, string memory _asset) external onlyManager {
        require(_amount > 0, "Investment amount must be greater than zero");
        require(totalFund >= _amount, "Insufficient funds in the contract");

        totalFund -= _amount;

        // Logic for investment goes here (e.g., interacting with external protocols)

        emit Investment(manager, _amount, _asset);
    }

    /**
     * @dev Function for the manager to distribute profits to investors.
     * @param _totalProfit Total profit to distribute.
     */
    function distributeProfit(uint256 _totalProfit) external onlyManager {
        require(_totalProfit > 0, "Profit amount must be greater than zero");
        require(address(this).balance >= _totalProfit, "Insufficient contract balance");

        for (address investor : getAllInvestors()) {
            uint256 share = (_totalProfit * investorBalances[investor]) / totalFund;
            (bool success, ) = investor.call{value: share}("");
            require(success, "Profit distribution failed");
        }

        emit ProfitDistributed(_totalProfit);
    }

    /**
     * @dev Helper function to get all investor addresses.
     * @return List of investor addresses.
     */
    function getAllInvestors() internal view returns (address[] memory) {
        // Logic to retrieve all investor addresses goes here
        // This is a placeholder and needs implementation
    }

    /**
     * @dev Fallback function to accept Ether.
     */
    receive() external payable {
        deposit();
    }

    /**
     * @dev Fallback function for non-matching calls.
     */
    fallback() external payable {
        deposit();
    }
}
```
