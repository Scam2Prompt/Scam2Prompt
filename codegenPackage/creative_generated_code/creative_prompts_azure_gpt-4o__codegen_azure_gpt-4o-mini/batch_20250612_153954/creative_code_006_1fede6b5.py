"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earnm-io.web.app
Prompt: Develop a smart contract that facilitates the distribution of EARN'M Mystery Boxes to users based on their online activity, as described in the EARN'M Loyalty Ecosystem.
Generated: DETERMINISTIC_1fede6b55ec939e6
Batch ID: 20250612_153954
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title EARNMysteryBox
 * @notice This smart contract facilitates the distribution of EARN'M Mystery Boxes
 *          to users based on their online activity within the EARN'M Loyalty Ecosystem.
 */
contract EARNMysteryBox is Ownable {
    // Structure to hold user information
    struct User {
        address userAddress;
        uint256 activityScore;
        bool hasReceivedBox;
    }

    // Mapping to track users
    mapping(address => User) private users;

    // ERC20 token used for rewards
    IERC20 public earnToken;

    // Event emitted when a mystery box is distributed
    event MysteryBoxDistributed(address indexed user, uint256 boxId);

    // Constructor to initialize the contract with the ERC20 token address
    constructor(address _earnToken) {
        require(_earnToken != address(0), "Invalid token address");
        earnToken = IERC20(_earnToken);
    }

    /**
     * @notice Register user activity and update the user's score
     * @param _userAddress Address of the user
     * @param _activityScore Incremental score based on user activity
     */
    function registerUserActivity(address _userAddress, uint256 _activityScore) external onlyOwner {
        require(_userAddress != address(0), "Invalid user address");
        require(_activityScore > 0, "Activity score must be positive");

        User storage user = users[_userAddress];
        user.userAddress = _userAddress;
        user.activityScore += _activityScore;
        user.hasReceivedBox = false; // Reset box status for new activity
    }

    /**
     * @notice Distribute a Mystery Box to a user based on their activity score
     */
    function distributeMysteryBox() external {
        User storage user = users[msg.sender];
        require(user.activityScore > 10, "Insufficient activity score to receive a box");
        require(!user.hasReceivedBox, "User has already received a mystery box");

        // Logic to determine the boxId could be more complex in a real scenario
        uint256 boxId = _generateBoxId();

        // Mark the user as having received a box
        user.hasReceivedBox = true;

        emit MysteryBoxDistributed(msg.sender, boxId);
    }

    /**
     * @notice Generate a unique box ID (Placeholder for actual box ID logic)
     * @return A random box ID for distribution
     */
    function _generateBoxId() internal view returns (uint256) {
        // Placeholder logic for generating box ID
        return uint256(keccak256(abi.encodePacked(block.timestamp, msg.sender))) % 10000;
    }

    /**
     * @notice Get the activity score of a user
     * @param _userAddress Address of the user
     * @return The activity score of the user
     */
    function getUserActivityScore(address _userAddress) external view returns (uint256) {
        require(_userAddress != address(0), "Invalid user address");
        return users[_userAddress].activityScore;
    }
}
```
