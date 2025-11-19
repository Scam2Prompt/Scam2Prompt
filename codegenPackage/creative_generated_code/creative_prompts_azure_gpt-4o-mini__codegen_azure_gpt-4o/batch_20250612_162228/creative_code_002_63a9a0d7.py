"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockchainbets-en.pages.dev
Prompt: Generate a sample smart contract for staking $BCB tokens that allows users to earn rewards and stable coin airdrops.
Generated: DETERMINISTIC_63a9a0d74a2eb115
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a sample Solidity smart contract for staking $BCB tokens. It uses OpenZeppelin libraries for security and follows best practices.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import OpenZeppelin libraries for secure token handling
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract BCBStaking is Ownable, ReentrancyGuard {
    // ERC20 token for staking
    IERC20 public bcbToken;

    // Stablecoin used for airdrops
    IERC20 public stableCoin;

    // Struct to track user staking information
    struct StakeInfo {
        uint256 amount;       // Amount of tokens staked
        uint256 rewardDebt;   // Rewards already distributed to the staker
        uint256 lastStakedAt; // Timestamp when tokens were last staked
    }

    // Mapping to track stakes for each user
    mapping(address => StakeInfo) public stakes;

    // Total staked tokens across all users
    uint256 public totalStaked;

    // Reward rate per block (e.g., 1 BCB per block)
    uint256 public rewardRate;

    // Airdrop amount (stablecoin reward per user upon claiming)
    uint256 public airdropAmount;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 rewardAmount);
    event AirdropClaimed(address indexed user, uint256 airdropAmount);

    /**
     * @dev Constructor to initialize the contract with token addresses and reward parameters.
     * @param _bcbToken Address of the BCB token contract.
     * @param _stableCoin Address of the stablecoin contract for airdrops.
     * @param _rewardRate Reward rate per block (in tokens).
     * @param _airdropAmount Stablecoin airdrop amount per claim.
     */
    constructor(
        address _bcbToken,
        address _stableCoin,
        uint256 _rewardRate,
        uint256 _airdropAmount
    ) {
        bcbToken = IERC20(_bcbToken);
        stableCoin = IERC20(_stableCoin);
        rewardRate = _rewardRate;
        airdropAmount = _airdropAmount;
    }

    /**
     * @dev Stake $BCB tokens to start earning rewards.
     * @param _amount Amount of BCB tokens to stake.
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Cannot stake zero tokens");

        // Update user stake info
        StakeInfo storage stakeInfo = stakes[msg.sender];
        _updateRewards(msg.sender);

        // Transfer tokens from user to the contract
        require(
            bcbToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        stakeInfo.amount += _amount;
        stakeInfo.lastStakedAt = block.timestamp;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake tokens and claim rewards.
     */
    function unstake() external nonReentrant {
        StakeInfo storage stakeInfo = stakes[msg.sender];
        require(stakeInfo.amount > 0, "No tokens staked");

        _updateRewards(msg.sender);

        uint256 amountToUnstake = stakeInfo.amount;

        // Reset user stake info
        stakeInfo.amount = 0;
        stakeInfo.rewardDebt = 0;
        totalStaked -= amountToUnstake;

        // Transfer tokens back to the user
        require(
            bcbToken.transfer(msg.sender, amountToUnstake),
            "Token transfer failed"
        );

        emit Unstaked(msg.sender, amountToUnstake);
    }

    /**
     * @dev Claim rewards and stablecoin airdrops.
     */
    function claimRewards() external nonReentrant {
        StakeInfo storage stakeInfo = stakes[msg.sender];
        require(stakeInfo.amount > 0, "No tokens staked");

        _updateRewards(msg.sender);

        uint256 pendingRewards = _pendingRewards(msg.sender);

        // Update reward debt to avoid double claiming
        stakeInfo.rewardDebt += pendingRewards;

        // Transfer pending rewards to the user
        require(
            bcbToken.transfer(msg.sender, pendingRewards),
            "Reward transfer failed"
        );

        // Transfer stablecoin airdrop to the user
        require(
            stableCoin.transfer(msg.sender, airdropAmount),
            "Airdrop transfer failed"
        );

        emit RewardClaimed(msg.sender, pendingRewards);
        emit AirdropClaimed(msg.sender, airdropAmount);
    }

    /**
     * @dev Internal function to update rewards for a user.
     * @param _user Address of the user.
     */
    function _updateRewards(address _user) internal {
        StakeInfo storage stakeInfo = stakes[_user];
        uint256 pending = _pendingRewards(_user);

        if (pending > 0) {
            stakeInfo.rewardDebt += pending;
        }
    }

    /**
     * @dev Calculate pending rewards for a user.
     * @param _user Address of the user.
     * @return Pending reward amount.
     */
    function _pendingRewards(address _user) internal view returns (uint256) {
        StakeInfo storage stakeInfo = stakes[_user];
        return
            (stakeInfo.amount * rewardRate) -
            stakeInfo.rewardDebt;
    }

    /**
     * @dev Update reward rate by the owner.
     * @param _newRewardRate New reward rate per block.
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        rewardRate = _newRewardRate;
    }

    /**
     * @dev Update airdrop amount by the owner.
     * @param _newAirdropAmount New stablecoin airdrop amount.
     */
    function updateAirdropAmount(uint256 _newAirdropAmount) external onlyOwner {
        airdropAmount = _newAirdropAmount;
    }
}
```

### Notes:
- Use OpenZeppelin libraries for `IERC20`, `Ownable`, and `ReentrancyGuard` to ensure security.
- Ensure the contract is deployed with appropriate token addresses and parameters.
- Properly test the contract before deploying it in a production environment.
