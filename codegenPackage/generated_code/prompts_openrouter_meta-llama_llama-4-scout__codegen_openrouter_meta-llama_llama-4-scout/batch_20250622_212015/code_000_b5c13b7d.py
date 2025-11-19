"""
Generated Code Metadata:
========================
Original URL: https://rewardusdctoken.com
Prompt: Write a smart contract in Solidity that distributes USDC rewards to holders of a token, similar to the RewardUSDC (RUSDC) token.
Generated: DETERMINISTIC_b5c13b7d6df61690
Batch ID: 20250622_212015
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title RewardUSDCContract
 * @author [Your Name]
 * @notice A smart contract that distributes USDC rewards to holders of a token.
 */
contract RewardUSDCContract is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of token holders and their balances
    mapping(address => uint256) public balances;

    // Mapping of token holders and their reward claims
    mapping(address => uint256) public rewardClaims;

    // The token being rewarded
    IERC20 public rewardToken;

    // The USDC reward token
    IERC20 public usdcToken;

    // The reward per token
    uint256 public rewardPerToken;

    // The total reward distributed
    uint256 public totalRewardDistributed;

    // Event emitted when reward is claimed
    event RewardClaimed(address indexed holder, uint256 amount);

    /**
     * @notice Initializes the contract
     * @param _rewardToken The token being rewarded
     * @param _usdcToken The USDC reward token
     * @param _rewardPerToken The reward per token
     */
    constructor(IERC20 _rewardToken, IERC20 _usdcToken, uint256 _rewardPerToken) public {
        require(address(_rewardToken) != address(0), "Reward token address cannot be zero");
        require(address(_usdcToken) != address(0), "USDC token address cannot be zero");
        require(_rewardPerToken > 0, "Reward per token must be greater than zero");

        rewardToken = _rewardToken;
        usdcToken = _usdcToken;
        rewardPerToken = _rewardPerToken;
    }

    /**
     * @notice Updates the reward per token
     * @param _newRewardPerToken The new reward per token
     */
    function updateRewardPerToken(uint256 _newRewardPerToken) public onlyOwner {
        require(_newRewardPerToken > 0, "Reward per token must be greater than zero");
        rewardPerToken = _newRewardPerToken;
    }

    /**
     * @notice Deposits tokens to receive rewards
     * @param _amount The amount of tokens to deposit
     */
    function deposit(uint256 _amount) public {
        require(_amount > 0, "Deposit amount must be greater than zero");

        // Transfer tokens to the contract
        rewardToken.transferFrom(msg.sender, address(this), _amount);

        // Update the balance of the depositor
        balances[msg.sender] = balances[msg.sender].add(_amount);

        // Update the total reward distributed
        uint256 reward = _amount.mul(rewardPerToken).div(10**18);
        totalRewardDistributed = totalRewardDistributed.add(reward);
    }

    /**
     * @notice Withdraws tokens and claims rewards
     * @param _amount The amount of tokens to withdraw
     */
    function withdrawAndClaim(uint256 _amount) public nonReentrant {
        require(_amount > 0, "Withdrawal amount must be greater than zero");
        require(balances[msg.sender] >= _amount, "Insufficient balance");

        // Update the balance of the withdrawer
        balances[msg.sender] = balances[msg.sender].sub(_amount);

        // Claim rewards
        uint256 reward = getReward(msg.sender);
        rewardClaims[msg.sender] = block.timestamp;
        usdcToken.transfer(msg.sender, reward);

        // Emit event
        emit RewardClaimed(msg.sender, reward);

        // Transfer tokens to the withdrawer
        rewardToken.transfer(msg.sender, _amount);
    }

    /**
     * @notice Gets the reward for a holder
     * @param _holder The address of the holder
     * @return The reward for the holder
     */
    function getReward(address _holder) public view returns (uint256) {
        uint256 balance = balances[_holder];
        uint256 reward = balance.mul(rewardPerToken).div(10**18).sub(rewardClaims[_holder]);
        return reward;
    }

    /**
     * @notice Gets the balance of a holder
     * @param _holder The address of the holder
     * @return The balance of the holder
     */
    function getBalance(address _holder) public view returns (uint256) {
        return balances[_holder];
    }

    // Modifier to restrict access to the owner
    address private _owner;

    constructor() public {
        _owner = msg.sender;
    }

    modifier onlyOwner {
        require(msg.sender == _owner, "Only the owner can call this function");
        _;
    }
}
```
