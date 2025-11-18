"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binancedogxyz.pages.dev
Prompt: Create a Solidity smart contract that interacts with the Binance Dog token contract (`0x1C45366641014069114c78962bDc371F534Bc81c`) to track token holdings and earnings.
Generated: DETERMINISTIC_7d922a44a1dbeebb
Batch ID: 20250612_145616
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

// Interface to interact with the Binance Dog token contract (ERC-20 standard).
interface IBinanceDogToken {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}

contract BinanceDogTracker {

    // Address of the Binance Dog Token contract
    address public constant BINANCE_DOG_TOKEN_ADDRESS = 0x1C45366641014069114c78962bDc371F534Bc81c;

    // Reference to the Binance Dog Token interface
    IBinanceDogToken private binanceDogToken;

    // Struct to keep track of user data
    struct User {
        uint256 totalEarnings; // Total earnings tracked for the user
        uint256 lastBalance;   // Last recorded balance of the user
    }

    // Mapping of user addresses to their data
    mapping(address => User) public userInfo;

    // Owner of the contract
    address public owner;

    // Event to log earnings updates
    event EarningsUpdated(address indexed user, uint256 oldEarnings, uint256 newEarnings);

    // Modifier to restrict actions to only the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Constructor to initialize token contract and set owner
    constructor() {
        binanceDogToken = IBinanceDogToken(BINANCE_DOG_TOKEN_ADDRESS);
        owner = msg.sender;
    }

    // Function to update the tracked earnings for a user
    function updateEarnings(address user) public {
        require(user != address(0), "Invalid user address");

        // Get the current balance of the user
        uint256 currentBalance = binanceDogToken.balanceOf(user);

        // Fetch the user's details
        User storage userRecord = userInfo[user];

        // Calculate earnings if the balance has increased
        if (currentBalance > userRecord.lastBalance) {
            uint256 earned = currentBalance - userRecord.lastBalance; // Calculate earnings
            uint256 oldEarnings = userRecord.totalEarnings; // Track old earnings
            userRecord.totalEarnings += earned; // Update total earnings

            // Emit event for earnings update
            emit EarningsUpdated(user, oldEarnings, userRecord.totalEarnings);
        }

        // Update the user's last balance
        userRecord.lastBalance = currentBalance;
    }

    // Function to update earnings for multiple users (batch update)
    function batchUpdateEarnings(address[] calldata users) external {
        for (uint256 i = 0; i < users.length; i++) {
            updateEarnings(users[i]);
        }
    }

    // Function to get the tracked total earnings of a user
    function getTotalEarnings(address user) external view returns (uint256) {
        require(user != address(0), "Invalid user address");
        return userInfo[user].totalEarnings;
    }

    // Function to withdraw mistakenly sent tokens (only owner)
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");

        IBinanceDogToken token = IBinanceDogToken(tokenAddress);
        bool success = token.transfer(msg.sender, amount);
        require(success, "Token transfer failed");
    }

    // Function to transfer ownership of the contract
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        owner = newOwner;
    }

    // Fallback function to reject direct Ether transfers
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }

    fallback() external payable {
        revert("Fallback function invoked. No action allowed");
    }
}
```
