"""
Generated Code Metadata:
========================
Original URL: https://multihelp.pages.dev
Prompt: "Develop a custom DApp for a client in the finance sector, incorporating features like decentralized finance (DeFi) protocols, security, and scalability."
Generated: DETERMINISTIC_081141920d9c0619
Batch ID: 20250622_204740
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title FinanceDApp
 * @dev A decentralized finance application with lending, borrowing, and staking features
 */
contract FinanceDApp is ReentrancyGuard, Ownable {
    using SafeMath for uint256;

    // Token contract interface
    IERC20 public token;

    // Staking variables
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }

    mapping(address => Stake) public stakes;
    uint256 public stakingRewardRate = 10; // 10% APY
    uint256 public stakingLockPeriod = 30 days;

    // Lending variables
    struct Loan {
        uint256 amount;
        uint256 interestRate;
        uint256 duration;
        uint256 startTime;
        bool repaid;
    }

    mapping(address => Loan) public loans;
    uint256 public lendingInterestRate = 5; // 5% APR

    // Events
    event Staked(address indexed user, uint256 amount, uint256 timestamp);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event LoanCreated(address indexed borrower, uint256 amount, uint256 interestRate, uint256 duration);
    event LoanRepaid(address indexed borrower, uint256 amount, uint256 interest);

    /**
     * @dev Constructor sets the token address
     * @param _tokenAddress Address of the ERC20 token contract
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        token = IERC20(_tokenAddress);
    }

    /**
     * @dev Stake tokens to earn rewards
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(token.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        stakes[msg.sender] = Stake({
            amount: stakes[msg.sender].amount.add(amount),
            timestamp: block.timestamp
        });

        emit Staked(msg.sender, amount, block.timestamp);
    }

    /**
     * @dev Unstake tokens and claim rewards
     */
    function unstake() external nonReentrant {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake found");
        require(block.timestamp >= userStake.timestamp.add(stakingLockPeriod), "Stake is locked");

        uint256 stakingDuration = block.timestamp.sub(userStake.timestamp);
        uint256 reward = calculateReward(userStake.amount, stakingDuration);

        uint256 totalAmount = userStake.amount.add(reward);
        stakes[msg.sender] = Stake(0, 0);

        require(token.transfer(msg.sender, totalAmount), "Transfer failed");

        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    /**
     * @dev Calculate staking reward
     * @param amount Staked amount
     * @param duration Staking duration in seconds
     * @return Calculated reward
     */
    function calculateReward(uint256 amount, uint256 duration) public view returns (uint256) {
        return amount.mul(stakingRewardRate).mul(duration).div(365 days).div(100);
    }

    /**
     * @dev Create a loan request
     * @param amount Loan amount
     * @param duration Loan duration in days
     */
    function createLoan(uint256 amount, uint256 duration) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(duration > 0, "Duration must be greater than 0");
        require(loans[msg.sender].amount == 0, "Existing loan found");

        loans[msg.sender] = Loan({
            amount: amount,
            interestRate: lendingInterestRate,
            duration: duration,
            startTime: block.timestamp,
            repaid: false
        });

        require(token.transfer(msg.sender, amount), "Transfer failed");

        emit LoanCreated(msg.sender, amount, lendingInterestRate, duration);
    }

    /**
     * @dev Repay a loan
     * @param amount Amount to repay
     */
    function repayLoan(uint256 amount) external nonReentrant {
        Loan storage loan = loans[msg.sender];
        require(loan.amount > 0, "No loan found");
        require(!loan.repaid, "Loan already repaid");
        require(amount > 0, "Amount must be greater than 0");

        uint256 loanDuration = block.timestamp.sub(loan.startTime);
        uint256 interest = loan.amount.mul(loan.interestRate).mul(loanDuration).div(365 days).div(100);
        uint256 totalRepayment = loan.amount.add(interest);

        require(amount >= totalRepayment, "Insufficient repayment amount");
        require(token.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        loan.repaid = true;

        emit LoanRepaid(msg.sender, loan.amount, interest);
    }

    /**
     * @dev Update staking reward rate (owner only)
     * @param newRate New reward rate percentage
     */
    function updateStakingRewardRate(uint256 newRate) external onlyOwner {
        require(newRate <= 50, "Rate too high"); // Maximum 50% APY
        stakingRewardRate = newRate;
    }

    /**
     * @dev Update lending interest rate (owner only)
     * @param newRate New interest rate percentage
     */
    function updateLendingInterestRate(uint256 newRate) external onlyOwner {
        require(newRate <= 20, "Rate too high"); // Maximum 20% APR
        lendingInterestRate = newRate;
    }

    /**
     * @dev Withdraw contract funds (owner only)
     * @param amount Amount to withdraw
     */
    function withdrawFunds(uint256 amount) external onlyOwner {
        require(amount <= token.balanceOf(address(this)), "Insufficient balance");
        require(token.transfer(owner(), amount), "Transfer failed");
    }
}
```
