"""
Generated Code Metadata:
========================
Original URL: https://evm-zeta.vercel.app
Prompt: Design a secure protocol for staking and exchanging cryptocurrencies, incorporating the features and issue resolution mechanisms described on the EVM-Zeta website.
Generated: DETERMINISTIC_f34b2fe56aeb988c
Batch ID: 20250622_212307
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title Secure Staking and Exchange Protocol
 * @dev Implements a secure protocol for staking and exchanging tokens with issue resolution mechanisms
 */
contract EVMZetaProtocol is ReentrancyGuard, Ownable {
    using SafeMath for uint256;

    // Token addresses
    IERC20 public stakingToken;
    IERC20 public rewardToken;

    // Staking parameters
    uint256 public stakingPeriod;
    uint256 public rewardRate;
    uint256 public totalStaked;
    uint256 public lastUpdateTime;
    uint256 public rewardPerTokenStored;

    // Exchange parameters
    uint256 public exchangeRate;
    uint256 public exchangeFee;
    uint256 public minStakeAmount;

    // Dispute resolution parameters
    uint256 public disputeResolutionPeriod;
    uint256 public disputeFee;

    // Mappings
    mapping(address => uint256) public stakedBalances;
    mapping(address => uint256) public userRewardPerTokenPaid;
    mapping(address => uint256) public rewards;
    mapping(address => uint256) public lastStakeTime;
    mapping(bytes32 => Dispute) public disputes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event Exchanged(address indexed from, address indexed to, uint256 amount);
    event DisputeRaised(bytes32 indexed disputeId, address indexed raiser, string reason);
    event DisputeResolved(bytes32 indexed disputeId, address indexed resolver, bool resolution);

    // Structs
    struct Dispute {
        address raiser;
        address target;
        uint256 timestamp;
        string reason;
        bool resolved;
        bool resolution;
    }

    /**
     * @dev Constructor initializes the protocol parameters
     * @param _stakingToken Address of the staking token
     * @param _rewardToken Address of the reward token
     * @param _stakingPeriod Duration of staking period in seconds
     * @param _rewardRate Rate of rewards per token per second
     * @param _exchangeRate Rate for token exchange
     * @param _exchangeFee Fee percentage for exchanges
     * @param _minStakeAmount Minimum amount required to stake
     * @param _disputeResolutionPeriod Time for dispute resolution
     * @param _disputeFee Fee for raising a dispute
     */
    constructor(
        address _stakingToken,
        address _rewardToken,
        uint256 _stakingPeriod,
        uint256 _rewardRate,
        uint256 _exchangeRate,
        uint256 _exchangeFee,
        uint256 _minStakeAmount,
        uint256 _disputeResolutionPeriod,
        uint256 _disputeFee
    ) {
        stakingToken = IERC20(_stakingToken);
        rewardToken = IERC20(_rewardToken);
        stakingPeriod = _stakingPeriod;
        rewardRate = _rewardRate;
        exchangeRate = _exchangeRate;
        exchangeFee = _exchangeFee;
        minStakeAmount = _minStakeAmount;
        disputeResolutionPeriod = _disputeResolutionPeriod;
        disputeFee = _disputeFee;
    }

    /**
     * @dev Updates the reward for a given account
     * @param account Address of the staker
     */
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;
        if (account != address(0)) {
            rewards[account] = earned(account);
            userRewardPerTokenPaid[account] = rewardPerTokenStored;
        }
        _;
    }

    /**
     * @dev Calculates the current reward per token
     * @return Current reward per token
     */
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return
            rewardPerTokenStored.add(
                block.timestamp.sub(lastUpdateTime).mul(rewardRate).mul(1e18).div(totalStaked)
            );
    }

    /**
     * @dev Calculates the earned rewards for an account
     * @param account Address of the staker
     * @return Earned rewards
     */
    function earned(address account) public view returns (uint256) {
        return
            stakedBalances[account]
                .mul(rewardPerToken().sub(userRewardPerTokenPaid[account]))
                .div(1e18)
                .add(rewards[account]);
    }

    /**
     * @dev Stake tokens into the protocol
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount >= minStakeAmount, "Amount below minimum stake");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        stakedBalances[msg.sender] = stakedBalances[msg.sender].add(amount);
        totalStaked = totalStaked.add(amount);
        lastStakeTime[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked tokens
     * @param amount Amount of tokens to withdraw
     */
    function withdraw(uint256 amount) public nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        require(stakedBalances[msg.sender] >= amount, "Insufficient balance");
        require(
            block.timestamp >= lastStakeTime[msg.sender].add(stakingPeriod),
            "Staking period not completed"
        );

        stakedBalances[msg.sender] = stakedBalances[msg.sender].sub(amount);
        totalStaked = totalStaked.sub(amount);
        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim earned rewards
     */
    function claimReward() public nonReentrant updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        if (reward > 0) {
            rewards[msg.sender] = 0;
            require(rewardToken.transfer(msg.sender, reward), "Transfer failed");
            emit RewardPaid(msg.sender, reward);
        }
    }

    /**
     * @dev Exit the staking protocol by withdrawing all staked tokens and claiming rewards
     */
    function exit() external {
        withdraw(stakedBalances[msg.sender]);
        claimReward();
    }

    /**
     * @dev Exchange tokens based on the protocol exchange rate
     * @param amount Amount of tokens to exchange
     * @param recipient Address to receive exchanged tokens
     */
    function exchange(uint256 amount, address recipient) external nonReentrant {
        require(amount > 0, "Cannot exchange 0");
        uint256 fee = amount.mul(exchangeFee).div(100);
        uint256 amountAfterFee = amount.sub(fee);
        uint256 exchangedAmount = amountAfterFee.mul(exchangeRate).div(1e18);

        require(
            stakingToken.transferFrom(msg.sender, address(this), amount),
            "Transfer failed"
        );
        require(
            rewardToken.transfer(recipient, exchangedAmount),
            "Transfer failed"
        );

        emit Exchanged(msg.sender, recipient, amount);
    }

    /**
     * @dev Raise a dispute regarding a transaction
     * @param target Address involved in the dispute
     * @param reason Reason for the dispute
     * @return disputeId Unique identifier for the dispute
     */
    function raiseDispute(address target, string memory reason) external payable returns (bytes32) {
        require(msg.value >= disputeFee, "Insufficient dispute fee");
        bytes32 disputeId = keccak256(abi.encodePacked(msg.sender, target, block.timestamp, reason));
        
        disputes[disputeId] = Dispute({
            raiser: msg.sender,
            target: target,
            timestamp: block.timestamp,
            reason: reason,
            resolved: false,
            resolution: false
        });

        emit DisputeRaised(disputeId, msg.sender, reason);
        return disputeId;
    }

    /**
     * @dev Resolve a dispute
     * @param disputeId Identifier of the dispute
     * @param resolution Decision on the dispute
     */
    function resolveDispute(bytes32 disputeId, bool resolution) external onlyOwner {
        Dispute storage dispute = disputes[disputeId];
        require(!dispute.resolved, "Dispute already resolved");
        require(
            block.timestamp <= dispute.timestamp.add(disputeResolutionPeriod),
