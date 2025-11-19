"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://koalamemecoin.pages.dev
Prompt: Generate a code snippet for a smart contract that includes tokenomics similar to KoalaKash, including presale and staking rewards.
Generated: DETERMINISTIC_b33c7edaafca188e
Batch ID: 20250612_160946
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

// Importing OpenZeppelin's ERC20 token implementation and Ownable contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract KoalaKash is ERC20, Ownable, ReentrancyGuard {
    // Events to log important actions
    event PresaleStarted(uint256 indexed startTime, uint256 indexed endTime);
    event PresaleEnded(uint256 indexed endTime);
    event StakingRewarded(address indexed user, uint256 amount);

    // Presale variables
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    uint256 public presaleRate;
    uint256 public presaleCap;
    uint256 public totalPresaleTokens;
    mapping(address => uint256) public contributions;

    // Staking variables
    struct Stake {
        uint256 amount;
        uint256 timestamp;
    }
    mapping(address => Stake) public stakes;
    uint256 public rewardRate; // Reward rate for staking

    // Constructor to initialize token details
    constructor() ERC20("KoalaKash", "KKASH") {
        presaleRate = 100; // 1 ETH = 100 KKASH
        presaleCap = 10000 * 10 ** decimals(); // Presale cap in tokens
        rewardRate = 10; // 10% reward for staking
    }

    // Function to start the presale
    function startPresale(uint256 duration) external onlyOwner {
        presaleStartTime = block.timestamp;
        presaleEndTime = block.timestamp + duration;
        emit PresaleStarted(presaleStartTime, presaleEndTime);
    }

    // Function to end the presale
    function endPresale() external onlyOwner {
        require(block.timestamp >= presaleEndTime, "Presale is still ongoing");
        emit PresaleEnded(block.timestamp);
    }

    // Function to buy tokens during presale
    function buyTokens() external payable nonReentrant {
        require(block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime, "Presale is not active");
        require(msg.value > 0, "You need to send some ETH");
        
        uint256 tokensToBuy = msg.value * presaleRate;
        require(totalPresaleTokens + tokensToBuy <= presaleCap, "Presale cap exceeded");

        contributions[msg.sender] += msg.value;
        totalPresaleTokens += tokensToBuy;
        _mint(msg.sender, tokensToBuy);
    }

    // Function to stake tokens
    function stakeTokens(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to stake");

        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;
        _transfer(msg.sender, address(this), amount); // Transfer tokens to the contract
    }

    // Function to claim staking rewards
    function claimRewards() external nonReentrant {
        Stake storage stakeInfo = stakes[msg.sender];
        require(stakeInfo.amount > 0, "No tokens staked");

        uint256 rewardAmount = (stakeInfo.amount * rewardRate) / 100;
        _mint(msg.sender, rewardAmount); // Mint reward tokens to user

        emit StakingRewarded(msg.sender, rewardAmount);
    }

    // Function to withdraw tokens (for owner)
    function withdraw(uint256 amount) external onlyOwner {
        payable(owner()).transfer(amount);
    }

    // Function to withdraw unsold presale tokens (for owner)
    function withdrawUnsoldTokens() external onlyOwner {
        require(block.timestamp >= presaleEndTime, "Presale not ended yet");
        uint256 unsoldTokens = presaleCap - totalPresaleTokens;
        require(unsoldTokens > 0, "No unsold tokens available");

        _mint(owner(), unsoldTokens);
    }

    // Function to view contract balance
    function contractBalance() external view returns (uint256) {
        return address(this).balance;
    }

    // Function to view staked amount
    function stakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }
}
```
