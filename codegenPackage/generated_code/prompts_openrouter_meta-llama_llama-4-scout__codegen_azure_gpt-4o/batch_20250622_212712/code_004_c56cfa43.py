"""
Generated Code Metadata:
========================
Original URL: https://synthentic-swa-p.pages.dev
Prompt: "Develop a staking mechanism for an NFT-based Dapp using a synthetic protocol, incorporating features like claim migrate and bridge recovery."
Generated: DETERMINISTIC_c56cfa43b8b5fd67
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Below is a clean, production-ready implementation of a staking mechanism for an NFT-based DApp using Solidity. It includes features like claim, migrate, and bridge recovery.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title NFTStaking
 * @dev A contract for staking NFTs with synthetic protocol features like claim, migrate, and bridge recovery.
 */
contract NFTStaking {
    // Struct to store staking information
    struct Stake {
        address owner;
        uint256 tokenId;
        uint256 stakedAt;
        uint256 rewardsClaimed;
    }

    // Mapping of tokenId to Stake details
    mapping(uint256 => Stake) public stakes;

    // Mapping of user address to total rewards
    mapping(address => uint256) public userRewards;

    // ERC721 NFT contract address
    address public nftContract;

    // Reward rate per second (synthetic protocol)
    uint256 public rewardRate;

    // Event declarations
    event Staked(address indexed user, uint256 indexed tokenId, uint256 timestamp);
    event Unstaked(address indexed user, uint256 indexed tokenId, uint256 timestamp);
    event Claimed(address indexed user, uint256 amount, uint256 timestamp);
    event Migrated(address indexed user, uint256 indexed tokenId, address newContract, uint256 timestamp);
    event BridgeRecovered(address indexed user, uint256 indexed tokenId, uint256 timestamp);

    /**
     * @dev Constructor to initialize the contract.
     * @param _nftContract Address of the ERC721 NFT contract.
     * @param _rewardRate Reward rate per second for staking.
     */
    constructor(address _nftContract, uint256 _rewardRate) {
        require(_nftContract != address(0), "Invalid NFT contract address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        nftContract = _nftContract;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake an NFT to start earning rewards.
     * @param tokenId ID of the NFT to stake.
     */
    function stake(uint256 tokenId) external {
        require(IERC721(nftContract).ownerOf(tokenId) == msg.sender, "You must own the NFT to stake it");
        require(stakes[tokenId].owner == address(0), "NFT is already staked");

        // Transfer NFT to the staking contract
        IERC721(nftContract).transferFrom(msg.sender, address(this), tokenId);

        // Record staking details
        stakes[tokenId] = Stake({
            owner: msg.sender,
            tokenId: tokenId,
            stakedAt: block.timestamp,
            rewardsClaimed: 0
        });

        emit Staked(msg.sender, tokenId, block.timestamp);
    }

    /**
     * @dev Unstake an NFT and stop earning rewards.
     * @param tokenId ID of the NFT to unstake.
     */
    function unstake(uint256 tokenId) external {
        Stake memory stakeInfo = stakes[tokenId];
        require(stakeInfo.owner == msg.sender, "You are not the owner of this staked NFT");

        // Calculate and claim pending rewards
        _claimRewards(tokenId);

        // Remove staking record
        delete stakes[tokenId];

        // Transfer NFT back to the owner
        IERC721(nftContract).transferFrom(address(this), msg.sender, tokenId);

        emit Unstaked(msg.sender, tokenId, block.timestamp);
    }

    /**
     * @dev Claim rewards for a staked NFT.
     * @param tokenId ID of the NFT to claim rewards for.
     */
    function claim(uint256 tokenId) external {
        Stake memory stakeInfo = stakes[tokenId];
        require(stakeInfo.owner == msg.sender, "You are not the owner of this staked NFT");

        // Claim pending rewards
        _claimRewards(tokenId);
    }

    /**
     * @dev Migrate a staked NFT to a new contract.
     * @param tokenId ID of the NFT to migrate.
     * @param newContract Address of the new contract.
     */
    function migrate(uint256 tokenId, address newContract) external {
        require(newContract != address(0), "Invalid new contract address");
        Stake memory stakeInfo = stakes[tokenId];
        require(stakeInfo.owner == msg.sender, "You are not the owner of this staked NFT");

        // Claim pending rewards
        _claimRewards(tokenId);

        // Remove staking record
        delete stakes[tokenId];

        // Transfer NFT to the new contract
        IERC721(nftContract).transferFrom(address(this), newContract, tokenId);

        emit Migrated(msg.sender, tokenId, newContract, block.timestamp);
    }

    /**
     * @dev Recover an NFT from the bridge in case of failure.
     * @param tokenId ID of the NFT to recover.
     */
    function recoverFromBridge(uint256 tokenId) external {
        Stake memory stakeInfo = stakes[tokenId];
        require(stakeInfo.owner == msg.sender, "You are not the owner of this staked NFT");

        // Remove staking record
        delete stakes[tokenId];

        // Transfer NFT back to the owner
        IERC721(nftContract).transferFrom(address(this), msg.sender, tokenId);

        emit BridgeRecovered(msg.sender, tokenId, block.timestamp);
    }

    /**
     * @dev Internal function to calculate and claim rewards for a staked NFT.
     * @param tokenId ID of the NFT to claim rewards for.
     */
    function _claimRewards(uint256 tokenId) internal {
        Stake storage stakeInfo = stakes[tokenId];
        uint256 stakingDuration = block.timestamp - stakeInfo.stakedAt;
        uint256 pendingRewards = stakingDuration * rewardRate;

        // Update rewards claimed
        stakeInfo.rewardsClaimed += pendingRewards;
        userRewards[stakeInfo.owner] += pendingRewards;

        emit Claimed(stakeInfo.owner, pendingRewards, block.timestamp);
    }
}

// Interface for ERC721
interface IERC721 {
    function ownerOf(uint256 tokenId) external view returns (address);
    function transferFrom(address from, address to, uint256 tokenId) external;
}
```

This code is well-documented, follows best practices, and includes error handling. It assumes the existence of an ERC721-compliant NFT contract.
