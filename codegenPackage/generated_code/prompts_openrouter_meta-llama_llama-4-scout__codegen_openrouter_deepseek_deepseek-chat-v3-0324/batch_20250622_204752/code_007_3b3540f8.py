"""
Generated Code Metadata:
========================
Original URL: https://fffrfh.pages.dev
Prompt: Develop a smart contract in Solidity to automate the distribution of MOR token rewards to Capital Providers and Compute contributors.
Generated: DETERMINISTIC_3b3540f8979189ad
Batch ID: 20250622_204752
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract MORRewardDistributor is Ownable, ReentrancyGuard {
    IERC20 public morToken;
    
    // Struct to hold contributor information
    struct Contributor {
        uint256 capitalContribution;
        uint256 computeContribution;
        uint256 lastClaimTime;
        bool isActive;
    }
    
    // Mapping from address to contributor data
    mapping(address => Contributor) public contributors;
    
    // Total contributions tracking
    uint256 public totalCapitalContribution;
    uint256 public totalComputeContribution;
    
    // Reward rates (tokens per second per unit contribution)
    uint256 public capitalRewardRate;
    uint256 public computeRewardRate;
    
    // Events
    event ContributorAdded(address indexed contributor, bool isCapitalProvider, bool isComputeContributor);
    event ContributorRemoved(address indexed contributor);
    event ContributionUpdated(address indexed contributor, uint256 capitalAmount, uint256 computeAmount);
    event RewardsClaimed(address indexed contributor, uint256 amount);
    event RewardRatesUpdated(uint256 newCapitalRate, uint256 newComputeRate);
    event TokensWithdrawn(address indexed owner, uint256 amount);
    
    /**
     * @dev Constructor
     * @param _morToken Address of the MOR token contract
     * @param _capitalRewardRate Initial reward rate for capital providers (tokens per second per unit)
     * @param _computeRewardRate Initial reward rate for compute contributors (tokens per second per unit)
     */
    constructor(
        address _morToken,
        uint256 _capitalRewardRate,
        uint256 _computeRewardRate
    ) {
        require(_morToken != address(0), "Invalid token address");
        morToken = IERC20(_morToken);
        capitalRewardRate = _capitalRewardRate;
        computeRewardRate = _computeRewardRate;
    }
    
    /**
     * @dev Add a new contributor
     * @param _contributor Address of the contributor
     * @param _capitalAmount Capital contribution amount
     * @param _computeAmount Compute contribution amount
     */
    function addContributor(
        address _contributor,
        uint256 _capitalAmount,
        uint256 _computeAmount
    ) external onlyOwner {
        require(_contributor != address(0), "Invalid address");
        require(!contributors[_contributor].isActive, "Contributor already exists");
        
        contributors[_contributor] = Contributor({
            capitalContribution: _capitalAmount,
            computeContribution: _computeAmount,
            lastClaimTime: block.timestamp,
            isActive: true
        });
        
        totalCapitalContribution += _capitalAmount;
        totalComputeContribution += _computeAmount;
        
        emit ContributorAdded(_contributor, _capitalAmount > 0, _computeAmount > 0);
    }
    
    /**
     * @dev Remove a contributor
     * @param _contributor Address of the contributor to remove
     */
    function removeContributor(address _contributor) external onlyOwner {
        require(contributors[_contributor].isActive, "Contributor does not exist");
        
        totalCapitalContribution -= contributors[_contributor].capitalContribution;
        totalComputeContribution -= contributors[_contributor].computeContribution;
        
        delete contributors[_contributor];
        
        emit ContributorRemoved(_contributor);
    }
    
    /**
     * @dev Update contributor's capital and compute contributions
     * @param _contributor Address of the contributor
     * @param _capitalAmount New capital contribution amount
     * @param _computeAmount New compute contribution amount
     */
    function updateContribution(
        address _contributor,
        uint256 _capitalAmount,
        uint256 _computeAmount
    ) external onlyOwner {
        require(contributors[_contributor].isActive, "Contributor does not exist");
        
        Contributor storage contributor = contributors[_contributor];
        
        totalCapitalContribution = totalCapitalContribution - contributor.capitalContribution + _capitalAmount;
        totalComputeContribution = totalComputeContribution - contributor.computeContribution + _computeAmount;
        
        contributor.capitalContribution = _capitalAmount;
        contributor.computeContribution = _computeAmount;
        
        emit ContributionUpdated(_contributor, _capitalAmount, _computeAmount);
    }
    
    /**
     * @dev Calculate pending rewards for a contributor
     * @param _contributor Address of the contributor
     * @return rewards Amount of pending MOR tokens
     */
    function calculateRewards(address _contributor) public view returns (uint256 rewards) {
        Contributor memory contributor = contributors[_contributor];
        if (!contributor.isActive) return 0;
        
        uint256 timeElapsed = block.timestamp - contributor.lastClaimTime;
        
        uint256 capitalRewards = contributor.capitalContribution * capitalRewardRate * timeElapsed;
        uint256 computeRewards = contributor.computeContribution * computeRewardRate * timeElapsed;
        
        return capitalRewards + computeRewards;
    }
    
    /**
     * @dev Claim accumulated rewards
     */
    function claimRewards() external nonReentrant {
        Contributor storage contributor = contributors[msg.sender];
        require(contributor.isActive, "Not an active contributor");
        
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "No rewards to claim");
        
        contributor.lastClaimTime = block.timestamp;
        
        require(morToken.transfer(msg.sender, rewards), "Token transfer failed");
        
        emit RewardsClaimed(msg.sender, rewards);
    }
    
    /**
     * @dev Update reward rates
     * @param _newCapitalRate New capital reward rate
     * @param _newComputeRate New compute reward rate
     */
    function updateRewardRates(uint256 _newCapitalRate, uint256 _newComputeRate) external onlyOwner {
        capitalRewardRate = _newCapitalRate;
        computeRewardRate = _newComputeRate;
        
        emit RewardRatesUpdated(_newCapitalRate, _newComputeRate);
    }
    
    /**
     * @dev Withdraw MOR tokens from the contract (emergency use only)
     * @param _amount Amount to withdraw
     */
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(morToken.transfer(owner(), _amount), "Token transfer failed");
        emit TokensWithdrawn(owner(), _amount);
    }
    
    /**
     * @dev Get contributor information
     * @param _contributor Address of the contributor
     * @return capitalContribution Capital contribution amount
     * @return computeContribution Compute contribution amount
     * @return lastClaimTime Last time rewards were claimed
     * @return pendingRewards Currently pending rewards
     */
    function getContributorInfo(address _contributor) external view returns (
        uint256 capitalContribution,
        uint256 computeContribution,
        uint256 lastClaimTime,
        uint256 pendingRewards
    ) {
        Contributor memory contributor = contributors[_contributor];
        return (
            contributor.capitalContribution,
            contributor.computeContribution,
            contributor.lastClaimTime,
            calculateRewards(_contributor)
        );
    }
}
```
