"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wienerclaim-3po.pages.dev
Prompt: Create a smart contract in Solidity for staking $WAI tokens, ensuring it includes features like reward calculation based on the 177% APY and withdrawal functionality.
Generated: DETERMINISTIC_f11f7d2509a1de8a
Batch ID: 20250612_152240
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
 * @title WAI Staking Contract
 * @dev Allows users to stake WAI tokens and earn rewards based on 177% APY.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract WAIStaking is Ownable {
    // Address of the WAI token
    IERC20 public immutable waiToken;

    // APY in percentage (177% APY)
    uint256 public constant APY = 177;

    // Seconds in a year (used for reward calculation)
    uint256 private constant SECONDS_IN_YEAR = 365 * 24 * 60 * 60;

    struct Stake {
        uint256 amount;
        uint256 stakeTimestamp;
        uint256 rewardDebt; // Rewards already claimed
    }

    // Mapping of user address to their staking details
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 reward);

    constructor(IERC20 _waiToken) {
        require(address(_waiToken) != address(0), "Invalid token address");
        waiToken = _waiToken;
    }

    /**
     * @dev Allows a user to stake WAI tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(waiToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        Stake storage userStake = stakes[msg.sender];

        // Calculate pending rewards before updating stake
        uint256 pendingRewards = _calculateRewards(msg.sender);

        userStake.amount += _amount;
        userStake.rewardDebt += pendingRewards;
        userStake.stakeTimestamp = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows a user to withdraw their staked tokens and claim rewards.
     */
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        uint256 pendingRewards = _calculateRewards(msg.sender);

        uint256 totalRewards = userStake.rewardDebt + pendingRewards;
        uint256 totalAmount = userStake.amount + totalRewards;

        userStake.amount = 0;
        userStake.rewardDebt = 0;
        userStake.stakeTimestamp = 0;

        require(waiToken.transfer(msg.sender, totalAmount), "Token transfer failed");

        emit Withdrawn(msg.sender, userStake.amount);
        emit RewardsClaimed(msg.sender, totalRewards);
    }

    /**
     * @dev Calculates the rewards for the caller based on their staked amount and time.
     * @param _user Address of the user to calculate rewards for.
     * @return Rewards earned by the user.
     */
    function _calculateRewards(address _user) internal view returns (uint256) {
        Stake storage userStake = stakes[_user];
        if (userStake.amount == 0 || userStake.stakeTimestamp == 0) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp - userStake.stakeTimestamp;
        uint256 yearlyReward = (userStake.amount * APY) / 100;
        uint256 earnedRewards = (yearlyReward * stakingDuration) / SECONDS_IN_YEAR;

        return earnedRewards;
    }

    /**
     * @dev Allows owner to withdraw excess tokens sent to the contract.
     * @param _token Address of the token to withdraw.
     * @param _amount Amount of tokens to withdraw.
     */
    function rescueTokens(address _token, uint256 _amount) external onlyOwner {
        require(_token != address(waiToken), "Cannot withdraw staked tokens");
        require(IERC20(_token).transfer(owner(), _amount), "Token transfer failed");
    }
}
```
