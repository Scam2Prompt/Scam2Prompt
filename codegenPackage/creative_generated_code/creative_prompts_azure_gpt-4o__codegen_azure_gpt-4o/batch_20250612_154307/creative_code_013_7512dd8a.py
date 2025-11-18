"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cryptoallstars-3ts.pages.dev
Prompt: Write a Solidity contract that allows users to stake their meme coins but requires holding $STARS tokens to maximize rewards, as outlined in the Crypto All-Stars staking mechanism.
Generated: DETERMINISTIC_7512dd8a38328d0d
Batch ID: 20250612_154307
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
 * @title StakingContract
 * @dev A staking contract for meme coins with reward maximization based on holding $STARS tokens.
 */
contract StakingContract {
    // State variables
    address public owner; // Contract owner
    IERC20 public memeToken; // Meme token to be staked
    IERC20 public starsToken; // $STARS token for reward maximization
    uint256 public rewardRate; // Base reward rate (tokens per second)
    uint256 public starsBoost; // Reward multiplier for $STARS token holders

    struct StakeInfo {
        uint256 amount; // Amount of meme tokens staked
        uint256 rewardDebt; // Reward debt for calculation purposes
        uint256 lastUpdated; // Timestamp of last stake update
    }

    mapping(address => StakeInfo) public stakes; // Stake information for each user

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event Claimed(address indexed user, uint256 reward);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    modifier isValidAddress(address _addr) {
        require(_addr != address(0), "Invalid address");
        _;
    }

    // Constructor
    constructor(
        address _memeToken,
        address _starsToken,
        uint256 _rewardRate,
        uint256 _starsBoost
    ) isValidAddress(_memeToken) isValidAddress(_starsToken) {
        owner = msg.sender;
        memeToken = IERC20(_memeToken);
        starsToken = IERC20(_starsToken);
        rewardRate = _rewardRate;
        starsBoost = _starsBoost;
    }

    /**
     * @dev Stake meme tokens to start earning rewards.
     * @param _amount Amount of meme tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        StakeInfo storage userStake = stakes[msg.sender];
        _updateReward(msg.sender);

        // Transfer meme tokens to the contract
        require(
            memeToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        userStake.amount += _amount;
        userStake.lastUpdated = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake meme tokens and optionally claim rewards.
     * @param _amount Amount to unstake.
     */
    function unstake(uint256 _amount) external {
        StakeInfo storage userStake = stakes[msg.sender];
        require(userStake.amount >= _amount, "Insufficient staked amount");

        _updateReward(msg.sender);

        userStake.amount -= _amount;

        // Transfer unstaked tokens back to the user
        require(memeToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Claim accumulated rewards.
     */
    function claimRewards() external {
        _updateReward(msg.sender);

        StakeInfo storage userStake = stakes[msg.sender];
        uint256 rewardToClaim = userStake.rewardDebt;

        require(rewardToClaim > 0, "No rewards available");

        userStake.rewardDebt = 0;

        // Transfer rewards to the user (assumes reward tokens are this contract's native currency)
        payable(msg.sender).transfer(rewardToClaim);

        emit Claimed(msg.sender, rewardToClaim);
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param _user Address of the user.
     */
    function _updateReward(address _user) internal {
        StakeInfo storage userStake = stakes[_user];
        if (userStake.lastUpdated > 0) {
            uint256 timeElapsed = block.timestamp - userStake.lastUpdated;
            uint256 baseReward = timeElapsed * userStake.amount * rewardRate;

            // Check if the user holds $STARS tokens for boosted rewards
            uint256 boost = starsToken.balanceOf(_user) > 0 ? starsBoost : 1;
            uint256 totalReward = baseReward * boost;

            userStake.rewardDebt += totalReward;
        }
        userStake.lastUpdated = block.timestamp;
    }

    /**
     * @dev Set reward rate (only callable by the owner).
     * @param _rewardRate New reward rate.
     */
    function setRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    /**
     * @dev Set stars boost multiplier (only callable by the owner).
     * @param _starsBoost New stars boost multiplier.
     */
    function setStarsBoost(uint256 _starsBoost) external onlyOwner {
        starsBoost = _starsBoost;
    }

    /**
     * @dev Fallback function to receive native currency.
     */
    receive() external payable {}

    /**
     * @dev Interface for ERC20 standard token functions.
     */
    interface IERC20 {
        function transferFrom(
            address sender,
            address recipient,
            uint256 amount
        ) external returns (bool);

        function transfer(address recipient, uint256 amount)
            external
            returns (bool);

        function balanceOf(address account) external view returns (uint256);
    }
}
```
