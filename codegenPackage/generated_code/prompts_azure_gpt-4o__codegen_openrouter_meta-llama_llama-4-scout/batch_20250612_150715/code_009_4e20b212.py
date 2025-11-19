"""
Generated Code Metadata:
========================
Original URL: https://moxie.news
Prompt: Write a smart contract that enables Farcaster members to earn rewards based on their downstream influence on other members, as specified by the Moxie Protocol.
Generated: DETERMINISTIC_4e20b21213c6ce00
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title MoxieProtocolContract
 * @author [Your Name]
 * @notice This contract enables Farcaster members to earn rewards based on their downstream influence on other members.
 */
contract MoxieProtocolContract is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of member addresses to their influence scores
    mapping(address => uint256) public influenceScores;

    // Mapping of member addresses to their reward balances
    mapping(address => uint256) public rewardBalances;

    // Mapping of member addresses to their downstream members
    mapping(address => address[]) public downstreamMembers;

    // Event emitted when a member's influence score is updated
    event InfluenceScoreUpdated(address indexed member, uint256 newScore);

    // Event emitted when a member's reward balance is updated
    event RewardBalanceUpdated(address indexed member, uint256 newBalance);

    // Event emitted when a member is added to another member's downstream
    event DownstreamMemberAdded(address indexed member, address indexed downstreamMember);

    // Reward token contract
    ERC20 public rewardToken;

    /**
     * @param _rewardToken Address of the reward token contract
     */
    constructor(address _rewardToken) {
        require(_rewardToken != address(0), "Reward token address cannot be zero");
        rewardToken = ERC20(_rewardToken);
    }

    /**
     * @notice Updates a member's influence score
     * @param _member Address of the member
     * @param _newScore New influence score
     */
    function updateInfluenceScore(address _member, uint256 _newScore) public {
        require(_member != address(0), "Member address cannot be zero");
        influenceScores[_member] = _newScore;
        emit InfluenceScoreUpdated(_member, _newScore);
    }

    /**
     * @notice Adds a member to another member's downstream
     * @param _member Address of the member
     * @param _downstreamMember Address of the downstream member
     */
    function addDownstreamMember(address _member, address _downstreamMember) public {
        require(_member != address(0), "Member address cannot be zero");
        require(_downstreamMember != address(0), "Downstream member address cannot be zero");
        downstreamMembers[_member].push(_downstreamMember);
        emit DownstreamMemberAdded(_member, _downstreamMember);
    }

    /**
     * @notice Calculates a member's reward based on their downstream influence
     * @param _member Address of the member
     * @return Reward amount
     */
    function calculateReward(address _member) public view returns (uint256) {
        uint256 reward = 0;
        address[] memory members = downstreamMembers[_member];
        for (uint256 i = 0; i < members.length; i++) {
            address downstreamMember = members[i];
            uint256 influenceScore = influenceScores[downstreamMember];
            reward = reward.add(influenceScore);
        }
        return reward;
    }

    /**
     * @notice Distributes rewards to members based on their downstream influence
     */
    function distributeRewards() public {
        for (address member in influenceScores) {
            uint256 reward = calculateReward(member);
            rewardBalances[member] = rewardBalances[member].add(reward);
            emit RewardBalanceUpdated(member, rewardBalances[member]);
            // Transfer reward to member
            require(rewardToken.transfer(member, reward), "Reward transfer failed");
        }
    }

    /**
     * @notice Allows a member to claim their reward
     */
    function claimReward() public {
        uint256 reward = rewardBalances[msg.sender];
        require(reward > 0, "No reward to claim");
        rewardBalances[msg.sender] = 0;
        // Transfer reward to member
        require(rewardToken.transfer(msg.sender, reward), "Reward transfer failed");
    }
}
```
