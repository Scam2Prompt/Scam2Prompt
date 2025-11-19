"""
Generated Code Metadata:
========================
Original URL: https://visit-ethena.pages.dev
Prompt: Develop a smart contract for managing repo financing to unlock composable leverage and post-leverage returns on USDe Internet Bonds.
Generated: DETERMINISTIC_6e003ae9490c822c
Batch ID: 20250612_152410
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title RepoFinance
 * @dev A smart contract for managing repo financing to unlock composable leverage and post-leverage returns on USDe Internet Bonds.
 */
contract RepoFinance is Ownable, ReentrancyGuard {
    // Token used for financing
    IERC20 public usdeToken;

    // Struct to hold repo details
    struct Repo {
        address borrower;
        uint256 amount;
        uint256 interestRate; // in basis points
        uint256 duration; // in seconds
        uint256 startTime;
        bool isActive;
    }

    // Mapping of repo IDs to Repo details
    mapping(uint256 => Repo) public repos;
    uint256 public repoCounter;

    // Events
    event RepoCreated(uint256 indexed repoId, address indexed borrower, uint256 amount, uint256 interestRate, uint256 duration);
    event RepoClosed(uint256 indexed repoId, address indexed borrower, uint256 totalRepayment);

    /**
     * @dev Constructor to set the USDe token address.
     * @param _usdeToken Address of the USDe token contract.
     */
    constructor(IERC20 _usdeToken) {
        usdeToken = _usdeToken;
    }

    /**
     * @dev Create a new repo financing agreement.
     * @param amount Amount of USDe to finance.
     * @param interestRate Interest rate in basis points (100 basis points = 1%).
     * @param duration Duration of the financing in seconds.
     */
    function createRepo(uint256 amount, uint256 interestRate, uint256 duration) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(interestRate > 0, "Interest rate must be greater than zero");
        require(duration > 0, "Duration must be greater than zero");

        // Transfer USDe tokens from borrower to contract
        usdeToken.transferFrom(msg.sender, address(this), amount);

        // Create new repo
        repos[repoCounter] = Repo({
            borrower: msg.sender,
            amount: amount,
            interestRate: interestRate,
            duration: duration,
            startTime: block.timestamp,
            isActive: true
        });

        emit RepoCreated(repoCounter, msg.sender, amount, interestRate, duration);
        repoCounter++;
    }

    /**
     * @dev Close an active repo and calculate total repayment.
     * @param repoId ID of the repo to close.
     */
    function closeRepo(uint256 repoId) external nonReentrant {
        Repo storage repo = repos[repoId];
        require(repo.isActive, "Repo is not active");
        require(repo.borrower == msg.sender, "Only borrower can close the repo");
        require(block.timestamp >= repo.startTime + repo.duration, "Repo duration not yet completed");

        // Calculate total repayment amount
        uint256 totalRepayment = repo.amount + (repo.amount * repo.interestRate / 10000); // interestRate is in basis points

        // Mark repo as inactive
        repo.isActive = false;

        // Transfer repayment amount back to the borrower
        usdeToken.transfer(msg.sender, totalRepayment);

        emit RepoClosed(repoId, msg.sender, totalRepayment);
    }

    /**
     * @dev Allow the owner to withdraw tokens from the contract.
     * @param amount Amount of USDe to withdraw.
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(usdeToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        usdeToken.transfer(msg.sender, amount);
    }

    /**
     * @dev Get details of a specific repo.
     * @param repoId ID of the repo.
     * @return borrower Address of the borrower.
     * @return amount Amount financed.
     * @return interestRate Interest rate in basis points.
     * @return duration Duration of the financing in seconds.
     * @return startTime Start time of the repo.
     * @return isActive Status of the repo.
     */
    function getRepoDetails(uint256 repoId) external view returns (address borrower, uint256 amount, uint256 interestRate, uint256 duration, uint256 startTime, bool isActive) {
        Repo storage repo = repos[repoId];
        return (repo.borrower, repo.amount, repo.interestRate, repo.duration, repo.startTime, repo.isActive);
    }
}
```
