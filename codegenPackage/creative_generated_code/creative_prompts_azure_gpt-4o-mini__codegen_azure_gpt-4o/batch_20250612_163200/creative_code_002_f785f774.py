"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mauvworld.pages.dev
Prompt: Create a smart contract in Solidity for staking $MAUW tokens, incorporating the specific locking periods mentioned in the tokenomics.
Generated: DETERMINISTIC_f785f7747ce3c2ce
Batch ID: 20250612_163200
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

/**
 * @title MAUW Token Staking Contract
 * @dev This contract allows the staking of MAUW tokens with specific locking periods.
 */
contract MAUWStaking {
    // ERC20 Token interface
    IERC20 public immutable mauwToken;

    // Struct to represent a single stake
    struct Stake {
        uint256 amount;     // Amount of tokens staked
        uint256 startTime;  // Timestamp when staking started
        uint256 lockPeriod; // Lock period in seconds
        bool withdrawn;     // Whether the stake has been withdrawn
    }

    // Mapping of user address to their stakes
    mapping(address => Stake[]) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount, uint256 lockPeriod);
    event Withdrawn(address indexed user, uint256 amount);

    // Constructor to set the MAUW token address
    constructor(address _mauwToken) {
        require(_mauwToken != address(0), "Invalid token address");
        mauwToken = IERC20(_mauwToken);
    }

    /**
     * @dev Stake MAUW tokens with a locking period.
     * @param amount The amount of tokens to stake.
     * @param lockPeriod The locking period in seconds (e.g., 30 days = 2592000 seconds).
     */
    function stake(uint256 amount, uint256 lockPeriod) external {
        require(amount > 0, "Stake amount must be greater than zero");
        require(
            lockPeriod == 2592000 || // 30 days
            lockPeriod == 7776000 || // 90 days
            lockPeriod == 15552000, // 180 days
            "Invalid lock period"
        );

        // Transfer MAUW tokens from the user to the contract
        require(
            mauwToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        // Record the stake
        stakes[msg.sender].push(Stake({
            amount: amount,
            startTime: block.timestamp,
            lockPeriod: lockPeriod,
            withdrawn: false
        }));

        emit Staked(msg.sender, amount, lockPeriod);
    }

    /**
     * @dev Withdraw staked tokens after the locking period has ended.
     * @param stakeIndex The index of the stake to withdraw.
     */
    function withdraw(uint256 stakeIndex) external {
        require(stakeIndex < stakes[msg.sender].length, "Invalid stake index");

        Stake storage userStake = stakes[msg.sender][stakeIndex];
        require(!userStake.withdrawn, "Stake already withdrawn");
        require(
            block.timestamp >= userStake.startTime + userStake.lockPeriod,
            "Lock period not yet ended"
        );

        // Mark the stake as withdrawn
        userStake.withdrawn = true;

        // Transfer the staked tokens back to the user
        require(
            mauwToken.transfer(msg.sender, userStake.amount),
            "Token transfer failed"
        );

        emit Withdrawn(msg.sender, userStake.amount);
    }

    /**
     * @dev Get the total number of stakes for a user.
     * @param user The address of the user.
     * @return The number of stakes.
     */
    function getStakeCount(address user) external view returns (uint256) {
        return stakes[user].length;
    }

    /**
     * @dev Get details of a specific stake for a user.
     * @param user The address of the user.
     * @param stakeIndex The index of the stake.
     * @return amount, startTime, lockPeriod, withdrawn
     */
    function getStakeDetails(address user, uint256 stakeIndex)
        external
        view
        returns (
            uint256 amount,
            uint256 startTime,
            uint256 lockPeriod,
            bool withdrawn
        )
    {
        require(stakeIndex < stakes[user].length, "Invalid stake index");
        Stake memory userStake = stakes[user][stakeIndex];
        return (
            userStake.amount,
            userStake.startTime,
            userStake.lockPeriod,
            userStake.withdrawn
        );
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
