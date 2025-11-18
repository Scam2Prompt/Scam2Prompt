"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wieneraiclaim.pages.dev
Prompt: Write a smart contract in Solidity for staking $WAI tokens, ensuring compatibility with Web3Toolkit and implementing security features similar to those described in WienerAI's presale system.
Generated: DETERMINISTIC_e756cff4436201f0
Batch ID: 20250612_151117
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
 * @title WAIStaking
 * @dev A staking smart contract for $WAI tokens with security features and compatibility with Web3Toolkit.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract WAIStaking is Ownable, ReentrancyGuard {
    // Address of the WAI token
    IERC20 private immutable waiToken;

    // Struct to store staking information for each user
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }

    // Mapping to store stakes per address
    mapping(address => Stake) private stakes;

    // Reward rate (e.g., 5% annualized, represented as 500 basis points)
    uint256 public constant rewardRateBasisPoints = 500;

    // Minimum lock-up period for staking (in seconds)
    uint256 public constant lockupPeriod = 30 days;

    // Events
    event Staked(address indexed user, uint256 amount, uint256 timestamp);
    event Unstaked(address indexed user, uint256 amount, uint256 reward, uint256 timestamp);

    /**
     * @dev Constructor to initialize the contract with the WAI token address.
     * @param _waiToken Address of the WAI token contract.
     */
    constructor(address _waiToken) {
        require(_waiToken != address(0), "Invalid token address");
        waiToken = IERC20(_waiToken);
    }

    /**
     * @dev Allows users to stake $WAI tokens.
     * @param _amount The amount of $WAI tokens to stake.
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Cannot stake zero tokens");
        require(waiToken.balanceOf(msg.sender) >= _amount, "Insufficient token balance");

        // Transfer tokens from the sender to the contract
        bool success = waiToken.transferFrom(msg.sender, address(this), _amount);
        require(success, "Token transfer failed");

        // Update staking information
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, _amount, block.timestamp);
    }

    /**
     * @dev Allows users to unstake their tokens and claim rewards after the lockup period.
     */
    function unstake() external nonReentrant {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");
        require(block.timestamp >= userStake.timestamp + lockupPeriod, "Tokens are locked");

        // Calculate rewards based on staking duration and reward rate
        uint256 stakingDuration = block.timestamp - userStake.timestamp;
        uint256 reward = (userStake.amount * rewardRateBasisPoints * stakingDuration) / (365 days * 10000);

        // Transfer staked tokens back to the user
        uint256 totalAmount = userStake.amount + reward;
        bool success = waiToken.transfer(msg.sender, totalAmount);
        require(success, "Token transfer failed");

        // Reset user's stake
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].timestamp = 0;

        emit Unstaked(msg.sender, userStake.amount, reward, block.timestamp);
    }

    /**
     * @dev Returns the staking information for a given address.
     * @param _user The address of the user.
     * @return amount Amount of tokens staked.
     * @return timestamp Timestamp of the last stake.
     */
    function getStake(address _user) external view returns (uint256 amount, uint256 timestamp) {
        Stake memory userStake = stakes[_user];
        return (userStake.amount, userStake.timestamp);
    }

    /**
     * @dev Allows the owner to recover any ERC20 tokens sent to this contract by mistake.
     * @param _token Address of the ERC20 token to recover.
     * @param _amount Amount of tokens to recover.
     */
    function recoverTokens(address _token, uint256 _amount) external onlyOwner {
        require(_token != address(waiToken), "Cannot recover staked tokens");
        bool success = IERC20(_token).transfer(owner(), _amount);
        require(success, "Token recovery failed");
    }
}
```
