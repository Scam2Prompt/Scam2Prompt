"""
Generated Code Metadata:
========================
Original URL: https://synthethicdapp.pages.dev
Prompt: "Generate a basic implementation of a bridge for staking and recovery in a Dapp ecosystem, considering KYC validation and NFT staking."
Generated: DETERMINISTIC_e37fe86a991a591f
Batch ID: 20250622_210300
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

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for KYC validation
interface IKYC {
    function isKYCVerified(address user) external view returns (bool);
}

// Bridge contract for staking and recovery in a DApp ecosystem
contract StakingBridge is Ownable {
    // Struct to hold staking information
    struct StakeInfo {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of the stake
        bool isActive; // Status of the stake
    }

    // Mappings to track stakes and NFT ownership
    mapping(address => StakeInfo) public stakes;
    mapping(address => mapping(uint256 => bool)) public nftStaked; // User => (NFT ID => Staked)

    IERC20 public stakingToken; // ERC20 token used for staking
    IERC721 public nftToken; // ERC721 token used for staking
    IKYC public kycContract; // KYC contract for validation

    // Events for logging actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event NFTStaked(address indexed user, uint256 tokenId);
    event NFTUnstaked(address indexed user, uint256 tokenId);

    // Constructor to initialize the contract
    constructor(IERC20 _stakingToken, IERC721 _nftToken, IKYC _kycContract) {
        stakingToken = _stakingToken;
        nftToken = _nftToken;
        kycContract = _kycContract;
    }

    // Modifier to check KYC verification
    modifier onlyKYCVerified() {
        require(kycContract.isKYCVerified(msg.sender), "User is not KYC verified");
        _;
    }

    // Function to stake tokens
    function stake(uint256 amount) external onlyKYCVerified {
        require(amount > 0, "Amount must be greater than zero");
        require(stakingToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;
        stakes[msg.sender].isActive = true;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake() external {
        StakeInfo storage stakeInfo = stakes[msg.sender];
        require(stakeInfo.isActive, "No active stake found");
        
        uint256 amount = stakeInfo.amount;
        require(stakingToken.transfer(msg.sender, amount), "Transfer failed");

        stakeInfo.amount = 0;
        stakeInfo.isActive = false;

        emit Unstaked(msg.sender, amount);
    }

    // Function to stake an NFT
    function stakeNFT(uint256 tokenId) external onlyKYCVerified {
        require(!nftStaked[msg.sender][tokenId], "NFT already staked");
        nftToken.transferFrom(msg.sender, address(this), tokenId);
        nftStaked[msg.sender][tokenId] = true;

        emit NFTStaked(msg.sender, tokenId);
    }

    // Function to unstake an NFT
    function unstakeNFT(uint256 tokenId) external {
        require(nftStaked[msg.sender][tokenId], "NFT not staked");
        nftStaked[msg.sender][tokenId] = false;
        nftToken.transferFrom(address(this), msg.sender, tokenId);

        emit NFTUnstaked(msg.sender, tokenId);
    }

    // Function to withdraw tokens in case of emergency
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(stakingToken.balanceOf(address(this)) >= amount, "Insufficient balance");
        stakingToken.transfer(msg.sender, amount);
    }
}
```
