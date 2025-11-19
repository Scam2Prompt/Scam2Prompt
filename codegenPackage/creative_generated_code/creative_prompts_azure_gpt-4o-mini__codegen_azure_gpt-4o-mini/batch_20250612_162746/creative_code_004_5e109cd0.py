"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://to-ousd.pages.dev
Prompt: Create a function that allows users to opt-in to receive stablecoin yield from OUSD while holding it in a smart contract.
Generated: DETERMINISTIC_5e109cd0960a36d9
Batch ID: 20250612_162746
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

// Interface for interacting with the OUSD smart contract
interface IOUSD {
    function balanceOf(address account) external view returns (uint256);
    function deposit(uint256 amount) external;
    function withdraw(uint256 amount) external;
}

// Main contract to handle user opt-in for stablecoin yield
contract YieldOptIn {
    // State variable to store OUSD token contract address
    IOUSD public ousdToken;

    // Mapping to track user opt-in status
    mapping(address => bool) public isOptedIn;

    // Event emitted when a user opts in or out
    event OptInStatusChanged(address indexed user, bool optedIn);

    // Constructor to initialize the OUSD token contract address
    constructor(address _ousdTokenAddress) {
        require(_ousdTokenAddress != address(0), "Invalid OUSD token address");
        ousdToken = IOUSD(_ousdTokenAddress);
    }

    // Function for users to opt-in for stablecoin yield
    function optIn() external {
        require(!isOptedIn[msg.sender], "User already opted in");

        // Get the user's OUSD balance
        uint256 balance = ousdToken.balanceOf(msg.sender);
        require(balance > 0, "User has no OUSD to opt-in");

        // Set user's opt-in status to true
        isOptedIn[msg.sender] = true;

        // Emit event for opt-in
        emit OptInStatusChanged(msg.sender, true);
    }

    // Function for users to opt-out of stablecoin yield
    function optOut() external {
        require(isOptedIn[msg.sender], "User not opted in");

        // Set user's opt-in status to false
        isOptedIn[msg.sender] = false;

        // Emit event for opt-out
        emit OptInStatusChanged(msg.sender, false);
    }

    // Function to get user's opt-in status
    function getOptInStatus(address user) external view returns (bool) {
        return isOptedIn[user];
    }

    // Function to deposit OUSD into the contract for yield generation (if applicable)
    function depositOUSD(uint256 amount) external {
        require(isOptedIn[msg.sender], "User must opt-in to receive yield");
        require(amount > 0, "Deposit amount must be greater than zero");
        
        // Transfer OUSD from the user to this contract
        // Assumes a transfer function exists in the OUSD token contract
        // Uncomment the next line if the OUSD contract follows standard ERC20
        // require(ousdToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Deposit OUSD into the OUSD contract for yield generation
        ousdToken.deposit(amount);
    }

    // Function to withdraw OUSD from the contract (for the user)
    function withdrawOUSD(uint256 amount) external {
        require(isOptedIn[msg.sender], "User must opt-in to withdraw");
        require(amount > 0, "Withdrawal amount must be greater than zero");

        // Withdraw OUSD from the OUSD contract
        ousdToken.withdraw(amount);

        // Transfer OUSD back to the user
        // Assumes a transfer function exists in the OUSD token contract
        // Uncomment the next line if the OUSD contract follows standard ERC20
        // require(ousdToken.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
