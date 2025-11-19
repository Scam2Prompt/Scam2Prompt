"""
Generated Code Metadata:
========================
Original URL: https://neiro.pages.dev
Prompt: Generate a smart contract in Solidity for a token called $neiro that rewards participants on the Ethereum chain, incorporating features from the Neiro project.
Generated: DETERMINISTIC_cb1f6b40c90494c0
Batch ID: 20250612_155242
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract NeiroToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Reward parameters
    uint256 public constant REWARD_INTERVAL = 1 days;
    uint256 public constant REWARD_RATE = 1; // 1 token per day per staked token
    uint256 public constant MAX_SUPPLY = 1000000000 * 10**18; // 1 billion tokens

    // Staking variables
    mapping(address => uint256) public stakedBalances;
    mapping(address => uint256) public lastClaimTimes;
    uint256 public totalStaked;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    constructor() ERC20("Neiro Token", "NEIRO") {
        _mint(msg.sender, MAX_SUPPLY.mul(20).div(100)); // 20% initial supply
    }

    // Stake tokens to earn rewards
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Claim any pending rewards before staking
        _claimRewards(msg.sender);

        // Transfer tokens from user to contract
        _transfer(msg.sender, address(this), amount);

        // Update staking balances
        stakedBalances[msg.sender] = stakedBalances[msg.sender].add(amount);
        totalStaked = totalStaked.add(amount);

        emit Staked(msg.sender, amount);
    }

    // Unstake tokens
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakedBalances[msg.sender] >= amount, "Insufficient staked balance");

        // Claim any pending rewards before unstaking
        _claimRewards(msg.sender);

        // Update staking balances
        stakedBalances[msg.sender] = stakedBalances[msg.sender].sub(amount);
        totalStaked = totalStaked.sub(amount);

        // Transfer tokens back to user
        _transfer(address(this), msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Claim accumulated rewards
    function claimRewards() external {
        _claimRewards(msg.sender);
    }

    // Internal function to calculate and claim rewards
    function _claimRewards(address user) internal {
        uint256 reward = calculateReward(user);
        if (reward > 0) {
            // Ensure we don't exceed max supply
            uint256 remainingSupply = MAX_SUPPLY.sub(totalSupply());
            if (reward > remainingSupply) {
                reward = remainingSupply;
            }

            if (reward > 0) {
                _mint(user, reward);
                emit RewardClaimed(user, reward);
            }
        }
        lastClaimTimes[user] = block.timestamp;
    }

    // Calculate pending rewards for a user
    function calculateReward(address user) public view returns (uint256) {
        if (stakedBalances[user] == 0) {
            return 0;
        }

        uint256 timeSinceLastClaim = block.timestamp.sub(
            lastClaimTimes[user] == 0 ? block.timestamp : lastClaimTimes[user]
        );
        uint256 reward = stakedBalances[user]
            .mul(REWARD_RATE)
            .mul(timeSinceLastClaim)
            .div(REWARD_INTERVAL);

        return reward;
    }

    // Owner function to mint additional tokens (for ecosystem growth)
    function mint(address to, uint256 amount) external onlyOwner {
        require(totalSupply().add(amount) <= MAX_SUPPLY, "Exceeds max supply");
        _mint(to, amount);
    }

    // Override transfer to prevent transfers while staking
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal override {
        require(
            stakedBalances[sender] == 0 || 
            balanceOf(sender).sub(stakedBalances[sender]) >= amount,
            "Cannot transfer staked tokens"
        );
        super._transfer(sender, recipient, amount);
    }
}
```
