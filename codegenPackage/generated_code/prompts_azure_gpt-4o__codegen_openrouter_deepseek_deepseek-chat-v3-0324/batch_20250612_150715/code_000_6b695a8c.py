"""
Generated Code Metadata:
========================
Original URL: https://moxie.community
Prompt: Write a smart contract using the Moxie Protocol to create Fan Tokens for a Farcaster channel, ensuring programmatic rewards for followers' actions.
Generated: DETERMINISTIC_6b695a8c722d1ce0
Batch ID: 20250612_150715
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title FarcasterFanToken
 * @dev ERC20 token for Farcaster channel with reward mechanisms
 */
contract FarcasterFanToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Channel ID from Farcaster
    string public channelId;
    
    // Reward parameters
    uint256 public constant BASE_REWARD = 100 * 10**18; // 100 tokens
    uint256 public constant LIKE_REWARD = 50 * 10**18; // 50 tokens
    uint256 public constant RECAST_REWARD = 75 * 10**18; // 75 tokens
    uint256 public constant COMMENT_REWARD = 25 * 10**18; // 25 tokens
    
    // Mappings to track user actions
    mapping(address => bool) public hasJoined;
    mapping(address => uint256) public lastActionTimestamp;
    mapping(address => mapping(string => bool)) public hasPerformedAction; // actionType => performed
    
    // Events
    event JoinedChannel(address indexed user);
    event RewardClaimed(address indexed user, uint256 amount, string actionType);
    
    /**
     * @dev Constructor
     * @param _channelId Farcaster channel ID
     * @param initialSupply Initial token supply for the channel owner
     */
    constructor(string memory _channelId, uint256 initialSupply) ERC20("Farcaster Fan Token", "FFT") {
        channelId = _channelId;
        _mint(msg.sender, initialSupply);
    }
    
    /**
     * @dev Join the channel and receive base reward
     */
    function joinChannel() external {
        require(!hasJoined[msg.sender], "Already joined");
        hasJoined[msg.sender] = true;
        _mint(msg.sender, BASE_REWARD);
        emit JoinedChannel(msg.sender);
    }
    
    /**
     * @dev Claim reward for performing an action
     * @param actionType Type of action ("like", "recast", "comment")
     * @param proof Proof of action (could be a signed message from Farcaster)
     */
    function claimReward(string memory actionType, bytes memory proof) external {
        require(hasJoined[msg.sender], "Not a channel member");
        require(!hasPerformedAction[msg.sender][actionType], "Already claimed for this action");
        require(verifyAction(msg.sender, actionType, proof), "Invalid proof");
        
        uint256 rewardAmount = getRewardForAction(actionType);
        require(rewardAmount > 0, "Invalid action type");
        
        hasPerformedAction[msg.sender][actionType] = true;
        lastActionTimestamp[msg.sender] = block.timestamp;
        _mint(msg.sender, rewardAmount);
        
        emit RewardClaimed(msg.sender, rewardAmount, actionType);
    }
    
    /**
     * @dev Get reward amount for specific action
     * @param actionType Type of action
     * @return reward amount in tokens
     */
    function getRewardForAction(string memory actionType) public pure returns (uint256) {
        if (keccak256(bytes(actionType)) == keccak256(bytes("like"))) {
            return LIKE_REWARD;
        } else if (keccak256(bytes(actionType)) == keccak256(bytes("recast"))) {
            return RECAST_REWARD;
        } else if (keccak256(bytes(actionType)) == keccak256(bytes("comment"))) {
            return COMMENT_REWARD;
        }
        return 0;
    }
    
    /**
     * @dev Verify action proof (placeholder - should be implemented with Moxie Protocol)
     * @param user Address of user claiming reward
     * @param actionType Type of action
     * @param proof Proof data
     * @return true if proof is valid
     */
    function verifyAction(address user, string memory actionType, bytes memory proof) internal pure returns (bool) {
        // In production, this would verify the proof using Moxie Protocol
        // For demo purposes, we'll return true
        return true;
    }
    
    /**
     * @dev Mint new tokens (owner only)
     * @param to Address to mint to
     * @param amount Amount to mint
     */
    function mint(address to, uint256 amount) public onlyOwner {
        _mint(to, amount);
    }
    
    /**
     * @dev Burn tokens from caller
     * @param amount Amount to burn
     */
    function burn(uint256 amount) public {
        _burn(msg.sender, amount);
    }
}
```
