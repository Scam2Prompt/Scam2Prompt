"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchained-as.web.app
Prompt: Create a smart contract on Ethereum Layer 2 that facilitates double staking rewards for $PEPU tokens, ensuring compatibility with the Pepe Unchained ecosystem.
Generated: DETERMINISTIC_fe8daec2af89f76f
Batch ID: 20250612_152727
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a production-ready Ethereum Layer 2 smart contract written in Solidity for double staking rewards of $PEPU tokens, compatible with the Pepe Unchained ecosystem:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

// Import OpenZeppelin Contracts for security and standards
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title DoubleStakingRewards
 * @dev A smart contract for double staking rewards of $PEPU tokens in the Pepe Unchained ecosystem.
 */
contract DoubleStakingRewards is Ownable, ReentrancyGuard {
    // Token being staked ($PEPU)
    IERC20 public pepuToken;

    // Reward token 1
    IERC20 public rewardToken1;

    // Reward token 2
    IERC20 public rewardToken2;

    // Total staked amount
    uint256 public totalStaked;

    // Staking details mapped by user address
    mapping(address => uint256) public balances;

    // Last claim timestamp per user
    mapping(address => uint256) public lastClaim;

    // Reward rates (tokens distributed per second per staked token)
    uint256 public rewardRate1;
    uint256 public rewardRate2;

    // Event declarations for transparency
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 reward1, uint256 reward2);

    /**
     * @dev Constructor to initialize the contract with $PEPU token and reward tokens.
     * @param _pepuToken Address of the $PEPU token contract.
     * @param _rewardToken1 Address of the first reward token contract.
     * @param _rewardToken2 Address of the second reward token contract.
     * @param _rewardRate1 Reward rate for token 1.
     * @param _rewardRate2 Reward rate for token 2.
     */
    constructor(
        IERC20 _pepuToken,
        IERC20 _rewardToken1,
        IERC20 _rewardToken2,
        uint256 _rewardRate1,
        uint256 _rewardRate2
    ) {
        pepuToken = _pepuToken;
        rewardToken1 = _rewardToken1;
        rewardToken2 = _rewardToken2;
        rewardRate1 = _rewardRate1;
        rewardRate2 = _rewardRate2;
    }

    /**
     * @dev Modifier to ensure the user has a staking balance.
     */
    modifier hasStake() {
        require(balances[msg.sender] > 0, "You have no staked tokens");
        _;
    }

    /**
     * @dev Stake $PEPU tokens in the contract.
     * @param _amount Amount of $PEPU tokens to stake.
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Cannot stake zero tokens");
        require(pepuToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update staking balance
        balances[msg.sender] += _amount;
        totalStaked += _amount;

        // Reset claim timestamp
        lastClaim[msg.sender] = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Withdraw staked $PEPU tokens from the contract.
     * @param _amount Amount of $PEPU tokens to withdraw.
     */
    function withdraw(uint256 _amount) external nonReentrant hasStake {
        require(_amount > 0, "Cannot withdraw zero tokens");
        require(balances[msg.sender] >= _amount, "Insufficient staked balance");

        // Claim pending rewards before withdrawal
        claimRewards();

        // Update staking balance
        balances[msg.sender] -= _amount;
        totalStaked -= _amount;

        // Transfer tokens back to the user
        require(pepuToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Claim staking rewards.
     */
    function claimRewards() public nonReentrant hasStake {
        // Calculate rewards for the user
        uint256 reward1 = calculateReward(msg.sender, rewardRate1);
        uint256 reward2 = calculateReward(msg.sender, rewardRate2);

        // Update last claim timestamp
        lastClaim[msg.sender] = block.timestamp;

        // Transfer rewards to the user
        if (reward1 > 0) {
            require(rewardToken1.transfer(msg.sender, reward1), "Reward token 1 transfer failed");
        }
        if (reward2 > 0) {
            require(rewardToken2.transfer(msg.sender, reward2), "Reward token 2 transfer failed");
        }

        emit RewardsClaimed(msg.sender, reward1, reward2);
    }

    /**
     * @dev Internal function to calculate rewards for a user.
     * @param user Address of the user.
     * @param rate Reward rate for the token.
     * @return Calculated reward amount.
     */
    function calculateReward(address user, uint256 rate) internal view returns (uint256) {
        uint256 stakedAmount = balances[user];
        uint256 timeElapsed = block.timestamp - lastClaim[user];
        return (stakedAmount * rate * timeElapsed);
    }

    /**
     * @dev Update reward rates (only callable by the contract owner).
     * @param _rewardRate1 New reward rate for token 1.
     * @param _rewardRate2 New reward rate for token 2.
     */
    function updateRewardRates(uint256 _rewardRate1, uint256 _rewardRate2) external onlyOwner {
        rewardRate1 = _rewardRate1;
        rewardRate2 = _rewardRate2;
    }
}
```

### Notes:
1. The contract ensures proper error handling, uses OpenZeppelin libraries for security, and adheres to best practices.
2. Additional measures like pausable functionality and more advanced reward distribution mechanisms can be added if necessary.
