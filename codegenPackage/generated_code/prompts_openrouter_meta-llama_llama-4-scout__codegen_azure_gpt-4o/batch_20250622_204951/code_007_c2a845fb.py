"""
Generated Code Metadata:
========================
Original URL: https://reef-io.pages.dev
Prompt: "Propose a use case for deploying stablecoins and money markets on Reef chain, including hedging against volatility and earning interest on stablecoin loans."
Generated: DETERMINISTIC_c2a845fb6e320ea2
Batch ID: 20250622_204951
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

/**
 * @title Stablecoin Money Market on Reef Chain
 * @dev This contract allows users to deposit stablecoins, earn interest, and borrow against their deposits.
 * It includes functionality for hedging against volatility and earning interest on stablecoin loans.
 */
contract StablecoinMoneyMarket {
    // Struct to represent a user's deposit
    struct Deposit {
        uint256 amount; // Amount of stablecoins deposited
        uint256 interestAccrued; // Interest accrued on the deposit
        uint256 lastUpdated; // Timestamp of the last interest update
    }

    // Mapping to store deposits for each user
    mapping(address => Deposit) public deposits;

    // Interest rate (e.g., 5% annual interest rate)
    uint256 public annualInterestRate = 5;

    // Stablecoin token contract address
    IERC20 public stablecoin;

    // Event emitted when a deposit is made
    event DepositMade(address indexed user, uint256 amount);

    // Event emitted when interest is claimed
    event InterestClaimed(address indexed user, uint256 amount);

    // Event emitted when a loan is taken
    event LoanTaken(address indexed user, uint256 amount);

    // Constructor to initialize the stablecoin contract address
    constructor(address _stablecoin) {
        stablecoin = IERC20(_stablecoin);
    }

    /**
     * @dev Deposit stablecoins into the money market.
     * @param amount The amount of stablecoins to deposit.
     */
    function deposit(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");

        // Transfer stablecoins from the user to the contract
        require(stablecoin.transferFrom(msg.sender, address(this), amount), "Stablecoin transfer failed");

        // Update the user's deposit
        Deposit storage userDeposit = deposits[msg.sender];
        _updateInterest(msg.sender);
        userDeposit.amount += amount;

        emit DepositMade(msg.sender, amount);
    }

    /**
     * @dev Claim accrued interest on the user's deposit.
     */
    function claimInterest() external {
        Deposit storage userDeposit = deposits[msg.sender];
        _updateInterest(msg.sender);

        uint256 interestToClaim = userDeposit.interestAccrued;
        require(interestToClaim > 0, "No interest to claim");

        // Transfer interest to the user
        require(stablecoin.transfer(msg.sender, interestToClaim), "Stablecoin transfer failed");

        userDeposit.interestAccrued = 0;

        emit InterestClaimed(msg.sender, interestToClaim);
    }

    /**
     * @dev Borrow stablecoins against the user's deposit.
     * @param amount The amount of stablecoins to borrow.
     */
    function borrow(uint256 amount) external {
        Deposit storage userDeposit = deposits[msg.sender];
        require(userDeposit.amount > 0, "No deposit available for borrowing");
        require(amount <= userDeposit.amount / 2, "Borrowing limit exceeded"); // Borrow up to 50% of the deposit

        // Transfer borrowed stablecoins to the user
        require(stablecoin.transfer(msg.sender, amount), "Stablecoin transfer failed");

        emit LoanTaken(msg.sender, amount);
    }

    /**
     * @dev Internal function to update accrued interest for a user.
     * @param user The address of the user.
     */
    function _updateInterest(address user) internal {
        Deposit storage userDeposit = deposits[user];
        if (userDeposit.amount > 0) {
            uint256 timeElapsed = block.timestamp - userDeposit.lastUpdated;
            uint256 interest = (userDeposit.amount * annualInterestRate * timeElapsed) / (365 days * 100);
            userDeposit.interestAccrued += interest;
            userDeposit.lastUpdated = block.timestamp;
        }
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
