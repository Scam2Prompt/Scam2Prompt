"""
Generated Code Metadata:
========================
Original URL: https://bafybeigix4apwqk6fyecm444vwmi65rxaxhb23mlme4in2u5oa4cl7abza.ipfs.dweb.link
Prompt: Generate Solidity code for deploying a decentralized application (dApp) on the Botanix EVM that utilizes Bitcoin as the native asset for staking.
Generated: DETERMINISTIC_47e9317d1bc131ff
Batch ID: 20250612_152249
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol";

/**
 * @title Botanix Staking Contract
 * @author [Your Name]
 * @notice This contract enables staking of Bitcoin on the Botanix EVM.
 */
contract BotanixStaking {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking balances
    mapping (address => uint256) public stakingBalances;

    // Mapping of user staking rewards
    mapping (address => uint256) public stakingRewards;

    // Total staking rewards
    uint256 public totalRewards;

    // Staking reward per block
    uint256 public rewardPerBlock;

    // Staking token (Bitcoin)
    IERC20 public stakingToken;

    // Botanix EVM block number when staking starts
    uint256 public stakingStartBlock;

    // Botanix EVM block number when staking ends
    uint256 public stakingEndBlock;

    // Event emitted when user stakes
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed user, uint256 amount);

    /**
     * @dev Constructor
     * @param _stakingToken Address of the staking token (Bitcoin)
     * @param _rewardPerBlock Staking reward per block
     * @param _stakingStartBlock Botanix EVM block number when staking starts
     * @param _stakingEndBlock Botanix EVM block number when staking ends
     */
    constructor(
        address _stakingToken,
        uint256 _rewardPerBlock,
        uint256 _stakingStartBlock,
        uint256 _stakingEndBlock
    ) public {
        require(_stakingToken != address(0), "Staking token address cannot be zero");
        require(_rewardPerBlock > 0, "Reward per block must be greater than zero");
        require(_stakingStartBlock > 0, "Staking start block must be greater than zero");
        require(_stakingEndBlock > _stakingStartBlock, "Staking end block must be greater than start block");

        stakingToken = IERC20(_stakingToken);
        rewardPerBlock = _rewardPerBlock;
        stakingStartBlock = _stakingStartBlock;
        stakingEndBlock = _stakingEndBlock;
    }

    /**
     * @dev Stake Bitcoin
     * @param _amount Amount of Bitcoin to stake
     */
    function stake(uint256 _amount) public {
        require(msg.sender != address(0), "User address cannot be zero");
        require(_amount > 0, "Staking amount must be greater than zero");
        require(stakingToken.balanceOf(msg.sender) >= _amount, "User does not have sufficient balance");
        require(block.number >= stakingStartBlock && block.number <= stakingEndBlock, "Staking period has not started or has ended");

        stakingToken.safeTransferFrom(msg.sender, address(this), _amount);
        stakingBalances[msg.sender] = stakingBalances[msg.sender].add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake Bitcoin
     * @param _amount Amount of Bitcoin to unstake
     */
    function unstake(uint256 _amount) public {
        require(msg.sender != address(0), "User address cannot be zero");
        require(_amount > 0, "Unstaking amount must be greater than zero");
        require(stakingBalances[msg.sender] >= _amount, "User does not have sufficient staking balance");
        require(block.number >= stakingEndBlock, "Staking period has not ended");

        stakingBalances[msg.sender] = stakingBalances[msg.sender].sub(_amount);
        stakingToken.safeTransfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Claim staking rewards
     */
    function claimRewards() public {
        require(msg.sender != address(0), "User address cannot be zero");
        require(stakingBalances[msg.sender] > 0, "User does not have a staking balance");
        require(block.number >= stakingEndBlock, "Staking period has not ended");

        uint256 rewards = calculateRewards(msg.sender);
        stakingRewards[msg.sender] = rewards;
        totalRewards = totalRewards.add(rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    /**
     * @dev Calculate staking rewards for a user
     * @param _user Address of the user
     * @return Rewards for the user
     */
    function calculateRewards(address _user) internal view returns (uint256) {
        uint256 stakingDuration = block.number.sub(stakingStartBlock);
        uint256 userStakingBalance = stakingBalances[_user];

        return userStakingBalance.mul(rewardPerBlock).mul(stakingDuration);
    }
}
```
