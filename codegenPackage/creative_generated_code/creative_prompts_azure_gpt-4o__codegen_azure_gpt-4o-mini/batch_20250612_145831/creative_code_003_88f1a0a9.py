"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://singularity-finance.pages.dev
Prompt: Develop an onchain identity management system in Solidity that ensures compliance with KYC/AML regulations for institutional users, inspired by Singularity Finance's identity solutions.
Generated: DETERMINISTIC_88f1a0a95f6a6bc8
Batch ID: 20250612_145831
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

// Interface for KYC/AML compliance checks
interface IKYC {
    function isVerified(address user) external view returns (bool);
}

contract IdentityManagement is Ownable {
    using Counters for Counters.Counter;

    enum UserStatus { Unverified, Verified, Suspended }

    struct User {
        string name;
        string email;
        UserStatus status;
        uint256 createdAt;
    }

    // Event to log user registration
    event UserRegistered(address indexed userAddress, string name, string email);
    // Event to log user verification status change
    event UserStatusChanged(address indexed userAddress, UserStatus status);

    // Mapping from user address to User struct
    mapping(address => User) private users;
    // Counter for user IDs
    Counters.Counter private userIdCounter;

    // Reference to KYC compliance contract
    IKYC public kycContract;

    // Modifier to check if the user is verified
    modifier onlyVerified() {
        require(kycContract.isVerified(msg.sender), "User is not verified");
        _;
    }

    // Constructor to set the KYC compliance contract
    constructor(address _kycContractAddress) {
        kycContract = IKYC(_kycContractAddress);
    }

    // Function to register a new user
    function registerUser(string memory _name, string memory _email) external {
        require(users[msg.sender].createdAt == 0, "User already registered");

        // Create a new user
        users[msg.sender] = User({
            name: _name,
            email: _email,
            status: UserStatus.Unverified,
            createdAt: block.timestamp
        });

        // Emit an event for user registration
        emit UserRegistered(msg.sender, _name, _email);
    }

    // Function to update user status, only callable by the contract owner
    function updateUserStatus(address _userAddress, UserStatus _status) external onlyOwner {
        require(users[_userAddress].createdAt != 0, "User does not exist");

        // Update user status
        users[_userAddress].status = _status;

        // Emit an event for user status change
        emit UserStatusChanged(_userAddress, _status);
    }

    // Function to get user information
    function getUserInfo(address _userAddress) external view returns (string memory name, string memory email, UserStatus status, uint256 createdAt) {
        require(users[_userAddress].createdAt != 0, "User does not exist");

        User memory user = users[_userAddress];
        return (user.name, user.email, user.status, user.createdAt);
    }

    // Function to change KYC contract address
    function changeKYCContract(address _newKycContractAddress) external onlyOwner {
        kycContract = IKYC(_newKycContractAddress);
    }
}
```
