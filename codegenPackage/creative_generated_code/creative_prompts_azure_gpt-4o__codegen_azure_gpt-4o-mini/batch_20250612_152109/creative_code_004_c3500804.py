"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethenaapp.pages.dev
Prompt: Provide an example of how to implement capital-efficient repo financing for composable leverage using USDe collateral in a DeFi money market, inspired by Ethena's repo financing mechanism.
Generated: DETERMINISTIC_c3500804e7b6f298
Batch ID: 20250612_152109
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for a standard DeFi Money Market
interface IMoneyMarket {
    function deposit(address asset, uint256 amount) external;
    function withdraw(address asset, uint256 amount) external;
    function borrow(address asset, uint256 amount) external;
    function repay(address asset, uint256 amount) external;
}

// CapitalEfficientRepo is a contract that implements repo financing for composable leverage
contract CapitalEfficientRepo is Ownable {
    IERC20 public usde; // USDe collateral token
    IMoneyMarket public moneyMarket; // Reference to the DeFi money market

    // Struct to hold repo details
    struct Repo {
        address borrower; // Address of the borrower
        uint256 collateralAmount; // Amount of USDe collateral
        uint256 borrowedAmount; // Amount borrowed
        uint256 interestRate; // Interest rate for the repo
        uint256 duration; // Duration of the repo in seconds
        uint256 startTime; // Start time of the repo
    }

    // Mapping from repo ID to Repo details
    mapping(uint256 => Repo) public repos;
    uint256 public nextRepoId; // Counter for repo IDs

    // Event emitted when a new repo is created
    event RepoCreated(uint256 indexed repoId, address indexed borrower, uint256 collateralAmount, uint256 borrowedAmount);

    // Constructor to initialize the contract with USDe and money market addresses
    constructor(IERC20 _usde, IMoneyMarket _moneyMarket) {
        usde = _usde;
        moneyMarket = _moneyMarket;
    }

    // Function to create a new repo
    function createRepo(uint256 collateralAmount, uint256 borrowedAmount, uint256 interestRate, uint256 duration) external {
        require(collateralAmount > 0, "Collateral must be greater than zero");
        require(borrowedAmount > 0, "Borrowed amount must be greater than zero");
        require(duration > 0, "Duration must be greater than zero");

        // Transfer USDe collateral to the contract
        require(usde.transferFrom(msg.sender, address(this), collateralAmount), "Transfer failed");

        // Deposit collateral into the money market
        moneyMarket.deposit(address(usde), collateralAmount);

        // Create a new repo
        repos[nextRepoId] = Repo({
            borrower: msg.sender,
            collateralAmount: collateralAmount,
            borrowedAmount: borrowedAmount,
            interestRate: interestRate,
            duration: duration,
            startTime: block.timestamp
        });

        emit RepoCreated(nextRepoId, msg.sender, collateralAmount, borrowedAmount);

        // Borrow from money market
        moneyMarket.borrow(address(usde), borrowedAmount);
        
        nextRepoId++;
    }

    // Function to repay the borrowed amount and close the repo
    function repayRepo(uint256 repoId) external {
        Repo storage repo = repos[repoId];

        require(repo.borrower == msg.sender, "Only borrower can repay the repo");
        require(block.timestamp <= repo.startTime + repo.duration, "Repo duration expired");

        // Repay the borrowed amount
        require(usde.transferFrom(msg.sender, address(this), repo.borrowedAmount), "Repayment transfer failed");
        moneyMarket.repay(address(usde), repo.borrowedAmount);

        // Withdraw collateral from money market
        moneyMarket.withdraw(address(usde), repo.collateralAmount);

        // Transfer collateral back to the borrower
        require(usde.transfer(repo.borrower, repo.collateralAmount), "Collateral transfer failed");

        // Delete the repo details
        delete repos[repoId];
    }

    // Function to retrieve repo details
    function getRepoDetails(uint256 repoId) external view returns (Repo memory) {
        return repos[repoId];
    }
}
```
