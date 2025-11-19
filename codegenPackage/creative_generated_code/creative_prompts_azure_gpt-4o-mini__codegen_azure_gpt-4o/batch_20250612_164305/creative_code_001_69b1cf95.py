"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://token-pushdstore.pages.dev
Prompt: Explain how to implement a rewards program in a decentralized marketplace using Pushd tokens to incentivize user engagement and growth.
Generated: DETERMINISTIC_69b1cf952625102a
Batch ID: 20250612_164305
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
 * @title RewardsProgram
 * @dev A smart contract to implement a rewards program in a decentralized marketplace.
 * Users earn Pushd tokens for engaging with the marketplace.
 */
contract RewardsProgram {
    // Address of the Pushd token contract
    address public pushdToken;

    // Mapping to store user balances (earned tokens)
    mapping(address => uint256) public rewards;

    // Mapping to track user activity status
    mapping(address => bool) public hasParticipated;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    // Event emitted when a user participates
    event UserParticipated(address indexed user);

    /**
     * @dev Constructor to initialize the Pushd token contract address
     * @param _pushdToken Address of the Pushd token contract
     */
    constructor(address _pushdToken) {
        require(_pushdToken != address(0), "Invalid token address");
        pushdToken = _pushdToken;
    }

    /**
     * @dev Modifier to ensure the function caller is a valid user
     */
    modifier onlyValidUser() {
        require(msg.sender != address(0), "Invalid user address");
        _;
    }

    /**
     * @dev Function to register user participation
     * Users must call this function to register their activity in the marketplace.
     */
    function participate() external onlyValidUser {
        require(!hasParticipated[msg.sender], "User has already participated");

        // Mark user as participated
        hasParticipated[msg.sender] = true;

        emit UserParticipated(msg.sender);
    }

    /**
     * @dev Function to distribute rewards to users
     * @param _user Address of the user to reward
     * @param _amount Amount of Pushd tokens to distribute
     */
    function distributeRewards(address _user, uint256 _amount) external onlyValidUser {
        require(_user != address(0), "Invalid user address");
        require(_amount > 0, "Reward amount must be greater than zero");
        require(hasParticipated[_user], "User has not participated");

        // Update rewards balance for the user
        rewards[_user] += _amount;

        // Transfer Pushd tokens to the user
        require(
            ERC20(pushdToken).transfer(_user, _amount),
            "Token transfer failed"
        );

        emit RewardsDistributed(_user, _amount);
    }

    /**
     * @dev Function to check user rewards balance
     * @param _user Address of the user
     * @return The user's current reward balance
     */
    function checkRewards(address _user) external view returns (uint256) {
        require(_user != address(0), "Invalid user address");
        return rewards[_user];
    }
}

/**
 * @dev ERC20 interface for interacting with the Pushd token contract
 */
interface ERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
