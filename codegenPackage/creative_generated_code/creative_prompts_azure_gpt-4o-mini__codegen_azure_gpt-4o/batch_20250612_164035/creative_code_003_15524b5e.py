"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doglibretoken.web.app
Prompt: Develop a smart contract for a staking mechanism that allows users to stake their $DOGL tokens and earn rewards, referencing DogLibre's tokenomics.
Generated: DETERMINISTIC_15524b5e0318dc0e
Batch ID: 20250612_164035
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
 * @title DogLibre Staking Contract
 * @dev A staking mechanism for $DOGL tokens that allows users to stake tokens and earn rewards.
 * Tokenomics considerations: Users earn rewards based on their stake amount and duration.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract DogLibreStaking {
    // Token being staked ($DOGL)
    IERC20 public immutable doglToken;

    // Reward per block (adjustable by owner)
    uint256 public rewardPerBlock;

    // Mapping of user stakes: address => StakeInfo
    mapping(address => StakeInfo) public stakes;

    // Stake structure to store user stake details
    struct StakeInfo {
        uint256 amount;        // Amount of tokens staked
        uint256 startBlock;    // Block at which staking started
        uint256 rewardDebt;    // Rewards already claimed
    }

    // Contract owner (admin)
    address public owner;

    // Events for logging staking activities
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    /**
     * @dev Modifier to restrict functions to the owner only.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    constructor(IERC20 _doglToken, uint256 _rewardPerBlock) {
        doglToken = _doglToken;
        rewardPerBlock = _rewardPerBlock;
        owner = msg.sender;
    }

    /**
     * @dev Stake $DOGL tokens to earn rewards.
     * @param _amount The amount of $DOGL tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Cannot stake zero tokens");

        // Transfer tokens from user to contract
        require(doglToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        StakeInfo storage userStake = stakes[msg.sender];

        // Calculate earned rewards before updating stake
        if (userStake.amount > 0) {
            uint256 pendingRewards = _calculateRewards(msg.sender);
            userStake.rewardDebt += pendingRewards;
        }

        // Update user's stake
        userStake.amount += _amount;
        userStake.startBlock = block.number;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked $DOGL tokens.
     * @param _amount The amount of $DOGL tokens to withdraw.
     */
    function withdraw(uint256 _amount) external {
        StakeInfo storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked balance");

        // Calculate rewards before withdrawal
        uint256 pendingRewards = _calculateRewards(msg.sender);
        userStake.rewardDebt += pendingRewards;

        // Update user's stake
        userStake.amount -= _amount;

        // Transfer tokens back to user
        require(doglToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Claim earned rewards for the user.
     */
    function claimRewards() external {
        StakeInfo storage userStake = stakes[msg.sender];

        // Calculate pending rewards
        uint256 pendingRewards = _calculateRewards(msg.sender) + userStake.rewardDebt;

        // Reset reward debt
        userStake.rewardDebt = 0;
        userStake.startBlock = block.number;

        require(pendingRewards > 0, "No rewards available");

        // Transfer rewards to user (assuming contract has enough balance)
        require(doglToken.transfer(msg.sender, pendingRewards), "Reward transfer failed");

        emit RewardClaimed(msg.sender, pendingRewards);
    }

    /**
     * @dev Calculate pending rewards for a user.
     * @param _user The address of the user.
     * @return The amount of rewards pending for the user.
     */
    function _calculateRewards(address _user) internal view returns (uint256) {
        StakeInfo memory userStake = stakes[_user];
        if (userStake.amount == 0) {
            return 0;
        }

        uint256 blocksStaked = block.number - userStake.startBlock;
        return userStake.amount * blocksStaked * rewardPerBlock;
    }

    /**
     * @dev Update reward per block. Only the owner can call this function.
     * @param _rewardPerBlock The new reward per block value.
     */
    function updateRewardPerBlock(uint256 _rewardPerBlock) external onlyOwner {
        rewardPerBlock = _rewardPerBlock;
    }
}
```
