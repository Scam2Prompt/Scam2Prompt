"""
Generated Code Metadata:
========================
Original URL: https://scottytheai-xyz.pages.dev
Prompt: Generate a smart contract code in Solidity to create a new token on the Scotty AI platform, similar to $SCOTTY, with a total supply of 1 million tokens and a 10% staking reward mechanism.
Generated: DETERMINISTIC_4e17e7c0a40205fe
Batch ID: 20250622_210806
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
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title ScottyAIToken
 * @dev ERC20 token with staking rewards, burnable, pausable, and ownable features
 */
contract ScottyAIToken is ERC20, ERC20Burnable, Pausable, Ownable {
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10**18;
    uint256 public constant REWARD_RATE = 10; // 10% annual reward rate
    uint256 public constant REWARD_INTERVAL = 365 days;

    mapping(address => uint256) public stakingBalances;
    mapping(address => uint256) public lastClaimTimes;
    mapping(address => uint256) public stakingStartTimes;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    /**
     * @dev Constructor that mints the total supply to the contract deployer
     */
    constructor() ERC20("Scotty AI Token", "SCOTTY") {
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    /**
     * @dev Pause all token transfers
     */
    function pause() public onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause all token transfers
     */
    function unpause() public onlyOwner {
        _unpause();
    }

    /**
     * @dev Stake tokens to earn rewards
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external whenNotPaused {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        _updateRewards(msg.sender);

        _transfer(msg.sender, address(this), amount);
        stakingBalances[msg.sender] += amount;
        stakingStartTimes[msg.sender] = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Unstake tokens and claim any pending rewards
     * @param amount Amount of tokens to unstake
     */
    function unstake(uint256 amount) external whenNotPaused {
        require(amount > 0, "Amount must be greater than 0");
        require(stakingBalances[msg.sender] >= amount, "Insufficient staked balance");

        _updateRewards(msg.sender);

        stakingBalances[msg.sender] -= amount;
        _transfer(address(this), msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @dev Claim staking rewards
     */
    function claimReward() external whenNotPaused {
        _updateRewards(msg.sender);
        uint256 reward = calculateReward(msg.sender);
        
        require(reward > 0, "No rewards to claim");
        
        lastClaimTimes[msg.sender] = block.timestamp;
        _mint(msg.sender, reward);

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculate the current reward for a staker
     * @param staker Address of the staker
     * @return reward Calculated reward amount
     */
    function calculateReward(address staker) public view returns (uint256) {
        if (stakingBalances[staker] == 0) return 0;

        uint256 lastClaimTime = lastClaimTimes[staker] == 0 
            ? stakingStartTimes[staker] 
            : lastClaimTimes[staker];
        
        uint256 timeElapsed = block.timestamp - lastClaimTime;
        uint256 reward = (stakingBalances[staker] * REWARD_RATE * timeElapsed) / (REWARD_INTERVAL * 100);

        return reward;
    }

    /**
     * @dev Internal function to update rewards for a staker
     * @param staker Address of the staker
     */
    function _updateRewards(address staker) internal {
        uint256 reward = calculateReward(staker);
        if (reward > 0) {
            lastClaimTimes[staker] = block.timestamp;
            _mint(staker, reward);
            emit RewardClaimed(staker, reward);
        }
    }

    /**
     * @dev Override ERC20 transfer to include pausable functionality
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override whenNotPaused {
        super._beforeTokenTransfer(from, to, amount);
    }
}
```
