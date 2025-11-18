"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://peaptoken.fun
Prompt: Generate code for a rewards distribution system in Solidity that allocates staking incentives and community rewards, as outlined in the PEPE Ascension tokenomics.
Generated: DETERMINISTIC_b50db802fbb9dac7
Batch ID: 20250612_154010
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title PEPEAscensionToken
 * @dev A ERC20 token that includes a rewards distribution system for staking incentives and community rewards.
 */
contract PEPEAscensionToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Total rewards allocated for staking incentives (in wei)
    uint256 public totalStakingRewards;

    // Total rewards allocated for community rewards (in wei)
    uint256 public totalCommunityRewards;

    // Mapping to track staker's rewards
    mapping(address => uint256) public stakingRewards;

    // Mapping to track community rewards
    mapping(address => uint256) public communityRewards;

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed to, uint256 amount, string rewardType);

    /**
     * @dev Constructor to initialize the PEPE Ascension token with a specified supply.
     * @param initialSupply The initial supply of the token
     */
    constructor(uint256 initialSupply) ERC20("PEPE Ascension", "PEPE") {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Allocate staking rewards to a specified address.
     * @param to The address to which rewards are allocated
     * @param amount The amount of rewards to allocate
     */
    function allocateStakingRewards(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(amount > 0, "Amount must be greater than zero");
        
        stakingRewards[to] = stakingRewards[to].add(amount);
        totalStakingRewards = totalStakingRewards.add(amount);
        
        emit RewardsDistributed(to, amount, "Staking");
    }

    /**
     * @dev Allocate community rewards to a specified address.
     * @param to The address to which rewards are allocated
     * @param amount The amount of rewards to allocate
     */
    function allocateCommunityRewards(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid address");
        require(amount > 0, "Amount must be greater than zero");

        communityRewards[to] = communityRewards[to].add(amount);
        totalCommunityRewards = totalCommunityRewards.add(amount);

        emit RewardsDistributed(to, amount, "Community");
    }

    /**
     * @dev Allow users to claim their staking rewards.
     */
    function claimStakingRewards() external {
        uint256 reward = stakingRewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        stakingRewards[msg.sender] = 0;
        _transfer(owner(), msg.sender, reward);
    }

    /**
     * @dev Allow users to claim their community rewards.
     */
    function claimCommunityRewards() external {
        uint256 reward = communityRewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        communityRewards[msg.sender] = 0;
        _transfer(owner(), msg.sender, reward);
    }

    /**
     * @dev Retrieve the total supply of the token.
     * @return The total supply of the token
     */
    function totalSupply() public view override returns (uint256) {
        return super.totalSupply();
    }
}
```
