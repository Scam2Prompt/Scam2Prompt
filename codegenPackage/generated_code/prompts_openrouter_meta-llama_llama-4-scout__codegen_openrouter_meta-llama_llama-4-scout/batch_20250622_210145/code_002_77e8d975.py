"""
Generated Code Metadata:
========================
Original URL: https://ipmbway.pages.dev
Prompt: Design a smart contract in Solidity for a simple staking mechanism that allows users to stake GoldPro Tokens and receive a discount on redeemable physical gold through GEM NFTs.
Generated: DETERMINISTIC_77e8d975eeb565ff
Batch ID: 20250622_210145
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
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title GoldPro Staking Contract
 * @author [Your Name]
 * @notice This contract allows users to stake GoldPro Tokens and receive a discount on redeemable physical gold through GEM NFTs.
 */
contract GoldProStaking is ReentrancyGuard {
    // Mapping of user staking balances
    mapping(address => uint256) public stakingBalances;

    // Mapping of user GEM NFT balances
    mapping(address => uint256) public gemNFTBalances;

    // GoldPro Token contract
    ERC20 public goldProToken;

    // GEM NFT contract
    ERC721 public gemNFT;

    // Staking reward rate (1 = 1%)
    uint256 public stakingRewardRate;

    // Physical gold redemption price (in GEM NFTs)
    uint256 public redemptionPrice;

    // Event emitted when a user stakes GoldPro Tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when a user unstakes GoldPro Tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when a user redeems physical gold
    event Redeemed(address indexed user, uint256 amount);

    /**
     * @param _goldProToken Address of the GoldPro Token contract
     * @param _gemNFT Address of the GEM NFT contract
     * @param _stakingRewardRate Staking reward rate (1 = 1%)
     * @param _redemptionPrice Physical gold redemption price (in GEM NFTs)
     */
    constructor(
        address _goldProToken,
        address _gemNFT,
        uint256 _stakingRewardRate,
        uint256 _redemptionPrice
    ) {
        goldProToken = ERC20(_goldProToken);
        gemNFT = ERC721(_gemNFT);
        stakingRewardRate = _stakingRewardRate;
        redemptionPrice = _redemptionPrice;
    }

    /**
     * @notice Stake GoldPro Tokens
     * @param amount Amount of GoldPro Tokens to stake
     */
    function stake(uint256 amount) external {
        require(goldProToken.balanceOf(msg.sender) >= amount, "Insufficient GoldPro Tokens");
        require(amount > 0, "Stake amount must be greater than 0");

        stakingBalances[msg.sender] += amount;
        goldProToken.transferFrom(msg.sender, address(this), amount);

        emit Staked(msg.sender, amount);
    }

    /**
     * @notice Unstake GoldPro Tokens
     * @param amount Amount of GoldPro Tokens to unstake
     */
    function unstake(uint256 amount) external {
        require(stakingBalances[msg.sender] >= amount, "Insufficient staked balance");
        require(amount > 0, "Unstake amount must be greater than 0");

        stakingBalances[msg.sender] -= amount;
        goldProToken.transfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    /**
     * @notice Redeem physical gold using GEM NFTs
     * @param amount Amount of physical gold to redeem
     */
    function redeem(uint256 amount) external {
        require(gemNFTBalances[msg.sender] >= redemptionPrice * amount, "Insufficient GEM NFTs");
        require(amount > 0, "Redemption amount must be greater than 0");

        gemNFTBalances[msg.sender] -= redemptionPrice * amount;
        // Add logic for physical gold redemption (e.g., increment a counter, update a mapping, etc.)

        emit Redeemed(msg.sender, amount);
    }

    /**
     * @notice Mint GEM NFTs to a user
     * @param user Address of the user to mint GEM NFTs to
     * @param amount Amount of GEM NFTs to mint
     */
    function mintGEMNFTs(address user, uint256 amount) external {
        require(msg.sender == address(gemNFT), "Only the GEM NFT contract can mint GEM NFTs");

        for (uint256 i = 0; i < amount; i++) {
            gemNFT.mint(user, uint256(keccak256(abi.encodePacked(user, i))));
        }

        gemNFTBalances[user] += amount;
    }

    /**
     * @notice Get the staking balance of a user
     * @param user Address of the user to get the staking balance of
     * @return The staking balance of the user
     */
    function getStakingBalance(address user) external view returns (uint256) {
        return stakingBalances[user];
    }

    /**
     * @notice Get the GEM NFT balance of a user
     * @param user Address of the user to get the GEM NFT balance of
     * @return The GEM NFT balance of the user
     */
    function getGEMNFTBalance(address user) external view returns (uint256) {
        return gemNFTBalances[user];
    }
}
```
