"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://defie.me
Prompt: Generate a Solidity smart contract for a simple DeFi lending and borrowing system.
Generated: DETERMINISTIC_802edb1e597ad1ac
Batch ID: 20250612_154002
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
 * @title DeFi Lending and Borrowing Contract
 * @dev This contract allows users to deposit funds to earn interest and borrow funds by providing collateral.
 */
contract DeFiLending {
    // Struct to keep track of user balances
    struct UserAccount {
        uint256 depositBalance; // Amount deposited by the user
        uint256 borrowBalance;  // Amount borrowed by the user
    }

    // Mapping to store accounts of each user
    mapping(address => UserAccount) private userAccounts;

    // Interest rate for deposits and borrowing (in percentage, e.g., 5 = 5%)
    uint256 public constant depositInterestRate = 5; // Annual interest rate
    uint256 public constant borrowInterestRate = 10; // Annual borrow interest rate

    // Collateralization ratio (e.g., 150 means 150%)
    uint256 public constant collateralizationRatio = 150;

    // Owner of the contract
    address public owner;

    // Event declarations
    event Deposited(address indexed user, uint256 amount);
    event Borrowed(address indexed user, uint256 amount);
    event Repaid(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Allows a user to deposit funds into the contract.
     * @param _amount The amount of funds to deposit (in wei).
     */
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");

        // Update user's deposit balance
        userAccounts[msg.sender].depositBalance += msg.value;

        emit Deposited(msg.sender, msg.value);
    }

    /**
     * @dev Allows a user to borrow funds by providing collateral.
     * @param _amount The amount of funds to borrow (in wei).
     */
    function borrow(uint256 _amount) external {
        require(_amount > 0, "Borrow amount must be greater than zero");

        UserAccount storage account = userAccounts[msg.sender];

        // Calculate the maximum borrowable amount based on collateralization ratio
        uint256 maxBorrowable = (account.depositBalance * 100) / collateralizationRatio;
        require(_amount <= maxBorrowable, "Borrow amount exceeds collateral limit");

        // Update user's borrow balance
        account.borrowBalance += _amount;

        // Transfer borrowed funds to the user
        payable(msg.sender).transfer(_amount);

        emit Borrowed(msg.sender, _amount);
    }

    /**
     * @dev Allows a user to repay borrowed funds.
     * @param _amount The amount of funds to repay (in wei).
     */
    function repay() external payable {
        require(msg.value > 0, "Repayment amount must be greater than zero");

        UserAccount storage account = userAccounts[msg.sender];
        require(account.borrowBalance > 0, "No borrow balance to repay");

        // Update user's borrow balance
        uint256 repaymentAmount = msg.value;
        if (repaymentAmount > account.borrowBalance) {
            repaymentAmount = account.borrowBalance; // Cap repayment to borrow balance
        }
        account.borrowBalance -= repaymentAmount;

        emit Repaid(msg.sender, repaymentAmount);
    }

    /**
     * @dev Allows a user to withdraw their deposited funds. Ensures collateral requirements are met.
     * @param _amount The amount of funds to withdraw (in wei).
     */
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Withdraw amount must be greater than zero");

        UserAccount storage account = userAccounts[msg.sender];
        require(account.depositBalance >= _amount, "Insufficient deposit balance");

        // Ensure collateral requirements are met
        uint256 remainingCollateral = account.depositBalance - _amount;
        uint256 maxBorrowableAfterWithdrawal = (remainingCollateral * 100) / collateralizationRatio;
        require(account.borrowBalance <= maxBorrowableAfterWithdrawal, "Withdraw would violate collateral requirements");

        // Update user's deposit balance
        account.depositBalance -= _amount;

        // Transfer withdrawn funds to the user
        payable(msg.sender).transfer(_amount);

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Allows the owner to withdraw contract funds in case of emergency.
     * @param _amount The amount of funds to withdraw (in wei).
     */
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(address(this).balance >= _amount, "Insufficient contract balance");
        payable(owner).transfer(_amount);
    }

    /**
     * @dev Returns the deposit and borrow balances of a user.
     * @param _user The address of the user.
     * @return depositBalance The deposit balance of the user.
     * @return borrowBalance The borrow balance of the user.
     */
    function getUserBalances(address _user) external view returns (uint256 depositBalance, uint256 borrowBalance) {
        UserAccount storage account = userAccounts[_user];
        return (account.depositBalance, account.borrowBalance);
    }

    /**
     * @dev Returns the contract's current balance.
     * @return The balance of the contract (in wei).
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
