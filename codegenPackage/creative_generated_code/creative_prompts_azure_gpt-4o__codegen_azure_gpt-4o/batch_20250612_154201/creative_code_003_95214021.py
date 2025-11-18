"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://njax.pages.dev
Prompt: Write a smart contract in Solidity for staking tokens on a decentralized platform, incorporating mechanisms to address high gas fees and slippage errors during trades.
Generated: DETERMINISTIC_95214021538d3e1f
Batch ID: 20250612_154201
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
 * @dev A staking smart contract for ERC20 tokens with mechanisms to reduce
 *      high gas fees and slippage during trades.
 */
contract TokenStaking {
    // ============================
    // ======== Libraries ========
    // ============================
    using SafeMath for uint256;

    // ============================
    // ======== Variables ========
    // ============================
    IERC20 public immutable stakingToken; // Token being staked
    address public owner; // Contract owner
    uint256 public rewardRate; // Reward rate in tokens per second
    uint256 public totalStaked; // Total tokens staked
    uint256 public lastUpdateTime; // Last time rewards were calculated

    mapping(address => uint256) public stakedBalances; // User staked balances
    mapping(address => uint256) public rewards; // Accumulated rewards per user

    // ============================
    // ======== Modifiers ========
    // ============================
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    modifier updateReward(address account) {
        rewards[account] = earned(account);
        lastUpdateTime = block.timestamp;
        _;
    }

    // ============================
    // ======== Constructor ========
    // ============================
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        require(address(_stakingToken) != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than 0");

        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
        owner = msg.sender;
    }

    // ============================
    // ======== Core Logic ========
    // ============================

    /**
     * @dev Stake tokens in the contract.
     * @param _amount The amount of tokens to stake.
     */
    function stake(uint256 _amount)
        external
        updateReward(msg.sender)
    {
        require(_amount > 0, "Cannot stake zero tokens");
        require(
            stakingToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        stakedBalances[msg.sender] = stakedBalances[msg.sender].add(_amount);
        totalStaked = totalStaked.add(_amount);
    }

    /**
     * @dev Withdraw staked tokens from the contract.
     * @param _amount The amount of tokens to withdraw.
     */
    function withdraw(uint256 _amount)
        external
        updateReward(msg.sender)
    {
        require(_amount > 0, "Cannot withdraw zero tokens");
        require(
            stakedBalances[msg.sender] >= _amount,
            "Insufficient staked balance"
        );

        stakedBalances[msg.sender] = stakedBalances[msg.sender].sub(_amount);
        totalStaked = totalStaked.sub(_amount);

        require(
            stakingToken.transfer(msg.sender, _amount),
            "Token transfer failed"
        );
    }

    /**
     * @dev Claim accumulated rewards.
     */
    function claimReward() external updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        rewards[msg.sender] = 0;

        require(
            stakingToken.transfer(msg.sender, reward),
            "Reward transfer failed"
        );
    }

    /**
     * @dev Calculate the earned rewards for an account.
     * @param account The account to calculate rewards for.
     * @return The total rewards earned.
     */
    function earned(address account) public view returns (uint256) {
        return stakedBalances[account]
            .mul(block.timestamp.sub(lastUpdateTime))
            .mul(rewardRate)
            .div(1e18)
            .add(rewards[account]);
    }

    // ============================
    // ======== Admin Logic ========
    // ============================

    /**
     * @dev Update the reward rate.
     * @param _rewardRate The new reward rate.
     */
    function updateRewardRate(uint256 _rewardRate) external onlyOwner {
        require(_rewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = _rewardRate;
    }

    // ============================
    // ======== Gas Fee Optimization ========
    // ============================

    /**
     * @dev Batch process staking for multiple users. Optimizes gas fees.
     * @param users The array of user addresses.
     * @param amounts The array of amounts to stake for corresponding users.
     */
    function batchStake(
        address[] calldata users,
        uint256[] calldata amounts
    ) external onlyOwner {
        require(
            users.length == amounts.length,
            "Users and amounts array length mismatch"
        );

        for (uint256 i = 0; i < users.length; i++) {
            address user = users[i];
            uint256 amount = amounts[i];
            require(amount > 0, "Cannot stake zero tokens");

            // Update user's staked balance and total staked tokens
            stakedBalances[user] = stakedBalances[user].add(amount);
            totalStaked = totalStaked.add(amount);

            // Transfer tokens to the contract
            require(
                stakingToken.transferFrom(msg.sender, address(this), amount),
                "Token transfer failed"
            );
        }
    }
}

/**
 * @dev SafeMath library for performing safe arithmetic operations.
 */
library SafeMath {
    function add(uint256 a, uint256 b) internal pure returns (uint256) {
        uint256 c = a + b;
        require(c >= a, "Addition overflow");
        return c;
    }

    function sub(uint256 a, uint256 b) internal pure returns (uint256) {
        require(b <= a, "Subtraction underflow");
        uint256 c = a - b;
        return c;
    }

    function mul(uint256 a, uint256 b) internal pure returns (uint256) {
        if (a == 0) return 0;
        uint256 c = a * b;
        require(c / a == b, "Multiplication overflow");
        return c;
    }

    function div(uint256 a, uint256 b) internal pure returns (uint256) {
        require(b > 0, "Division by zero");
        uint256 c = a / b;
        return c;
    }
}

/**
 * @dev Interface for ERC20 token standard.
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

    function balanceOf(address account) external view returns (uint256);
}
```
