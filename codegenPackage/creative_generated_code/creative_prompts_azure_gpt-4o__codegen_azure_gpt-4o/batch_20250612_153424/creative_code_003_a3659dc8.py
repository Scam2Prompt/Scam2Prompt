"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iziswap.fi
Prompt: Write a smart contract in Solidity for a liquidity-mining-based bond like iUSD, ensuring it is 100% collateralized and avoids impermanent loss for LP farming.
Generated: DETERMINISTIC_a3659dc8e4072cb0
Batch ID: 20250612_153424
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
 * @title Liquidity Mining-Based Bond
 * @dev A smart contract for a collateralized liquidity-mining bond that avoids impermanent loss.
 */
contract LiquidityMiningBond {
    // State variables
    address public owner; // Contract owner
    uint256 public totalCollateral; // Total collateral held in the contract
    uint256 public bondPrice; // Bond price
    uint256 public bondInterestRate; // Annual interest rate in percentage
    uint256 public bondDuration; // Duration of bond in seconds
    mapping(address => uint256) public userCollateral; // Tracks collateral deposited by each user
    mapping(address => uint256) public userBondBalance; // Tracks bond balance for each user

    // Events
    event CollateralDeposited(address indexed user, uint256 amount);
    event BondPurchased(address indexed user, uint256 bondAmount);
    event BondRedeemed(address indexed user, uint256 bondAmount, uint256 collateralReturned);
    event CollateralWithdrawn(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract.
     * @param _bondPrice Initial price of the bond.
     * @param _bondInterestRate Annual interest rate for the bond.
     * @param _bondDuration Duration of the bond in seconds.
     */
    constructor(uint256 _bondPrice, uint256 _bondInterestRate, uint256 _bondDuration) {
        require(_bondPrice > 0, "Bond price must be greater than zero");
        require(_bondInterestRate > 0, "Interest rate must be greater than zero");
        require(_bondDuration > 0, "Bond duration must be greater than zero");

        owner = msg.sender;
        bondPrice = _bondPrice;
        bondInterestRate = _bondInterestRate;
        bondDuration = _bondDuration;
    }

    /**
     * @dev Modifier to limit access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Deposit collateral to the contract.
     * @param amount Amount of collateral to deposit.
     */
    function depositCollateral() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");

        userCollateral[msg.sender] += msg.value;
        totalCollateral += msg.value;

        emit CollateralDeposited(msg.sender, msg.value);
    }

    /**
     * @dev Purchase bonds using deposited collateral.
     * @param bondAmount Amount of bonds to purchase.
     */
    function purchaseBond(uint256 bondAmount) external {
        require(bondAmount > 0, "Bond amount must be greater than zero");
        uint256 requiredCollateral = bondAmount * bondPrice;
        require(userCollateral[msg.sender] >= requiredCollateral, "Insufficient collateral");

        userCollateral[msg.sender] -= requiredCollateral;
        userBondBalance[msg.sender] += bondAmount;

        emit BondPurchased(msg.sender, bondAmount);
    }

    /**
     * @dev Redeem bonds and withdraw collateral.
     * @param bondAmount Amount of bonds to redeem.
     */
    function redeemBond(uint256 bondAmount) external {
        require(bondAmount > 0, "Bond amount must be greater than zero");
        require(userBondBalance[msg.sender] >= bondAmount, "Insufficient bond balance");

        uint256 collateralToReturn = bondAmount * bondPrice;
        uint256 interest = (collateralToReturn * bondInterestRate * bondDuration) / (365 days * 100); // Simple interest formula
        collateralToReturn += interest;

        require(totalCollateral >= collateralToReturn, "Insufficient contract collateral");

        userBondBalance[msg.sender] -= bondAmount;
        totalCollateral -= collateralToReturn;

        payable(msg.sender).transfer(collateralToReturn);

        emit BondRedeemed(msg.sender, bondAmount, collateralToReturn);
    }

    /**
     * @dev Withdraw unused collateral from the contract.
     * @param amount Amount of collateral to withdraw.
     */
    function withdrawCollateral(uint256 amount) external {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(userCollateral[msg.sender] >= amount, "Insufficient collateral balance");

        userCollateral[msg.sender] -= amount;
        totalCollateral -= amount;

        payable(msg.sender).transfer(amount);

        emit CollateralWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Owner can withdraw unused collateral in the contract.
     * @param amount Amount of collateral to withdraw.
     */
    function ownerWithdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(totalCollateral >= amount, "Insufficient collateral in the contract");

        totalCollateral -= amount;

        payable(msg.sender).transfer(amount);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("Direct payments not allowed");
    }

    /**
     * @dev Receive function for explicit Ether transfers.
     */
    receive() external payable {
        revert("Direct payments not allowed");
    }
}
```
