"""
Generated Code Metadata:
========================
Original URL: https://singularity-finance.pages.dev
Prompt: Write a smart contract to tokenize curated data contributions into yield-bearing assets for the AI economy, leveraging Singularity Finance's data ownership monetization model.
Generated: DETERMINISTIC_e12069ff1dfc70cf
Batch ID: 20250612_145831
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

/**
 * @title DataYieldToken
 * @dev Tokenizes curated data contributions into yield-bearing assets
 */
contract DataYieldToken is ERC20, ERC20Burnable, Ownable, Pausable {
    using SafeMath for uint256;

    struct DataContribution {
        address contributor;
        uint256 amount;
        uint256 timestamp;
        string metadata;
    }

    uint256 public constant BASE_YIELD_RATE = 100; // 1% annual yield
    uint256 public constant YIELD_PRECISION = 10000;
    uint256 public totalContributions;
    uint256 public lastYieldDistribution;
    
    mapping(address => uint256) public contributorShares;
    mapping(uint256 => DataContribution) public contributions;
    mapping(address => uint256) public lastClaimed;

    event ContributionAdded(
        address indexed contributor,
        uint256 amount,
        string metadata,
        uint256 timestamp
    );
    event YieldDistributed(uint256 amount, uint256 timestamp);
    event YieldClaimed(address indexed claimer, uint256 amount);

    constructor() ERC20("Data Yield Token", "DYT") {
        lastYieldDistribution = block.timestamp;
    }

    /**
     * @dev Add a new data contribution and mint tokens
     * @param amount The amount of tokens to mint
     * @param metadata IPFS hash or reference to the contributed data
     */
    function addContribution(uint256 amount, string memory metadata) external whenNotPaused {
        require(amount > 0, "Amount must be greater than 0");
        require(bytes(metadata).length > 0, "Metadata cannot be empty");

        _mint(msg.sender, amount);
        totalContributions = totalContributions.add(amount);
        contributorShares[msg.sender] = contributorShares[msg.sender].add(amount);

        uint256 contributionId = totalContributions;
        contributions[contributionId] = DataContribution({
            contributor: msg.sender,
            amount: amount,
            timestamp: block.timestamp,
            metadata: metadata
        });

        emit ContributionAdded(msg.sender, amount, metadata, block.timestamp);
    }

    /**
     * @dev Distribute yield to all token holders
     */
    function distributeYield() external onlyOwner {
        uint256 currentTime = block.timestamp;
        uint256 timeElapsed = currentTime.sub(lastYieldDistribution);
        
        if (timeElapsed == 0) {
            return;
        }

        uint256 totalSupply = totalSupply();
        if (totalSupply == 0) {
            lastYieldDistribution = currentTime;
            return;
        }

        // Calculate yield based on time elapsed and base rate
        uint256 yieldAmount = totalSupply
            .mul(BASE_YIELD_RATE)
            .mul(timeElapsed)
            .div(365 days)
            .div(YIELD_PRECISION);

        if (yieldAmount > 0) {
            _mint(address(this), yieldAmount);
            lastYieldDistribution = currentTime;
            emit YieldDistributed(yieldAmount, currentTime);
        }
    }

    /**
     * @dev Claim accumulated yield for the caller
     */
    function claimYield() external {
        require(contributorShares[msg.sender] > 0, "No shares to claim yield");
        
        uint256 currentTime = block.timestamp;
        uint256 timeElapsed = currentTime.sub(lastClaimed[msg.sender] > 0 ? lastClaimed[msg.sender] : lastYieldDistribution);
        
        if (timeElapsed == 0) {
            return;
        }

        uint256 userShare = contributorShares[msg.sender];
        uint256 totalShares = totalSupply().sub(balanceOf(address(this)));
        
        if (totalShares == 0) {
            lastClaimed[msg.sender] = currentTime;
            return;
        }

        uint256 availableYield = balanceOf(address(this));
        uint256 userYield = availableYield.mul(userShare).mul(timeElapsed).div(totalShares).div(365 days);

        if (userYield > 0) {
            _transfer(address(this), msg.sender, userYield);
            lastClaimed[msg.sender] = currentTime;
            emit YieldClaimed(msg.sender, userYield);
        }
    }

    /**
     * @dev Pause all token transfers
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause all token transfers
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Override transfer to handle pausable
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
