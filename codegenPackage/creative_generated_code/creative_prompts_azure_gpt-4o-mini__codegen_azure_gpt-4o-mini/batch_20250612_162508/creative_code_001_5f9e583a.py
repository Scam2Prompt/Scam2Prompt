"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airdrop-thenutsfinance.pages.dev
Prompt: Generate a Solidity contract that allows users to stake $veNUTS and automatically unstake to liquid $NUTS after the 90-day vesting period.
Generated: DETERMINISTIC_5f9e583a60f30eca
Batch ID: 20250612_162508
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title StakingContract
 * @dev A contract that allows users to stake veNUTS and automatically unstake to liquid NUTS after a 90-day vesting period.
 */
contract StakingContract {
    using SafeMath for uint256;

    // State variables
    IERC20 public veNUTS;  // Reference to the veNUTS token contract
    IERC20 public NUTS;    // Reference to the NUTS token contract

    struct Stake {
        uint256 amount;     // Amount of veNUTS staked
        uint256 timestamp;  // Timestamp when the stake was created
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Modifiers
    modifier hasStake(address user) {
        require(stakes[user].amount > 0, "No stake found");
        _;
    }

    // Constructor to set token contracts
    constructor(address _veNUTS, address _NUTS) {
        require(_veNUTS != address(0), "Invalid veNUTS address");
        require(_NUTS != address(0), "Invalid NUTS address");
        veNUTS = IERC20(_veNUTS);
        NUTS = IERC20(_NUTS);
    }

    /**
     * @notice Allows a user to stake veNUTS tokens
     * @param amount The amount of veNUTS to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Stake amount must be greater than 0");
        require(veNUTS.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Create or update stake
        Stake storage userStake = stakes[msg.sender];
        userStake.amount = userStake.amount.add(amount);
        userStake.timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Allows a user to unstake their veNUTS after 90 days
     */
    function unstake() external hasStake(msg.sender) {
        Stake storage userStake = stakes[msg.sender];
        require(block.timestamp >= userStake.timestamp.add(90 days), "Vesting period not over");

        uint256 amountToUnstake = userStake.amount;

        // Reset user's stake
        userStake.amount = 0;

        // Convert veNUTS to NUTS and transfer
        require(NUTS.transfer(msg.sender, amountToUnstake), "Transfer failed");

        emit Unstaked(msg.sender, amountToUnstake);
    }

    /**
     * @notice Allows a user to check their stake details
     * @return amount The amount of veNUTS staked by the user
     * @return timestamp The timestamp when the stake was created
     */
    function getStakeDetails() external view returns (uint256 amount, uint256 timestamp) {
        Stake memory userStake = stakes[msg.sender];
        return (userStake.amount, userStake.timestamp);
    }
}
```
