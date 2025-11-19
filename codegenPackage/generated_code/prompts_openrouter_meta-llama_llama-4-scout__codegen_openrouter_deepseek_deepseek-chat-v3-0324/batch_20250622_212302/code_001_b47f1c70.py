"""
Generated Code Metadata:
========================
Original URL: https://crudo-protocol.xyz
Prompt: Write a smart contract on the Binance Smart Chain (BEP20) for the CRUDO token, including functions for token sale, staking, and reward distribution.
Generated: DETERMINISTIC_b47f1c7051bc2183
Batch ID: 20250622_212302
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract CRUDOToken is ERC20, ERC20Burnable, Pausable, Ownable {
    using SafeMath for uint256;

    // Token sale parameters
    uint256 public constant MAX_SUPPLY = 1000000000 * 10**18; // 1 billion tokens
    uint256 public constant SALE_RATE = 1000; // 1 BNB = 1000 CRUDO
    uint256 public saleEndTime;
    bool public saleActive = false;

    // Staking parameters
    struct Stake {
        uint256 amount;
        uint256 stakedAt;
    }
    mapping(address => Stake) public stakes;
    uint256 public stakingRewardRate = 10; // 10% APY
    uint256 public totalStaked;

    // Events
    event TokensPurchased(address indexed buyer, uint256 bnbAmount, uint256 tokenAmount);
    event TokensStaked(address indexed staker, uint256 amount);
    event TokensUnstaked(address indexed staker, uint256 amount, uint256 reward);
    event RewardDistributed(address indexed staker, uint256 reward);

    constructor() ERC20("CRUDO Token", "CRUDO") {
        _mint(msg.sender, MAX_SUPPLY.mul(20).div(100)); // 20% for team/development
    }

    // Token sale functions
    function startSale(uint256 durationInDays) external onlyOwner {
        require(!saleActive, "Sale is already active");
        saleActive = true;
        saleEndTime = block.timestamp.add(durationInDays.mul(1 days));
    }

    function endSale() external onlyOwner {
        require(saleActive, "Sale is not active");
        saleActive = false;
    }

    function buyTokens() external payable whenNotPaused {
        require(saleActive, "Sale is not active");
        require(block.timestamp <= saleEndTime, "Sale has ended");
        require(msg.value > 0, "BNB amount must be greater than 0");

        uint256 tokens = msg.value.mul(SALE_RATE);
        require(totalSupply().add(tokens) <= MAX_SUPPLY, "Exceeds max supply");

        _mint(msg.sender, tokens);
        emit TokensPurchased(msg.sender, msg.value, tokens);
    }

    // Staking functions
    function stake(uint256 amount) external whenNotPaused {
        require(amount > 0, "Amount must be greater than 0");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");

        if (stakes[msg.sender].amount > 0) {
            _distributeReward(msg.sender);
        }

        _transfer(msg.sender, address(this), amount);
        stakes[msg.sender] = Stake({
            amount: stakes[msg.sender].amount.add(amount),
            stakedAt: block.timestamp
        });
        totalStaked = totalStaked.add(amount);

        emit TokensStaked(msg.sender, amount);
    }

    function unstake(uint256 amount) external whenNotPaused {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient staked amount");

        _distributeReward(msg.sender);

        stakes[msg.sender].amount = stakes[msg.sender].amount.sub(amount);
        totalStaked = totalStaked.sub(amount);
        _transfer(address(this), msg.sender, amount);

        emit TokensUnstaked(msg.sender, amount, 0); // Reward is already distributed
    }

    function claimReward() external whenNotPaused {
        require(stakes[msg.sender].amount > 0, "No staked tokens");
        _distributeReward(msg.sender);
    }

    function _distributeReward(address staker) internal {
        Stake storage stakeInfo = stakes[staker];
        if (stakeInfo.amount == 0) return;

        uint256 stakingDuration = block.timestamp.sub(stakeInfo.stakedAt);
        uint256 reward = stakeInfo.amount
            .mul(stakingRewardRate)
            .mul(stakingDuration)
            .div(365 days)
            .div(100);

        if (reward > 0) {
            _mint(staker, reward);
            emit RewardDistributed(staker, reward);
        }

        stakeInfo.stakedAt = block.timestamp;
    }

    // Admin functions
    function setRewardRate(uint256 newRate) external onlyOwner {
        require(newRate <= 100, "Rate cannot exceed 100%");
        stakingRewardRate = newRate;
    }

    function withdrawBNB() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    function pause() external onlyOwner {
        _pause();
    }

    function unpause() external onlyOwner {
        _unpause();
    }

    function emergencyWithdraw(address tokenAddress) external onlyOwner {
        require(tokenAddress != address(this), "Cannot withdraw CRUDO tokens");
        IERC20 token = IERC20(tokenAddress);
        token.transfer(owner(), token.balanceOf(address(this)));
    }
}
```
