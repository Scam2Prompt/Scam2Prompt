"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kangamoon-claim.pages.dev
Prompt: Write a smart contract in Solidity for an ERC-20 token similar to $KANG, including features for presale, staking, and rewards distribution as described in Kangamoon's tokenomics.
Generated: DETERMINISTIC_f2cf87c4179850fa
Batch ID: 20250612_145625
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title KangToken
 * @dev ERC20 Token with presale, staking, and rewards distribution functionalities
 */
contract KangToken is ERC20, Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Variables for presale and staking
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    uint256 public presaleRate; // Rate of token per ETH during presale
    uint256 public totalStaked;
    uint256 public rewardsPool;

    // Mapping for staking
    mapping(address => uint256) public stakedBalance;
    mapping(address => uint256) public rewards;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event Staked(address indexed staker, uint256 amount);
    event Unstaked(address indexed staker, uint256 amount);
    event RewardsDistributed(address indexed staker, uint256 amount);
    
    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("KangToken", "KANG") {
        _mint(msg.sender, 1_000_000 * 10 ** decimals()); // Mint initial supply to owner
        presaleRate = 100; // Example rate: 100 KANG per 1 ETH
        presaleStartTime = block.timestamp; // Start presale immediately
        presaleEndTime = block.timestamp + 7 days; // Presale lasts for 7 days
    }

    // Modifier to check during presale
    modifier onlyDuringPresale() {
        require(block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime, "Presale is not active");
        _;
    }

    // Function to purchase tokens during presale
    function purchaseTokens() external payable onlyDuringPresale {
        require(msg.value > 0, "Must send ETH to buy tokens");
        uint256 tokenAmount = msg.value.mul(presaleRate);
        _transfer(owner(), msg.sender, tokenAmount);
        emit TokensPurchased(msg.sender, tokenAmount);
    }

    // Function to stake tokens
    function stakeTokens(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to stake");
        
        stakedBalance[msg.sender] = stakedBalance[msg.sender].add(amount);
        totalStaked = totalStaked.add(amount);

        _transfer(msg.sender, address(this), amount); // Transfer tokens to the contract
        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstakeTokens(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(stakedBalance[msg.sender] >= amount, "Insufficient staked balance");

        stakedBalance[msg.sender] = stakedBalance[msg.sender].sub(amount);
        totalStaked = totalStaked.sub(amount);
        
        _transfer(address(this), msg.sender, amount); // Transfer tokens back to the user
        emit Unstaked(msg.sender, amount);
    }

    // Function to distribute rewards to stakers
    function distributeRewards(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(totalStaked > 0, "No staked tokens to distribute rewards");

        rewardsPool = rewardsPool.add(amount);
        for (address staker in stakers) {
            uint256 reward = amount.mul(stakedBalance[staker]).div(totalStaked);
            rewards[staker] = rewards[staker].add(reward);
            emit RewardsDistributed(staker, reward);
        }
    }

    // Function to claim rewards
    function claimRewards() external nonReentrant {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        rewards[msg.sender] = 0; // Reset rewards
        _transfer(address(this), msg.sender, reward); // Transfer rewards to user
    }

    // Fallback function to receive ETH
    receive() external payable {
        purchaseTokens();
    }
}
```
