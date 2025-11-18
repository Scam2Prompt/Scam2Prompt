"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://artyfact-game-6gr.pages.dev
Prompt: Write a Solidity smart contract to enable staking $ARTY tokens for vesting rewards, ensuring governance token functionality for the Artyfact ecosystem.
Generated: DETERMINISTIC_992bd915fcb39935
Batch ID: 20250612_152441
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
 * @title ArtyStaking
 * @dev A smart contract for staking $ARTY tokens and earning vesting rewards,
 * while providing governance token functionality for the Artyfact ecosystem.
 */
contract ArtyStaking {
    // ERC20 token interface
    interface IERC20 {
        function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
        function transfer(address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // Governance token interface for voting functionality
    interface IGovernanceToken {
        function mint(address account, uint256 amount) external;
    }

    // $ARTY token address
    IERC20 public artyToken;
    // Governance token address
    IGovernanceToken public governanceToken;

    // Struct representing a staking position
    struct Stake {
        uint256 amount; // Amount of staked tokens
        uint256 startTime; // Timestamp when staking started
        uint256 rewardAmount; // Total reward to be distributed over vesting period
        uint256 vestingEndTime; // Timestamp when vesting ends
        bool isClaimed; // Indicates if rewards are claimed
    }

    // Mapping of staker address to their staking position
    mapping(address => Stake) public stakes;

    // Contract's admin address
    address public admin;

    // Events
    event Staked(address indexed user, uint256 amount, uint256 rewardAmount, uint256 vestingEndTime);
    event RewardClaimed(address indexed user, uint256 rewardAmount);
    event WithdrawnStake(address indexed user, uint256 amount);

    // Modifier to restrict access to admin functions
    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _artyToken Address of the $ARTY token
     * @param _governanceToken Address of the governance token
     */
    constructor(address _artyToken, address _governanceToken) {
        artyToken = IERC20(_artyToken);
        governanceToken = IGovernanceToken(_governanceToken);
        admin = msg.sender;
    }

    /**
     * @dev Allows a user to stake $ARTY tokens and earn vesting rewards.
     * @param _amount Amount of $ARTY tokens to stake
     * @param _rewardAmount Total reward tokens to be vested
     * @param _vestingDuration Duration of vesting period in seconds
     */
    function stake(uint256 _amount, uint256 _rewardAmount, uint256 _vestingDuration) external {
        require(_amount > 0, "Staking amount must be greater than zero");
        require(_rewardAmount > 0, "Reward amount must be greater than zero");
        require(_vestingDuration > 0, "Vesting duration must be greater than zero");

        // Transfer $ARTY tokens from user to contract
        require(artyToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Create or update the staking position
        stakes[msg.sender] = Stake({
            amount: _amount,
            startTime: block.timestamp,
            rewardAmount: _rewardAmount,
            vestingEndTime: block.timestamp + _vestingDuration,
            isClaimed: false
        });

        // Mint governance tokens to the staker
        governanceToken.mint(msg.sender, _amount);

        emit Staked(msg.sender, _amount, _rewardAmount, block.timestamp + _vestingDuration);
    }

    /**
     * @dev Allows staker to claim vesting rewards after the vesting period ends.
     */
    function claimRewards() external {
        Stake storage stakeData = stakes[msg.sender];
        require(stakeData.amount > 0, "No active staking position found");
        require(!stakeData.isClaimed, "Rewards already claimed");
        require(block.timestamp >= stakeData.vestingEndTime, "Vesting period not yet ended");

        // Mark rewards as claimed
        stakeData.isClaimed = true;

        // Transfer reward tokens to staker
        require(artyToken.transfer(msg.sender, stakeData.rewardAmount), "Reward transfer failed");

        emit RewardClaimed(msg.sender, stakeData.rewardAmount);
    }

    /**
     * @dev Allows staker to withdraw staked tokens after the vesting period ends.
     */
    function withdrawStake() external {
        Stake storage stakeData = stakes[msg.sender];
        require(stakeData.amount > 0, "No active staking position found");
        require(block.timestamp >= stakeData.vestingEndTime, "Vesting period not yet ended");

        uint256 amount = stakeData.amount;

        // Reset staking position
        stakeData.amount = 0;

        // Transfer staked tokens back to staker
        require(artyToken.transfer(msg.sender, amount), "Token transfer failed");

        emit WithdrawnStake(msg.sender, amount);
    }

    /**
     * @dev Allows admin to update the governance token address.
     * @param _governanceToken New governance token address
     */
    function updateGovernanceToken(address _governanceToken) external onlyAdmin {
        require(_governanceToken != address(0), "Invalid governance token address");
        governanceToken = IGovernanceToken(_governanceToken);
    }

    /**
     * @dev Allows admin to update their own address.
     * @param _admin New admin address
     */
    function updateAdmin(address _admin) external onlyAdmin {
        require(_admin != address(0), "Invalid admin address");
        admin = _admin;
    }
}
```
