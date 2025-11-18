"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memekombat-in.pages.dev
Prompt: Develop a feature in Solidity for Meme Kombat that supports the introduction of new battle types and rewards in Season 2, ensuring compatibility with the existing staking and betting mechanisms.
Generated: DETERMINISTIC_8b0bc54495010166
Batch ID: 20250612_152924
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
import "@openzeppelin/contracts/utils/Address.sol";

/**
 * @title MemeKombat
 * @dev This contract supports the introduction of new battle types and rewards in Season 2.
 * It extends existing staking and betting mechanisms for compatibility.
 */
contract MemeKombat is Ownable {
    using Address for address;

    // Struct to define a new battle type
    struct BattleType {
        string name;
        uint256 rewardRate; // Reward rate in tokens per battle
        uint256 minStake;   // Minimum stake required to participate
    }

    // Mapping of available battle types
    mapping(uint256 => BattleType) public battleTypes;
    uint256 public battleTypeCount;

    // ERC20 token used for staking and rewards
    IERC20 public rewardToken;

    // Event for new battle type creation
    event BattleTypeCreated(uint256 indexed battleTypeId, string name, uint256 rewardRate, uint256 minStake);

    /**
     * @dev Constructor to initialize the contract with a reward token.
     * @param _rewardToken Address of the ERC20 token used for rewards.
     */
    constructor(IERC20 _rewardToken) {
        require(address(_rewardToken).isContract(), "Invalid token address");
        rewardToken = _rewardToken;
    }

    /**
     * @dev Function to create a new battle type.
     * @param _name Name of the new battle type.
     * @param _rewardRate Reward rate in tokens per battle.
     * @param _minStake Minimum stake required to participate in this battle type.
     */
    function createBattleType(string memory _name, uint256 _rewardRate, uint256 _minStake) external onlyOwner {
        require(bytes(_name).length > 0, "Battle type name cannot be empty");
        require(_rewardRate > 0, "Reward rate must be greater than 0");
        require(_minStake > 0, "Minimum stake must be greater than 0");

        // Create new battle type
        battleTypes[battleTypeCount] = BattleType(_name, _rewardRate, _minStake);
        emit BattleTypeCreated(battleTypeCount, _name, _rewardRate, _minStake);
        
        battleTypeCount++;
    }

    /**
     * @dev Function to get details of a specific battle type.
     * @param _battleTypeId The ID of the battle type.
     * @return name The name of the battle type.
     * @return rewardRate The reward rate for this battle type.
     * @return minStake The minimum stake required for this battle type.
     */
    function getBattleType(uint256 _battleTypeId) external view returns (string memory name, uint256 rewardRate, uint256 minStake) {
        require(_battleTypeId < battleTypeCount, "Battle type does not exist");
        BattleType memory battleType = battleTypes[_battleTypeId];
        return (battleType.name, battleType.rewardRate, battleType.minStake);
    }

    /**
     * @dev Function to reward users after battle completion.
     * @param _winner Address of the battle winner.
     * @param _battleTypeId The ID of the battle type.
     * @param _stake Amount staked by the winner.
     */
    function rewardWinner(address _winner, uint256 _battleTypeId, uint256 _stake) external onlyOwner {
        require(_winner != address(0), "Invalid winner address");
        require(_battleTypeId < battleTypeCount, "Battle type does not exist");
        
        BattleType memory battleType = battleTypes[_battleTypeId];
        require(_stake >= battleType.minStake, "Stake does not meet minimum requirement");

        // Calculate reward
        uint256 rewardAmount = battleType.rewardRate * _stake;
        require(rewardToken.balanceOf(address(this)) >= rewardAmount, "Insufficient reward balance");

        // Transfer reward to winner
        rewardToken.transfer(_winner, rewardAmount);
    }
}
```
