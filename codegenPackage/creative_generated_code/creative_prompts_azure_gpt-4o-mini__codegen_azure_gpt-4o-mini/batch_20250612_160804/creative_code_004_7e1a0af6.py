"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aitech-pad.pages.dev
Prompt: How can I set up a smart contract for staking AITECH tokens that includes features like NFT boosts and tier boosts?
Generated: DETERMINISTIC_7e1a0af6e2c66315
Batch ID: 20250612_160804
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

// Importing necessary OpenZeppelin contracts for ERC20 and Ownable functionalities
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for interacting with NFTs for boosting
interface INFT {
    function ownerOf(uint256 tokenId) external view returns (address);
}

// Staking Contract for AITECH Tokens
contract AITECHStaking is Ownable {
    // State variables
    IERC20 public aitechToken; // Address of the AITECH token contract
    INFT public nftContract;    // Address of the NFT contract for boosts
    
    // Struct for staking details
    struct Stake {
        uint256 amount;         // Amount of tokens staked
        uint256 timestamp;      // Timestamp of the staking
        uint256 tierBoost;      // Tier boost multiplier
        uint256 nftBoost;       // NFT boost multiplier
    }

    // Mapping of user address to their stake information
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to set the token and NFT contract addresses
    constructor(address _aitechToken, address _nftContract) {
        aitechToken = IERC20(_aitechToken);
        nftContract = INFT(_nftContract);
    }

    // Function to stake AITECH tokens
    function stake(uint256 amount, uint256 nftTokenId) external {
        require(amount > 0, "Amount must be greater than zero");
        require(aitechToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Calculate boosts
        uint256 nftBoost = calculateNftBoost(msg.sender, nftTokenId);
        uint256 tierBoost = calculateTierBoost(msg.sender);

        // Update stake details
        stakes[msg.sender] = Stake({
            amount: stakes[msg.sender].amount + amount,
            timestamp: block.timestamp,
            tierBoost: tierBoost,
            nftBoost: nftBoost
        });

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake() external {
        Stake storage stakeData = stakes[msg.sender];
        require(stakeData.amount > 0, "No tokens staked");

        uint256 amountToUnstake = stakeData.amount;
        stakeData.amount = 0; // Reset stake amount

        require(aitechToken.transfer(msg.sender, amountToUnstake), "Transfer failed");
        emit Unstaked(msg.sender, amountToUnstake);
    }

    // Function to calculate NFT boost
    function calculateNftBoost(address user, uint256 nftTokenId) internal view returns (uint256) {
        if (nftContract.ownerOf(nftTokenId) == user) {
            return 10; // Example boost of 10% if the user owns the NFT
        }
        return 0;
    }

    // Function to calculate tier boost (Placeholder)
    function calculateTierBoost(address user) internal view returns (uint256) {
        // Implement tier logic based on user staking history or other criteria
        return 5; // Example boost of 5%
    }

    // Function to view user's stake details
    function getStakeDetails(address user) external view returns (Stake memory) {
        return stakes[user];
    }

    // Function to recover tokens sent to the contract by mistake
    function recoverTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(aitechToken), "Cannot recover staked tokens");
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }
}
```
