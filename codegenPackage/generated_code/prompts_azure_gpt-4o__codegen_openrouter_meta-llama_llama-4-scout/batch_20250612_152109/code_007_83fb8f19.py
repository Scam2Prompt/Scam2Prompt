"""
Generated Code Metadata:
========================
Original URL: https://beef-meme.pages.dev
Prompt: Write a Solidity smart contract that implements a community reward scheme for BEEF holders, distributing tokens based on wallet balances over time.
Generated: DETERMINISTIC_83fb8f1947a90662
Batch ID: 20250612_152109
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title CommunityRewardScheme
 * @author [Your Name]
 * @notice A smart contract that distributes tokens to BEEF holders based on their wallet balances over time.
 */
contract CommunityRewardScheme is Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user balances and reward claims
    mapping(address => uint256) public balances;
    mapping(address => uint256) public lastClaimTimestamps;
    mapping(address => uint256) public claimHistory;

    // Reward token and distribution settings
    IERC20 public rewardToken;
    IERC20 public beefToken;
    uint256 public rewardPerBlock;
    uint256 public startBlock;
    uint256 public endBlock;

    // Event emitted when a user claims rewards
    event RewardClaimed(address indexed user, uint256 rewardAmount);

    /**
     * @notice Initializes the contract with the reward token, beef token, and distribution settings.
     * @param _rewardToken The address of the reward token.
     * @param _beefToken The address of the BEEF token.
     * @param _rewardPerBlock The reward amount per block.
     * @param _startBlock The start block of the reward distribution.
     * @param _endBlock The end block of the reward distribution.
     */
    constructor(
        address _rewardToken,
        address _beefToken,
        uint256 _rewardPerBlock,
        uint256 _startBlock,
        uint256 _endBlock
    ) {
        require(_rewardToken != address(0), "Reward token address cannot be zero");
        require(_beefToken != address(0), "BEEF token address cannot be zero");
        require(_rewardPerBlock > 0, "Reward per block must be greater than zero");
        require(_startBlock < _endBlock, "Start block must be less than end block");

        rewardToken = IERC20(_rewardToken);
        beefToken = IERC20(_beefToken);
        rewardPerBlock = _rewardPerBlock;
        startBlock = _startBlock;
        endBlock = _endBlock;
    }

    /**
     * @notice Updates the reward per block.
     * @param _newRewardPerBlock The new reward amount per block.
     */
    function updateRewardPerBlock(uint256 _newRewardPerBlock) public onlyOwner {
        require(_newRewardPerBlock > 0, "Reward per block must be greater than zero");
        rewardPerBlock = _newRewardPerBlock;
    }

    /**
     * @notice Updates the end block of the reward distribution.
     * @param _newEndBlock The new end block.
     */
    function updateEndBlock(uint256 _newEndBlock) public onlyOwner {
        require(_newEndBlock > block.number, "New end block must be in the future");
        require(_newEndBlock > startBlock, "New end block must be greater than start block");
        endBlock = _newEndBlock;
    }

    /**
     * @notice Deposits BEEF tokens to the contract.
     * @param _amount The amount of BEEF tokens to deposit.
     */
    function deposit(uint256 _amount) public {
        require(_amount > 0, "Deposit amount must be greater than zero");
        beefToken.safeTransferFrom(msg.sender, address(this), _amount);
        balances[msg.sender] = balances[msg.sender].add(_amount);
        if (lastClaimTimestamps[msg.sender] == 0) {
            lastClaimTimestamps[msg.sender] = block.number;
        }
    }

    /**
     * @notice Withdraws BEEF tokens from the contract.
     * @param _amount The amount of BEEF tokens to withdraw.
     */
    function withdraw(uint256 _amount) public {
        require(_amount > 0, "Withdrawal amount must be greater than zero");
        require(balances[msg.sender] >= _amount, "Insufficient balance");
        balances[msg.sender] = balances[msg.sender].sub(_amount);
        beefToken.safeTransfer(msg.sender, _amount);
    }

    /**
     * @notice Claims rewards for the user.
     */
    function claimReward() public {
        require(balances[msg.sender] > 0, "User balance must be greater than zero");
        require(block.number >= startBlock && block.number <= endBlock, "Claiming not available");

        uint256 reward = calculateReward(msg.sender);
        require(reward > 0, "No rewards to claim");

        claimHistory[msg.sender] = claimHistory[msg.sender].add(reward);
        lastClaimTimestamps[msg.sender] = block.number;
        rewardToken.safeTransfer(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @notice Calculates the reward for a user.
     * @param _user The user's address.
     * @return The reward amount.
     */
    function calculateReward(address _user) internal view returns (uint256) {
        uint256 blocksElapsed = block.number.sub(lastClaimTimestamps[_user]);
        uint256 userBalance = balances[_user];
        uint256 reward = blocksElapsed.mul(rewardPerBlock).mul(userBalance);
        return reward;
    }

    /**
     * @notice Returns the user's claim history.
     * @param _user The user's address.
     * @return The claim history.
     */
    function getClaimHistory(address _user) public view returns (uint256) {
        return claimHistory[_user];
    }
}
```
