"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gofurs-cash.pages.dev
Prompt: Outline the steps to implement a staking mechanism for GOFURS tokens, considering the automatic NFT minting and burning features of the ERC404 standard.
Generated: DETERMINISTIC_5a82a61238c295db
Batch ID: 20250612_162404
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

// Importing required interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for ERC404 (assuming a standard interface for NFT minting and burning)
interface IERC404 {
    function mintNFT(address to, uint256 tokenId) external;
    function burnNFT(uint256 tokenId) external;
}

// Staking contract for GOFURS tokens with NFT minting and burning features
contract StakingContract is Ownable {
    // Token interface for GOFURS
    IERC20 public gofursToken;
    IERC404 public nftContract;

    // Struct to hold staking information
    struct Stake {
        uint256 amount;
        uint256 timestamp;
        bool isActive;
    }

    // Mapping from user address to their stake information
    mapping(address => Stake) public stakes;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to set the GOFURS token and NFT contract addresses
    constructor(IERC20 _gofursToken, IERC404 _nftContract) {
        gofursToken = _gofursToken;
        nftContract = _nftContract;
    }

    // Function to stake tokens
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(gofursToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Store the stake information
        stakes[msg.sender] = Stake(amount, block.timestamp, true);
        
        // Emit Staked event
        emit Staked(msg.sender, amount);

        // Mint NFT to the user upon staking
        nftContract.mintNFT(msg.sender, block.timestamp);
    }

    // Function to unstake tokens
    function unstakeTokens() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.isActive, "No active stake found");

        // Transfer back the staked tokens to the user
        require(gofursToken.transfer(msg.sender, userStake.amount), "Transfer failed");
        
        // Burn the NFT associated with the stake (assumed tokenId is based on timestamp)
        nftContract.burnNFT(userStake.timestamp);

        // Reset the stake information
        userStake.amount = 0;
        userStake.isActive = false;

        // Emit Unstaked event
        emit Unstaked(msg.sender, userStake.amount);
    }

    // Function to check the staked amount
    function getStakedAmount(address user) external view returns (uint256) {
        return stakes[user].amount;
    }

    // Function to check if user has an active stake
    function hasActiveStake(address user) external view returns (bool) {
        return stakes[user].isActive;
    }
}
```
