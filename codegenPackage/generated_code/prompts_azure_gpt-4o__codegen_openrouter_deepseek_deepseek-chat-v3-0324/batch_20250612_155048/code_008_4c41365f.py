"""
Generated Code Metadata:
========================
Original URL: https://dikmansdeli.ru
Prompt: Write a Solidity contract to automate the repayment of loans on Venus Protocol when a specific token price threshold is met.
Generated: DETERMINISTIC_4c41365fa4b1eb02
Batch ID: 20250612_155048
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "./interfaces/IVenusComptroller.sol";
import "./interfaces/IVToken.sol";
import "./interfaces/IPriceOracle.sol";

contract VenusLoanRepayer is Ownable {
    IVenusComptroller public comptroller;
    IPriceOracle public priceOracle;
    
    struct LoanRepayment {
        address borrower;
        address vTokenBorrowed;
        address vTokenCollateral;
        uint256 repayAmount;
        uint256 priceThreshold;
        bool isAboveThreshold;
        bool isActive;
    }
    
    mapping(uint256 => LoanRepayment) public loanRepayments;
    uint256 public loanRepaymentCount;
    
    event LoanRepaymentCreated(
        uint256 indexed id,
        address indexed borrower,
        address vTokenBorrowed,
        address vTokenCollateral,
        uint256 repayAmount,
        uint256 priceThreshold,
        bool isAboveThreshold
    );
    
    event LoanRepaymentExecuted(
        uint256 indexed id,
        address indexed borrower,
        address vTokenBorrowed,
        uint256 repayAmount,
        uint256 collateralRedeemed
    );
    
    event LoanRepaymentCancelled(uint256 indexed id);
    
    constructor(address _comptroller, address _priceOracle) {
        comptroller = IVenusComptroller(_comptroller);
        priceOracle = IPriceOracle(_priceOracle);
    }
    
    function createLoanRepayment(
        address _vTokenBorrowed,
        address _vTokenCollateral,
        uint256 _repayAmount,
        uint256 _priceThreshold,
        bool _isAboveThreshold
    ) external returns (uint256) {
        require(_repayAmount > 0, "Repay amount must be greater than 0");
        require(_priceThreshold > 0, "Price threshold must be greater than 0");
        
        loanRepaymentCount++;
        loanRepayments[loanRepaymentCount] = LoanRepayment({
            borrower: msg.sender,
            vTokenBorrowed: _vTokenBorrowed,
            vTokenCollateral: _vTokenCollateral,
            repayAmount: _repayAmount,
            priceThreshold: _priceThreshold,
            isAboveThreshold: _isAboveThreshold,
            isActive: true
        });
        
        emit LoanRepaymentCreated(
            loanRepaymentCount,
            msg.sender,
            _vTokenBorrowed,
            _vTokenCollateral,
            _repayAmount,
            _priceThreshold,
            _isAboveThreshold
        );
        
        return loanRepaymentCount;
    }
    
    function executeLoanRepayment(uint256 _id) external {
        LoanRepayment storage repayment = loanRepayments[_id];
        require(repayment.isActive, "Repayment is not active");
        require(repayment.borrower == msg.sender || msg.sender == owner(), "Unauthorized");
        
        address underlyingBorrowed = IVToken(repayment.vTokenBorrowed).underlying();
        uint256 currentPrice = priceOracle.getUnderlyingPrice(repayment.vTokenBorrowed);
        
        bool priceConditionMet = repayment.isAboveThreshold 
            ? currentPrice >= repayment.priceThreshold 
            : currentPrice <= repayment.priceThreshold;
            
        require(priceConditionMet, "Price condition not met");
        
        IERC20(underlyingBorrowed).transferFrom(
            msg.sender,
            address(this),
            repayment.repayAmount
        );
        
        IERC20(underlyingBorrowed).approve(
            repayment.vTokenBorrowed,
            repayment.repayAmount
        );
        
        uint256 errorCode = IVToken(repayment.vTokenBorrowed).repayBorrowBehalf(
            repayment.borrower,
            repayment.repayAmount
        );
        
        require(errorCode == 0, "Repayment failed");
        
        uint256 collateralRedeemed = 0;
        if (repayment.vTokenCollateral != address(0)) {
            collateralRedeemed = IVToken(repayment.vTokenCollateral).balanceOfUnderlying(address(this));
            IVToken(repayment.vTokenCollateral).redeemUnderlying(collateralRedeemed);
            
            address underlyingCollateral = IVToken(repayment.vTokenCollateral).underlying();
            IERC20(underlyingCollateral).transfer(repayment.borrower, collateralRedeemed);
        }
        
        repayment.isActive = false;
        
        emit LoanRepaymentExecuted(
            _id,
            repayment.borrower,
            repayment.vTokenBorrowed,
            repayment.repayAmount,
            collateralRedeemed
        );
    }
    
    function cancelLoanRepayment(uint256 _id) external {
        LoanRepayment storage repayment = loanRepayments[_id];
        require(repayment.isActive, "Repayment is not active");
        require(repayment.borrower == msg.sender || msg.sender == owner(), "Unauthorized");
        
        repayment.isActive = false;
        
        emit LoanRepaymentCancelled(_id);
    }
    
    function setComptroller(address _comptroller) external onlyOwner {
        comptroller = IVenusComptroller(_comptroller);
    }
    
    function setPriceOracle(address _priceOracle) external onlyOwner {
        priceOracle = IPriceOracle(_priceOracle);
    }
    
    function withdrawToken(address _token, uint256 _amount) external onlyOwner {
        IERC20(_token).transfer(msg.sender, _amount);
    }
}
```
