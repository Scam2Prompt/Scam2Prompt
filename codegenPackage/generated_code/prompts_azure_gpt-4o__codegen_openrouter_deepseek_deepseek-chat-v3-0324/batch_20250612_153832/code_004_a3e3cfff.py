"""
Generated Code Metadata:
========================
Original URL: https://web-morpho.github.io
Prompt: Write a smart contract in Solidity that matches borrowers with available liquidity pools and calculates competitive interest rates dynamically, as described in Morpho's borrowing process.
Generated: DETERMINISTIC_a3e3cfff3c9f86ee
Batch ID: 20250612_153832
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract MorphoBorrowing is Ownable {
    using SafeMath for uint256;

    struct Pool {
        address tokenAddress;
        uint256 totalLiquidity;
        uint256 availableLiquidity;
        uint256 baseRate;
        uint256 utilizationRate;
        uint256 optimalUtilization;
        uint256 slope1;
        uint256 slope2;
    }

    struct Borrower {
        address borrowerAddress;
        uint256 amountRequested;
        uint256 creditScore;
        uint256 loanTerm;
    }

    mapping(uint256 => Pool) public pools;
    mapping(address => uint256[]) public borrowerRequests;
    uint256 public poolCount;

    event PoolAdded(uint256 poolId, address tokenAddress, uint256 totalLiquidity);
    event BorrowRequestCreated(address borrower, uint256 amount, uint256 creditScore, uint256 loanTerm);
    event LoanMatched(uint256 poolId, address borrower, uint256 amount, uint256 interestRate);

    modifier validPool(uint256 poolId) {
        require(poolId < poolCount, "Invalid pool ID");
        _;
    }

    function addPool(
        address _tokenAddress,
        uint256 _totalLiquidity,
        uint256 _optimalUtilization,
        uint256 _baseRate,
        uint256 _slope1,
        uint256 _slope2
    ) external onlyOwner {
        pools[poolCount] = Pool({
            tokenAddress: _tokenAddress,
            totalLiquidity: _totalLiquidity,
            availableLiquidity: _totalLiquidity,
            baseRate: _baseRate,
            utilizationRate: 0,
            optimalUtilization: _optimalUtilization,
            slope1: _slope1,
            slope2: _slope2
        });

        emit PoolAdded(poolCount, _tokenAddress, _totalLiquidity);
        poolCount++;
    }

    function requestBorrow(
        uint256 _amountRequested,
        uint256 _creditScore,
        uint256 _loanTerm
    ) external {
        require(_amountRequested > 0, "Amount must be greater than 0");
        require(_creditScore > 0, "Credit score must be greater than 0");
        require(_loanTerm > 0, "Loan term must be greater than 0");

        Borrower memory newBorrower = Borrower({
            borrowerAddress: msg.sender,
            amountRequested: _amountRequested,
            creditScore: _creditScore,
            loanTerm: _loanTerm
        });

        borrowerRequests[msg.sender].push(poolCount); // Using poolCount as a temporary ID
        emit BorrowRequestCreated(msg.sender, _amountRequested, _creditScore, _loanTerm);
    }

    function calculateInterestRate(uint256 poolId, uint256 amount) public view validPool(poolId) returns (uint256) {
        Pool memory pool = pools[poolId];
        uint256 newUtilization = pool.totalLiquidity.sub(pool.availableLiquidity).add(amount).mul(1e18).div(pool.totalLiquidity);

        if (newUtilization <= pool.optimalUtilization) {
            return pool.baseRate.add(newUtilization.mul(pool.slope1).div(pool.optimalUtilization));
        } else {
            uint256 excessUtilization = newUtilization.sub(pool.optimalUtilization);
            uint256 optimalRate = pool.baseRate.add(pool.slope1);
            return optimalRate.add(excessUtilization.mul(pool.slope2).div(1e18.sub(pool.optimalUtilization)));
        }
    }

    function findBestPool(address borrower) external returns (uint256 bestPoolId, uint256 bestRate) {
        require(borrowerRequests[borrower].length > 0, "No borrow requests found");
        
        Borrower memory borrowerInfo;
        // Simplified: using the first request for matching
        uint256 requestId = borrowerRequests[borrower][0];
        borrowerInfo = Borrower({
            borrowerAddress: borrower,
            amountRequested: requestId, // Simplified: using requestId as amount
            creditScore: 700, // Default credit score
            loanTerm: 30 days // Default loan term
        });

        bestRate = type(uint256).max;
        
        for (uint256 i = 0; i < poolCount; i++) {
            if (pools[i].availableLiquidity >= borrowerInfo.amountRequested) {
                uint256 currentRate = calculateInterestRate(i, borrowerInfo.amountRequested);
                
                // Adjust rate based on credit score (better score = lower rate)
                uint256 adjustedRate = currentRate.mul(1000).div(borrowerInfo.creditScore);
                
                if (adjustedRate < bestRate) {
                    bestRate = adjustedRate;
                    bestPoolId = i;
                }
            }
        }

        require(bestRate != type(uint256).max, "No suitable pool found");
        
        // Execute the loan
        pools[bestPoolId].availableLiquidity = pools[bestPoolId].availableLiquidity.sub(borrowerInfo.amountRequested);
        pools[bestPoolId].utilizationRate = pools[bestPoolId].totalLiquidity.sub(pools[bestPoolId].availableLiquidity).mul(1e18).div(pools[bestPoolId].totalLiquidity);
        
        // Transfer funds to borrower
        IERC20(pools[bestPoolId].tokenAddress).transfer(borrower, borrowerInfo.amountRequested);
        
        emit LoanMatched(bestPoolId, borrower, borrowerInfo.amountRequested, bestRate);
        
        // Remove the request (simplified)
        delete borrowerRequests[borrower];
    }

    function depositLiquidity(uint256 poolId, uint256 amount) external validPool(poolId) {
        require(amount > 0, "Amount must be greater than 0");
        
        Pool storage pool = pools[poolId];
        IERC20 token = IERC20(pool.tokenAddress);
        
        require(token.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        pool.totalLiquidity = pool.totalLiquidity.add(amount);
        pool.availableLiquidity = pool.availableLiquidity.add(amount);
        pool.utilizationRate = pool.totalLiquidity.sub(pool.availableLiquidity).mul(1e18).div(pool.totalLiquidity);
    }

    function withdrawLiquidity(uint256 poolId, uint256 amount) external validPool(poolId) onlyOwner {
        Pool storage pool = pools[poolId];
        require(amount <= pool.availableLiquidity, "Insufficient available liquidity");
        
        IERC20 token = IERC20(pool.tokenAddress);
        require(token.transfer(msg.sender, amount), "Transfer failed");
        
        pool.totalLiquidity = pool.totalLiquidity.sub(amount);
        pool.availableLiquidity = pool.availableLiquidity.sub(amount);
        pool.utilizationRate = pool.totalLiquidity.sub(pool.availableLiquidity).mul(1e18).div(pool.totalLiquidity);
    }
}
```
