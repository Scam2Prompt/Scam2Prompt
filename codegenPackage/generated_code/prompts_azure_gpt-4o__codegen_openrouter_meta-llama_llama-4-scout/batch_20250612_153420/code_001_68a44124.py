"""
Generated Code Metadata:
========================
Original URL: https://scottytheai-xyz.pages.dev
Prompt: Using the tokenomics details provided, create a Solidity smart contract for $SCOTTY that includes functionality for staking, presale allocation, and reward distribution.
Generated: DETERMINISTIC_68a4412416238871
Batch ID: 20250612_153420
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title ScottToken Contract
 * @author [Your Name]
 * @notice Tokenomics implementation for $SCOTTY, including staking, presale allocation, and reward distribution.
 */
contract ScottToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping for staker information
    mapping(address => Staker) public stakers;

    // Mapping for presale allocations
    mapping(address => uint256) public presaleAllocations;

    // Total staked tokens
    uint256 public totalStaked;

    // Reward per block
    uint256 public rewardPerBlock;

    // Total reward distributed
    uint256 public totalRewardDistributed;

    // Presale start and end blocks
    uint256 public presaleStartBlock;
    uint256 public presaleEndBlock;

    // Staking start block
    uint256 public stakingStartBlock;

    // Maximum presale allocation
    uint256 public maxPresaleAllocation;

    // Event emitted when a user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed user, uint256 amount);

    // Event emitted when presale allocation is updated
    event PresaleAllocationUpdated(address indexed user, uint256 amount);

    // Struct for staker information
    struct Staker {
        uint256 stakedAmount;
        uint256 rewardDebt;
    }

    /**
     * @notice Constructor for ScottToken contract
     * @param _name Token name
     * @param _symbol Token symbol
     * @param _totalSupply Total token supply
     * @param _rewardPerBlock Reward per block
     * @param _presaleStartBlock Presale start block
     * @param _presaleEndBlock Presale end block
     * @param _stakingStartBlock Staking start block
     * @param _maxPresaleAllocation Maximum presale allocation
     */
    constructor(
        string memory _name,
        string memory _symbol,
        uint256 _totalSupply,
        uint256 _rewardPerBlock,
        uint256 _presaleStartBlock,
        uint256 _presaleEndBlock,
        uint256 _stakingStartBlock,
        uint256 _maxPresaleAllocation
    ) ERC20(_name, _symbol) {
        _mint(msg.sender, _totalSupply);

        rewardPerBlock = _rewardPerBlock;
        presaleStartBlock = _presaleStartBlock;
        presaleEndBlock = _presaleEndBlock;
        stakingStartBlock = _stakingStartBlock;
        maxPresaleAllocation = _maxPresaleAllocation;
    }

    /**
     * @notice Presale allocation function
     * @param _amount Allocation amount
     */
    function presaleAllocation(uint256 _amount) external {
        require(
            block.number >= presaleStartBlock && block.number <= presaleEndBlock,
            "Presale not active"
        );
        require(
            presaleAllocations[msg.sender].add(_amount) <= maxPresaleAllocation,
            "Exceeds maximum presale allocation"
        );

        presaleAllocations[msg.sender] = presaleAllocations[msg.sender].add(
            _amount
        );
        _transfer(msg.sender, address(this), _amount);

        emit PresaleAllocationUpdated(msg.sender, _amount);
    }

    /**
     * @notice Stake tokens function
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) external {
        require(
            block.number >= stakingStartBlock,
            "Staking not started yet"
        );
        require(
            balanceOf(msg.sender) >= _amount,
            "Insufficient balance"
        );

        Staker storage staker = stakers[msg.sender];
        uint256 currentReward = staker.stakedAmount.mul(rewardPerBlock).sub(
            staker.rewardDebt
        );

        if (staker.stakedAmount > 0) {
            _transferRewards(msg.sender, currentReward);
        }

        staker.stakedAmount = staker.stakedAmount.add(_amount);
        staker.rewardDebt = staker.stakedAmount.mul(rewardPerBlock);
        totalStaked = totalStaked.add(_amount);

        _transfer(msg.sender, address(this), _amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake tokens function
     * @param _amount Amount to unstake
     */
    function unstake(uint256 _amount) external {
        require(
            stakers[msg.sender].stakedAmount >= _amount,
            "Insufficient staked amount"
        );

        Staker storage staker = stakers[msg.sender];
        uint256 currentReward = staker.stakedAmount.mul(rewardPerBlock).sub(
            staker.rewardDebt
        );

        staker.stakedAmount = staker.stakedAmount.sub(_amount);
        staker.rewardDebt = staker.stakedAmount.mul(rewardPerBlock);
        totalStaked = totalStaked.sub(_amount);

        _transfer(address(this), msg.sender, _amount.add(currentReward));

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Transfer rewards function
     * @param _user User to transfer rewards to
     * @param _amount Reward amount
     */
    function _transferRewards(address _user, uint256 _amount) internal {
        totalRewardDistributed = totalRewardDistributed.add(_amount);
        _transfer(address(this), _user, _amount);

        emit RewardsDistributed(_user, _amount);
    }

    /**
     * @notice Update reward per block function
     * @param _newRewardPerBlock New reward per block
     */
    function updateRewardPerBlock(uint256 _newRewardPerBlock) external onlyOwner {
        rewardPerBlock = _newRewardPerBlock;
    }
}
```
