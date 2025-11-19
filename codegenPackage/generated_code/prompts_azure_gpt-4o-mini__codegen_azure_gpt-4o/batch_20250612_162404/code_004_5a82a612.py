"""
Generated Code Metadata:
========================
Original URL: https://gofurs-cash.pages.dev
Prompt: Outline the steps to implement a staking mechanism for GOFURS tokens, considering the automatic NFT minting and burning features of the ERC404 standard.
Generated: DETERMINISTIC_5a82a61238c295db
Batch ID: 20250612_162404
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

/**
 * @title GOFURS Staking Contract
 * @dev Implements staking mechanism for GOFURS tokens with automatic NFT minting and burning (ERC404 standard).
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

interface IERC404 {
    function mintNFT(address to) external returns (uint256);
    function burnNFT(uint256 tokenId) external;
}

contract GOFURSStaking {
    // State variables
    IERC20 public gofursToken;
    IERC404 public nftContract;
    uint256 public stakingDuration; // Duration in seconds
    uint256 public rewardRate; // Reward rate per token staked

    struct Stake {
        uint256 amount;
        uint256 startTime;
        uint256 nftId;
    }

    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount, uint256 nftId);
    event Unstaked(address indexed user, uint256 amount, uint256 reward, uint256 nftId);

    // Constructor
    constructor(address _gofursToken, address _nftContract, uint256 _stakingDuration, uint256 _rewardRate) {
        require(_gofursToken != address(0), "Invalid GOFURS token address");
        require(_nftContract != address(0), "Invalid NFT contract address");
        require(_stakingDuration > 0, "Staking duration must be greater than 0");
        require(_rewardRate > 0, "Reward rate must be greater than 0");

        gofursToken = IERC20(_gofursToken);
        nftContract = IERC404(_nftContract);
        stakingDuration = _stakingDuration;
        rewardRate = _rewardRate;
    }

    // Stake GOFURS tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(stakes[msg.sender].amount == 0, "Already staking");

        // Transfer GOFURS tokens to the contract
        bool success = gofursToken.transferFrom(msg.sender, address(this), amount);
        require(success, "Token transfer failed");

        // Mint NFT for the staker
        uint256 nftId = nftContract.mintNFT(msg.sender);

        // Record staking details
        stakes[msg.sender] = Stake({
            amount: amount,
            startTime: block.timestamp,
            nftId: nftId
        });

        emit Staked(msg.sender, amount, nftId);
    }

    // Unstake GOFURS tokens
    function unstake() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No active stake");
        require(block.timestamp >= userStake.startTime + stakingDuration, "Staking period not yet completed");

        // Calculate reward
        uint256 reward = userStake.amount * rewardRate;

        // Transfer staked tokens and reward back to the user
        bool success = gofursToken.transfer(msg.sender, userStake.amount + reward);
        require(success, "Token transfer failed");

        // Burn the NFT
        nftContract.burnNFT(userStake.nftId);

        // Clear staking record
        delete stakes[msg.sender];

        emit Unstaked(msg.sender, userStake.amount, reward, userStake.nftId);
    }

    // View function to check staking details
    function getStakeDetails(address user) external view returns (uint256 amount, uint256 startTime, uint256 nftId) {
        Stake memory userStake = stakes[user];
        return (userStake.amount, userStake.startTime, userStake.nftId);
    }
}
```
