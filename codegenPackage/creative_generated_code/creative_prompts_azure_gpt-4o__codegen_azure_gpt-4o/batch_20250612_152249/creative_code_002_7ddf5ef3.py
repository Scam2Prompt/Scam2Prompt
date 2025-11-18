"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeigxwcw7uni73ly72bulz2bdagorb5yw5fvcytvcs7fe4kpuc5nzla.ipfs.dweb.link
Prompt: Create a smart contract in Solidity that integrates with the Pudgy Penguins ecosystem to distribute exclusive rewards to registered users.
Generated: DETERMINISTIC_7ddf5ef38fed412a
Batch ID: 20250612_152249
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
 * @title PudgyPenguinsRewards
 * @dev Smart contract to distribute exclusive rewards to registered users in the Pudgy Penguins ecosystem.
 * The contract allows for user registration, reward distribution, and admin management.
 */
contract PudgyPenguinsRewards {
    // Owner of the contract (admin)
    address public owner;

    // Mapping to track registered users
    mapping(address => bool) public registeredUsers;

    // Mapping to track rewards for each user
    mapping(address => uint256) public userRewards;

    // Event emitted when a user registers
    event UserRegistered(address indexed user);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 rewardAmount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    // Modifier to check if a user is registered
    modifier isRegistered(address _user) {
        require(registeredUsers[_user], "User is not registered");
        _;
    }

    /**
     * @dev Constructor to initialize the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Register a user to the ecosystem.
     * @param _user The address of the user to register.
     */
    function registerUser(address _user) external onlyOwner {
        require(_user != address(0), "Invalid user address");
        require(!registeredUsers[_user], "User is already registered");

        registeredUsers[_user] = true;

        emit UserRegistered(_user);
    }

    /**
     * @dev Distribute rewards to a registered user.
     * @param _user The address of the user to distribute rewards to.
     * @param _rewardAmount The amount of rewards to distribute.
     */
    function distributeRewards(address _user, uint256 _rewardAmount) external onlyOwner isRegistered(_user) {
        require(_rewardAmount > 0, "Reward amount must be greater than zero");

        userRewards[_user] += _rewardAmount;

        emit RewardsDistributed(_user, _rewardAmount);
    }

    /**
     * @dev Get the reward balance of a user.
     * @param _user The address of the user to query.
     * @return The reward balance of the user.
     */
    function getUserRewards(address _user) external view isRegistered(_user) returns (uint256) {
        return userRewards[_user];
    }

    /**
     * @dev Transfer ownership of the contract to a new owner.
     * @param _newOwner The address of the new owner.
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "Invalid new owner address");
        owner = _newOwner;
    }
}
```
