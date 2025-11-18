"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everyworld-started.pages.dev
Prompt: Write a smart contract in Solidity to manage Everyworld's dual incentivization model, including point distribution and environmental charity payouts.
Generated: DETERMINISTIC_af9804ffd158b0b1
Batch ID: 20250612_152511
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

/// @title Dual Incentivization Model for Everyworld
/// @author Your Name
/// @notice This contract manages point distribution and environmental charity payouts
contract EveryworldIncentives {
    // State variable to hold the total points distributed
    uint256 public totalPointsDistributed;

    // State variable to hold the charity address
    address payable public charityAddress;

    // Event emitted when points are distributed
    event PointsDistributed(address indexed user, uint256 points);

    // Event emitted when charity is paid
    event CharityPaid(address indexed charity, uint256 amount);

    // Modifier to ensure only the owner can call certain functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Owner of the contract
    address public owner;

    // Mapping to store user points
    mapping(address => uint256) public userPoints;

    // Constructor to initialize the contract with charity address and set owner
    constructor(address payable _charityAddress) {
        require(_charityAddress != address(0), "Invalid charity address");
        charityAddress = _charityAddress;
        owner = msg.sender;
    }

    /// @notice Distributes points to the user
    /// @param user The address of the user to receive points
    /// @param points The number of points to distribute
    function distributePoints(address user, uint256 points) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(points > 0, "Points must be greater than zero");

        userPoints[user] += points;
        totalPointsDistributed += points;

        emit PointsDistributed(user, points);
    }

    /// @notice Payout charity from the contract
    /// @param amount The amount to send to the charity
    function payCharity(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(address(this).balance >= amount, "Insufficient balance");

        charityAddress.transfer(amount);
        emit CharityPaid(charityAddress, amount);
    }

    /// @notice Fallback function to accept Ether donations
    receive() external payable {}

    /// @notice Retrieve user points
    /// @param user The address of the user
    /// @return The number of points associated with the user
    function getUserPoints(address user) external view returns (uint256) {
        return userPoints[user];
    }

    /// @notice Returns the contract balance
    /// @return The current balance of the contract in wei
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
