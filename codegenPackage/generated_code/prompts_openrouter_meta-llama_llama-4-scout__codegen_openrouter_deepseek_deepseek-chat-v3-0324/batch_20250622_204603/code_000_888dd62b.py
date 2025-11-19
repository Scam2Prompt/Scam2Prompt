"""
Generated Code Metadata:
========================
Original URL: https://kamalahorriss.pages.dev
Prompt: Write a smart contract for a token called $KAMA inspired by Kamala Harris, including functions for buying, claiming, and rewarding.
Generated: DETERMINISTIC_888dd62b7958d8c8
Batch ID: 20250622_204603
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

contract KAMAToken is ERC20, Ownable {
    using SafeMath for uint256;

    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens
    uint256 public constant TOKEN_PRICE = 0.0001 ether; // Price per token
    uint256 public constant CLAIM_PERIOD = 30 days; // Claim period duration
    uint256 public constant CLAIM_AMOUNT = 100 * 10**18; // Tokens per claim

    uint256 public claimStartTime;
    mapping(address => bool) public hasClaimed;
    mapping(address => uint256) public rewards;

    event TokensPurchased(address indexed buyer, uint256 amount);
    event TokensClaimed(address indexed claimer, uint256 amount);
    event RewardAdded(address indexed recipient, uint256 amount);
    event RewardClaimed(address indexed recipient, uint256 amount);

    constructor() ERC20("KAMA Token", "KAMA") {
        _mint(msg.sender, MAX_SUPPLY.div(2)); // Mint 50% to owner
        claimStartTime = block.timestamp;
    }

    function buyTokens() external payable {
        require(msg.value > 0, "KAMA: Must send ETH to buy tokens");
        uint256 tokensToBuy = msg.value.div(TOKEN_PRICE);
        require(totalSupply().add(tokensToBuy) <= MAX_SUPPLY, "KAMA: Exceeds max supply");

        _mint(msg.sender, tokensToBuy);
        emit TokensPurchased(msg.sender, tokensToBuy);
    }

    function claimTokens() external {
        require(block.timestamp <= claimStartTime.add(CLAIM_PERIOD), "KAMA: Claim period ended");
        require(!hasClaimed[msg.sender], "KAMA: Already claimed");
        require(balanceOf(address(this)) >= CLAIM_AMOUNT, "KAMA: Insufficient contract balance");

        hasClaimed[msg.sender] = true;
        _transfer(address(this), msg.sender, CLAIM_AMOUNT);
        emit TokensClaimed(msg.sender, CLAIM_AMOUNT);
    }

    function addReward(address recipient, uint256 amount) external onlyOwner {
        require(amount > 0, "KAMA: Reward amount must be positive");
        require(balanceOf(msg.sender) >= amount, "KAMA: Insufficient balance");

        rewards[recipient] = rewards[recipient].add(amount);
        _transfer(msg.sender, address(this), amount);
        emit RewardAdded(recipient, amount);
    }

    function claimReward() external {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "KAMA: No rewards available");

        rewards[msg.sender] = 0;
        _transfer(address(this), msg.sender, reward);
        emit RewardClaimed(msg.sender, reward);
    }

    function withdrawETH() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "KAMA: No ETH to withdraw");
        payable(owner()).transfer(balance);
    }

    function remainingClaimPeriod() external view returns (uint256) {
        if (block.timestamp > claimStartTime.add(CLAIM_PERIOD)) {
            return 0;
        }
        return claimStartTime.add(CLAIM_PERIOD).sub(block.timestamp);
    }
}
```
