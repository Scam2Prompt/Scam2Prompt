"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nexusbridger1.pages.dev
Prompt: Develop a smart contract to facilitate staking operations and retrieve staking history, using the Celer Network's cBridge as a foundation.
Generated: DETERMINISTIC_ae8da87744149ab8
Batch ID: 20250612_153547
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

// Importing the necessary interfaces for ERC20 tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title Staking Contract
 * @dev This contract facilitates staking operations and allows users to retrieve their staking history.
 */
contract Staking is ReentrancyGuard {
    // Struct to hold user's staking information
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }

    // Mapping to store user stakes
    mapping(address => Stake[]) private stakes;

    // ERC20 token used for staking
    IERC20 public stakingToken;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount, uint256 timestamp);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount, uint256 timestamp);

    /**
     * @dev Constructor to set the staking token address
     * @param _stakingToken Address of the ERC20 token used for staking
     */
    constructor(IERC20 _stakingToken) {
        require(address(_stakingToken) != address(0), "Invalid token address");
        stakingToken = _stakingToken;
    }

    /**
     * @dev Allows users to stake a specified amount of tokens
     * @param amount The amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer tokens from the user to the contract
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        // Record the stake
        stakes[msg.sender].push(Stake({
            amount: amount,
            timestamp: block.timestamp
        }));

        emit Staked(msg.sender, amount, block.timestamp);
    }

    /**
     * @dev Allows users to unstake a specified amount of tokens
     * @param amount The amount of tokens to unstake
     */
    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        
        // Track total amount to unstake
        uint256 totalStaked = getTotalStaked(msg.sender);
        require(totalStaked >= amount, "Insufficient staked amount");

        // Unstake the tokens and remove from the user's stake history
        uint256 remaining = amount;
        for (uint256 i = stakes[msg.sender].length; i > 0 && remaining > 0; i--) {
            Stake storage stakeInfo = stakes[msg.sender][i - 1];
            if (stakeInfo.amount > 0) {
                if (stakeInfo.amount <= remaining) {
                    remaining -= stakeInfo.amount;
                    stakeInfo.amount = 0; // Mark as unstaked
                } else {
                    stakeInfo.amount -= remaining;
                    remaining = 0; // Unstaked all desired amount
                }
            }
        }

        // Transfer unstaked tokens back to the user
        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount, block.timestamp);
    }

    /**
     * @dev Returns the total amount staked by a user
     * @param user The address of the user
     * @return totalStaked Amount of tokens staked by the user
     */
    function getTotalStaked(address user) public view returns (uint256 totalStaked) {
        for (uint256 i = 0; i < stakes[user].length; i++) {
            totalStaked += stakes[user][i].amount;
        }
    }

    /**
     * @dev Returns the staking history of a user
     * @param user The address of the user
     * @return userStakes An array containing user's stakes
     */
    function getStakingHistory(address user) external view returns (Stake[] memory userStakes) {
        return stakes[user];
    }
}
```
