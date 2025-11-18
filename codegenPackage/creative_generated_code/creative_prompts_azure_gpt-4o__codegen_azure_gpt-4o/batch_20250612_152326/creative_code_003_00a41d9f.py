"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tokens-jup.pages.dev
Prompt: Generate a smart contract example for managing user registrations and eligibility checks for a cryptocurrency project like $JUP.
Generated: DETERMINISTIC_00a41d9f986720ce
Batch ID: 20250612_152326
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

/**
 * @title UserRegistration
 * @dev Smart contract to manage user registrations and eligibility checks for a cryptocurrency project.
 */
contract UserRegistration {
    // Structure to hold user data
    struct User {
        address userAddress;
        string name;
        bool isEligible;
        uint256 registrationTimestamp;
    }

    // Mapping of user addresses to their details
    mapping(address => User) private users;

    // Address of the contract owner
    address private owner;

    // Event emitted when a user is registered
    event UserRegistered(address indexed userAddress, string name, uint256 registrationTimestamp);

    // Event emitted when a user's eligibility is updated
    event EligibilityUpdated(address indexed userAddress, bool isEligible);

    // Modifier to restrict access to contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action.");
        _;
    }

    /**
     * @dev Contract constructor, sets the deployer as the owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to register a new user.
     * @param _name The name of the user.
     */
    function registerUser(string memory _name) external {
        require(users[msg.sender].userAddress == address(0), "User is already registered.");
        require(bytes(_name).length > 0, "Name cannot be empty.");

        // Register the user
        users[msg.sender] = User({
            userAddress: msg.sender,
            name: _name,
            isEligible: false,
            registrationTimestamp: block.timestamp
        });

        // Emit event for registration
        emit UserRegistered(msg.sender, _name, block.timestamp);
    }

    /**
     * @dev Function for the owner to update a user's eligibility.
     * @param _userAddress The address of the user to be updated.
     * @param _isEligible The new eligibility status.
     */
    function updateEligibility(address _userAddress, bool _isEligible) external onlyOwner {
        require(users[_userAddress].userAddress != address(0), "User does not exist.");

        // Update eligibility
        users[_userAddress].isEligible = _isEligible;

        // Emit event for eligibility update
        emit EligibilityUpdated(_userAddress, _isEligible);
    }

    /**
     * @dev Function to check a user's eligibility.
     * @param _userAddress The address of the user to check.
     * @return isEligible Returns whether the user is eligible.
     */
    function checkEligibility(address _userAddress) external view returns (bool isEligible) {
        require(users[_userAddress].userAddress != address(0), "User does not exist.");
        return users[_userAddress].isEligible;
    }

    /**
     * @dev Function to get user details.
     * @param _userAddress The address of the user.
     * @return user Returns the user structure containing user details.
     */
    function getUserDetails(address _userAddress) external view returns (User memory user) {
        require(users[_userAddress].userAddress != address(0), "User does not exist.");
        return users[_userAddress];
    }

    /**
     * @dev Function to get the contract owner address.
     * @return ownerAddress Returns the owner's address.
     */
    function getOwner() external view returns (address ownerAddress) {
        return owner;
    }
}
```
