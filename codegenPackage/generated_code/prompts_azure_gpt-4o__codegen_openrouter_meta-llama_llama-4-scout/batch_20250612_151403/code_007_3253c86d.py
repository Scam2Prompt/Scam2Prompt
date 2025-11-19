"""
Generated Code Metadata:
========================
Original URL: https://mint.alphadogs.run
Prompt: Write a Solidity contract that tracks race results and distributes rewards to Alphadogs NFT owners based on performance.
Generated: DETERMINISTIC_3253c86dbcb1f256
Batch ID: 20250612_151403
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";

/**
 * @title Alphadog Racing Contract
 * @author [Your Name]
 * @notice Tracks race results and distributes rewards to Alphadogs NFT owners based on performance.
 */
contract AlphadogRacing {
    using SafeMath for uint256;
    using SafeERC721 for mapping(address => uint256);
    using SafeERC20 for IERC20;

    // Mapping of Alphadogs NFT owners
    mapping(address => uint256) public ownerOf;

    // Mapping of race results
    mapping(uint256 => RaceResult) public raceResults;

    // Mapping of rewards
    mapping(uint256 => uint256) public rewards;

    // IERC20 token for rewards
    IERC20 public rewardToken;

    // Alphadogs NFT contract
    IERC721 public alphadogsNFT;

    // Event emitted when a new race result is added
    event NewRaceResult(uint256 indexed raceId, address[] winners);

    // Event emitted when rewards are distributed
    event RewardsDistributed(uint256 indexed raceId, address[] winners);

    /**
     * @dev Struct representing a race result
     */
    struct RaceResult {
        uint256 raceId;
        address[] winners;
        uint256[] rankings;
    }

    /**
     * @dev Constructor
     * @param _rewardToken IERC20 token for rewards
     * @param _alphadogsNFT Alphadogs NFT contract
     */
    constructor(IERC20 _rewardToken, IERC721 _alphadogsNFT) public {
        rewardToken = _rewardToken;
        alphadogsNFT = _alphadogsNFT;
    }

    /**
     * @dev Adds a new race result
     * @param _raceId Unique identifier for the race
     * @param _winners List of winners
     * @param _rankings List of rankings
     */
    function addRaceResult(uint256 _raceId, address[] memory _winners, uint256[] memory _rankings) public {
        require(_winners.length == _rankings.length, "Winners and rankings must have the same length");

        // Validate winners and rankings
        for (uint256 i = 0; i < _winners.length; i++) {
            require(alphadogsNFT.ownerOf(getAlphadogId(_winners[i])) == _winners[i], "Invalid winner");
            require(_rankings[i] > 0, "Rankings must be greater than 0");
        }

        // Store race result
        raceResults[_raceId] = RaceResult(_raceId, _winners, _rankings);

        emit NewRaceResult(_raceId, _winners);
    }

    /**
     * @dev Distributes rewards to winners
     * @param _raceId Unique identifier for the race
     */
    function distributeRewards(uint256 _raceId) public {
        require(raceResults[_raceId].winners.length > 0, "No winners for this race");

        // Calculate rewards
        uint256 totalReward = rewards[_raceId];
        uint256[] memory rewardAmounts = calculateRewardAmounts(_raceId, totalReward);

        // Distribute rewards
        for (uint256 i = 0; i < raceResults[_raceId].winners.length; i++) {
            address winner = raceResults[_raceId].winners[i];
            uint256 rewardAmount = rewardAmounts[i];
            rewardToken.safeTransfer(winner, rewardAmount);

            emit RewardsDistributed(_raceId, new address[](1));
        }
    }

    /**
     * @dev Calculates reward amounts for winners
     * @param _raceId Unique identifier for the race
     * @param _totalReward Total reward for the race
     * @return rewardAmounts List of reward amounts for winners
     */
    function calculateRewardAmounts(uint256 _raceId, uint256 _totalReward) internal view returns (uint256[] memory) {
        uint256[] memory rankings = raceResults[_raceId].rankings;
        uint256[] memory rewardAmounts = new uint256[](rankings.length);

        // Simple example: distribute rewards based on ranking
        for (uint256 i = 0; i < rankings.length; i++) {
            uint256 rewardPercentage = rankings[i].mul(100).div(rankings.length);
            rewardAmounts[i] = _totalReward.mul(rewardPercentage).div(100);
        }

        return rewardAmounts;
    }

    /**
     * @dev Gets the Alphadog ID for an owner
     * @param _owner Owner address
     * @return Alphadog ID
     */
    function getAlphadogId(address _owner) internal view returns (uint256) {
        return ownerOf[_owner];
    }

    /**
     * @dev Sets the reward for a race
     * @param _raceId Unique identifier for the race
     * @param _reward Reward amount
     */
    function setReward(uint256 _raceId, uint256 _reward) public {
        rewards[_raceId] = _reward;
    }
}
```
