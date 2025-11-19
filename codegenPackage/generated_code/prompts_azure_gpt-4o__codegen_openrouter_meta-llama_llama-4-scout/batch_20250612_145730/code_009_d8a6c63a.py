"""
Generated Code Metadata:
========================
Original URL: https://pepearab.pages.dev
Prompt: Generate a Solidity contract to handle the presale process for $PEAB tokens, including wallet connection, token swapping, and staking functionality.
Generated: DETERMINISTIC_d8a6c63a63315603
Batch ID: 20250612_145730
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title PEAB Presale Contract
 * @author [Your Name]
 * @notice This contract handles the presale process for $PEAB tokens.
 */
contract PEABPresale is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user wallet connections
    mapping (address => bool) public connectedWallets;

    // Mapping of user token swaps
    mapping (address => uint256) public swappedTokens;

    // Mapping of user staking information
    mapping (address => StakingInfo) public stakingInfo;

    // Token contract instance
    IERC20 public peabToken;

    // Presale token price
    uint256 public presalePrice;

    // Presale start and end timestamps
    uint256 public presaleStart;
    uint256 public presaleEnd;

    // Staking start timestamp
    uint256 public stakingStart;

    // Staking rewards
    uint256 public stakingRewards;

    // Struct to hold staking information
    struct StakingInfo {
        uint256 stakedAmount;
        uint256 stakingTimestamp;
    }

    /**
     * @notice Constructor function
     * @param _peabToken Address of the $PEAB token contract
     * @param _presalePrice Presale token price
     * @param _presaleStart Presale start timestamp
     * @param _presaleEnd Presale end timestamp
     * @param _stakingStart Staking start timestamp
     * @param _stakingRewards Staking rewards
     */
    constructor(
        address _peabToken,
        uint256 _presalePrice,
        uint256 _presaleStart,
        uint256 _presaleEnd,
        uint256 _stakingStart,
        uint256 _stakingRewards
    ) public {
        peabToken = IERC20(_peabToken);
        presalePrice = _presalePrice;
        presaleStart = _presaleStart;
        presaleEnd = _presaleEnd;
        stakingStart = _stakingStart;
        stakingRewards = _stakingRewards;
    }

    /**
     * @notice Connect wallet to presale
     */
    function connectWallet() public {
        require(!connectedWallets[msg.sender], "Wallet already connected");
        connectedWallets[msg.sender] = true;
    }

    /**
     * @notice Swap tokens for $PEAB
     * @param _amount Amount of tokens to swap
     */
    function swapTokens(uint256 _amount) public nonReentrant {
        require(connectedWallets[msg.sender], "Wallet not connected");
        require(block.timestamp >= presaleStart && block.timestamp <= presaleEnd, "Presale not active");
        require(_amount > 0, "Swap amount must be greater than 0");

        uint256 peabAmount = _amount.mul(presalePrice);
        swappedTokens[msg.sender] = peabAmount;

        // Transfer tokens from user to contract
        IERC20(msg.sender).transferFrom(msg.sender, address(this), _amount);

        // Transfer $PEAB tokens to user
        peabToken.transfer(msg.sender, peabAmount);
    }

    /**
     * @notice Stake $PEAB tokens
     * @param _amount Amount of $PEAB tokens to stake
     */
    function stakeTokens(uint256 _amount) public nonReentrant {
        require(connectedWallets[msg.sender], "Wallet not connected");
        require(block.timestamp >= stakingStart, "Staking not started");
        require(_amount > 0, "Stake amount must be greater than 0");
        require(swappedTokens[msg.sender] >= _amount, "Insufficient swapped tokens");

        stakingInfo[msg.sender].stakedAmount = stakingInfo[msg.sender].stakedAmount.add(_amount);
        stakingInfo[msg.sender].stakingTimestamp = block.timestamp;

        // Transfer $PEAB tokens from user to contract
        peabToken.transferFrom(msg.sender, address(this), _amount);
    }

    /**
     * @notice Claim staking rewards
     */
    function claimRewards() public nonReentrant {
        require(connectedWallets[msg.sender], "Wallet not connected");
        require(stakingInfo[msg.sender].stakedAmount > 0, "No staked tokens");

        uint256 rewards = stakingInfo[msg.sender].stakedAmount.mul(stakingRewards).div(100);
        stakingInfo[msg.sender].stakedAmount = 0;

        // Transfer rewards to user
        peabToken.transfer(msg.sender, rewards);
    }

    /**
     * @notice Emergency withdraw
     */
    function emergencyWithdraw() public nonReentrant {
        require(connectedWallets[msg.sender], "Wallet not connected");

        // Transfer swapped tokens back to user
        uint256 swappedAmount = swappedTokens[msg.sender];
        swappedTokens[msg.sender] = 0;
        peabToken.transfer(msg.sender, swappedAmount);
    }
}
```
