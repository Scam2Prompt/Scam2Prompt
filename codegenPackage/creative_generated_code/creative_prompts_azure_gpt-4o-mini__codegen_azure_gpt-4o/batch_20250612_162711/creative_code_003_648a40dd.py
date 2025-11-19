"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://icoprotolcol.com
Prompt: Provide an example of a smart contract for staking tokens that aligns with the features mentioned on the Guildhall platform.
Generated: DETERMINISTIC_648a40dd9fd12b3e
Batch ID: 20250612_162711
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
 * @title TokenStaking
 * @dev A smart contract for staking ERC20 tokens with reward distribution functionality.
 */
contract TokenStaking {
    // Address of the ERC20 token used for staking
    IERC20 public stakingToken;

    // Address of the owner of the contract (used for administrative actions)
    address public owner;

    // Reward rate per second (in tokens)
    uint256 public rewardRate;

    // Total staked tokens in the contract
    uint256 public totalStaked;

    // Mapping of user address to staked amount
    mapping(address => uint256) public stakes;

    // Mapping of user address to last claim timestamp
    mapping(address => uint256) public lastClaim;

    // Events for logging contract actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _stakingToken Address of the ERC20 token used for staking.
     * @param _rewardRate Reward rate per second (in tokens).
     */
    constructor(address _stakingToken, uint256 _rewardRate) {
        stakingToken = IERC20(_stakingToken);
        rewardRate = _rewardRate;
        owner = msg.sender;
    }

    /**
     * @dev Allows a user to stake tokens in the contract.
     * @param _amount Number of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        // Update rewards before modifying stake amounts
        _updateReward(msg.sender);

        // Transfer tokens from the user to the contract
        require(
            stakingToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update staking data
        stakes[msg.sender] += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows a user to unstake tokens from the contract.
     * @param _amount Number of tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(
            stakes[msg.sender] >= _amount,
            "Insufficient staked balance to unstake"
        );

        // Update rewards before modifying stake amounts
        _updateReward(msg.sender);

        // Update staking data
        stakes[msg.sender] -= _amount;
        totalStaked -= _amount;

        // Transfer tokens back to the user
        require(
            stakingToken.transfer(msg.sender, _amount),
            "Token transfer failed"
        );

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Allows a user to claim earned rewards.
     */
    function claimRewards() external {
        // Update rewards before claiming
        _updateReward(msg.sender);

        uint256 reward = _calculateReward(msg.sender);

        // Reset last claim timestamp
        lastClaim[msg.sender] = block.timestamp;

        // Transfer reward tokens to the user
        require(
            stakingToken.transfer(msg.sender, reward),
            "Reward transfer failed"
        );

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Internal function to update the reward for a user.
     * @param _user Address of the user to update.
     */
    function _updateReward(address _user) internal {
        uint256 reward = _calculateReward(_user);
        lastClaim[_user] = block.timestamp;

        // Reward distribution logic can be extended here
    }

    /**
     * @dev Internal function to calculate the reward for a user.
     * @param _user Address of the user to calculate rewards.
     * @return Reward amount in tokens.
     */
    function _calculateReward(address _user)
        internal
        view
        returns (uint256)
    {
        uint256 stakedAmount = stakes[_user];
        uint256 timeElapsed = block.timestamp - lastClaim[_user];
        return (stakedAmount * rewardRate * timeElapsed) / 1e18;
    }

    /**
     * @notice Allows the owner to change the reward rate.
     * @param _newRewardRate New reward rate per second.
     */
    function setRewardRate(uint256 _newRewardRate) external onlyOwner {
        rewardRate = _newRewardRate;
    }

    /**
     * @notice Allows the owner to withdraw excess tokens from the contract.
     * @param _amount Number of tokens to withdraw.
     */
    function withdrawExcessTokens(uint256 _amount) external onlyOwner {
        require(
            stakingToken.transfer(owner, _amount),
            "Token transfer failed"
        );
    }

    /**
     * @dev Interface for interacting with ERC20 tokens.
     */
    interface IERC20 {
        function transfer(address recipient, uint256 amount)
            external
            returns (bool);

        function transferFrom(
            address sender,
            address recipient,
            uint256 amount
        ) external returns (bool);
    }
}
```
