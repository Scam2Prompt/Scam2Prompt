"""
Generated Code Metadata:
========================
Original URL: https://paraxweb3dapp.pages.dev
Prompt: Create a Solidity smart contract for staking NFTs in the ParaX platform's NFT Staking Pool, ensuring compatibility with ERC-721 tokens and integration with Chainlink price feeds.
Generated: DETERMINISTIC_b7a901f4fc3a8edb
Batch ID: 20250612_145619
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
import "@openzeppelin/contracts/token/ERC721/IERC721Receiver.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

contract ParaXNFTStakingPool is ReentrancyGuard, IERC721Receiver {
    using SafeMath for uint256;

    // Mapping of staked NFTs
    mapping(address => mapping(uint256 => StakedNFT)) public stakedNFTs;

    // Mapping of user staking balances
    mapping(address => uint256) public userBalances;

    // Mapping of NFT owners
    mapping(uint256 => address) public nftOwners;

    // Chainlink price feed
    AggregatorV3Interface public priceFeed;

    // ERC-721 token contract
    IERC721 public nftContract;

    // Staking pool address
    address public stakingPoolAddress;

    // Event emitted when an NFT is staked
    event NFTStaked(address indexed user, uint256 nftId);

    // Event emitted when an NFT is unstaked
    event NFTUnstaked(address indexed user, uint256 nftId);

    // Event emitted when a user claims rewards
    event RewardsClaimed(address indexed user, uint256 rewards);

    // Struct to represent a staked NFT
    struct StakedNFT {
        uint256 nftId;
        uint256 stakingTimestamp;
    }

    // Constructor
    constructor(
        address _nftContract,
        address _priceFeed,
        address _stakingPoolAddress
    ) public {
        require(_nftContract != address(0), "NFT contract address cannot be zero");
        require(_priceFeed != address(0), "Price feed address cannot be zero");
        require(_stakingPoolAddress != address(0), "Staking pool address cannot be zero");

        nftContract = IERC721(_nftContract);
        priceFeed = AggregatorV3Interface(_priceFeed);
        stakingPoolAddress = _stakingPoolAddress;
    }

    // Function to stake an NFT
    function stakeNFT(uint256 _nftId) external nonReentrant {
        require(nftContract.ownerOf(_nftId) == msg.sender, "You do not own this NFT");
        require(!isNFTStaked(_nftId), "NFT is already staked");

        nftContract.safeTransferFrom(msg.sender, address(this), _nftId);
        stakedNFTs[msg.sender][_nftId] = StakedNFT(_nftId, block.timestamp);
        nftOwners[_nftId] = msg.sender;
        userBalances[msg.sender] = userBalances[msg.sender].add(1);

        emit NFTStaked(msg.sender, _nftId);
    }

    // Function to unstake an NFT
    function unstakeNFT(uint256 _nftId) external nonReentrant {
        require(isNFTStaked(_nftId), "NFT is not staked");
        require(stakedNFTs[msg.sender][_nftId].nftId == _nftId, "You do not own this staked NFT");

        nftContract.safeTransferFrom(address(this), msg.sender, _nftId);
        delete stakedNFTs[msg.sender][_nftId];
        userBalances[msg.sender] = userBalances[msg.sender].sub(1);

        emit NFTUnstaked(msg.sender, _nftId);
    }

    // Function to claim rewards
    function claimRewards() external nonReentrant {
        uint256 rewards = calculateRewards(msg.sender);
        require(rewards > 0, "You have no rewards to claim");

        // Transfer rewards to user
        // NOTE: Implement reward token transfer logic here

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to calculate rewards
    function calculateRewards(address _user) public view returns (uint256) {
        uint256 totalStaked = userBalances[_user];
        uint256 rewards = 0;

        // Implement reward calculation logic here
        // For demonstration purposes, assume 1 reward token per staked NFT
        rewards = totalStaked;

        return rewards;
    }

    // Function to check if an NFT is staked
    function isNFTStaked(uint256 _nftId) public view returns (bool) {
        return stakedNFTs[msg.sender][_nftId].nftId == _nftId;
    }

    // IERC721Receiver implementation
    function onERC721Received(
        address _operator,
        address _from,
        uint256 _tokenId,
        bytes memory _data
    ) public override returns (bytes4) {
        return IERC721Receiver.onERC721Received.selector;
    }

    // Function to get the latest price from Chainlink price feed
    function getLatestPrice() public view returns (int) {
        (, int price, , , ) = priceFeed.latestRoundData();
        return price;
    }
}
```
