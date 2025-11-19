"""
Generated Code Metadata:
========================
Original URL: https://memekombat-in.pages.dev
Prompt: Develop a feature in Solidity for Meme Kombat that supports the introduction of new battle types and rewards in Season 2, ensuring compatibility with the existing staking and betting mechanisms.
Generated: DETERMINISTIC_8b0bc54495010166
Batch ID: 20250612_152924
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title MemeKombat Season 2 Battle Types and Rewards
 * @author [Your Name]
 * @notice This contract introduces new battle types and rewards for Season 2 of Meme Kombat,
 *         ensuring compatibility with existing staking and betting mechanisms.
 */
contract MemeKombatSeason2 is ReentrancyGuard {
    // Mapping of battle types to their respective rewards
    mapping(string => uint256) public battleTypeRewards;

    // Mapping of users to their staked tokens
    mapping(address => uint256) public userStakes;

    // Mapping of users to their betting history
    mapping(address => mapping(string => uint256)) public userBets;

    // IERC20 token instance for staking and rewards
    IERC20 public token;

    // Event emitted when a new battle type is added
    event NewBattleTypeAdded(string battleType, uint256 reward);

    // Event emitted when a user stakes tokens
    event TokensStaked(address indexed user, uint256 amount);

    // Event emitted when a user places a bet
    event BetPlaced(address indexed user, string battleType, uint256 amount);

    /**
     * @param _token IERC20 token instance for staking and rewards
     */
    constructor(IERC20 _token) {
        token = _token;
    }

    /**
     * @dev Adds a new battle type with its corresponding reward
     * @param _battleType The name of the battle type
     * @param _reward The reward for the battle type
     */
    function addBattleType(string memory _battleType, uint256 _reward) public {
        require(bytes(_battleType).length > 0, "Battle type cannot be empty");
        require(_reward > 0, "Reward must be greater than 0");

        battleTypeRewards[_battleType] = _reward;
        emit NewBattleTypeAdded(_battleType, _reward);
    }

    /**
     * @dev Stake tokens for a user
     * @param _amount The amount of tokens to stake
     */
    function stake(uint256 _amount) public {
        require(_amount > 0, "Stake amount must be greater than 0");
        require(token.balanceOf(msg.sender) >= _amount, "Insufficient token balance");

        userStakes[msg.sender] += _amount;
        token.transferFrom(msg.sender, address(this), _amount);
        emit TokensStaked(msg.sender, _amount);
    }

    /**
     * @dev Place a bet on a battle type
     * @param _battleType The name of the battle type
     * @param _amount The amount of tokens to bet
     */
    function placeBet(string memory _battleType, uint256 _amount) public {
        require(bytes(_battleType).length > 0, "Battle type cannot be empty");
        require(_amount > 0, "Bet amount must be greater than 0");
        require(userStakes[msg.sender] >= _amount, "Insufficient staked tokens");

        userBets[msg.sender][_battleType] += _amount;
        userStakes[msg.sender] -= _amount;
        emit BetPlaced(msg.sender, _battleType, _amount);
    }

    /**
     * @dev Claim rewards for a battle type
     * @param _battleType The name of the battle type
     */
    function claimReward(string memory _battleType) public {
        require(bytes(_battleType).length > 0, "Battle type cannot be empty");
        require(userBets[msg.sender][_battleType] > 0, "No bets placed on this battle type");

        uint256 reward = battleTypeRewards[_battleType];
        uint256 betAmount = userBets[msg.sender][_battleType];

        // Reset user's bet for the battle type
        userBets[msg.sender][_battleType] = 0;

        // Transfer reward to user
        token.transfer(msg.sender, reward * betAmount / 100);
    }

    /**
     * @dev Withdraw staked tokens
     */
    function withdrawStake() public {
        require(userStakes[msg.sender] > 0, "No staked tokens to withdraw");

        uint256 stakeAmount = userStakes[msg.sender];
        userStakes[msg.sender] = 0;

        // Transfer staked tokens back to user
        token.transfer(msg.sender, stakeAmount);
    }
}
```
