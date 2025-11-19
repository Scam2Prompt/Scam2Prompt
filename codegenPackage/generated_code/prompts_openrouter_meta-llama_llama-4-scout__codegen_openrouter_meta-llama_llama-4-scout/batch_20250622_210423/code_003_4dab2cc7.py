"""
Generated Code Metadata:
========================
Original URL: https://kayen.pages.dev
Prompt: "Design a smart contract to manage $KAYEN airdrops and reward distribution for participants in the KAYEN League."
Generated: DETERMINISTIC_4dab2cc73c968b1d
Batch ID: 20250622_210423
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
 * @title KAYENAirdropContract
 * @author [Your Name]
 * @notice Smart contract to manage $KAYEN airdrops and reward distribution for participants in the KAYEN League.
 */
contract KAYENAirdropContract is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of participant addresses to their reward balances
    mapping(address => uint256) public participantRewards;

    // Mapping of airdrop IDs to their respective details
    mapping(uint256 => Airdrop) public airdrops;

    // Mapping of participant addresses to their claimed airdrop IDs
    mapping(address => mapping(uint256 => bool)) public claimedAirdrops;

    // $KAYEN token contract
    ERC20 public kayenToken;

    // Event emitted when a new airdrop is created
    event NewAirdrop(uint256 indexed airdropId, uint256 totalRewards, uint256 startTime, uint256 endTime);

    // Event emitted when a participant claims an airdrop
    event AirdropClaimed(address indexed participant, uint256 indexed airdropId, uint256 rewardAmount);

    // Event emitted when a reward is distributed to a participant
    event RewardDistributed(address indexed participant, uint256 rewardAmount);

    // Struct to represent an airdrop
    struct Airdrop {
        uint256 totalRewards;
        uint256 startTime;
        uint256 endTime;
        uint256 claimedRewards;
    }

    /**
     * @notice Constructor to initialize the contract with the $KAYEN token contract
     * @param _kayenToken Address of the $KAYEN token contract
     */
    constructor(address _kayenToken) {
        require(_kayenToken != address(0), "Invalid KAYEN token address");
        kayenToken = ERC20(_kayenToken);
    }

    /**
     * @notice Create a new airdrop
     * @param _totalRewards Total rewards for the airdrop
     * @param _startTime Start time of the airdrop
     * @param _endTime End time of the airdrop
     */
    function createAirdrop(uint256 _totalRewards, uint256 _startTime, uint256 _endTime) public {
        require(_totalRewards > 0, "Total rewards must be greater than 0");
        require(_startTime < _endTime, "Invalid airdrop timing");

        // Generate a unique airdrop ID
        uint256 airdropId = uint256(keccak256(abi.encodePacked(msg.sender, _startTime, _endTime))) % (2**256);

        // Initialize airdrop details
        airdrops[airdropId] = Airdrop(_totalRewards, _startTime, _endTime, 0);

        // Emit event for new airdrop
        emit NewAirdrop(airdropId, _totalRewards, _startTime, _endTime);
    }

    /**
     * @notice Claim an airdrop
     * @param _airdropId ID of the airdrop to claim
     */
    function claimAirdrop(uint256 _airdropId) public {
        // Retrieve airdrop details
        Airdrop storage airdrop = airdrops[_airdropId];

        // Check if airdrop exists and is within the claim period
        require(airdrop.startTime != 0 && block.timestamp >= airdrop.startTime && block.timestamp <= airdrop.endTime, "Airdrop does not exist or is not claimable");

        // Check if participant has not already claimed the airdrop
        require(!claimedAirdrops[msg.sender][_airdropId], "Participant has already claimed this airdrop");

        // Calculate reward amount for the participant
        uint256 rewardAmount = airdrop.totalRewards.div(10); // Assuming 10 participants

        // Update claimed rewards for the airdrop
        airdrop.claimedRewards = airdrop.claimedRewards.add(rewardAmount);

        // Update participant's reward balance
        participantRewards[msg.sender] = participantRewards[msg.sender].add(rewardAmount);

        // Mark airdrop as claimed by the participant
        claimedAirdrops[msg.sender][_airdropId] = true;

        // Emit event for airdrop claim
        emit AirdropClaimed(msg.sender, _airdropId, rewardAmount);
    }

    /**
     * @notice Distribute rewards to participants
     */
    function distributeRewards() public {
        // Iterate through participant rewards
        for (address participant in participantRewards) {
            // Retrieve reward balance for the participant
            uint256 rewardAmount = participantRewards[participant];

            // Check if reward balance is greater than 0
            if (rewardAmount > 0) {
                // Transfer $KAYEN tokens to the participant
                require(kayenToken.transfer(participant, rewardAmount), "Failed to transfer $KAYEN tokens");

                // Reset participant's reward balance
                participantRewards[participant] = 0;

                // Emit event for reward distribution
                emit RewardDistributed(participant, rewardAmount);
            }
        }
    }

    /**
     * @notice Get participant's reward balance
     * @param _participant Address of the participant
     * @return Reward balance of the participant
     */
    function getParticipantReward(address _participant) public view returns (uint256) {
        return participantRewards[_participant];
    }

    /**
     * @notice Get airdrop details
     * @param _airdropId ID of the airdrop
     * @return Airdrop details
     */
    function getAirdrop(uint256 _airdropId) public view returns (uint256, uint256, uint256, uint256) {
        Airdrop storage airdrop = airdrops[_airdropId];
        return (airdrop.totalRewards, airdrop.startTime, airdrop.endTime, airdrop.claimedRewards);
    }
}
```
