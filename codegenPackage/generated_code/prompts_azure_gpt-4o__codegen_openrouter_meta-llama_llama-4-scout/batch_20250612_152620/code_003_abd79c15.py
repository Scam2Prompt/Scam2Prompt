"""
Generated Code Metadata:
========================
Original URL: https://pepewifhat.pages.dev
Prompt: Develop a Solidity smart contract snippet to integrate a staking mechanism for PEPE WIF HAT NFTs, allowing holders to earn $PIF and other tokens as rewards.
Generated: DETERMINISTIC_abd79c158810bde0
Batch ID: 20250612_152620
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC721/SafeERC721.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";

/**
 * @title PEPE WIF HAT Staking Contract
 * @author [Your Name]
 * @notice This contract allows PEPE WIF HAT NFT holders to stake their NFTs and earn $PIF and other tokens as rewards.
 */
contract PEPEWIFHATStaking {
    using SafeMath for uint256;
    using SafeERC721 for IERC721;
    using SafeERC20 for IERC20;

    // Mapping of staker address to staking information
    mapping (address => Staker) public stakers;

    // Mapping of NFT ID to staker address
    mapping (uint256 => address) public nftOwners;

    // PEPE WIF HAT NFT contract address
    address public nftContractAddress;

    // $PIF token contract address
    address public pifTokenAddress;

    // Other token contract addresses
    mapping (string => address) public otherTokenAddresses;

    // Reward rates for $PIF and other tokens
    mapping (string => uint256) public rewardRates;

    // Staking duration in seconds
    uint256 public stakingDuration;

    // Total staked NFTs
    uint256 public totalStaked;

    // Event emitted when a staker stakes an NFT
    event Staked(address indexed staker, uint256 indexed nftId);

    // Event emitted when a staker unstakes an NFT
    event Unstaked(address indexed staker, uint256 indexed nftId);

    // Event emitted when a staker claims rewards
    event RewardsClaimed(address indexed staker, uint256 pifRewards, uint256 otherRewards);

    // Struct to represent a staker's information
    struct Staker {
        uint256[] nftIds;
        uint256 lastStakeTime;
        uint256 pifRewards;
        mapping (string => uint256) otherRewards;
    }

    /**
     * @notice Constructor function
     * @param _nftContractAddress PEPE WIF HAT NFT contract address
     * @param _pifTokenAddress $PIF token contract address
     */
    constructor(address _nftContractAddress, address _pifTokenAddress) public {
        nftContractAddress = _nftContractAddress;
        pifTokenAddress = _pifTokenAddress;
        stakingDuration = 30 days; // 30 days
    }

    /**
     * @notice Stake an NFT
     * @param _nftId NFT ID to stake
     */
    function stake(uint256 _nftId) public {
        require(msg.sender == IERC721(nftContractAddress).ownerOf(_nftId), "Only the NFT owner can stake");
        require(nftOwners[_nftId] == address(0), "NFT is already staked");

        IERC721(nftContractAddress).safeTransferFrom(msg.sender, address(this), _nftId);
        nftOwners[_nftId] = msg.sender;

        stakers[msg.sender].nftIds.push(_nftId);
        stakers[msg.sender].lastStakeTime = block.timestamp;

        totalStaked++;

        emit Staked(msg.sender, _nftId);
    }

    /**
     * @notice Unstake an NFT
     * @param _nftId NFT ID to unstake
     */
    function unstake(uint256 _nftId) public {
        require(nftOwners[_nftId] == msg.sender, "Only the staker can unstake");
        require(stakers[msg.sender].lastStakeTime != 0, "Staker has not staked any NFTs");

        IERC721(nftContractAddress).safeTransferFrom(address(this), msg.sender, _nftId);
        nftOwners[_nftId] = address(0);

        // Remove NFT ID from staker's array
        for (uint256 i = 0; i < stakers[msg.sender].nftIds.length; i++) {
            if (stakers[msg.sender].nftIds[i] == _nftId) {
                stakers[msg.sender].nftIds[i] = stakers[msg.sender].nftIds[stakers[msg.sender].nftIds.length - 1];
                stakers[msg.sender].nftIds.pop();
                break;
            }
        }

        totalStaked--;

        emit Unstaked(msg.sender, _nftId);
    }

    /**
     * @notice Claim rewards
     */
    function claimRewards() public {
        require(stakers[msg.sender].lastStakeTime != 0, "Staker has not staked any NFTs");
        require(block.timestamp >= stakers[msg.sender].lastStakeTime.add(stakingDuration), "Staking duration has not ended");

        uint256 pifRewards = calculatePifRewards(msg.sender);
        stakers[msg.sender].pifRewards = pifRewards;

        // Claim $PIF rewards
        IERC20(pifTokenAddress).safeTransfer(msg.sender, pifRewards);

        // Claim other token rewards
        for (string memory tokenName in otherTokenAddresses) {
            uint256 otherRewards = calculateOtherRewards(msg.sender, tokenName);
            stakers[msg.sender].otherRewards[tokenName] = otherRewards;
            IERC20(otherTokenAddresses[tokenName]).safeTransfer(msg.sender, otherRewards);
        }

        stakers[msg.sender].lastStakeTime = block.timestamp;

        emit RewardsClaimed(msg.sender, pifRewards, 0); // todo: calculate total other rewards
    }

    /**
     * @notice Calculate $PIF rewards for a staker
     * @param _staker Staker address
     * @return $PIF rewards
     */
    function calculatePifRewards(address _staker) internal view returns (uint256) {
        // todo: implement reward calculation logic
        return 0;
    }

    /**
     * @notice Calculate other token rewards for a staker
     * @param _staker Staker address
     * @param _tokenName Token name
     * @return Other token rewards
     */
    function calculateOtherRewards(address _staker, string memory _tokenName) internal view returns (uint256) {
        // todo: implement reward calculation logic
        return 0;
    }

    /**
     * @notice Add other token contract address
     * @param _tokenName Token name
     * @param _tokenAddress Token contract address
     */
    function addOtherToken(string memory _tokenName, address _tokenAddress) public {
        require(otherTokenAddresses[_tokenName] == address(0), "Token already added");
        otherTokenAddresses[_tokenName] = _tokenAddress;
    }

    /**
     * @notice Set reward rate for $PIF or other tokens
     * @param _tokenName Token name
     * @param _rewardRate Reward rate
     */
    function setRewardRate(string memory _tokenName, uint256 _rewardRate) public {
        rewardRates[_tokenName] = _rewardRate;
    }
}
```
