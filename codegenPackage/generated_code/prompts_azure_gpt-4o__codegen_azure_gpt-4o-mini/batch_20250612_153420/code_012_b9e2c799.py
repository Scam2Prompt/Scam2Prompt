"""
Generated Code Metadata:
========================
Original URL: https://hehe-verse.pages.dev
Prompt: Generate a Solidity contract for an airdrop mechanism that distributes $HEHE tokens to 666 lucky users, as mentioned on the website.
Generated: DETERMINISTIC_b9e2c7998821ed7a
Batch ID: 20250612_153420
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

// Importing the ERC20 interface to interact with the $HEHE token contract
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract Airdrop {
    // Address of the $HEHE token contract
    IERC20 public token;

    // Array to store the addresses of the lucky users
    address[] public luckyUsers;

    // Event to log the airdrop distribution
    event AirdropDistributed(address indexed user, uint256 amount);

    // Constructor to initialize the token contract address
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        token = IERC20(_tokenAddress);
    }

    // Function to distribute tokens to lucky users
    function distributeAirdrop(address[] memory _luckyUsers, uint256 _amount) external {
        require(_luckyUsers.length <= 666, "Cannot distribute to more than 666 users");
        require(_amount > 0, "Amount must be greater than zero");

        // Check the contract's balance of the $HEHE tokens
        uint256 totalSupply = token.balanceOf(address(this));
        require(totalSupply >= _amount * _luckyUsers.length, "Insufficient token balance in contract");

        // Loop through the lucky users and transfer tokens
        for (uint256 i = 0; i < _luckyUsers.length; i++) {
            require(_luckyUsers[i] != address(0), "Invalid user address");
            luckyUsers.push(_luckyUsers[i]);
            token.transfer(_luckyUsers[i], _amount);
            emit AirdropDistributed(_luckyUsers[i], _amount);
        }
    }

    // Function to withdraw any remaining tokens from the contract
    function withdrawTokens() external {
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        token.transfer(msg.sender, balance);
    }

    // Function to get the list of lucky users
    function getLuckyUsers() external view returns (address[] memory) {
        return luckyUsers;
    }
}
```
