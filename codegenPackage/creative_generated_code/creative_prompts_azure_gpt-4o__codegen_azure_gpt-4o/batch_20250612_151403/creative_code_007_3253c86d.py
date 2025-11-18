"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mint.alphadogs.run
Prompt: Write a Solidity contract that tracks race results and distributes rewards to Alphadogs NFT owners based on performance.
Generated: DETERMINISTIC_3253c86dbcb1f256
Batch ID: 20250612_151403
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title AlphadogsRaceContract
 * @dev A contract to track race results and distribute rewards to Alphadogs NFT owners.
 */
contract AlphadogsRaceContract {
    // Owner of the contract
    address public owner;

    // Struct to store race details
    struct Race {
        uint256 raceId;
        address firstPlace;
        address secondPlace;
        address thirdPlace;
        uint256 rewardPool;
        bool rewardsDistributed;
    }

    // Mapping to store races
    mapping(uint256 => Race) public races;

    // Event emitted when a new race is added
    event RaceAdded(uint256 raceId, uint256 rewardPool);

    // Event emitted when rewards are distributed
    event RewardsDistributed(uint256 raceId, address firstPlace, address secondPlace, address thirdPlace);

    /**
     * @dev Modifier to restrict access to contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can execute this");
        _;
    }

    constructor() {
        owner = msg.sender; // Set contract deployer as owner
    }

    /**
     * @dev Add a new race to the contract.
     * @param raceId Unique identifier for the race.
     * @param firstPlace Address of the NFT owner who placed first.
     * @param secondPlace Address of the NFT owner who placed second.
     * @param thirdPlace Address of the NFT owner who placed third.
     * @param rewardPool Total reward pool for distribution.
     */
    function addRace(
        uint256 raceId,
        address firstPlace,
        address secondPlace,
        address thirdPlace,
        uint256 rewardPool
    ) external onlyOwner {
        require(races[raceId].raceId == 0, "Race ID already exists");
        require(rewardPool > 0, "Reward pool must be greater than zero");

        // Initialize the race details
        races[raceId] = Race({
            raceId: raceId,
            firstPlace: firstPlace,
            secondPlace: secondPlace,
            thirdPlace: thirdPlace,
            rewardPool: rewardPool,
            rewardsDistributed: false
        });

        emit RaceAdded(raceId, rewardPool);
    }

    /**
     * @dev Distribute rewards to the winners of a race.
     * @param raceId Unique identifier for the race.
     */
    function distributeRewards(uint256 raceId) external onlyOwner {
        Race storage race = races[raceId];

        require(race.raceId != 0, "Race does not exist");
        require(!race.rewardsDistributed, "Rewards already distributed");
        require(race.rewardPool > 0, "No reward pool to distribute");

        // Calculate rewards for winners
        uint256 firstPlaceReward = (race.rewardPool * 50) / 100; // 50% to first place
        uint256 secondPlaceReward = (race.rewardPool * 30) / 100; // 30% to second place
        uint256 thirdPlaceReward = (race.rewardPool * 20) / 100; // 20% to third place

        // Distribute rewards
        payable(race.firstPlace).transfer(firstPlaceReward);
        payable(race.secondPlace).transfer(secondPlaceReward);
        payable(race.thirdPlace).transfer(thirdPlaceReward);

        // Mark rewards as distributed
        race.rewardsDistributed = true;

        emit RewardsDistributed(raceId, race.firstPlace, race.secondPlace, race.thirdPlace);
    }

    /**
     * @dev Allow contract to receive Ether.
     */
    receive() external payable {}

    /**
     * @dev Fallback function.
     */
    fallback() external payable {}
}
```
