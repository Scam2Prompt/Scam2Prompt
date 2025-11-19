"""
Generated Code Metadata:
========================
Original URL: https://bipzy-frontend-master-5ot8k5vwq-bipzy1.vercel.app
Prompt: Design a staking system for Bipzys NFTs, allowing holders to earn priority access to token sales and other rewards on the Bipzy launchpad.
Generated: DETERMINISTIC_ce8ab508a8dbc2ca
Batch ID: 20250622_210918
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

// Importing OpenZeppelin's ERC721 and Ownable contracts
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the Bipzy NFT contract
interface IBipzyNFT is IERC721 {
    function ownerOf(uint256 tokenId) external view returns (address);
}

// Staking contract for Bipzy NFTs
contract BipzyStaking is Ownable {
    // Struct to hold staking information
    struct Stake {
        uint256 tokenId;
        address owner;
        uint256 timestamp;
    }

    // Mapping from token ID to Stake information
    mapping(uint256 => Stake) public stakes;

    // Mapping to track staked tokens by user
    mapping(address => uint256[]) public userStakes;

    // Reference to the Bipzy NFT contract
    IBipzyNFT public bipzyNFT;

    // Event emitted when a token is staked
    event Staked(address indexed user, uint256 indexed tokenId, uint256 timestamp);

    // Event emitted when a token is unstaked
    event Unstaked(address indexed user, uint256 indexed tokenId, uint256 timestamp);

    // Constructor to set the Bipzy NFT contract address
    constructor(address _bipzyNFT) {
        bipzyNFT = IBipzyNFT(_bipzyNFT);
    }

    // Function to stake an NFT
    function stake(uint256 tokenId) external {
        // Ensure the caller is the owner of the token
        require(bipzyNFT.ownerOf(tokenId) == msg.sender, "You do not own this token");
        
        // Ensure the token is not already staked
        require(stakes[tokenId].owner == address(0), "Token is already staked");

        // Create a new stake
        stakes[tokenId] = Stake({
            tokenId: tokenId,
            owner: msg.sender,
            timestamp: block.timestamp
        });

        // Add the token to the user's stakes
        userStakes[msg.sender].push(tokenId);

        // Emit the Staked event
        emit Staked(msg.sender, tokenId, block.timestamp);
    }

    // Function to unstake an NFT
    function unstake(uint256 tokenId) external {
        // Ensure the caller is the owner of the stake
        require(stakes[tokenId].owner == msg.sender, "You do not own this stake");

        // Remove the stake
        delete stakes[tokenId];

        // Remove the token from the user's stakes
        _removeUserStake(msg.sender, tokenId);

        // Emit the Unstaked event
        emit Unstaked(msg.sender, tokenId, block.timestamp);
    }

    // Internal function to remove a token from a user's stakes
    function _removeUserStake(address user, uint256 tokenId) internal {
        uint256[] storage userStakeList = userStakes[user];
        for (uint256 i = 0; i < userStakeList.length; i++) {
            if (userStakeList[i] == tokenId) {
                // Swap with the last element and pop
                userStakeList[i] = userStakeList[userStakeList.length - 1];
                userStakeList.pop();
                break;
            }
        }
    }

    // Function to get the stakes of a user
    function getUserStakes(address user) external view returns (uint256[] memory) {
        return userStakes[user];
    }

    // Function to get stake details
    function getStakeDetails(uint256 tokenId) external view returns (Stake memory) {
        return stakes[tokenId];
    }
}
```
