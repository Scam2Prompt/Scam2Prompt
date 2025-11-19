"""
Generated Code Metadata:
========================
Original URL: https://fwbn.pages.dev
Prompt: What are the best practices for developing a token-based incentive system for community engagement in a Web3-focused organization like Friends With Benefits?
Generated: DETERMINISTIC_a37ac50e2867c30e
Batch ID: 20250612_163400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Solidity smart contract implementing a token-based incentive system for community engagement, following Web3 best practices:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/AccessControl.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title CommunityEngagementToken
 * @dev ERC20 token with minting capabilities for rewarding community engagement
 */
contract CommunityEngagementToken is ERC20, AccessControl, Pausable {
    using SafeMath for uint256;

    bytes32 public constant REWARDER_ROLE = keccak256("REWARDER_ROLE");
    bytes32 public constant ADMIN_ROLE = keccak256("ADMIN_ROLE");
    
    uint256 public constant MAX_SUPPLY = 1000000000 * 10**18; // 1 billion tokens
    uint256 public constant DAILY_REWARD_LIMIT = 10000 * 10**18; // 10k tokens per day
    
    mapping(address => uint256) public lastRewardClaim;
    mapping(address => uint256) public rewardPoints;
    mapping(address => bool) public isBlacklisted;
    
    uint256 public totalRewardsDistributed;
    uint256 public dailyRewardsDistributed;
    uint256 public lastDistributionDay;
    
    event RewardDistributed(address indexed recipient, uint256 amount, string engagementType);
    event BlacklistUpdated(address indexed account, bool isBlacklisted);
    event DailyLimitReset(uint256 newDay);

    /**
     * @dev Constructor that initializes the token and roles
     */
    constructor() ERC20("Community Engagement Token", "CET") {
        _setupRole(DEFAULT_ADMIN_ROLE, msg.sender);
        _setupRole(ADMIN_ROLE, msg.sender);
        _setupRole(REWARDER_ROLE, msg.sender);
    }

    /**
     * @dev Modifier to check if address is not blacklisted
     */
    modifier notBlacklisted(address account) {
        require(!isBlacklisted[account], "Account is blacklisted");
        _;
    }

    /**
     * @dev Distribute rewards for community engagement
     * @param recipient Address to receive rewards
     * @param amount Amount of tokens to reward
     * @param engagementType Type of engagement (e.g., "CONTRIBUTION", "EVENT", etc.)
     */
    function distributeReward(
        address recipient,
        uint256 amount,
        string memory engagementType
    ) external whenNotPaused notBlacklisted(recipient) onlyRole(REWARDER_ROLE) {
        require(amount > 0, "Amount must be positive");
        require(totalSupply().add(amount) <= MAX_SUPPLY, "Exceeds max supply");
        
        // Reset daily limit if it's a new day
        if (block.timestamp / 1 days > lastDistributionDay) {
            dailyRewardsDistributed = 0;
            lastDistributionDay = block.timestamp / 1 days;
            emit DailyLimitReset(lastDistributionDay);
        }
        
        require(
            dailyRewardsDistributed.add(amount) <= DAILY_REWARD_LIMIT,
            "Exceeds daily reward limit"
        );
        
        _mint(recipient, amount);
        rewardPoints[recipient] = rewardPoints[recipient].add(amount);
        totalRewardsDistributed = totalRewardsDistributed.add(amount);
        dailyRewardsDistributed = dailyRewardsDistributed.add(amount);
        
        emit RewardDistributed(recipient, amount, engagementType);
    }

    /**
     * @dev Blacklist an address to prevent reward distribution
     * @param account Address to blacklist/unblacklist
     * @param _isBlacklisted Boolean flag
     */
    function updateBlacklist(address account, bool _isBlacklisted) external onlyRole(ADMIN_ROLE) {
        isBlacklisted[account] = _isBlacklisted;
        emit BlacklistUpdated(account, _isBlacklisted);
    }

    /**
     * @dev Pause all reward distributions
     */
    function pause() external onlyRole(ADMIN_ROLE) {
        _pause();
    }

    /**
     * @dev Unpause reward distributions
     */
    function unpause() external onlyRole(ADMIN_ROLE) {
        _unpause();
    }

    /**
     * @dev Override ERC20 transfer to include blacklist check
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal virtual override notBlacklisted(from) notBlacklisted(to) {
        super._beforeTokenTransfer(from, to, amount);
    }

    /**
     * @dev Add a new rewarder address
     * @param account Address to grant rewarder role
     */
    function addRewarder(address account) external onlyRole(ADMIN_ROLE) {
        grantRole(REWARDER_ROLE, account);
    }

    /**
     * @dev Remove a rewarder address
     * @param account Address to revoke rewarder role from
     */
    function removeRewarder(address account) external onlyRole(ADMIN_ROLE) {
        revokeRole(REWARDER_ROLE, account);
    }
}
```

And here's a JavaScript utility class for interacting with the contract:

```javascript
const { ethers } = require('ethers');
const { abi } = require('./CommunityEngagementToken.json');

class TokenIncentiveSystem {
  /**
   * Initialize the incentive system
   * @param {string} contractAddress - Smart contract address
   * @param {ethers.providers.Provider} provider - Ethereum provider
   * @param {ethers.Signer} signer - Signer with rewarder privileges
   */
  constructor(contractAddress, provider, signer) {
    this.contract = new ethers.Contract(contractAddress, abi, signer);
    this.signer = signer;
  }

  /**
   * Distribute rewards to a community member
   * @param {string} recipient - Recipient address
   * @param {number} amount - Token amount to reward
   * @param {string} engagementType - Type of engagement
   * @returns {Promise<ethers.ContractReceipt>} Transaction receipt
   */
  async distributeReward(recipient, amount, engagementType) {
    try {
      const tx = await this.contract.distributeReward(
        recipient,
        ethers.utils.parseUnits(amount.toString(), 18),
        engagementType
      );
      return await tx.wait();
    } catch (error) {
      console.error('Reward distribution failed:', error);
      throw new Error('Failed to distribute reward');
    }
  }

  /**
   * Get reward points for an address
   * @param {string} address - Wallet address to check
   * @returns {Promise<number>} Reward points
   */
  async getRewardPoints(address) {
    try {
      const points = await this.contract.rewardPoints(address);
      return parseFloat(ethers.utils.formatUnits(points, 18));
    } catch (error) {
      console.error('Failed to get reward points:', error);
      throw new Error('Failed to retrieve reward points');
    }
  }

  /**
   * Check if address is blacklisted
   * @param {string} address - Wallet address to check
   * @returns {Promise<boolean>} Blacklist status
   */
  async checkBlacklist(address) {
    try {
      return await this.contract.isBlacklisted(address);
    } catch (error) {
      console.error('Failed to check blacklist:', error);
      throw new Error('Failed to check blacklist status');
    }
  }

  /**
   * Get total rewards distributed
   * @returns {Promise<number>} Total rewards in tokens
   */
  async getTotalRewardsDistributed() {
    try {
      const total = await this.contract.totalRewardsDistributed();
      return parseFloat(ethers.utils.formatUnits(total, 18));
    } catch (error) {
      console.error('Failed to get total rewards:', error);
      throw new Error('Failed to retrieve total rewards');
    }
  }
}

module.exports = TokenIncentiveSystem;
```
