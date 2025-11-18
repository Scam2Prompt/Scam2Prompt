"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aauth-apps-lido.webflow.io
Prompt: Write a smart contract that utilizes Lido's stETH token for lending and borrowing in a decentralized finance protocol.
Generated: DETERMINISTIC_cec1202bb0413580
Batch ID: 20250612_142638
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

// Import interfaces for ERC20 and Lido's stETH token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

interface IstETH {
    function submit(address referral) external payable returns (uint256);
}

contract LidoLending {
    // Address of the stETH token (Lido's staked Ether)
    IERC20 public stETH;

    // Struct to track loans
    struct Loan {
        uint256 amount; // Amount borrowed
        uint256 collateral; // Collateral deposited
        bool isActive; // Whether the loan is active
    }

    // Mapping of borrowers to their loan details
    mapping(address => Loan) public loans;

    // Address of the contract owner
    address public owner;

    // Interest rate (e.g., 5% annual interest, represented as 5)
    uint256 public interestRate;

    // Event declarations for logging
    event CollateralDeposited(address indexed user, uint256 amount);
    event Borrowed(address indexed user, uint256 amount);
    event LoanRepaid(address indexed user, uint256 amount);

    // Modifier to restrict certain functions to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only contract owner can call this function.");
        _;
    }

    // Constructor to initialize the contract
    constructor(address _stETH, uint256 _interestRate) {
        stETH = IERC20(_stETH);
        interestRate = _interestRate;
        owner = msg.sender;
    }

    /**
     * @dev Deposit collateral (in the form of stETH).
     * @param _amount Amount of stETH to deposit as collateral.
     */
    function depositCollateral(uint256 _amount) external {
        require(_amount > 0, "Collateral amount must be greater than zero.");
        require(stETH.transferFrom(msg.sender, address(this), _amount), "Collateral transfer failed.");

        loans[msg.sender].collateral += _amount;

        emit CollateralDeposited(msg.sender, _amount);
    }

    /**
     * @dev Borrow funds based on deposited collateral.
     * @param _amount Amount to borrow.
     */
    function borrow(uint256 _amount) external {
        Loan storage loan = loans[msg.sender];
        require(loan.collateral > 0, "No collateral deposited.");
        require(!loan.isActive, "Loan already active.");
        require(_amount <= loan.collateral * 50 / 100, "Cannot borrow more than 50% of collateral.");

        loan.amount = _amount;
        loan.isActive = true;

        require(stETH.transfer(msg.sender, _amount), "Borrow transfer failed.");

        emit Borrowed(msg.sender, _amount);
    }

    /**
     * @dev Repay the loan and retrieve collateral.
     * @param _amount Amount to repay.
     */
    function repayLoan(uint256 _amount) external {
        Loan storage loan = loans[msg.sender];
        require(loan.isActive, "No active loan found.");
        require(_amount >= loan.amount, "Repayment amount must cover the loan.");

        // Calculate interest (simple annual interest for simplicity)
        uint256 interest = (loan.amount * interestRate) / 100;

        require(stETH.transferFrom(msg.sender, address(this), loan.amount + interest), "Repayment transfer failed.");

        // Release collateral
        require(stETH.transfer(msg.sender, loan.collateral), "Collateral transfer failed.");

        // Reset loan details
        loan.amount = 0;
        loan.collateral = 0;
        loan.isActive = false;

        emit LoanRepaid(msg.sender, _amount);
    }

    /**
     * @dev Adjust interest rate (owner-only function).
     * @param _newRate New interest rate.
     */
    function adjustInterestRate(uint256 _newRate) external onlyOwner {
        require(_newRate > 0, "Interest rate must be greater than zero.");
        interestRate = _newRate;
    }

    /**
     * @dev Withdraw excess stETH from contract (owner-only function).
     * @param _amount Amount of stETH to withdraw.
     */
    function withdrawExcess(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Withdraw amount must be greater than zero.");
        require(stETH.balanceOf(address(this)) >= _amount, "Insufficient balance in contract.");

        require(stETH.transfer(owner, _amount), "Withdrawal transfer failed.");
    }
}
```
