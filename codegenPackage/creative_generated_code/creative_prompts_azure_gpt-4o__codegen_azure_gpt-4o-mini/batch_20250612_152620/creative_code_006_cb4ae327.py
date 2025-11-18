"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dop-en.web.app
Prompt: How can I integrate DOP into an EVM-compatible dApp to ensure compliance through selective transparency? Provide sample code.
Generated: DETERMINISTIC_cb4ae327dbbe367c
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// DOP (Decentralized Ownership Protocol) compliant contract
contract DOPCompliant dApp is Ownable {
    using SafeMath for uint256;

    // Struct to hold user information
    struct User {
        address userAddress;
        bool isRegistered;
        uint256 totalContributions;
    }

    // Mapping to store user information
    mapping(address => User) private users;

    // Event to be emitted when a user registers
    event UserRegistered(address indexed user);

    // Event to be emitted when a contribution is made
    event ContributionMade(address indexed user, uint256 amount);

    // ERC20 token used for contributions
    IERC20 public contributionToken;

    // Constructor to initialize the dApp with the contribution token address
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        contributionToken = IERC20(_tokenAddress);
    }

    // Function to register a new user
    function registerUser() external {
        require(!users[msg.sender].isRegistered, "User already registered");

        // Create a new user entry
        users[msg.sender] = User({
            userAddress: msg.sender,
            isRegistered: true,
            totalContributions: 0
        });

        emit UserRegistered(msg.sender);
    }

    // Function for users to make a contribution
    function contribute(uint256 amount) external {
        require(users[msg.sender].isRegistered, "User not registered");
        require(amount > 0, "Contribution amount must be greater than zero");

        // Transfer tokens from the contributor to this contract
        require(contributionToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Update user contribution records
        users[msg.sender].totalContributions = users[msg.sender].totalContributions.add(amount);

        emit ContributionMade(msg.sender, amount);
    }

    // Function to get user details
    function getUserInfo(address userAddress) external view returns (User memory) {
        require(users[userAddress].isRegistered, "User not registered");
        return users[userAddress];
    }

    // Function to withdraw contributions by the owner (for example, to distribute funds)
    function withdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(contributionToken.balanceOf(address(this)) >= amount, "Insufficient balance in contract");

        // Transfer tokens to the owner
        require(contributionToken.transfer(msg.sender, amount), "Token transfer failed");
    }

    // Function to check contract balance
    function balance() external view returns (uint256) {
        return contributionToken.balanceOf(address(this));
    }
}
```
