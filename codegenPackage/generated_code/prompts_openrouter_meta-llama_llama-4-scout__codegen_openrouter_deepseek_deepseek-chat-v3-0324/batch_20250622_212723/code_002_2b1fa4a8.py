"""
Generated Code Metadata:
========================
Original URL: https://worldmobile-token.pages.dev
Prompt: "Generate a smart contract in Solidity for managing WMTx token transactions, including earning rewards for EarthNode operators and stakers."
Generated: DETERMINISTIC_2b1fa4a8f00d29dd
Batch ID: 20250622_212723
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Snapshot.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract WMTxToken is ERC20, ERC20Burnable, ERC20Snapshot, Ownable, Pausable {
    using SafeMath for uint256;

    // Struct to store staker information
    struct Staker {
        uint256 amount;
        uint256 rewardDebt;
        uint256 lastRewardTime;
    }

    // Struct to store EarthNode operator information
    struct EarthNodeOperator {
        uint256 amount;
        uint256 rewardDebt;
        uint256 lastRewardTime;
        bool isActive;
    }

    // Reward parameters
    uint256 public constant REWARD_PER_SECOND = 1 ether; // 1 WMTx per second
    uint256 public constant EARTH_NODE_REWARD_MULTIPLIER = 2; // 2x rewards for EarthNode operators
    uint256 public constant MIN_STAKE_AMOUNT = 100 ether; // Minimum stake amount
    uint256 public constant MIN_EARTH_NODE_STAKE = 1000 ether; // Minimum for EarthNode operator

    // Total staked amounts
    uint256 public totalStaked;
    uint256 public totalEarthNodeStaked;

    // Staking and EarthNode operator mappings
    mapping(address => Staker) public stakers;
    mapping(address => EarthNodeOperator) public earthNodeOperators;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event EarthNodeRegistered(address indexed operator);
    event EarthNodeDeregistered(address indexed operator);
    event EarthNodeStaked(address indexed operator, uint256 amount);
    event EarthNodeUnstaked(address indexed operator, uint256 amount);

    constructor() ERC20("WMTx Token", "WMTx") {
        _mint(msg.sender, 1000000000 * 10 ** decimals()); // 1 billion tokens
    }

    // Create a snapshot of token balances
    function snapshot() public onlyOwner {
        _snapshot();
    }

    // Pause all token transfers
    function pause() public onlyOwner {
        _pause();
    }

    // Unpause all token transfers
    function unpause() public onlyOwner {
        _unpause();
    }

    // Override transfer functions to allow pausing
    function _beforeTokenTransfer(address from, address to, uint256 amount)
        internal
        whenNotPaused
        override(ERC20, ERC20Snapshot)
    {
        super._beforeTokenTransfer(from, to, amount);
    }

    // Stake tokens to earn rewards
    function stake(uint256 amount) external {
        require(amount >= MIN_STAKE_AMOUNT, "Amount below minimum stake");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        Staker storage staker = stakers[msg.sender];
        
        // Claim any pending rewards first
        if (staker.amount > 0) {
            _claimStakerReward(msg.sender);
        }

        // Transfer tokens from user to contract
        _transfer(msg.sender, address(this), amount);

        // Update staker information
        staker.amount = staker.amount.add(amount);
        staker.rewardDebt = staker.amount.mul(_calculateRewardPerToken());
        staker.lastRewardTime = block.timestamp;

        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    // Unstake tokens
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amount >= amount, "Insufficient staked amount");

        // Claim any pending rewards first
        _claimStakerReward(msg.sender);

        // Update staker information
        staker.amount = staker.amount.sub(amount);
        staker.rewardDebt = staker.amount.mul(_calculateRewardPerToken());
        staker.lastRewardTime = block.timestamp;

        // Transfer tokens back to user
        _transfer(address(this), msg.sender, amount);

        totalStaked = totalStaked.sub(amount);

        emit Unstaked(msg.sender, amount);
    }

    // Register as an EarthNode operator
    function registerEarthNodeOperator() external {
        require(!earthNodeOperators[msg.sender].isActive, "Already registered");
        earthNodeOperators[msg.sender] = EarthNodeOperator({
            amount: 0,
            rewardDebt: 0,
            lastRewardTime: 0,
            isActive: true
        });
        emit EarthNodeRegistered(msg.sender);
    }

    // Deregister as an EarthNode operator
    function deregisterEarthNodeOperator() external {
        EarthNodeOperator storage operator = earthNodeOperators[msg.sender];
        require(operator.isActive, "Not registered");
        require(operator.amount == 0, "Must unstake first");

        delete earthNodeOperators[msg.sender];
        emit EarthNodeDeregistered(msg.sender);
    }

    // Stake tokens as an EarthNode operator
    function stakeAsEarthNode(uint256 amount) external {
        EarthNodeOperator storage operator = earthNodeOperators[msg.sender];
        require(operator.isActive, "Not an EarthNode operator");
        require(amount >= MIN_EARTH_NODE_STAKE, "Amount below minimum");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Claim any pending rewards first
        if (operator.amount > 0) {
            _claimEarthNodeReward(msg.sender);
        }

        // Transfer tokens from user to contract
        _transfer(msg.sender, address(this), amount);

        // Update operator information
        operator.amount = operator.amount.add(amount);
        operator.rewardDebt = operator.amount.mul(_calculateRewardPerToken());
        operator.lastRewardTime = block.timestamp;

        totalEarthNodeStaked = totalEarthNodeStaked.add(amount);

        emit EarthNodeStaked(msg.sender, amount);
    }

    // Unstake tokens as an EarthNode operator
    function unstakeAsEarthNode(uint256 amount) external {
        EarthNodeOperator storage operator = earthNodeOperators[msg.sender];
        require(operator.isActive, "Not an EarthNode operator");
        require(operator.amount >= amount, "Insufficient staked amount");

        // Claim any pending rewards first
        _claimEarthNodeReward(msg.sender);

        // Update operator information
        operator.amount = operator.amount.sub(amount);
        operator.rewardDebt = operator.amount.mul(_calculateRewardPerToken());
        operator.lastRewardTime = block.timestamp;

        // Transfer tokens back to user
        _transfer(address(this), msg.sender, amount);

        totalEarthNodeStaked = totalEarthNodeStaked.sub(amount);

        emit EarthNodeUnstaked(msg.sender, amount);
    }

    // Claim staking rewards
    function claimStakerReward() external {
        require(stakers[msg.sender].amount > 0, "No staked amount");
        _claimStakerReward(msg.sender);
    }

    // Claim EarthNode operator rewards
    function claimEarthNodeReward() external {
        EarthNodeOperator storage operator = earthNodeOperators[msg.sender];
        require(operator.isActive && operator.amount > 0, "No staked amount");
        _claimEarthNodeReward(msg.sender);
    }

    // Internal function to calculate reward per token
    function _calculateRewardPerToken() internal view returns (uint256) {
        if (totalStaked == 0 && totalEarthNodeStaked == 0) {
            return 0;
        }
        return REWARD_PER_SECOND.mul(1e18).div(totalStaked.add(totalEarthNodeStaked.mul(EARTH_NODE_REWARD_MULTIPLIER)));
    }

    // Internal function to claim staker rewards
    function _claimStakerReward(address user) internal {
        Staker storage staker = stakers[user];
        uint256 pending = staker.amount.mul(_calculateRewardPerToken()).sub(staker.rewardDebt);
        
        if (pending > 0) {
            staker.rewardDebt = staker.amount.mul(_calculateRewardPerToken());
            staker.lastRewardTime = block.timestamp;
            _mint(user, pending);
            emit RewardClaimed(user, pending);
        }
    }

    //
