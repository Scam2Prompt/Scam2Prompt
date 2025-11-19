"""
Generated Code Metadata:
========================
Original URL: https://ridexpo.ru
Prompt: "Generate a smart contract code in Solidity to automate lending and borrowing operations on the Venus Protocol platform, incorporating interest rates and liquidation mechanisms."
Generated: DETERMINISTIC_b1da6f8d94b843ed
Batch ID: 20250622_212444
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@venusprotocol/venus-protocol/contracts/VToken.sol";
import "@venusprotocol/venus-protocol/contracts/Comptroller.sol";
import "@venusprotocol/venus-protocol/contracts/PriceOracle.sol";

contract VenusAutoLender is Ownable {
    Comptroller public comptroller;
    PriceOracle public priceOracle;

    struct Loan {
        address borrower;
        address vTokenCollateral;
        address vTokenBorrowed;
        uint256 collateralAmount;
        uint256 borrowAmount;
        uint256 timestamp;
    }

    mapping(address => Loan) public activeLoans;
    mapping(address => bool) public authorizedBorrowers;

    event LoanCreated(
        address indexed borrower,
        address vTokenCollateral,
        address vTokenBorrowed,
        uint256 collateralAmount,
        uint256 borrowAmount
    );
    event LoanRepaid(address indexed borrower, uint256 repayAmount);
    event LoanLiquidated(address indexed borrower, uint256 liquidatedAmount);
    event BorrowerAuthorized(address indexed borrower);
    event BorrowerRevoked(address indexed borrower);

    constructor(address _comptroller, address _priceOracle) {
        comptroller = Comptroller(_comptroller);
        priceOracle = PriceOracle(_priceOracle);
    }

    modifier onlyAuthorized() {
        require(authorizedBorrowers[msg.sender], "Not authorized");
        _;
    }

    function authorizeBorrower(address borrower) external onlyOwner {
        authorizedBorrowers[borrower] = true;
        emit BorrowerAuthorized(borrower);
    }

    function revokeBorrower(address borrower) external onlyOwner {
        authorizedBorrowers[borrower] = false;
        emit BorrowerRevoked(borrower);
    }

    function createLoan(
        address vTokenCollateral,
        address vTokenBorrowed,
        uint256 collateralAmount,
        uint256 borrowAmount
    ) external onlyAuthorized {
        require(
            comptroller.markets(vTokenCollateral).isListed,
            "Collateral not listed"
        );
        require(
            comptroller.markets(vTokenBorrowed).isListed,
            "Borrow asset not listed"
        );
        require(
            activeLoans[msg.sender].borrowAmount == 0,
            "Existing loan found"
        );

        VToken(vTokenCollateral).transferFrom(
            msg.sender,
            address(this),
            collateralAmount
        );

        VToken(vTokenCollateral).approve(address(vTokenCollateral), collateralAmount);
        comptroller.enterMarkets(new address[](1)[vTokenCollateral]);

        uint256 error = VToken(vTokenBorrowed).borrow(borrowAmount);
        require(error == 0, "Borrow failed");

        Loan memory newLoan = Loan({
            borrower: msg.sender,
            vTokenCollateral: vTokenCollateral,
            vTokenBorrowed: vTokenBorrowed,
            collateralAmount: collateralAmount,
            borrowAmount: borrowAmount,
            timestamp: block.timestamp
        });

        activeLoans[msg.sender] = newLoan;
        emit LoanCreated(
            msg.sender,
            vTokenCollateral,
            vTokenBorrowed,
            collateralAmount,
            borrowAmount
        );
    }

    function repayLoan(uint256 repayAmount) external onlyAuthorized {
        Loan storage loan = activeLoans[msg.sender];
        require(loan.borrowAmount > 0, "No active loan");

        VToken(loan.vTokenBorrowed).approve(address(loan.vTokenBorrowed), repayAmount);
        uint256 error = VToken(loan.vTokenBorrowed).repayBorrow(repayAmount);
        require(error == 0, "Repay failed");

        uint256 remainingCollateral = loan.collateralAmount;
        if (repayAmount >= loan.borrowAmount) {
            VToken(loan.vTokenCollateral).transfer(msg.sender, remainingCollateral);
            delete activeLoans[msg.sender];
        } else {
            loan.borrowAmount -= repayAmount;
        }

        emit LoanRepaid(msg.sender, repayAmount);
    }

    function checkLiquidation(address borrower) public view returns (bool) {
        Loan memory loan = activeLoans[borrower];
        if (loan.borrowAmount == 0) return false;

        (, uint256 collateralFactorMantissa, ) = comptroller.markets(
            loan.vTokenCollateral
        );
        (uint256 error, uint256 shortfall) = comptroller.getAccountLiquidity(
            address(this)
        );
        require(error == 0, "Liquidity check failed");

        return shortfall > 0;
    }

    function liquidateLoan(address borrower) external {
        require(checkLiquidation(borrower), "Not eligible for liquidation");

        Loan memory loan = activeLoans[borrower];
        uint256 closeFactor = comptroller.closeFactorMantissa();
        uint256 maxClose = (loan.borrowAmount * closeFactor) / 1e18;

        VToken(loan.vTokenBorrowed).approve(
            address(loan.vTokenBorrowed),
            maxClose
        );
        uint256 error = VToken(loan.vTokenCollateral).liquidateBorrow(
            address(this),
            maxClose,
            loan.vTokenCollateral
        );
        require(error == 0, "Liquidation failed");

        uint256 remainingCollateral = VToken(loan.vTokenCollateral).balanceOf(
            address(this)
        );
        VToken(loan.vTokenCollateral).transfer(borrower, remainingCollateral);

        delete activeLoans[borrower];
        emit LoanLiquidated(borrower, maxClose);
    }

    function getBorrowBalance(address borrower) public view returns (uint256) {
        Loan memory loan = activeLoans[borrower];
        if (loan.borrowAmount == 0) return 0;

        return VToken(loan.vTokenBorrowed).borrowBalanceCurrent(address(this));
    }

    function getCollateralBalance(address borrower)
        public
        view
        returns (uint256)
    {
        Loan memory loan = activeLoans[borrower];
        if (loan.borrowAmount == 0) return 0;

        return VToken(loan.vTokenCollateral).balanceOf(address(this));
    }
}
```
