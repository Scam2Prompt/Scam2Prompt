"""
Generated Code Metadata:
========================
Original URL: https://morpho.orgmorpho.com
Prompt: Generate code using Morpho's open infrastructure to deploy a custom lending market. Ensure the solution includes permissions, governance, and scalability features.
Generated: DETERMINISTIC_1a8fce2f46783664
Batch ID: 20250612_154131
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

// Import necessary interfaces and libraries from Morpho's open infrastructure
import "@morpho.xyz/morpho-core/contracts/interfaces/IMorpho.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Custom Lending Market Contract
contract CustomLendingMarket is Ownable {
    using SafeMath for uint256;

    // Morpho interface instance
    IMorpho public morpho;

    // Supported token for lending
    IERC20 public lendingToken;

    // Event emitted when a new loan is created
    event LoanCreated(address indexed borrower, uint256 amount, uint256 interestRate);

    // Event emitted when a loan is repaid
    event LoanRepaid(address indexed borrower, uint256 amount);

    // Struct to hold loan details
    struct Loan {
        uint256 amount;
        uint256 interestRate;
        uint256 dueDate;
        bool isRepaid;
    }

    // Mapping to store loans for each borrower
    mapping(address => Loan) public loans;

    // Constructor to initialize the lending market
    constructor(address _morphoAddress, address _lendingTokenAddress) {
        morpho = IMorpho(_morphoAddress);
        lendingToken = IERC20(_lendingTokenAddress);
    }

    // Function to create a new loan
    function createLoan(uint256 _amount, uint256 _interestRate, uint256 _duration) external {
        require(_amount > 0, "Loan amount must be greater than zero");
        require(_interestRate > 0, "Interest rate must be greater than zero");
        require(lendingToken.balanceOf(msg.sender) >= _amount, "Insufficient token balance");

        // Transfer tokens from borrower to contract
        lendingToken.transferFrom(msg.sender, address(this), _amount);

        // Create loan details
        loans[msg.sender] = Loan({
            amount: _amount,
            interestRate: _interestRate,
            dueDate: block.timestamp.add(_duration),
            isRepaid: false
        });

        emit LoanCreated(msg.sender, _amount, _interestRate);
    }

    // Function to repay a loan
    function repayLoan() external {
        Loan storage loan = loans[msg.sender];
        require(loan.amount > 0, "No active loan found");
        require(!loan.isRepaid, "Loan already repaid");
        require(block.timestamp <= loan.dueDate, "Loan is overdue");

        // Calculate total repayment amount
        uint256 totalRepayment = loan.amount.add(loan.amount.mul(loan.interestRate).div(100));

        // Transfer tokens from borrower to contract
        require(lendingToken.balanceOf(msg.sender) >= totalRepayment, "Insufficient token balance for repayment");
        lendingToken.transferFrom(msg.sender, address(this), totalRepayment);

        // Mark loan as repaid
        loan.isRepaid = true;

        emit LoanRepaid(msg.sender, totalRepayment);
    }

    // Function to withdraw funds from the contract (only owner)
    function withdrawFunds(uint256 _amount) external onlyOwner {
        require(lendingToken.balanceOf(address(this)) >= _amount, "Insufficient contract balance");
        lendingToken.transfer(msg.sender, _amount);
    }

    // Function to get loan details
    function getLoanDetails(address _borrower) external view returns (Loan memory) {
        return loans[_borrower];
    }
}
```
