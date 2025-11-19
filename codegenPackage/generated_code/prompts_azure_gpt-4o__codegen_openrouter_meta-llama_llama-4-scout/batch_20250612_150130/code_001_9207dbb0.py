"""
Generated Code Metadata:
========================
Original URL: https://gasprofitsoftware.com
Prompt: Generate a smart contract in Solidity that facilitates decentralized finance transactions without intermediaries, ensuring transparency and low transaction fees, as outlined by Gas Profit.
Generated: DETERMINISTIC_9207dbb06803d448
Batch ID: 20250612_150130
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";

/**
 * @title GasProfit Contract
 * @author [Your Name]
 * @notice A decentralized finance contract facilitating transactions without intermediaries.
 */
contract GasProfit {
    using SafeMath for uint256;

    // Mapping of user balances
    mapping (address => uint256) public balances;

    // Mapping of transaction history
    mapping (address => mapping (address => uint256)) public transactionHistory;

    // Event emitted when a transaction is made
    event TransactionMade(address indexed from, address indexed to, uint256 amount);

    // Event emitted when a user deposits funds
    event DepositMade(address indexed user, uint256 amount);

    // Event emitted when a user withdraws funds
    event WithdrawalMade(address indexed user, uint256 amount);

    // Address of the ERC20 token used for transactions
    address public tokenAddress;

    /**
     * @dev Constructor function
     * @param _tokenAddress Address of the ERC20 token used for transactions
     */
    constructor(address _tokenAddress) public {
        require(_tokenAddress != address(0), "Token address cannot be zero");
        tokenAddress = _tokenAddress;
    }

    /**
     * @dev Deposits funds into the contract
     * @param _amount Amount of funds to deposit
     */
    function deposit(uint256 _amount) public {
        require(_amount > 0, "Deposit amount must be greater than zero");
        IERC20(tokenAddress).transferFrom(msg.sender, address(this), _amount);
        balances[msg.sender] = balances[msg.sender].add(_amount);
        emit DepositMade(msg.sender, _amount);
    }

    /**
     * @dev Withdraws funds from the contract
     * @param _amount Amount of funds to withdraw
     */
    function withdraw(uint256 _amount) public {
        require(_amount > 0, "Withdrawal amount must be greater than zero");
        require(balances[msg.sender] >= _amount, "Insufficient balance");
        balances[msg.sender] = balances[msg.sender].sub(_amount);
        IERC20(tokenAddress).transfer(msg.sender, _amount);
        emit WithdrawalMade(msg.sender, _amount);
    }

    /**
     * @dev Transfers funds to another user
     * @param _to Address of the recipient
     * @param _amount Amount of funds to transfer
     */
    function transfer(address _to, uint256 _amount) public {
        require(_to != address(0), "Recipient address cannot be zero");
        require(_amount > 0, "Transfer amount must be greater than zero");
        require(balances[msg.sender] >= _amount, "Insufficient balance");
        balances[msg.sender] = balances[msg.sender].sub(_amount);
        balances[_to] = balances[_to].add(_amount);
        transactionHistory[msg.sender][_to] = transactionHistory[msg.sender][_to].add(_amount);
        IERC20(tokenAddress).transfer(_to, _amount);
        emit TransactionMade(msg.sender, _to, _amount);
    }

    /**
     * @dev Gets the balance of a user
     * @param _user Address of the user
     * @return Balance of the user
     */
    function getBalance(address _user) public view returns (uint256) {
        return balances[_user];
    }

    /**
     * @dev Gets the transaction history between two users
     * @param _from Address of the sender
     * @param _to Address of the recipient
     * @return Transaction history between the two users
     */
    function getTransactionHistory(address _from, address _to) public view returns (uint256) {
        return transactionHistory[_from][_to];
    }
}
```
