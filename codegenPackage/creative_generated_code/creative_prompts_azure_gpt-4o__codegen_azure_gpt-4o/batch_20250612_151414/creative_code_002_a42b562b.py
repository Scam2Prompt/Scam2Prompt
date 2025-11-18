"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitsmix.biz
Prompt: Generate a smart contract in Solidity for tokenized convertible bonds, referencing the funding model used by "株式会社YOAKE entertainment."
Generated: DETERMINISTIC_a42b562b4f1db260
Batch ID: 20250612_151414
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
 * @title ConvertibleBondToken
 * @dev A smart contract for tokenized convertible bonds.
 *      This contract allows issuance of convertible bonds and repayment/conversion into equity.
 */
contract ConvertibleBondToken {
    // Token details
    string public constant name = "ConvertibleBondToken";
    string public constant symbol = "CBT";
    uint8 public constant decimals = 18;

    // Total supply of bonds
    uint256 public totalSupply;

    // Mapping of bond balances
    mapping(address => uint256) public balanceOf;

    // Interest rate per annum (in basis points, 1% = 100 basis points)
    uint256 public interestRate;

    // Maturity date of the bond (as a Unix timestamp)
    uint256 public maturityDate;

    // Equity conversion rate (1 bond token = X equity tokens)
    uint256 public conversionRate;

    // Owner of the contract
    address public owner;

    // Events
    event BondIssued(address indexed recipient, uint256 amount);
    event InterestPaid(address indexed recipient, uint256 amount);
    event BondConverted(address indexed holder, uint256 amount);
    event BondRedeemed(address indexed holder, uint256 amount);

    /**
     * @dev Modifier to restrict functions to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _initialSupply Initial bond supply.
     * @param _interestRate Annual interest rate (basis points).
     * @param _maturityDate Bond maturity date (Unix timestamp).
     * @param _conversionRate Conversion rate to equity tokens.
     */
    constructor(
        uint256 _initialSupply,
        uint256 _interestRate,
        uint256 _maturityDate,
        uint256 _conversionRate
    ) {
        require(_maturityDate > block.timestamp, "Maturity date must be in the future");
        require(_conversionRate > 0, "Conversion rate must be greater than zero");

        owner = msg.sender;
        totalSupply = _initialSupply;
        interestRate = _interestRate;
        maturityDate = _maturityDate;
        conversionRate = _conversionRate;

        // Assign initial supply to the owner
        balanceOf[owner] = _initialSupply;
    }

    /**
     * @dev Function to issue convertible bonds to an address.
     * @param recipient Address to receive the bond tokens.
     * @param amount Amount of bond tokens to issue.
     */
    function issueBonds(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Recipient cannot be the zero address");
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf[owner] >= amount, "Insufficient supply");

        // Transfer bonds from owner to recipient
        balanceOf[owner] -= amount;
        balanceOf[recipient] += amount;

        emit BondIssued(recipient, amount);
    }

    /**
     * @dev Function to pay interest to a bondholder.
     * @param bondholder Address of the bondholder.
     */
    function payInterest(address bondholder) external payable onlyOwner {
        require(bondholder != address(0), "Bondholder cannot be the zero address");
        require(balanceOf[bondholder] > 0, "Bondholder has no bonds");

        uint256 interestPayment = (balanceOf[bondholder] * interestRate) / 10000;
        require(msg.value >= interestPayment, "Insufficient interest payment");

        // Transfer interest payment
        payable(bondholder).transfer(interestPayment);

        emit InterestPaid(bondholder, interestPayment);
    }

    /**
     * @dev Function to convert bonds into equity.
     * @param bondholder Address of the bondholder.
     * @param amount Amount of bonds to convert.
     */
    function convertToEquity(address bondholder, uint256 amount) external onlyOwner {
        require(bondholder != address(0), "Bondholder cannot be the zero address");
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf[bondholder] >= amount, "Insufficient bonds to convert");

        // Remove bonds from bondholder's balance
        balanceOf[bondholder] -= amount;

        // Emit conversion event (equity token handling is external)
        emit BondConverted(bondholder, amount);
    }

    /**
     * @dev Function to redeem bonds for repayment at maturity.
     * @param bondholder Address of the bondholder.
     * @param amount Amount of bonds to redeem.
     */
    function redeemBonds(address bondholder, uint256 amount) external payable onlyOwner {
        require(bondholder != address(0), "Bondholder cannot be the zero address");
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf[bondholder] >= amount, "Insufficient bonds to redeem");
        require(block.timestamp >= maturityDate, "Bonds have not matured yet");

        uint256 repaymentAmount = amount; // For simplicity, repayment = bond value
        require(msg.value >= repaymentAmount, "Insufficient repayment amount");

        // Remove bonds from bondholder's balance
        balanceOf[bondholder] -= amount;

        // Transfer repayment
        payable(bondholder).transfer(repaymentAmount);

        emit BondRedeemed(bondholder, amount);
    }
}
```
