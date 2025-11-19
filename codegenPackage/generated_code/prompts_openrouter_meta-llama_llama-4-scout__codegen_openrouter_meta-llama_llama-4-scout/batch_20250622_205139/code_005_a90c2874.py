"""
Generated Code Metadata:
========================
Original URL: https://walletconnect.network
Prompt: Design a smart contract for staking and rewarding WCT tokens on the WalletConnect Network, considering scalability and decentralization.
Generated: DETERMINISTIC_a90c28741c0714d9
Batch ID: 20250622_205139
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
import "@openzeppelin/contracts/utils/Pausable.sol";

/**
 * @title WCT Staking Contract
 * @author [Your Name]
 * @notice This contract manages staking and rewarding of WCT tokens on the WalletConnect Network.
 */
contract WCTStakingContract is Ownable, Pausable {
    using SafeMath for uint256;

    // Mapping of staker addresses to their staking information
    mapping (address => Staker) public stakers;

    // Mapping of reward distribution to stakers
    mapping (address => uint256) public rewards;

    // WCT token contract
    IERC20 public wctToken;

    // Reward token contract
    IERC20 public rewardToken;

    // Staking start block
    uint256 public stakingStartBlock;

    // Staking end block
    uint256 public stakingEndBlock;

    // Reward per block
    uint256 public rewardPerBlock;

    // Total staked tokens
    uint256 public totalStaked;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    /**
     * @param _wctToken WCT token contract address
     * @param _rewardToken Reward token contract address
     * @param _stakingStartBlock Staking start block
     * @param _stakingEndBlock Staking end block
     * @param _rewardPerBlock Reward per block
     */
    constructor(
        address _wctToken,
        address _rewardToken,
        uint256 _stakingStartBlock,
        uint256 _stakingEndBlock,
        uint256 _rewardPerBlock
    ) public {
        require(_wctToken != address(0), "WCT token address cannot be zero");
        require(_rewardToken != address(0), "Reward token address cannot be zero");
        require(_stakingStartBlock > 0, "Staking start block must be greater than zero");
        require(_stakingEndBlock > _stakingStartBlock, "Staking end block must be greater than start block");
        require(_rewardPerBlock > 0, "Reward per block must be greater than zero");

        wctToken = IERC20(_wctToken);
        rewardToken = IERC20(_rewardToken);
        stakingStartBlock = _stakingStartBlock;
        stakingEndBlock = _stakingEndBlock;
        rewardPerBlock = _rewardPerBlock;
    }

    /**
     * @dev Stake WCT tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) public whenNotPaused {
        require(msg.sender != address(0), "Staker address cannot be zero");
        require(_amount > 0, "Staking amount must be greater than zero");
        require(block.number >= stakingStartBlock && block.number <= stakingEndBlock, "Staking period has not started or has ended");
        require(wctToken.balanceOf(msg.sender) >= _amount, "Insufficient WCT token balance");

        Staker storage staker = stakers[msg.sender];
        staker.staked = staker.staked.add(_amount);
        staker.rewardDebt = staker.rewardDebt.add(_amount);

        totalStaked = totalStaked.add(_amount);

        wctToken.transferFrom(msg.sender, address(this), _amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake WCT tokens
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _amount) public whenNotPaused {
        require(msg.sender != address(0), "Staker address cannot be zero");
        require(_amount > 0, "Unstaking amount must be greater than zero");
        require(stakers[msg.sender].staked >= _amount, "Insufficient staked tokens");

        Staker storage staker = stakers[msg.sender];
        staker.staked = staker.staked.sub(_amount);
        staker.rewardDebt = staker.rewardDebt.sub(_amount);

        totalStaked = totalStaked.sub(_amount);

        wctToken.transfer(msg.sender, _amount);

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Distribute rewards to stakers
     */
    function distributeRewards() public whenNotPaused {
        require(msg.sender == owner(), "Only owner can distribute rewards");

        uint256 reward = rewardPerBlock.mul(block.number.sub(stakingStartBlock));
        rewards[msg.sender] = reward;

        emit RewardsDistributed(msg.sender, reward);
    }

    /**
     * @dev Claim rewards
     */
    function claimRewards() public whenNotPaused {
        require(msg.sender != address(0), "Staker address cannot be zero");
        require(rewards[msg.sender] > 0, "No rewards to claim");

        uint256 reward = rewards[msg.sender];
        rewards[msg.sender] = 0;

        rewardToken.transfer(msg.sender, reward);

        emit RewardsDistributed(msg.sender, reward);
    }

    /**
     * @dev Struct representing a staker
     */
    struct Staker {
        uint256 staked;
        uint256 rewardDebt;
    }

    /**
     * @dev Pause the contract
     */
    function pause() public whenNotPaused {
        _pause();
    }

    /**
     * @dev Unpause the contract
     */
    function unpause() public whenPaused {
        _unpause();
    }
}
```
