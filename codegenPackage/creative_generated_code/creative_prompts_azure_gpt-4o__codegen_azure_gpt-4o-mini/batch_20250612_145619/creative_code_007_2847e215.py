"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paraxweb3dapp.pages.dev
Prompt: Generate code to integrate ParaX's Flooring Protocol into a DeFi application, enabling users to supply and borrow µBAYC tokens with specified APY rates.
Generated: DETERMINISTIC_2847e215ca24f3ad
Batch ID: 20250612_145619
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

// Import necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Defining the DeFi application contract
contract DeFiFlooring is Ownable {
    using SafeMath for uint256;

    // Define the µBAYC token interface
    IERC20 public muBAYCToken;

    // Structure to store user data
    struct User {
        uint256 suppliedAmount;
        uint256 borrowedAmount;
        uint256 interestRate; // APY in basis points
    }

    // Map user addresses to their data
    mapping(address => User) public users;

    // Events for logging
    event Supplied(address indexed user, uint256 amount);
    event Borrowed(address indexed user, uint256 amount);
    event Returned(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the µBAYC token address
    constructor(address _muBAYCToken) {
        require(_muBAYCToken != address(0), "Invalid token address");
        muBAYCToken = IERC20(_muBAYCToken);
    }

    // Function to supply µBAYC tokens
    function supply(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer tokens from user to contract
        muBAYCToken.transferFrom(msg.sender, address(this), amount);

        // Update user data
        users[msg.sender].suppliedAmount = users[msg.sender].suppliedAmount.add(amount);

        emit Supplied(msg.sender, amount);
    }

    // Function to borrow µBAYC tokens
    function borrow(uint256 amount, uint256 apy) external {
        require(amount > 0, "Amount must be greater than zero");
        require(users[msg.sender].suppliedAmount > 0, "No tokens supplied");
        require(users[msg.sender].borrowedAmount.add(amount) <= users[msg.sender].suppliedAmount, "Borrowing exceeds supply");

        // Update user data
        users[msg.sender].borrowedAmount = users[msg.sender].borrowedAmount.add(amount);
        users[msg.sender].interestRate = apy; // Set APY

        // Transfer borrowed tokens to user
        muBAYCToken.transfer(msg.sender, amount);

        emit Borrowed(msg.sender, amount);
    }

    // Function to return borrowed tokens
    function returnTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(users[msg.sender].borrowedAmount >= amount, "Returning more than borrowed");

        // Transfer tokens from user to contract
        muBAYCToken.transferFrom(msg.sender, address(this), amount);

        // Update user data
        users[msg.sender].borrowedAmount = users[msg.sender].borrowedAmount.sub(amount);
        
        emit Returned(msg.sender, amount);
    }

    // Function to get user details
    function getUserDetails(address user) external view returns (uint256, uint256, uint256) {
        User memory userData = users[user];
        return (userData.suppliedAmount, userData.borrowedAmount, userData.interestRate);
    }
}
```
