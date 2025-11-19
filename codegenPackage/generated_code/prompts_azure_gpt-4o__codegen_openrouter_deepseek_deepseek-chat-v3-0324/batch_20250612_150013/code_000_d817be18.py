"""
Generated Code Metadata:
========================
Original URL: https://popofrogs.pages.dev
Prompt: Write a smart contract in Solidity for a multichain token similar to $FROP, ensuring transparency and security as described in the Popo ecosystem. Include features for staking and rewards allocation.
Generated: DETERMINISTIC_d817be18bfc86c7e
Batch ID: 20250612_150013
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract PopoToken is ERC20, ERC20Burnable, Ownable, Pausable {
    using SafeMath for uint256;

    // Staking structure
    struct Stake {
        uint256 amount;
        uint256 startTime;
        uint256 rewardDebt;
    }

    // Reward parameters
    uint256 public constant REWARD_PER_BLOCK = 1 ether;
    uint256 public lastRewardBlock;
    uint256 public accRewardPerShare;
    uint256 public totalStaked;

    // Staking mappings
    mapping(address => Stake) public stakes;
    mapping(address => bool) public isStaking;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event TokensBurned(address indexed burner, uint256 amount);

    constructor() ERC20("Popo Ecosystem Token", "POPO") {
        _mint(msg.sender, 100000000 * 10 ** decimals());
        lastRewardBlock = block.number;
    }

    // Pause/unpause functions
    function pause() public onlyOwner {
        _pause();
    }

    function unpause() public onlyOwner {
        _unpause();
    }

    // Staking functions
    function stake(uint256 amount) external whenNotPaused {
        require(amount > 0, "Cannot stake 0 tokens");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        _updateRewards();

        if (isStaking[msg.sender]) {
            Stake storage userStake = stakes[msg.sender];
            uint256 pending = userStake.amount.mul(accRewardPerShare).div(1e12).sub(userStake.rewardDebt);
            if (pending > 0) {
                _mint(msg.sender, pending);
                emit RewardClaimed(msg.sender, pending);
            }
            userStake.amount = userStake.amount.add(amount);
            userStake.rewardDebt = userStake.amount.mul(accRewardPerShare).div(1e12);
        } else {
            stakes[msg.sender] = Stake({
                amount: amount,
                startTime: block.timestamp,
                rewardDebt: amount.mul(accRewardPerShare).div(1e12)
            });
            isStaking[msg.sender] = true;
        }

        totalStaked = totalStaked.add(amount);
        _transfer(msg.sender, address(this), amount);
        emit Staked(msg.sender, amount);
    }

    function unstake(uint256 amount) external whenNotPaused {
        require(isStaking[msg.sender], "No active stake");
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Insufficient staked amount");

        _updateRewards();

        uint256 pending = userStake.amount.mul(accRewardPerShare).div(1e12).sub(userStake.rewardDebt);
        if (pending > 0) {
            _mint(msg.sender, pending);
            emit RewardClaimed(msg.sender, pending);
        }

        userStake.amount = userStake.amount.sub(amount);
        userStake.rewardDebt = userStake.amount.mul(accRewardPerShare).div(1e12);
        totalStaked = totalStaked.sub(amount);

        if (userStake.amount == 0) {
            isStaking[msg.sender] = false;
            delete stakes[msg.sender];
        }

        _transfer(address(this), msg.sender, amount);
        emit Unstaked(msg.sender, amount);
    }

    function claimRewards() external whenNotPaused {
        require(isStaking[msg.sender], "No active stake");

        _updateRewards();

        Stake storage userStake = stakes[msg.sender];
        uint256 pending = userStake.amount.mul(accRewardPerShare).div(1e12).sub(userStake.rewardDebt);
        require(pending > 0, "No rewards to claim");

        _mint(msg.sender, pending);
        userStake.rewardDebt = userStake.amount.mul(accRewardPerShare).div(1e12);
        emit RewardClaimed(msg.sender, pending);
    }

    // Internal reward calculation
    function _updateRewards() internal {
        if (block.number <= lastRewardBlock || totalStaked == 0) {
            return;
        }

        uint256 blocksPassed = block.number.sub(lastRewardBlock);
        uint256 reward = blocksPassed.mul(REWARD_PER_BLOCK);
        accRewardPerShare = accRewardPerShare.add(reward.mul(1e12).div(totalStaked));
        lastRewardBlock = block.number;
    }

    // View functions
    function pendingRewards(address user) external view returns (uint256) {
        if (!isStaking[user] || totalStaked == 0) {
            return 0;
        }

        Stake storage userStake = stakes[user];
        uint256 currentAccRewardPerShare = accRewardPerShare;
        if (block.number > lastRewardBlock && totalStaked != 0) {
            uint256 blocksPassed = block.number.sub(lastRewardBlock);
            uint256 reward = blocksPassed.mul(REWARD_PER_BLOCK);
            currentAccRewardPerShare = currentAccRewardPerShare.add(reward.mul(1e12).div(totalStaked));
        }

        return userStake.amount.mul(currentAccRewardPerShare).div(1e12).sub(userStake.rewardDebt);
    }

    // Burn function with event emission
    function burn(uint256 amount) public override {
        super.burn(amount);
        emit TokensBurned(msg.sender, amount);
    }

    // Multichain bridge compatibility
    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
    }

    // Safety functions
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        IERC20(tokenAddress).transfer(owner(), tokenAmount);
    }
}
```
