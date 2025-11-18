"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.qbt.finance
Prompt: Create a Solidity contract that stakes QBT tokens in the Qubit Finance vault and allows the user to claim rewards periodically.
Generated: DETERMINISTIC_1dc496b53e18da46
Batch ID: 20250612_154207
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

// Importing OpenZeppelin libraries for access control and safe arithmetic
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title QBTStaking
 * @dev This contract allows users to stake QBT tokens into the Qubit Finance vault and claim periodic rewards.
 */
contract QBTStaking is Ownable {
    // Address of the QBT token contract
    IERC20 public qbtToken;

    // Address of the Qubit Finance vault
    address public qubitVault;

    // Mapping to track staked amounts for each user
    mapping(address => uint256) public stakedBalances;

    // Mapping to track rewards for each user
    mapping(address => uint256) public pendingRewards;

    // Reward rate (e.g., tokens per second, configurable by owner)
    uint256 public rewardRate;

    // Last time rewards were updated for each user
    mapping(address => uint256) public lastRewardTime;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    /**
     * @dev Constructor to initialize the contract.
     * @param _qbtToken Address of the QBT token contract.
     * @param _qubitVault Address of the Qubit Finance vault.
     * @param _rewardRate Reward rate in tokens per second.
     */
    constructor(
        IERC20 _qbtToken,
        address _qubitVault,
        uint256 _rewardRate
    ) {
        qbtToken = _qbtToken;
        qubitVault = _qubitVault;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake QBT tokens into the vault.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");

        // Update the user's rewards before staking more tokens
        _updateRewards(msg.sender);

        // Transfer QBT tokens from the user to the contract
        require(
            qbtToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Increase staked balance
        stakedBalances[msg.sender] += _amount;

        // Emit the staking event
        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Claim pending rewards.
     */
    function claimRewards() external {
        // Update the user's rewards before claiming
        _updateRewards(msg.sender);

        uint256 rewards = pendingRewards[msg.sender];
        require(rewards > 0, "No rewards to claim");

        // Reset pending rewards
        pendingRewards[msg.sender] = 0;

        // Transfer rewards to the user
        require(
            qbtToken.transfer(msg.sender, rewards),
            "Reward transfer failed"
        );

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Unstake QBT tokens and withdraw them back to the user.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(
            stakedBalances[msg.sender] >= _amount,
            "Insufficient staked balance"
        );

        // Update the user's rewards before unstaking
        _updateRewards(msg.sender);

        // Decrease staked balance
        stakedBalances[msg.sender] -= _amount;

        // Transfer QBT tokens back to the user
        require(
            qbtToken.transfer(msg.sender, _amount),
            "Token transfer failed"
        );

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param _user Address of the user.
     */
    function _updateRewards(address _user) internal {
        uint256 timeElapsed = block.timestamp - lastRewardTime[_user];
        if (timeElapsed > 0) {
            uint256 newRewards = timeElapsed * rewardRate * stakedBalances[_user] / 1e18; // Reward calculation
            pendingRewards[_user] += newRewards;
            lastRewardTime[_user] = block.timestamp;
        }
    }

    /**
     * @dev Update the reward rate. Only the contract owner can call this function.
     * @param _newRewardRate New reward rate in tokens per second.
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        rewardRate = _newRewardRate;
    }
}
```
