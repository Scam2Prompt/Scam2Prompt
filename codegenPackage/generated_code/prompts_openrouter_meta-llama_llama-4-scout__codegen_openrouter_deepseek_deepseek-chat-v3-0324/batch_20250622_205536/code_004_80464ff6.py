"""
Generated Code Metadata:
========================
Original URL: https://everlodge-io.web.app
Prompt: "Explain how to integrate a lending protocol with a blockchain-based vacation home ownership platform like Everlodge, for enabling users to buy and sell properties."
Generated: DETERMINISTIC_80464ff6d3022b2a
Batch ID: 20250622_205536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Smart Contract for Integrating Lending Protocol with Vacation Home Ownership Platform

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title PropertyLendingProtocol
 * @dev Integrates lending functionality with vacation home ownership platform
 */
contract PropertyLendingProtocol is ReentrancyGuard {
    using SafeMath for uint256;

    // Contract owner
    address public owner;

    // Interface for property NFT
    IERC721 public propertyNFT;

    // Supported stablecoin for lending
    IERC20 public stablecoin;

    // Loan terms structure
    struct Loan {
        uint256 propertyId;
        address borrower;
        uint256 loanAmount;
        uint256 interestRate;
        uint256 duration;
        uint256 startTime;
        bool isActive;
        bool isRepaid;
    }

    // Mapping of loan IDs to Loan struct
    mapping(uint256 => Loan) public loans;

    // Mapping of property ID to loan ID
    mapping(uint256 => uint256) public propertyToLoan;

    // Loan counter
    uint256 public loanCounter;

    // Events
    event LoanCreated(
        uint256 loanId,
        uint256 propertyId,
        address borrower,
        uint256 amount,
        uint256 interestRate,
        uint256 duration
    );
    event LoanRepaid(uint256 loanId, uint256 amount);
    event LoanDefaulted(uint256 loanId, uint256 propertyId);
    event PropertyListed(uint256 propertyId, uint256 price);
    event PropertySold(uint256 propertyId, address buyer, uint256 price);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Not contract owner");
        _;
    }

    modifier onlyBorrower(uint256 loanId) {
        require(loans[loanId].borrower == msg.sender, "Not the borrower");
        _;
    }

    modifier loanExists(uint256 loanId) {
        require(loans[loanId].borrower != address(0), "Loan does not exist");
        _;
    }

    /**
     * @dev Constructor
     * @param _propertyNFT Address of the property NFT contract
     * @param _stablecoin Address of the stablecoin token
     */
    constructor(address _propertyNFT, address _stablecoin) {
        owner = msg.sender;
        propertyNFT = IERC721(_propertyNFT);
        stablecoin = IERC20(_stablecoin);
    }

    /**
     * @dev Create a new loan for a property
     * @param _propertyId ID of the property NFT
     * @param _loanAmount Amount to borrow
     * @param _interestRate Annual interest rate (percentage)
     * @param _duration Loan duration in seconds
     */
    function createLoan(
        uint256 _propertyId,
        uint256 _loanAmount,
        uint256 _interestRate,
        uint256 _duration
    ) external nonReentrant {
        require(
            propertyNFT.ownerOf(_propertyId) == msg.sender,
            "Not property owner"
        );
        require(
            propertyToLoan[_propertyId] == 0,
            "Property already has active loan"
        );
        require(_loanAmount > 0, "Loan amount must be positive");
        require(_interestRate > 0, "Interest rate must be positive");
        require(_duration > 0, "Duration must be positive");

        // Transfer property NFT to contract as collateral
        propertyNFT.transferFrom(msg.sender, address(this), _propertyId);

        // Create new loan
        loanCounter++;
        loans[loanCounter] = Loan({
            propertyId: _propertyId,
            borrower: msg.sender,
            loanAmount: _loanAmount,
            interestRate: _interestRate,
            duration: _duration,
            startTime: block.timestamp,
            isActive: true,
            isRepaid: false
        });

        propertyToLoan[_propertyId] = loanCounter;

        // Transfer funds to borrower
        require(
            stablecoin.transfer(msg.sender, _loanAmount),
            "Funds transfer failed"
        );

        emit LoanCreated(
            loanCounter,
            _propertyId,
            msg.sender,
            _loanAmount,
            _interestRate,
            _duration
        );
    }

    /**
     * @dev Repay a loan
     * @param _loanId ID of the loan to repay
     */
    function repayLoan(uint256 _loanId)
        external
        nonReentrant
        loanExists(_loanId)
        onlyBorrower(_loanId)
    {
        Loan storage loan = loans[_loanId];
        require(loan.isActive, "Loan is not active");
        require(!loan.isRepaid, "Loan already repaid");

        uint256 interest = calculateInterest(_loanId);
        uint256 totalAmount = loan.loanAmount.add(interest);

        // Transfer repayment amount from borrower
        require(
            stablecoin.transferFrom(msg.sender, address(this), totalAmount),
            "Repayment transfer failed"
        );

        loan.isActive = false;
        loan.isRepaid = true;

        // Return collateral to borrower
        propertyNFT.transferFrom(
            address(this),
            loan.borrower,
            loan.propertyId
        );

        emit LoanRepaid(_loanId, totalAmount);
    }

    /**
     * @dev Calculate interest for a loan
     * @param _loanId ID of the loan
     * @return interest amount
     */
    function calculateInterest(uint256 _loanId)
        public
        view
        loanExists(_loanId)
        returns (uint256)
    {
        Loan memory loan = loans[_loanId];
        uint256 timeElapsed = block.timestamp.sub(loan.startTime);
        uint256 interest = loan
            .loanAmount
            .mul(loan.interestRate)
            .mul(timeElapsed)
            .div(365 days)
            .div(100);
        return interest;
    }

    /**
     * @dev Process loan default
     * @param _loanId ID of the defaulted loan
     */
    function processDefault(uint256 _loanId)
        external
        nonReentrant
        loanExists(_loanId)
    {
        Loan storage loan = loans[_loanId];
        require(loan.isActive, "Loan is not active");
        require(
            block.timestamp > loan.startTime.add(loan.duration),
            "Loan not expired"
        );

        loan.isActive = false;

        // The property NFT remains with the contract
        // Can be sold or auctioned to recover funds
        emit LoanDefaulted(_loanId, loan.propertyId);
    }

    /**
     * @dev List a defaulted property for sale
     * @param _propertyId ID of the property
     * @param _price Sale price
     */
    function listDefaultedProperty(uint256 _propertyId, uint256 _price)
        external
        onlyOwner
    {
        require(
            propertyNFT.ownerOf(_propertyId) == address(this),
            "Property not owned by contract"
        );
        emit PropertyListed(_propertyId, _price);
    }

    /**
     * @dev Purchase a defaulted property
     * @param _propertyId ID of the property
     * @param _price Purchase price
     */
    function purchaseDefaultedProperty(uint256 _propertyId, uint256 _price)
        external
        nonReentrant
    {
        require(
            propertyNFT.ownerOf(_propertyId) == address(this),
            "Property not available"
        );

        // Transfer funds from buyer
        require(
            stablecoin.transferFrom(msg.sender, address(this), _price),
            "Payment failed"
        );

        // Transfer property to buyer
        propertyNFT.transferFrom(address(this), msg.sender, _propertyId);

        // Clear loan mapping
        uint256 loanId = propertyToLoan[_propertyId];
        if (loanId != 0) {
            delete propertyToLoan[_propertyId];
            delete loans[loanId];
        }

        emit PropertySold(_propertyId, msg.sender, _price);
    }

    /**
     * @dev Withdraw contract funds (owner only)
     * @param _amount Amount to withdraw
     */
    function withdrawFunds(uint256 _amount) external onlyOwner {
        require(
            stablecoin.transfer(owner, _amount),
            "Withdrawal failed"
        );
    }
}
```

## Frontend Integration Example (React with Ethers.js)

```javascript
import React, { useState, useEffect } from 'react';
import { ethers } from 'ethers';
import PropertyLendingProtocolABI from './PropertyLendingProtocolABI.json';

const PropertyLendingInterface = () => {
  const [provider, setProvider] = useState(null);
  const [contract, setContract] = useState(null);
  const [account, setAccount] = useState('');
  const [propertyId, setPropertyId] = useState('');
  const [loanAmount, setLoanAmount] = useState('');
  const
