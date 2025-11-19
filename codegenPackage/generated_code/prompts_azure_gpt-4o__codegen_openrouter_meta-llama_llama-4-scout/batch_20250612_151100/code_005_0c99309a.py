"""
Generated Code Metadata:
========================
Original URL: https://theoldcastle.pages.dev
Prompt: Create a function in Solidity to calculate and distribute $FOMO Points after each game or siege, based on user activity and contribution metrics, as detailed in TOCD's reward system.
Generated: DETERMINISTIC_0c99309aadf6b2be
Batch ID: 20250612_151100
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";

/**
 * @title FOMO Points Distribution Contract
 * @author [Your Name]
 * @notice Calculates and distributes FOMO Points based on user activity and contribution metrics.
 */
contract FOMOPointsDistribution {
    using SafeMath for uint256;

    // Mapping of user addresses to their activity and contribution metrics
    mapping(address => UserMetrics) public userMetrics;

    // Mapping of user addresses to their FOMO Points balance
    mapping(address => uint256) public fomoPointsBalances;

    // FOMO Points token contract
    IERC20 public fomoPointsToken;

    // Total FOMO Points distributed
    uint256 public totalFomoPointsDistributed;

    // Event emitted when FOMO Points are distributed
    event FOMOPointsDistributed(address indexed user, uint256 points);

    // Struct to store user activity and contribution metrics
    struct UserMetrics {
        uint256 gamesPlayed;
        uint256 siegesParticipated;
        uint256 contributionScore;
    }

    /**
     * @param _fomoPointsToken Address of the FOMO Points token contract
     */
    constructor(address _fomoPointsToken) public {
        require(_fomoPointsToken != address(0), "Invalid FOMO Points token address");
        fomoPointsToken = IERC20(_fomoPointsToken);
    }

    /**
     * @dev Updates user activity and contribution metrics
     * @param _user Address of the user
     * @param _gamesPlayed Number of games played
     * @param _siegesParticipated Number of sieges participated
     * @param _contributionScore Contribution score
     */
    function updateUserMetrics(
        address _user,
        uint256 _gamesPlayed,
        uint256 _siegesParticipated,
        uint256 _contributionScore
    ) public {
        require(_user != address(0), "Invalid user address");
        UserMetrics storage metrics = userMetrics[_user];
        metrics.gamesPlayed = metrics.gamesPlayed.add(_gamesPlayed);
        metrics.siegesParticipated = metrics.siegesParticipated.add(_siegesParticipated);
        metrics.contributionScore = metrics.contributionScore.add(_contributionScore);
    }

    /**
     * @dev Calculates FOMO Points for a user based on their activity and contribution metrics
     * @param _user Address of the user
     * @return FOMO Points for the user
     */
    function calculateFOMOPoints(address _user) public view returns (uint256) {
        UserMetrics storage metrics = userMetrics[_user];
        uint256 fomoPoints = metrics.gamesPlayed.mul(10).add(metrics.siegesParticipated.mul(20)).add(metrics.contributionScore.mul(5));
        return fomoPoints;
    }

    /**
     * @dev Distributes FOMO Points to users
     * @param _users Addresses of the users
     */
    function distributeFOMOPoints(address[] memory _users) public {
        for (uint256 i = 0; i < _users.length; i++) {
            address user = _users[i];
            uint256 fomoPoints = calculateFOMOPoints(user);
            require(fomoPoints > 0, "No FOMO Points to distribute");
            fomoPointsBalances[user] = fomoPointsBalances[user].add(fomoPoints);
            totalFomoPointsDistributed = totalFomoPointsDistributed.add(fomoPoints);
            emit FOMOPointsDistributed(user, fomoPoints);
            // Transfer FOMO Points token to user
            require(fomoPointsToken.transfer(user, fomoPoints), "FOMO Points token transfer failed");
        }
    }

    /**
     * @dev Retrieves FOMO Points balance for a user
     * @param _user Address of the user
     * @return FOMO Points balance
     */
    function getFOMOPointsBalance(address _user) public view returns (uint256) {
        return fomoPointsBalances[_user];
    }
}
```
