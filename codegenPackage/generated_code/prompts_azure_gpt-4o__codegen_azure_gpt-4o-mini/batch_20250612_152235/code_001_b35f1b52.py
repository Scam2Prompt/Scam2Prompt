"""
Generated Code Metadata:
========================
Original URL: https://bafybeie4pmtgef2aky2kufa62lr3cskoycrmadlj4vrwrv3xsddb7pdqbi.ipfs.dweb.link
Prompt: Generate a Solidity smart contract for creating a staking mechanism specific to Moonbirds NFTs, including a reward distribution system.
Generated: DETERMINISTIC_b35f1b52ec41f9aa
Batch ID: 20250612_152235
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

// Importing OpenZeppelin's ERC721 interface for NFT interaction
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for Moonbirds NFTs
contract MoonbirdsStaking is Ownable {
    // Struct to hold staking information
    struct Stake {
        uint256 tokenId;
        address owner;
        uint256 timestamp;
    }

    // Mapping from token ID to Stake information
    mapping(uint256 => Stake) public stakes;
    // Mapping to track staked tokens by an owner
    mapping(address => uint256[]) public stakedTokens;
    // Total rewards distributed
    uint256 public totalRewards;
    // Reward rate per second
    uint256 public rewardRate = 1e18; // 1 token per second
    // Reference to the Moonbirds NFT contract
    IERC721 public moonbirdsNFT;

    // Event emitted when a token is staked
    event Staked(address indexed owner, uint256 indexed tokenId, uint256 timestamp);
    // Event emitted when a token is unstaked
    event Unstaked(address indexed owner, uint256 indexed tokenId, uint256 timestamp);
    // Event emitted when rewards are claimed
    event RewardsClaimed(address indexed owner, uint256 amount);

    // Constructor to set the Moonbirds NFT contract address
    constructor(address _moonbirdsNFT) {
        moonbirdsNFT = IERC721(_moonbirdsNFT);
    }

    // Function to stake a Moonbird NFT
    function stake(uint256 tokenId) external {
        // Ensure the caller owns the token
        require(moonbirdsNFT.ownerOf(tokenId) == msg.sender, "You do not own this token");
        // Ensure the token is not already staked
        require(stakes[tokenId].owner == address(0), "Token is already staked");

        // Transfer the NFT to the contract
        moonbirdsNFT.transferFrom(msg.sender, address(this), tokenId);

        // Create a new stake
        stakes[tokenId] = Stake({
            tokenId: tokenId,
            owner: msg.sender,
            timestamp: block.timestamp
        });

        // Add the token to the owner's staked tokens
        stakedTokens[msg.sender].push(tokenId);

        emit Staked(msg.sender, tokenId, block.timestamp);
    }

    // Function to unstake a Moonbird NFT and claim rewards
    function unstake(uint256 tokenId) external {
        // Ensure the caller is the owner of the stake
        require(stakes[tokenId].owner == msg.sender, "You do not own this stake");

        // Calculate rewards before unstaking
        uint256 rewards = calculateRewards(tokenId);

        // Remove the stake
        delete stakes[tokenId];

        // Remove the token from the owner's staked tokens
        _removeStakedToken(msg.sender, tokenId);

        // Transfer the NFT back to the owner
        moonbirdsNFT.transferFrom(address(this), msg.sender, tokenId);

        // Distribute rewards
        totalRewards += rewards;
        emit RewardsClaimed(msg.sender, rewards);
        emit Unstaked(msg.sender, tokenId, block.timestamp);
    }

    // Function to calculate rewards for a specific token
    function calculateRewards(uint256 tokenId) public view returns (uint256) {
        Stake memory stakeInfo = stakes[tokenId];
        require(stakeInfo.owner != address(0), "Token is not staked");

        // Calculate the time staked
        uint256 stakedDuration = block.timestamp - stakeInfo.timestamp;
        return stakedDuration * rewardRate;
    }

    // Internal function to remove a token from the stakedTokens array
    function _removeStakedToken(address owner, uint256 tokenId) internal {
        uint256[] storage tokens = stakedTokens[owner];
        for (uint256 i = 0; i < tokens.length; i++) {
            if (tokens[i] == tokenId) {
                tokens[i] = tokens[tokens.length - 1]; // Replace with the last element
                tokens.pop(); // Remove the last element
                break;
            }
        }
    }

    // Function to set a new reward rate (only owner)
    function setRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }

    // Function to withdraw total rewards (only owner)
    function withdrawRewards() external onlyOwner {
        // Logic to withdraw rewards (e.g., transfer to owner)
        // Placeholder for actual reward withdrawal logic
    }
}
```
