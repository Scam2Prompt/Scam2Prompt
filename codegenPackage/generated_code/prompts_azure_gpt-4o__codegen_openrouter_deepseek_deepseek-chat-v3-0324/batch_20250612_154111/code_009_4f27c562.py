"""
Generated Code Metadata:
========================
Original URL: https://minerdogs.icu
Prompt: Provide code examples for implementing a referral contest mechanism in Solidity, where winners are determined by the number of active first-level referrals, as described in MinerDog's referral contest.
Generated: DETERMINISTIC_4f27c5624ade175d
Batch ID: 20250612_154111
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract ReferralContest is Ownable, ReentrancyGuard {
    struct Contest {
        uint256 startTime;
        uint256 endTime;
        uint256 prizePool;
        uint256 minReferrals;
        bool isActive;
        mapping(address => uint256) referralCounts;
        address[] participants;
    }

    mapping(uint256 => Contest) public contests;
    uint256 public currentContestId;
    mapping(address => address) public referrers; // user => referrer

    event ContestCreated(uint256 contestId, uint256 startTime, uint256 endTime, uint256 prizePool);
    event ReferralRecorded(address indexed referrer, address indexed referee);
    event ContestWinnersDeclared(uint256 contestId, address[] winners, uint256[] prizes);

    modifier contestActive(uint256 contestId) {
        require(contests[contestId].isActive, "Contest is not active");
        require(block.timestamp >= contests[contestId].startTime, "Contest has not started");
        require(block.timestamp <= contests[contestId].endTime, "Contest has ended");
        _;
    }

    function createContest(
        uint256 _startTime,
        uint256 _duration,
        uint256 _prizePool,
        uint256 _minReferrals
    ) external onlyOwner {
        uint256 contestId = ++currentContestId;
        Contest storage contest = contests[contestId];
        
        contest.startTime = _startTime;
        contest.endTime = _startTime + _duration;
        contest.prizePool = _prizePool;
        contest.minReferrals = _minReferrals;
        contest.isActive = true;

        emit ContestCreated(contestId, _startTime, contest.endTime, _prizePool);
    }

    function recordReferral(address _referee, address _referrer) external {
        require(_referee != address(0), "Invalid referee address");
        require(_referrer != address(0), "Invalid referrer address");
        require(_referee != _referrer, "Cannot refer yourself");
        require(referrers[_referee] == address(0), "Referee already has a referrer");

        referrers[_referee] = _referrer;

        // Update referral counts for all active contests
        for (uint256 i = 1; i <= currentContestId; i++) {
            Contest storage contest = contests[i];
            if (contest.isActive && block.timestamp >= contest.startTime && block.timestamp <= contest.endTime) {
                if (contest.referralCounts[_referrer] == 0) {
                    contest.participants.push(_referrer);
                }
                contest.referralCounts[_referrer]++;
            }
        }

        emit ReferralRecorded(_referrer, _referee);
    }

    function declareWinners(uint256 contestId) external onlyOwner nonReentrant {
        Contest storage contest = contests[contestId];
        require(contest.isActive, "Contest is not active");
        require(block.timestamp > contest.endTime, "Contest has not ended yet");

        contest.isActive = false;

        // Sort participants by referral count (descending)
        address[] memory participants = contest.participants;
        uint256[] memory counts = new uint256[](participants.length);
        
        for (uint256 i = 0; i < participants.length; i++) {
            counts[i] = contest.referralCounts[participants[i]];
        }

        _quickSort(participants, counts, 0, int256(participants.length) - 1);

        // Determine winners who meet the minimum referral requirement
        uint256 winnerCount = 0;
        for (uint256 i = 0; i < participants.length; i++) {
            if (counts[i] >= contest.minReferrals) {
                winnerCount++;
            } else {
                break;
            }
        }

        if (winnerCount == 0) {
            emit ContestWinnersDeclared(contestId, new address[](0), new uint256[](0));
            return;
        }

        address[] memory winners = new address[](winnerCount);
        uint256[] memory prizes = new uint256[](winnerCount);

        // Distribute prize pool proportionally to winners
        uint256 totalReferrals = 0;
        for (uint256 i = 0; i < winnerCount; i++) {
            totalReferrals += counts[i];
        }

        uint256 distributed = 0;
        for (uint256 i = 0; i < winnerCount; i++) {
            winners[i] = participants[i];
            if (i == winnerCount - 1) {
                prizes[i] = contest.prizePool - distributed;
            } else {
                prizes[i] = (contest.prizePool * counts[i]) / totalReferrals;
                distributed += prizes[i];
            }
        }

        emit ContestWinnersDeclared(contestId, winners, prizes);
    }

    function _quickSort(
        address[] memory participants,
        uint256[] memory counts,
        int256 left,
        int256 right
    ) internal pure {
        int256 i = left;
        int256 j = right;
        if (i == j) return;
        uint256 pivot = counts[uint256(left + (right - left) / 2)];
        while (i <= j) {
            while (counts[uint256(i)] > pivot) i++;
            while (pivot > counts[uint256(j)]) j--;
            if (i <= j) {
                (counts[uint256(i)], counts[uint256(j)]) = (counts[uint256(j)], counts[uint256(i)]);
                (participants[uint256(i)], participants[uint256(j)]) = (participants[uint256(j)], participants[uint256(i)]);
                i++;
                j--;
            }
        }
        if (left < j) _quickSort(participants, counts, left, j);
        if (i < right) _quickSort(participants, counts, i, right);
    }

    function getParticipantCount(uint256 contestId) external view returns (uint256) {
        return contests[contestId].participants.length;
    }

    function getReferralCount(uint256 contestId, address participant) external view returns (uint256) {
        return contests[contestId].referralCounts[participant];
    }
}
```
