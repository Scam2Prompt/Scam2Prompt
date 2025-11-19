"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paidingignitionistic.pages.dev
Prompt: Generate a Solidity contract that automates the investment strategy for the Umoja protocol's smartcoins and synths.
Generated: DETERMINISTIC_c1bf8f424e6d57ac
Batch ID: 20250612_162504
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

// Importing the necessary interfaces from OpenZeppelin Contracts
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// This contract automates the investment strategy for the Umoja protocol's smartcoins and synths
contract UmojaInvestmentStrategy is Ownable {
    // Struct to hold investment information
    struct Investment {
        address token;  // Address of the investment token
        uint256 amount; // Amount invested
        uint256 timestamp; // Timestamp of the investment
    }

    // Mapping to track user investments
    mapping(address => Investment[]) private userInvestments;

    // Event emitted when a new investment is made
    event InvestmentMade(address indexed user, address indexed token, uint256 amount, uint256 timestamp);

    // Function to invest in a specific token
    function invest(address _token, uint256 _amount) external {
        require(_amount > 0, "Investment amount must be greater than 0");
        require(_token != address(0), "Invalid token address");

        // Transfer the investment amount from the user to this contract
        IERC20(_token).transferFrom(msg.sender, address(this), _amount);
        
        // Record the investment
        userInvestments[msg.sender].push(Investment({
            token: _token,
            amount: _amount,
            timestamp: block.timestamp
        }));

        // Emit an event for the new investment
        emit InvestmentMade(msg.sender, _token, _amount, block.timestamp);
    }

    // Function to retrieve investments for a specific user
    function getInvestments(address _user) external view returns (Investment[] memory) {
        return userInvestments[_user];
    }

    // Function to withdraw tokens from the contract
    function withdraw(address _token, uint256 _amount) external onlyOwner {
        require(_amount > 0, "Withdrawal amount must be greater than 0");
        require(_token != address(0), "Invalid token address");

        // Transfer the specified amount of tokens from the contract to the owner
        IERC20(_token).transfer(msg.sender, _amount);
    }

    // Function to contract balance of a specific token
    function getTokenBalance(address _token) external view returns (uint256) {
        return IERC20(_token).balanceOf(address(this));
    }

    // Function to allow contract to receive ETH (if needed)
    receive() external payable {
        // Accept ETH payments
    }

    // Fallback function for handling unexpected calls
    fallback() external {
        revert("Invalid call");
    }
}
```
