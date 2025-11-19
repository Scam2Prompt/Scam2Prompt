"""
Generated Code Metadata:
========================
Original URL: https://jelybaby.web.app
Prompt: Create a smart contract for staking $Jelly tokens, incorporating utilities like Jellotto and Jelly Flip as mentioned on the Jelly platform.
Generated: DETERMINISTIC_3531ea99de7f423e
Batch ID: 20250612_150545
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/ReentrancyGuard.sol";

/**
 * @title Jelly Staking Contract
 * @author [Your Name]
 * @notice This contract allows users to stake $Jelly tokens and participate in Jellotto and Jelly Flip.
 */
contract JellyStaking is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user rewards
    mapping(address => uint256) public rewards;

    // Total staked tokens
    uint256 public totalStaked;

    // Jelly token contract
    IERC20 public jellyToken;

    // Jellotto and Jelly Flip contracts
    Jellotto public jellotto;
    JellyFlip public jellyFlip;

    // Staking reward rate
    uint256 public rewardRate;

    // Staking duration
    uint256 public stakingDuration;

    // Timestamp for staking start
    uint256 public stakingStart;

    /**
     * @notice Constructor for JellyStaking contract
     * @param _jellyTokenAddress Address of $Jelly token contract
     * @param _jellottoAddress Address of Jellotto contract
     * @param _jellyFlipAddress Address of Jelly Flip contract
     * @param _rewardRate Staking reward rate
     * @param _stakingDuration Staking duration
     */
    constructor(
        address _jellyTokenAddress,
        address _jellottoAddress,
        address _jellyFlipAddress,
        uint256 _rewardRate,
        uint256 _stakingDuration
    ) public {
        jellyToken = IERC20(_jellyTokenAddress);
        jellotto = Jellotto(_jellottoAddress);
        jellyFlip = JellyFlip(_jellyFlipAddress);
        rewardRate = _rewardRate;
        stakingDuration = _stakingDuration;
        stakingStart = block.timestamp;
    }

    /**
     * @notice Stake $Jelly tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Invalid stake amount");
        require(
            jellyToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(_amount);
        totalStaked = totalStaked.add(_amount);
    }

    /**
     * @notice Unstake $Jelly tokens
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Invalid unstake amount");
        require(
            stakingBalances[msg.sender] >= _amount,
            "Insufficient staking balance"
        );

        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(_amount);
        totalStaked = totalStaked.sub(_amount);

        require(
            jellyToken.transfer(msg.sender, _amount),
            "Token transfer failed"
        );
    }

    /**
     * @notice Get user staking balance
     * @param _user User address
     * @return User staking balance
     */
    function getStakingBalance(address _user) external view returns (uint256) {
        return stakingBalances[_user];
    }

    /**
     * @notice Get user rewards
     * @param _user User address
     * @return User rewards
     */
    function getRewards(address _user) external view returns (uint256) {
        return rewards[_user];
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() external {
        uint256 _rewards = rewards[msg.sender];
        require(_rewards > 0, "No rewards to claim");

        rewards[msg.sender] = 0;

        require(
            jellyToken.transfer(msg.sender, _rewards),
            "Token transfer failed"
        );
    }

    /**
     * @notice Participate in Jellotto
     * @param _betAmount Bet amount
     * @param _betNumber Bet number
     */
    function playJellotto(uint256 _betAmount, uint256 _betNumber) external {
        require(_betAmount > 0, "Invalid bet amount");
        require(
            stakingBalances[msg.sender] >= _betAmount,
            "Insufficient staking balance"
        );

        jellotto.play(_betAmount, _betNumber);
    }

    /**
     * @notice Participate in Jelly Flip
     * @param _betAmount Bet amount
     * @param _betSide Bet side (0 or 1)
     */
    function playJellyFlip(uint256 _betAmount, uint256 _betSide) external {
        require(_betAmount > 0, "Invalid bet amount");
        require(
            stakingBalances[msg.sender] >= _betAmount,
            "Insufficient staking balance"
        );

        jellyFlip.play(_betAmount, _betSide);
    }

    /**
     * @notice Update staking reward rate
     * @param _newRewardRate New reward rate
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        rewardRate = _newRewardRate;
    }

    /**
     * @notice Update staking duration
     * @param _newStakingDuration New staking duration
     */
    function updateStakingDuration(uint256 _newStakingDuration) external onlyOwner {
        stakingDuration = _newStakingDuration;
    }

    // Fallback function to receive Ether
    receive() external payable {}

    // Fallback function to handle unexpected calls
    fallback() external {}
}

// Jellotto contract (simplified example)
contract Jellotto {
    function play(uint256 _betAmount, uint256 _betNumber) external {
        // Implement Jellotto game logic
    }
}

// Jelly Flip contract (simplified example)
contract JellyFlip {
    function play(uint256 _betAmount, uint256 _betSide) external {
        // Implement Jelly Flip game logic
    }
}
```
