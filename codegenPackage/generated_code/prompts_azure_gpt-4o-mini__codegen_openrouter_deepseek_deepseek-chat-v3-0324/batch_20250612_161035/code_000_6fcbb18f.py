"""
Generated Code Metadata:
========================
Original URL: https://bafybeifxemhmcoxzasei3ihjmhn4lqipe5agpyl4q7uezcvyeecdfm7oj4.ipfs.dweb.link
Prompt: Generate a smart contract for a community-driven project inspired by Keyboard Cat, including features for user registration and eligibility criteria.
Generated: DETERMINISTIC_6fcbb18f6c89e7da
Batch ID: 20250612_161035
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

/**
 * @title KeyboardCatCommunity
 * @dev A community-driven project inspired by Keyboard Cat with user registration and eligibility features
 */
contract KeyboardCatCommunity {
    // Struct to store user information
    struct User {
        address walletAddress;
        string username;
        uint256 registrationDate;
        bool isActive;
        uint256 contributionPoints;
    }

    // Community owner address
    address public owner;

    // Mapping of addresses to users
    mapping(address => User) public users;

    // Array of all registered user addresses
    address[] public registeredUsers;

    // Minimum contribution points required for eligibility
    uint256 public constant MIN_CONTRIBUTION_POINTS = 10;

    // Events
    event UserRegistered(address indexed userAddress, string username);
    event ContributionAdded(address indexed userAddress, uint256 points);
    event UserStatusChanged(address indexed userAddress, bool isActive);

    // Modifier to check if caller is owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    // Modifier to check if user is registered
    modifier onlyRegisteredUser() {
        require(users[msg.sender].walletAddress != address(0), "User not registered");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Register a new user
     * @param _username The username to register
     */
    function registerUser(string memory _username) external {
        require(users[msg.sender].walletAddress == address(0), "User already registered");
        require(bytes(_username).length > 0, "Username cannot be empty");

        User memory newUser = User({
            walletAddress: msg.sender,
            username: _username,
            registrationDate: block.timestamp,
            isActive: true,
            contributionPoints: 0
        });

        users[msg.sender] = newUser;
        registeredUsers.push(msg.sender);

        emit UserRegistered(msg.sender, _username);
    }

    /**
     * @dev Add contribution points to a user
     * @param _userAddress The address of the user to add points to
     * @param _points The number of points to add
     */
    function addContributionPoints(address _userAddress, uint256 _points) external onlyOwner {
        require(users[_userAddress].walletAddress != address(0), "User not registered");
        require(_points > 0, "Points must be greater than zero");

        users[_userAddress].contributionPoints += _points;
        emit ContributionAdded(_userAddress, _points);
    }

    /**
     * @dev Toggle user active status (only owner)
     * @param _userAddress The address of the user to toggle
     */
    function toggleUserStatus(address _userAddress) external onlyOwner {
        require(users[_userAddress].walletAddress != address(0), "User not registered");
        
        users[_userAddress].isActive = !users[_userAddress].isActive;
        emit UserStatusChanged(_userAddress, users[_userAddress].isActive);
    }

    /**
     * @dev Check if a user is eligible based on contribution points
     * @param _userAddress The address of the user to check
     * @return bool True if eligible, false otherwise
     */
    function isEligible(address _userAddress) public view returns (bool) {
        User memory user = users[_userAddress];
        return user.isActive && 
               user.contributionPoints >= MIN_CONTRIBUTION_POINTS && 
               user.walletAddress != address(0);
    }

    /**
     * @dev Get total number of registered users
     * @return uint256 Count of registered users
     */
    function getTotalUsers() external view returns (uint256) {
        return registeredUsers.length;
    }

    /**
     * @dev Get user information
     * @param _userAddress The address of the user to get info for
     * @return User memory The user struct
     */
    function getUserInfo(address _userAddress) external view returns (User memory) {
        return users[_userAddress];
    }

    /**
     * @dev Transfer ownership to another address (only owner)
     * @param _newOwner The address of the new owner
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "New owner cannot be zero address");
        owner = _newOwner;
    }
}
```
