"""
Generated Code Metadata:
========================
Original URL: https://crudoprotocol-io.web.app
Prompt: Develop a blockchain-based staking mechanism for CRUDO tokens, allowing token holders to generate passive income.
Generated: DETERMINISTIC_9643848d84a97efc
Batch ID: 20250612_145711
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

// Importing OpenZeppelin's ERC20 interface and Ownable contract
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for CRUDO tokens
contract CRUDOStaking is Ownable {
    // Struct to hold staking information for each user
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of when the tokens were staked
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // The CRUDO token contract
    IERC20 public crudoToken;

    // Annual interest rate (in basis points, e.g., 500 = 5%)
    uint256 public annualInterestRate;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the CRUDO token address and interest rate
    constructor(IERC20 _crudoToken, uint256 _annualInterestRate) {
        crudoToken = _crudoToken;
        annualInterestRate = _annualInterestRate;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(crudoToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from the user to the contract
        crudoToken.transferFrom(msg.sender, address(this), amount);

        // Update the user's stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to calculate the earned interest
    function calculateInterest(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        uint256 stakingDuration = block.timestamp - userStake.timestamp; // Duration in seconds
        uint256 interest = (userStake.amount * annualInterestRate * stakingDuration) / (365 days * 10000); // Interest calculation

        return interest;
    }

    // Function to unstake tokens along with earned interest
    function unstake() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate total amount to return (staked amount + interest)
        uint256 interest = calculateInterest(msg.sender);
        uint256 totalAmount = userStake.amount + interest;

        // Reset the user's stake
        delete stakes[msg.sender];

        // Transfer the total amount back to the user
        crudoToken.transfer(msg.sender, totalAmount);

        emit Unstaked(msg.sender, totalAmount);
    }

    // Function to update the annual interest rate (only owner can call)
    function updateAnnualInterestRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Interest rate must be greater than 0");
        annualInterestRate = newRate;
    }

    // Function to withdraw tokens in case of emergency (only owner can call)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount <= crudoToken.balanceOf(address(this)), "Insufficient contract balance");
        crudoToken.transfer(msg.sender, amount);
    }
}
```
