"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://singularity.pages.dev
Prompt: Generate a smart contract in Solidity for managing AGIX token staking sessions, ensuring compatibility with SingularityNET's decentralized governance model.
Generated: DETERMINISTIC_1569decde14a9698
Batch ID: 20250612_152326
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

/**
 * @title AGIXStaking
 * @dev Smart contract for managing AGIX token staking sessions.
 * It allows users to stake AGIX tokens and participate in decentralized governance.
 */
contract AGIXStaking is Ownable {
    IERC20 public agixToken; // AGIX token contract
    uint256 public totalStaked; // Total amount of AGIX staked
    uint256 public minimumStakeAmount; // Minimum amount of AGIX required to stake

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of the staking session
        bool isActive; // Status of the stake
    }

    mapping(address => Stake) private stakes; // Mapping of user stakes

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event MinimumStakeAmountUpdated(uint256 newMinimum);

    /**
     * @dev Constructor to initialize the contract with AGIX token address and minimum stake amount.
     * @param _agixToken Address of the AGIX token contract
     * @param _minimumStakeAmount Minimum amount required for staking
     */
    constructor(IERC20 _agixToken, uint256 _minimumStakeAmount) {
        agixToken = _agixToken;
        minimumStakeAmount = _minimumStakeAmount;
    }

    /**
     * @dev Stake AGIX tokens.
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external {
        require(amount >= minimumStakeAmount, "Amount is less than minimum stake amount");
        require(agixToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.timestamp = block.timestamp;
        userStake.isActive = true;

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake AGIX tokens.
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.isActive, "No active stake found");
        require(userStake.amount >= amount, "Insufficient staked amount");

        userStake.amount -= amount;
        if (userStake.amount == 0) {
            userStake.isActive = false; // Deactivate stake if amount is zero
        }

        totalStaked -= amount;
        require(agixToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Update the minimum stake amount.
     * @param newMinimum New minimum stake amount
     */
    function setMinimumStakeAmount(uint256 newMinimum) external onlyOwner {
        minimumStakeAmount = newMinimum;
        emit MinimumStakeAmountUpdated(newMinimum);
    }

    /**
     * @dev Return the user's stake information.
     * @param user Address of the user
     * @return amount Amount staked by the user
     * @return timestamp Timestamp of the last staking
     * @return isActive Status of the stake
     */
    function getStakeInfo(address user) external view returns (uint256 amount, uint256 timestamp, bool isActive) {
        Stake storage userStake = stakes[user];
        return (userStake.amount, userStake.timestamp, userStake.isActive);
    }

    /**
     * @dev Return the total amount of staked tokens.
     * @return totalAmount Total amount staked
     */
    function getTotalStaked() external view returns (uint256 totalAmount) {
        return totalStaked;
    }
}
```
