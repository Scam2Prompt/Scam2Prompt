"""
Generated Code Metadata:
========================
Original URL: https://bitcoinminetrix-en.web.app
Prompt: Generate Solidity code for a smart contract that implements the "Stake-to-Mine" mechanism, where users stake BTCMTX tokens to earn non-transferable mining credits that can be burned for Bitcoin cloud mining power.
Generated: DETERMINISTIC_1c186e1408c93e4e
Batch ID: 20250612_151648
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
 * @title StakeToMine contract
 * @author [Your Name]
 * @notice This contract implements the "Stake-to-Mine" mechanism, 
 *          where users stake BTCMTX tokens to earn non-transferable mining credits 
 *          that can be burned for Bitcoin cloud mining power.
 */
contract StakeToMine is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking information
    mapping (address => UserStakingInfo) public userStakingInfos;

    // Mapping of mining credit balances
    mapping (address => uint256) public miningCreditBalances;

    // BTCMTX token contract
    IERC20 public btcmtxToken;

    // Mining credit price (in BTCMTX tokens)
    uint256 public miningCreditPrice;

    // Total staked tokens
    uint256 public totalStakedTokens;

    // Event emitted when user stakes tokens
    event Staked(address indexed user, uint256 amount);

    // Event emitted when user unstakes tokens
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when user earns mining credits
    event MiningCreditsEarned(address indexed user, uint256 amount);

    // Event emitted when user burns mining credits
    event MiningCreditsBurned(address indexed user, uint256 amount);

    /**
     * @dev Struct to store user staking information
     */
    struct UserStakingInfo {
        uint256 stakedTokens; // Tokens staked by user
        uint256 earnedMiningCredits; // Mining credits earned by user
    }

    /**
     * @dev Constructor
     * @param _btcmtxTokenAddress Address of the BTCMTX token contract
     * @param _miningCreditPrice Price of mining credits in BTCMTX tokens
     */
    constructor(address _btcmtxTokenAddress, uint256 _miningCreditPrice) public {
        require(_btcmtxTokenAddress != address(0), "Invalid token address");
        require(_miningCreditPrice > 0, "Invalid mining credit price");

        btcmtxToken = IERC20(_btcmtxTokenAddress);
        miningCreditPrice = _miningCreditPrice;
    }

    /**
     * @dev Stake BTCMTX tokens to earn mining credits
     * @param _amount Amount of tokens to stake
     */
    function stake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Invalid stake amount");
        require(btcmtxToken.balanceOf(msg.sender) >= _amount, "Insufficient token balance");
        require(btcmtxToken.allowance(msg.sender, address(this)) >= _amount, "Token allowance not set");

        // Transfer tokens from user to contract
        btcmtxToken.transferFrom(msg.sender, address(this), _amount);

        // Update user staking information
        userStakingInfos[msg.sender].stakedTokens = userStakingInfos[msg.sender].stakedTokens.add(_amount);
        totalStakedTokens = totalStakedTokens.add(_amount);

        // Emit event
        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake BTCMTX tokens
     * @param _amount Amount of tokens to unstake
     */
    function unstake(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Invalid unstake amount");
        require(userStakingInfos[msg.sender].stakedTokens >= _amount, "Insufficient staked tokens");

        // Update user staking information
        userStakingInfos[msg.sender].stakedTokens = userStakingInfos[msg.sender].stakedTokens.sub(_amount);
        totalStakedTokens = totalStakedTokens.sub(_amount);

        // Transfer tokens from contract to user
        btcmtxToken.transfer(msg.sender, _amount);

        // Emit event
        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Earn mining credits by staking tokens
     */
    function earnMiningCredits() external nonReentrant {
        require(userStakingInfos[msg.sender].stakedTokens > 0, "No staked tokens");

        // Calculate earned mining credits
        uint256 earnedMiningCredits = userStakingInfos[msg.sender].stakedTokens.div(miningCreditPrice);

        // Update user staking information
        userStakingInfos[msg.sender].earnedMiningCredits = userStakingInfos[msg.sender].earnedMiningCredits.add(earnedMiningCredits);
        miningCreditBalances[msg.sender] = miningCreditBalances[msg.sender].add(earnedMiningCredits);

        // Emit event
        emit MiningCreditsEarned(msg.sender, earnedMiningCredits);
    }

    /**
     * @dev Burn mining credits for Bitcoin cloud mining power
     * @param _amount Amount of mining credits to burn
     */
    function burnMiningCredits(uint256 _amount) external nonReentrant {
        require(_amount > 0, "Invalid burn amount");
        require(miningCreditBalances[msg.sender] >= _amount, "Insufficient mining credits");

        // Update mining credit balance
        miningCreditBalances[msg.sender] = miningCreditBalances[msg.sender].sub(_amount);

        // Emit event
        emit MiningCreditsBurned(msg.sender, _amount);
    }
}
```
