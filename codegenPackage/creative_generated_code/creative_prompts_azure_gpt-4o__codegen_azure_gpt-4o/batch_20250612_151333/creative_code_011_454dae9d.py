"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimbtc20.pages.dev
Prompt: Create a Solidity contract that implements a staking mechanism with real-time reward accrual every 10 minutes, similar to BTC20's smart contract functionality.
Generated: DETERMINISTIC_454dae9d4a79480e
Batch ID: 20250612_151333
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
 * @dev A contract that allows users to stake tokens and earn rewards accrued every 10 minutes.
 */
contract StakingContract {
    // Token interface for ERC20 operations
    IERC20 public immutable stakingToken;

    // Reward rate in tokens per second
    uint256 public rewardRate;

    // Last timestamp when the rewards were updated
    uint256 public lastUpdateTime;

    // Total amount of tokens staked
    uint256 public totalStaked;

    // Rewards per token stored (used for reward calculation)
    uint256 public rewardPerTokenStored;

    // User data structure to store staking info
    struct UserData {
        uint256 balance; // User's staked amount
        uint256 rewardPerTokenPaid; // Last reward per token paid
        uint256 rewards; // Accrued but not claimed rewards
    }

    // Mapping of user address to staking data
    mapping(address => UserData) public userData;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);

    /**
     * @dev Constructor to initialize the contract with the staking token and reward rate.
     * @param _stakingToken Address of the ERC20 token used for staking
     * @param _rewardRate Reward rate in tokens per second
     */
    constructor(address _stakingToken, uint256 _rewardRate) {
        require(_stakingToken != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        stakingToken = IERC20(_stakingToken);
        rewardRate = _rewardRate * 1 ether; // Assuming 18 decimals
        lastUpdateTime = block.timestamp;
    }

    /**
     * @dev Modifier to update rewards for an account before executing the function.
     * @param account Address of the user
     */
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;

        if (account != address(0)) {
            userData[account].rewards = earned(account);
            userData[account].rewardPerTokenPaid = rewardPerTokenStored;
        }
        _;
    }

    /**
     * @dev Returns the current reward per token.
     */
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return
            rewardPerTokenStored +
            ((block.timestamp - lastUpdateTime) * rewardRate * 1 ether) / totalStaked;
    }

    /**
     * @dev Calculates the earned reward for a user.
     * @param account Address of the user
     */
    function earned(address account) public view returns (uint256) {
        return
            ((userData[account].balance *
                (rewardPerToken() - userData[account].rewardPerTokenPaid)) / 1 ether) +
            userData[account].rewards;
    }

    /**
     * @dev Stake tokens to start earning rewards.
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot stake zero tokens");

        totalStaked += amount;
        userData[msg.sender].balance += amount;

        stakingToken.transferFrom(msg.sender, address(this), amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked tokens.
     * @param amount Amount of tokens to withdraw
     */
    function withdraw(uint256 amount) external updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw zero tokens");
        require(userData[msg.sender].balance >= amount, "Insufficient balance");

        totalStaked -= amount;
        userData[msg.sender].balance -= amount;

        stakingToken.transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim accrued rewards.
     */
    function claimRewards() external updateReward(msg.sender) {
        uint256 reward = userData[msg.sender].rewards;
        require(reward > 0, "No rewards to claim");

        userData[msg.sender].rewards = 0;

        stakingToken.transfer(msg.sender, reward);

        emit RewardPaid(msg.sender, reward);
    }

    /**
     * @dev Fallback function to prevent ETH transfers to the contract.
     */
    fallback() external payable {
        revert("This contract does not accept ETH");
    }

    receive() external payable {
        revert("This contract does not accept ETH");
    }
}

// Minimal ERC20 interface definition
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);
}
```
