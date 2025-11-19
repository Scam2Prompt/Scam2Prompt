"""
Generated Code Metadata:
========================
Original URL: https://satoshivmsquad.army
Prompt: Create a smart contract in Solidity for staking tokens and distributing airdrops, inspired by the SatoshiVM Squad staking model.
Generated: DETERMINISTIC_72e24defdb3dad2e
Batch ID: 20250612_152526
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title SatoshiVM Squad Staking Contract
 * @author [Your Name]
 * @notice This contract allows users to stake tokens and distribute airdrops.
 */
contract SatoshiVMStaking is ReentrancyGuard {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of user staking information
    mapping(address => UserInfo) public userInfo;

    // Mapping of airdrop information
    mapping(uint256 => AirdropInfo) public airdropInfo;

    // Token being staked
    IERC20 public stakingToken;

    // Total staked tokens
    uint256 public totalStaked;

    // Airdrop ID counter
    uint256 public airdropIdCounter;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when airdrop is created
    event AirdropCreated(uint256 indexed airdropId, uint256 amount);

    // Event emitted when airdrop is claimed
    event AirdropClaimed(address indexed user, uint256 indexed airdropId, uint256 amount);

    // Struct to store user staking information
    struct UserInfo {
        uint256 stakedAmount;
        mapping(uint256 => bool) claimedAirdrops;
    }

    // Struct to store airdrop information
    struct AirdropInfo {
        uint256 amount;
        uint256 distributionEnd;
    }

    /**
     * @param _stakingToken Address of the token being staked
     */
    constructor(IERC20 _stakingToken) public {
        require(address(_stakingToken) != address(0), "Staking token address cannot be zero");
        stakingToken = _stakingToken;
    }

    /**
     * @notice Stake tokens
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(stakingToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        userInfo[msg.sender].stakedAmount = userInfo[msg.sender].stakedAmount.add(_amount);
        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake tokens
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Unstake amount must be greater than zero");
        require(userInfo[msg.sender].stakedAmount >= _amount, "Insufficient staked amount");

        userInfo[msg.sender].stakedAmount = userInfo[msg.sender].stakedAmount.sub(_amount);
        totalStaked = totalStaked.sub(_amount);

        require(stakingToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Create airdrop
     * @param _amount Airdrop amount
     * @param _distributionEnd Airdrop distribution end timestamp
     */
    function createAirdrop(uint256 _amount, uint256 _distributionEnd) external {
        require(_amount > 0, "Airdrop amount must be greater than zero");
        require(_distributionEnd > block.timestamp, "Distribution end timestamp must be in the future");

        airdropIdCounter = airdropIdCounter.add(1);
        airdropInfo[airdropIdCounter] = AirdropInfo(_amount, _distributionEnd);

        emit AirdropCreated(airdropIdCounter, _amount);
    }

    /**
     * @notice Claim airdrop
     * @param _airdropId Airdrop ID
     */
    function claimAirdrop(uint256 _airdropId) external nonReentrant {
        require(airdropInfo[_airdropId].amount > 0, "Airdrop does not exist");
        require(airdropInfo[_airdropId].distributionEnd <= block.timestamp, "Airdrop distribution has not ended");
        require(!userInfo[msg.sender].claimedAirdrops[_airdropId], "Airdrop already claimed");

        userInfo[msg.sender].claimedAirdrops[_airdropId] = true;

        require(stakingToken.transfer(msg.sender, airdropInfo[_airdropId].amount), "Token transfer failed");

        emit AirdropClaimed(msg.sender, _airdropId, airdropInfo[_airdropId].amount);
    }

    /**
     * @notice Get user staking information
     * @param _user User address
     * @return User staking information
     */
    function getUserInfo(address _user) external view returns (uint256) {
        return userInfo[_user].stakedAmount;
    }

    /**
     * @notice Get airdrop information
     * @param _airdropId Airdrop ID
     * @return Airdrop information
     */
    function getAirdropInfo(uint256 _airdropId) external view returns (uint256, uint256) {
        return (airdropInfo[_airdropId].amount, airdropInfo[_airdropId].distributionEnd);
    }
}
```
