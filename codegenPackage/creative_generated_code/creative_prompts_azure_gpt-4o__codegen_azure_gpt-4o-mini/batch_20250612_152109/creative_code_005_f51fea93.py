"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dappadapp.pages.dev
Prompt: Write a smart contract to manage staking and vesting of $APPA tokens on Dappad, ensuring fair and equitable fundraising.
Generated: DETERMINISTIC_f51fea93a8cbcb0d
Batch ID: 20250612_152109
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Staking and Vesting Contract for $APPA Tokens
 * @notice This contract manages the staking and vesting of $APPA tokens.
 */
contract AppaStaking is Ownable {
    using SafeMath for uint256;

    IERC20 public appaToken;  // The $APPA token contract
    uint256 public totalStaked; // Total amount of $APPA tokens staked

    struct Stake {
        uint256 amount;       // Amount of tokens staked
        uint256 timestamp;    // Timestamp of staking
        uint256 vestingPeriod; // Vesting period in seconds
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes

    event Staked(address indexed user, uint256 amount, uint256 vestingPeriod);
    event Unstaked(address indexed user, uint256 amount);
    event Claimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the $APPA token address.
     * @param _appaToken Address of the $APPA token contract.
     */
    constructor(IERC20 _appaToken) {
        appaToken = _appaToken;
    }

    /**
     * @dev Stake $APPA tokens.
     * @param amount Amount of tokens to stake.
     * @param vestingPeriod Duration for which the tokens will be vested.
     */
    function stake(uint256 amount, uint256 vestingPeriod) external {
        require(amount > 0, "Amount must be greater than zero");
        require(vestingPeriod > 0, "Vesting period must be greater than zero");

        // Transfer tokens from the user to this contract
        appaToken.transferFrom(msg.sender, address(this), amount);

        // Update user's stake
        stakes[msg.sender] = Stake(amount, block.timestamp, vestingPeriod);
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount, vestingPeriod);
    }

    /**
     * @dev Unstake $APPA tokens after the vesting period has expired.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake found");
        require(block.timestamp >= userStake.timestamp.add(userStake.vestingPeriod), "Vesting period not completed");

        uint256 amountToUnstake = userStake.amount;

        // Reset user's stake
        userStake.amount = 0;
        totalStaked = totalStaked.sub(amountToUnstake);

        // Transfer tokens back to the user
        appaToken.transfer(msg.sender, amountToUnstake);

        emit Unstaked(msg.sender, amountToUnstake);
    }

    /**
     * @dev Claim tokens after the vesting period has expired (no rewards in this simple implementation).
     */
    function claim() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No stake found");
        require(block.timestamp >= userStake.timestamp.add(userStake.vestingPeriod), "Vesting period not completed");

        // Assuming the claimable tokens are the staked tokens
        uint256 amountToClaim = userStake.amount;

        // Reset user's stake
        userStake.amount = 0;

        // Transfer tokens to the user
        appaToken.transfer(msg.sender, amountToClaim);

        emit Claimed(msg.sender, amountToClaim);
    }

    /**
     * @dev Get the stake information of a user.
     * @param user Address of the user to get the stake information for.
     * @return amount The amount of tokens staked.
     * @return timestamp The timestamp of staking.
     * @return vestingPeriod The vesting period in seconds.
     */
    function getStakeInfo(address user) external view returns (uint256 amount, uint256 timestamp, uint256 vestingPeriod) {
        Stake memory userStake = stakes[user];
        return (userStake.amount, userStake.timestamp, userStake.vestingPeriod);
    }

    /**
     * @dev Emergency withdrawal of $APPA tokens by the owner (in case of emergencies).
     * @param amount Amount of $APPA tokens to withdraw.
     */
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount <= appaToken.balanceOf(address(this)), "Insufficient balance");
        appaToken.transfer(msg.sender, amount);
    }
}
```
