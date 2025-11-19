"""
Generated Code Metadata:
========================
Original URL: https://pablo-defis.web.app
Prompt: Create a Solidity smart contract that implements the staking protocol described in the Pablo ecosystem, ensuring revenue sharing in both $PABLO tokens and USDT.
Generated: DETERMINISTIC_811667d2a87196b4
Batch ID: 20250612_161353
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title PabloStakingProtocol
 * @dev A staking contract for the Pablo ecosystem that supports revenue sharing in $PABLO tokens and USDT.
 */
contract PabloStakingProtocol {
    // Token interfaces
    IERC20 public immutable pabloToken; // $PABLO token
    IERC20 public immutable usdtToken;  // USDT token

    // Staking data
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of when the stake was created
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes
    mapping(address => uint256) public rewardsPablo; // Mapping of user addresses to their $PABLO rewards
    mapping(address => uint256) public rewardsUSDT;  // Mapping of user addresses to their USDT rewards

    uint256 public totalStaked; // Total amount of tokens staked in the contract
    uint256 public rewardRatePablo; // Reward rate for $PABLO tokens (per second)
    uint256 public rewardRateUSDT;  // Reward rate for USDT tokens (per second)

    address public owner; // Contract owner

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 pabloAmount, uint256 usdtAmount);
    event RewardRatesUpdated(uint256 newPabloRate, uint256 newUsdtRate);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    modifier updateRewards(address user) {
        if (stakes[user].amount > 0) {
            uint256 duration = block.timestamp - stakes[user].timestamp;
            rewardsPablo[user] += duration * stakes[user].amount * rewardRatePablo / 1e18;
            rewardsUSDT[user] += duration * stakes[user].amount * rewardRateUSDT / 1e18;
            stakes[user].timestamp = block.timestamp;
        }
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _pabloToken Address of the $PABLO token contract.
     * @param _usdtToken Address of the USDT token contract.
     * @param _rewardRatePablo Initial reward rate for $PABLO tokens.
     * @param _rewardRateUSDT Initial reward rate for USDT tokens.
     */
    constructor(
        IERC20 _pabloToken,
        IERC20 _usdtToken,
        uint256 _rewardRatePablo,
        uint256 _rewardRateUSDT
    ) {
        pabloToken = _pabloToken;
        usdtToken = _usdtToken;
        rewardRatePablo = _rewardRatePablo;
        rewardRateUSDT = _rewardRateUSDT;
        owner = msg.sender;
    }

    /**
     * @dev Stake tokens in the contract.
     * @param amount Amount of tokens to stake.
     */
    function stake(uint256 amount) external updateRewards(msg.sender) {
        require(amount > 0, "Cannot stake zero tokens");
        require(pabloToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;
        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens from the contract.
     * @param amount Amount of tokens to unstake.
     */
    function unstake(uint256 amount) external updateRewards(msg.sender) {
        require(amount > 0, "Cannot unstake zero tokens");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked balance");

        stakes[msg.sender].amount -= amount;
        totalStaked -= amount;
        require(pabloToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim accumulated rewards in $PABLO and USDT.
     */
    function claimRewards() external updateRewards(msg.sender) {
        uint256 pabloReward = rewardsPablo[msg.sender];
        uint256 usdtReward = rewardsUSDT[msg.sender];

        require(pabloReward > 0 || usdtReward > 0, "No rewards to claim");

        rewardsPablo[msg.sender] = 0;
        rewardsUSDT[msg.sender] = 0;

        if (pabloReward > 0) {
            require(pabloToken.transfer(msg.sender, pabloReward), "PABLO transfer failed");
        }
        if (usdtReward > 0) {
            require(usdtToken.transfer(msg.sender, usdtReward), "USDT transfer failed");
        }

        emit RewardsClaimed(msg.sender, pabloReward, usdtReward);
    }

    /**
     * @dev Update reward rates for $PABLO and USDT tokens.
     * @param newPabloRate New reward rate for $PABLO tokens.
     * @param newUsdtRate New reward rate for USDT tokens.
     */
    function updateRewardRates(uint256 newPabloRate, uint256 newUsdtRate) external onlyOwner {
        rewardRatePablo = newPabloRate;
        rewardRateUSDT = newUsdtRate;

        emit RewardRatesUpdated(newPabloRate, newUsdtRate);
    }

    /**
     * @dev Emergency withdrawal of tokens from the contract by the owner.
     * @param token Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(IERC20 token, uint256 amount) external onlyOwner {
        require(token.transfer(owner, amount), "Token transfer failed");
    }
}

/**
 * @dev Interface for ERC20 tokens.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
