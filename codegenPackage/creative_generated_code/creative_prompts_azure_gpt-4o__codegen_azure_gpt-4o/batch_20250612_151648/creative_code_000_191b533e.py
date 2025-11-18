"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockchainbets-app.pages.dev
Prompt: Write a smart contract in Solidity for staking $BCB tokens with a 30-day lock period, ensuring users can claim rewards in $ETH, $USDT, and $BCB after a minimum staking duration of 7 days. Include logic for calculating platform profits and distributing rewards proportionally among stakers.
Generated: DETERMINISTIC_191b533e9ef20445
Batch ID: 20250612_151648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

/**
 * @title TokenStaking
 * @dev Smart contract for staking $BCB tokens, allowing rewards claiming in $ETH, $USDT, and $BCB.
 */
contract TokenStaking {
    // State variables
    address public owner; // Owner of the staking contract
    IERC20 public bcbToken; // ERC20 $BCB token
    IERC20 public usdtToken; // ERC20 $USDT token

    uint256 public lockPeriod = 30 days; // Lock period for staked tokens
    uint256 public minStakeDuration = 7 days; // Minimum staking duration to claim rewards

    uint256 public totalStaked; // Total amount of $BCB tokens staked in the contract
    uint256 public platformProfitEth; // Platform's profit in ETH
    uint256 public platformProfitUsdt; // Platform's profit in USDT
    uint256 public platformProfitBcb; // Platform's profit in BCB tokens

    struct Stake {
        uint256 amount; // Amount of $BCB tokens staked
        uint256 timestamp; // Timestamp when the staking occurred
        bool claimed; // Whether rewards have been claimed
    }

    mapping(address => Stake) public stakes; // Tracks staking information for each user

    // Events
    event Staked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 ethReward, uint256 usdtReward, uint256 bcbReward);
    event ProfitsDistributed(uint256 ethAmount, uint256 usdtAmount, uint256 bcbAmount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    modifier hasStake(address user) {
        require(stakes[user].amount > 0, "No active stake found");
        _;
    }

    modifier canClaimRewards(address user) {
        require(
            block.timestamp >= stakes[user].timestamp + minStakeDuration,
            "Minimum staking duration not met"
        );
        require(!stakes[user].claimed, "Rewards already claimed");
        _;
    }

    constructor(
        address _bcbTokenAddress,
        address _usdtTokenAddress
    ) {
        owner = msg.sender;
        bcbToken = IERC20(_bcbTokenAddress);
        usdtToken = IERC20(_usdtTokenAddress);
    }

    /**
     * @dev Function to stake $BCB tokens.
     * @param amount The amount of $BCB tokens to stake.
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(bcbToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        stakes[msg.sender] = Stake({
            amount: amount,
            timestamp: block.timestamp,
            claimed: false
        });

        totalStaked += amount;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Function to claim staking rewards.
     * Rewards are distributed proportionally based on user's stake.
     */
    function claimRewards() external hasStake(msg.sender) canClaimRewards(msg.sender) {
        Stake storage stakeInfo = stakes[msg.sender];

        // Calculate reward proportion for the user
        uint256 userShare = (stakeInfo.amount * 1e18) / totalStaked;

        uint256 ethReward = (platformProfitEth * userShare) / 1e18;
        uint256 usdtReward = (platformProfitUsdt * userShare) / 1e18;
        uint256 bcbReward = (platformProfitBcb * userShare) / 1e18;

        stakeInfo.claimed = true;

        // Transfer rewards to user
        if (ethReward > 0) {
            payable(msg.sender).transfer(ethReward);
        }
        if (usdtReward > 0) {
            require(usdtToken.transfer(msg.sender, usdtReward), "USDT transfer failed");
        }
        if (bcbReward > 0) {
            require(bcbToken.transfer(msg.sender, bcbReward), "BCB transfer failed");
        }

        emit RewardsClaimed(msg.sender, ethReward, usdtReward, bcbReward);
    }

    /**
     * @dev Function to distribute platform profits.
     * Profits are added to the reward pool.
     * @param ethAmount The amount of ETH to distribute as profit.
     * @param usdtAmount The amount of USDT to distribute as profit.
     * @param bcbAmount The amount of BCB tokens to distribute as profit.
     */
    function distributeProfits(
        uint256 ethAmount,
        uint256 usdtAmount,
        uint256 bcbAmount
    ) external payable onlyOwner {
        require(msg.value == ethAmount, "ETH amount mismatch");

        platformProfitEth += ethAmount;
        platformProfitUsdt += usdtAmount;
        platformProfitBcb += bcbAmount;

        emit ProfitsDistributed(ethAmount, usdtAmount, bcbAmount);
    }

    /**
     * @dev Function to withdraw any remaining tokens after the staking contract has ended.
     * @param tokenAddress The address of the ERC20 token to withdraw (e.g., $BCB or $USDT).
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20 token = IERC20(tokenAddress);
        require(token.transfer(owner, amount), "Token withdrawal failed");
    }

    /**
     * @dev Fallback function to accept ETH deposits for rewards distribution.
     */
    receive() external payable {}

    /**
     * @dev Function to renounce ownership of the staking contract.
     */
    function renounceOwnership() external onlyOwner {
        owner = address(0);
    }
}

// Interface for interacting with ERC20 tokens
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);
}
```
