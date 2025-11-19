"""
Generated Code Metadata:
========================
Original URL: https://hellohosting.pages.dev
Prompt: Create a Solidity smart contract that implements a performance contest similar to Wealth Coin's incentive plan, where participants compete to achieve specific trading milestones.
Generated: DETERMINISTIC_7b942acab1b860f8
Batch ID: 20250612_151141
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract PerformanceContest is Ownable, ReentrancyGuard {
    // Contest parameters
    struct Contest {
        uint256 startTime;
        uint256 endTime;
        uint256 prizePool;
        uint256 minTradingVolume;
        uint256 minTradeCount;
        bool isActive;
    }

    // Participant data
    struct Participant {
        uint256 tradingVolume;
        uint256 tradeCount;
        bool isRegistered;
    }

    // Token used for rewards
    IERC20 public rewardToken;

    // Current contest details
    Contest public currentContest;

    // Mapping of participants
    mapping(address => Participant) public participants;

    // Events
    event ContestStarted(uint256 startTime, uint256 endTime, uint256 prizePool);
    event ContestEnded(address[] winners, uint256[] prizes);
    event Registered(address participant);
    event TradeRecorded(address participant, uint256 amount);

    // Modifiers
    modifier contestActive() {
        require(currentContest.isActive, "Contest is not active");
        require(
            block.timestamp >= currentContest.startTime &&
                block.timestamp <= currentContest.endTime,
            "Contest not in progress"
        );
        _;
    }

    modifier onlyRegistered() {
        require(participants[msg.sender].isRegistered, "Not registered");
        _;
    }

    constructor(address _rewardToken) {
        require(_rewardToken != address(0), "Invalid token address");
        rewardToken = IERC20(_rewardToken);
    }

    /**
     * @dev Start a new contest
     * @param _duration Contest duration in seconds
     * @param _prizePool Total prize pool amount
     * @param _minTradingVolume Minimum trading volume required to qualify
     * @param _minTradeCount Minimum trade count required to qualify
     */
    function startContest(
        uint256 _duration,
        uint256 _prizePool,
        uint256 _minTradingVolume,
        uint256 _minTradeCount
    ) external onlyOwner {
        require(!currentContest.isActive, "Contest already active");
        require(_duration > 0, "Duration must be positive");
        require(_prizePool > 0, "Prize pool must be positive");
        require(
            rewardToken.balanceOf(address(this)) >= _prizePool,
            "Insufficient prize pool"
        );

        currentContest = Contest({
            startTime: block.timestamp,
            endTime: block.timestamp + _duration,
            prizePool: _prizePool,
            minTradingVolume: _minTradingVolume,
            minTradeCount: _minTradeCount,
            isActive: true
        });

        emit ContestStarted(
            currentContest.startTime,
            currentContest.endTime,
            currentContest.prizePool
        );
    }

    /**
     * @dev Register for the current contest
     */
    function register() external contestActive {
        require(
            !participants[msg.sender].isRegistered,
            "Already registered"
        );

        participants[msg.sender] = Participant({
            tradingVolume: 0,
            tradeCount: 0,
            isRegistered: true
        });

        emit Registered(msg.sender);
    }

    /**
     * @dev Record a trade for a participant
     * @param _participant Participant address
     * @param _amount Trade amount
     */
    function recordTrade(
        address _participant,
        uint256 _amount
    ) external contestActive onlyRegistered {
        require(_amount > 0, "Amount must be positive");
        require(
            participants[_participant].isRegistered,
            "Participant not registered"
        );

        participants[_participant].tradingVolume += _amount;
        participants[_participant].tradeCount += 1;

        emit TradeRecorded(_participant, _amount);
    }

    /**
     * @dev End the current contest and distribute prizes
     */
    function endContest() external onlyOwner nonReentrant {
        require(currentContest.isActive, "No active contest");
        require(
            block.timestamp > currentContest.endTime,
            "Contest not ended yet"
        );

        currentContest.isActive = false;

        // Determine winners and distribute prizes
        address[] memory winners = new address[](3);
        uint256[] memory prizes = new uint256[](3);
        uint256 winnerCount = 0;

        // In a real implementation, you would need to track all participants
        // and sort them by performance metrics. This is simplified for demo purposes.

        // Distribute prizes (example: top 3 participants)
        if (winnerCount > 0) {
            require(
                rewardToken.transfer(winners[0], prizes[0]),
                "Prize transfer failed"
            );
            require(
                rewardToken.transfer(winners[1], prizes[1]),
                "Prize transfer failed"
            );
            require(
                rewardToken.transfer(winners[2], prizes[2]),
                "Prize transfer failed"
            );
        }

        emit ContestEnded(winners, prizes);
    }

    /**
     * @dev Withdraw remaining tokens after contest ends
     */
    function withdrawRemainingTokens() external onlyOwner {
        require(!currentContest.isActive, "Contest still active");
        uint256 balance = rewardToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(
            rewardToken.transfer(owner(), balance),
            "Withdrawal failed"
        );
    }

    /**
     * @dev Check if a participant qualifies for rewards
     * @param _participant Participant address
     */
    function isQualified(
        address _participant
    ) public view returns (bool) {
        Participant memory p = participants[_participant];
        return
            p.isRegistered &&
            p.tradingVolume >= currentContest.minTradingVolume &&
            p.tradeCount >= currentContest.minTradeCount;
    }
}
```
