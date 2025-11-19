"""
Generated Code Metadata:
========================
Original URL: https://blockchainbets-en.pages.dev
Prompt: Write a smart contract in Solidity for a decentralized betting platform that incorporates token staking functionality, similar to the $BCB staking system described on Blockchain Bets.
Generated: DETERMINISTIC_7cfc38d1f64cdce7
Batch ID: 20250612_153420
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title BettingPlatform
 * @author [Your Name]
 * @notice Decentralized betting platform with token staking functionality
 */
contract BettingPlatform is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of users to their staking information
    mapping(address => Staker) public stakers;

    // Mapping of bets to their information
    mapping(uint256 => Bet) public bets;

    // Token contract instance
    ERC20 public token;

    // Total staked tokens
    uint256 public totalStaked;

    // Bet counter
    uint256 public betCounter;

    // Platform fee (in percentage)
    uint256 public platformFee;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event BetPlaced(uint256 indexed betId, address indexed user, uint256 amount, bool outcome);
    event BetSettled(uint256 indexed betId, bool outcome);

    // Structs
    struct Staker {
        uint256 stakedAmount;
        uint256 rewards;
    }

    struct Bet {
        address user;
        uint256 amount;
        bool outcome; // true for win, false for loss
        bool settled;
    }

    /**
     * @param _token Token contract address
     * @param _platformFee Platform fee (in percentage)
     */
    constructor(ERC20 _token, uint256 _platformFee) {
        token = _token;
        platformFee = _platformFee;
    }

    /**
     * @notice Stake tokens
     * @param _amount Amount to stake
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Invalid stake amount");
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        stakers[msg.sender].stakedAmount = stakers[msg.sender].stakedAmount.add(_amount);
        totalStaked = totalStaked.add(_amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @notice Unstake tokens
     * @param _amount Amount to unstake
     */
    function unstake(uint256 _amount) external {
        require(_amount > 0, "Invalid unstake amount");
        require(stakers[msg.sender].stakedAmount >= _amount, "Insufficient staked amount");

        stakers[msg.sender].stakedAmount = stakers[msg.sender].stakedAmount.sub(_amount);
        totalStaked = totalStaked.sub(_amount);

        require(token.transfer(msg.sender, _amount), "Token transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @notice Place a bet
     * @param _amount Bet amount
     * @param _outcome Bet outcome (true for win, false for loss)
     */
    function placeBet(uint256 _amount, bool _outcome) external {
        require(_amount > 0, "Invalid bet amount");
        require(stakers[msg.sender].stakedAmount >= _amount, "Insufficient staked amount");

        betCounter++;
        bets[betCounter] = Bet(msg.sender, _amount, _outcome, false);

        stakers[msg.sender].stakedAmount = stakers[msg.sender].stakedAmount.sub(_amount);

        emit BetPlaced(betCounter, msg.sender, _amount, _outcome);
    }

    /**
     * @notice Settle a bet
     * @param _betId Bet ID
     * @param _outcome Actual outcome (true for win, false for loss)
     */
    function settleBet(uint256 _betId, bool _outcome) external {
        require(bets[_betId].user != address(0), "Invalid bet ID");
        require(!bets[_betId].settled, "Bet already settled");

        Bet storage bet = bets[_betId];

        if (_outcome == bet.outcome) {
            // Win
            uint256 winnings = bet.amount.mul(2).sub(bet.amount.mul(platformFee).div(100));
            require(token.transfer(bet.user, winnings), "Token transfer failed");
        } else {
            // Loss
            uint256 platformEarnings = bet.amount.mul(platformFee).div(100);
            // Burn tokens
            token.burn(platformEarnings);
        }

        bet.settled = true;

        emit BetSettled(_betId, _outcome);
    }

    /**
     * @notice Get staker information
     * @param _user User address
     * @return Staker information
     */
    function getStakerInfo(address _user) external view returns (uint256 stakedAmount, uint256 rewards) {
        return (stakers[_user].stakedAmount, stakers[_user].rewards);
    }

    /**
     * @notice Get bet information
     * @param _betId Bet ID
     * @return Bet information
     */
    function getBetInfo(uint256 _betId) external view returns (address user, uint256 amount, bool outcome, bool settled) {
        return (bets[_betId].user, bets[_betId].amount, bets[_betId].outcome, bets[_betId].settled);
    }
}
```
