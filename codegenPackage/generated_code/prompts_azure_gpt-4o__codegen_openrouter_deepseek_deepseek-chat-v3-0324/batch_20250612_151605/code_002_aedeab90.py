"""
Generated Code Metadata:
========================
Original URL: https://bafybeidiclstnq4utj2pwl644m64fbyrgzsmyytshhypgwavuo7vertppe.ipfs.dweb.link
Prompt: Provide a Solidity smart contract example for integrating Amnis Finance's liquid staking tokens (amAPT and stAPT) into a DeFi lending platform.
Generated: DETERMINISTIC_aedeab90e2654d6e
Batch ID: 20250612_151605
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

interface IAmnisFinance {
    function convertToShares(uint256 assets) external view returns (uint256);
    function convertToAssets(uint256 shares) external view returns (uint256);
    function deposit(uint256 assets, address receiver) external returns (uint256);
    function redeem(uint256 shares, address receiver, address owner) external returns (uint256);
}

contract AmnisLendingPlatform is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Token contracts
    IERC20 public immutable aptosToken;
    IAmnisFinance public immutable amAPT;
    IAmnisFinance public immutable stAPT;

    // Lending parameters
    uint256 public interestRate; // in basis points (1% = 100)
    uint256 public collateralRatio; // in basis points (150% = 15000)
    uint256 public liquidationPenalty; // in basis points (5% = 500)

    struct Loan {
        uint256 amount;
        uint256 collateral;
        uint256 startTime;
        address borrower;
        bool liquidated;
    }

    mapping(address => Loan) public loans;
    mapping(address => uint256) public userStakes;

    event Deposit(address indexed user, uint256 amount);
    event Withdraw(address indexed user, uint256 amount);
    event Borrow(address indexed user, uint256 amount, uint256 collateral);
    event Repay(address indexed user, uint256 amount);
    event Liquidate(address indexed user, address indexed liquidator, uint256 amount);

    constructor(
        address _aptosToken,
        address _amAPT,
        address _stAPT,
        uint256 _interestRate,
        uint256 _collateralRatio,
        uint256 _liquidationPenalty
    ) {
        require(_aptosToken != address(0), "Invalid APT token address");
        require(_amAPT != address(0), "Invalid amAPT address");
        require(_stAPT != address(0), "Invalid stAPT address");
        
        aptosToken = IERC20(_aptosToken);
        amAPT = IAmnisFinance(_amAPT);
        stAPT = IAmnisFinance(_stAPT);
        
        interestRate = _interestRate;
        collateralRatio = _collateralRatio;
        liquidationPenalty = _liquidationPenalty;
    }

    function depositAPT(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        aptosToken.safeTransferFrom(msg.sender, address(this), amount);
        uint256 shares = amAPT.deposit(amount, address(this));
        
        userStakes[msg.sender] += shares;
        emit Deposit(msg.sender, amount);
    }

    function withdrawAPT(uint256 shares) external nonReentrant {
        require(shares > 0, "Shares must be greater than 0");
        require(userStakes[msg.sender] >= shares, "Insufficient balance");
        
        userStakes[msg.sender] -= shares;
        uint256 assets = amAPT.redeem(shares, msg.sender, address(this));
        
        emit Withdraw(msg.sender, assets);
    }

    function borrow(uint256 amount, uint256 collateralShares) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(collateralShares > 0, "Collateral must be greater than 0");
        require(loans[msg.sender].amount == 0, "Existing loan found");
        
        uint256 collateralValue = stAPT.convertToAssets(collateralShares);
        require(
            collateralValue * 10000 >= amount * collateralRatio,
            "Insufficient collateral"
        );
        
        require(
            userStakes[msg.sender] >= collateralShares,
            "Insufficient staked balance"
        );
        
        userStakes[msg.sender] -= collateralShares;
        loans[msg.sender] = Loan({
            amount: amount,
            collateral: collateralShares,
            startTime: block.timestamp,
            borrower: msg.sender,
            liquidated: false
        });
        
        aptosToken.safeTransfer(msg.sender, amount);
        emit Borrow(msg.sender, amount, collateralShares);
    }

    function repay() external nonReentrant {
        Loan storage loan = loans[msg.sender];
        require(loan.amount > 0, "No active loan");
        require(!loan.liquidated, "Loan already liquidated");
        
        uint256 interest = calculateInterest(loan.amount, loan.startTime);
        uint256 totalAmount = loan.amount + interest;
        
        aptosToken.safeTransferFrom(msg.sender, address(this), totalAmount);
        userStakes[msg.sender] += loan.collateral;
        
        delete loans[msg.sender];
        emit Repay(msg.sender, totalAmount);
    }

    function liquidate(address borrower) external nonReentrant {
        Loan storage loan = loans[borrower];
        require(loan.amount > 0, "No active loan");
        require(!loan.liquidated, "Loan already liquidated");
        
        uint256 interest = calculateInterest(loan.amount, loan.startTime);
        uint256 collateralValue = stAPT.convertToAssets(loan.collateral);
        uint256 debtValue = loan.amount + interest;
        
        require(
            collateralValue * 10000 < debtValue * collateralRatio,
            "Loan is not undercollateralized"
        );
        
        uint256 penaltyAmount = debtValue * liquidationPenalty / 10000;
        uint256 liquidatorReward = penaltyAmount / 2;
        
        aptosToken.safeTransferFrom(msg.sender, address(this), debtValue - liquidatorReward);
        aptosToken.safeTransfer(msg.sender, liquidatorReward);
        
        uint256 stAPTAmount = stAPT.redeem(
            loan.collateral,
            address(this),
            address(this)
        );
        amAPT.deposit(stAPTAmount, msg.sender);
        
        loan.liquidated = true;
        emit Liquidate(borrower, msg.sender, loan.amount);
    }

    function calculateInterest(uint256 principal, uint256 startTime) public view returns (uint256) {
        uint256 timeElapsed = block.timestamp - startTime;
        uint256 periods = timeElapsed / 1 days;
        return principal * interestRate * periods / 36500; // 365 days * 100 basis points
    }

    function updateParameters(
        uint256 _interestRate,
        uint256 _collateralRatio,
        uint256 _liquidationPenalty
    ) external onlyOwner {
        require(_interestRate > 0, "Invalid interest rate");
        require(_collateralRatio > 10000, "Collateral ratio too low");
        require(_liquidationPenalty > 0 && _liquidationPenalty < 10000, "Invalid penalty");
        
        interestRate = _interestRate;
        collateralRatio = _collateralRatio;
        liquidationPenalty = _liquidationPenalty;
    }

    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        IERC20(token).safeTransfer(owner(), amount);
    }
}
```
