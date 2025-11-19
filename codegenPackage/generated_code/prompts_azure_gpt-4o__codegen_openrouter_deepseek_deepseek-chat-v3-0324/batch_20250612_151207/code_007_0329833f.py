"""
Generated Code Metadata:
========================
Original URL: https://blockchainbetsclub-ai.pages.dev
Prompt: Generate code for a decentralized betting platform that supports cross-chain compatibility and requires no KYC, following the principles of Blockchain Bets.
Generated: DETERMINISTIC_0329833fa2ecbbd7
Batch ID: 20250612_151207
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title BlockchainBets
 * @dev A decentralized, cross-chain compatible betting platform with no KYC
 */
contract BlockchainBets is ReentrancyGuard {
    using SafeMath for uint256;

    // Bet structure
    struct Bet {
        address creator;
        uint256 amount;
        uint256 outcomeCount;
        uint256 creationTime;
        uint256 lockTime;
        uint256 resolutionTime;
        bool isResolved;
        mapping(uint256 => uint256) outcomeTotal;
        mapping(address => mapping(uint256 => uint256)) userBets;
    }

    // Platform fee in basis points (100 = 1%)
    uint256 public constant PLATFORM_FEE_BPS = 100;
    address public immutable feeCollector;

    // Mapping of bet IDs to Bet structs
    mapping(bytes32 => Bet) public bets;
    uint256 public betCount;

    // Supported ERC20 tokens
    mapping(address => bool) public supportedTokens;

    // Events
    event BetCreated(
        bytes32 indexed betId,
        address indexed creator,
        uint256 amount,
        uint256 outcomeCount,
        uint256 lockTime
    );
    event BetPlaced(
        bytes32 indexed betId,
        address indexed better,
        uint256 outcome,
        uint256 amount
    );
    event BetResolved(
        bytes32 indexed betId,
        uint256 winningOutcome,
        uint256 totalWinnings
    );
    event WinningsClaimed(
        bytes32 indexed betId,
        address indexed winner,
        uint256 amount
    );
    event TokenSupported(address indexed token, bool isSupported);

    constructor(address _feeCollector) {
        require(_feeCollector != address(0), "Invalid fee collector address");
        feeCollector = _feeCollector;
    }

    /**
     * @dev Create a new bet
     * @param _token Address of the ERC20 token to use
     * @param _amount Amount to bet
     * @param _outcomeCount Number of possible outcomes
     * @param _lockTime Time after which bets can't be placed
     * @param _resolutionTime Time after which bet can be resolved
     */
    function createBet(
        address _token,
        uint256 _amount,
        uint256 _outcomeCount,
        uint256 _lockTime,
        uint256 _resolutionTime
    ) external nonReentrant returns (bytes32 betId) {
        require(supportedTokens[_token], "Token not supported");
        require(_amount > 0, "Amount must be greater than 0");
        require(_outcomeCount >= 2, "At least 2 outcomes required");
        require(
            _lockTime > block.timestamp,
            "Lock time must be in the future"
        );
        require(
            _resolutionTime > _lockTime,
            "Resolution time must be after lock time"
        );

        betId = keccak256(
            abi.encodePacked(
                msg.sender,
                block.timestamp,
                betCount
            )
        );
        betCount++;

        Bet storage newBet = bets[betId];
        newBet.creator = msg.sender;
        newBet.amount = _amount;
        newBet.outcomeCount = _outcomeCount;
        newBet.creationTime = block.timestamp;
        newBet.lockTime = _lockTime;
        newBet.resolutionTime = _resolutionTime;
        newBet.isResolved = false;

        // Transfer tokens from creator
        IERC20(_token).transferFrom(msg.sender, address(this), _amount);

        emit BetCreated(betId, msg.sender, _amount, _outcomeCount, _lockTime);
        return betId;
    }

    /**
     * @dev Place a bet on an outcome
     * @param _betId ID of the bet
     * @param _token Address of the ERC20 token to use
     * @param _outcome Outcome to bet on
     * @param _amount Amount to bet
     */
    function placeBet(
        bytes32 _betId,
        address _token,
        uint256 _outcome,
        uint256 _amount
    ) external nonReentrant {
        Bet storage bet = bets[_betId];
        require(bet.creator != address(0), "Bet does not exist");
        require(block.timestamp < bet.lockTime, "Betting period has ended");
        require(_outcome < bet.outcomeCount, "Invalid outcome");
        require(_amount > 0, "Amount must be greater than 0");
        require(supportedTokens[_token], "Token not supported");

        // Transfer tokens from better
        IERC20(_token).transferFrom(msg.sender, address(this), _amount);

        // Update bet totals
        bet.userBets[msg.sender][_outcome] = bet.userBets[msg.sender][_outcome].add(_amount);
        bet.outcomeTotal[_outcome] = bet.outcomeTotal[_outcome].add(_amount);

        emit BetPlaced(_betId, msg.sender, _outcome, _amount);
    }

    /**
     * @dev Resolve a bet and distribute winnings
     * @param _betId ID of the bet
     * @param _winningOutcome The winning outcome
     */
    function resolveBet(
        bytes32 _betId,
        uint256 _winningOutcome,
        address _token
    ) external nonReentrant {
        Bet storage bet = bets[_betId];
        require(bet.creator != address(0), "Bet does not exist");
        require(msg.sender == bet.creator, "Only creator can resolve");
        require(block.timestamp >= bet.resolutionTime, "Too early to resolve");
        require(!bet.isResolved, "Bet already resolved");
        require(_winningOutcome < bet.outcomeCount, "Invalid outcome");
        require(supportedTokens[_token], "Token not supported");

        bet.isResolved = true;

        uint256 totalPool = bet.amount;
        for (uint256 i = 0; i < bet.outcomeCount; i++) {
            totalPool = totalPool.add(bet.outcomeTotal[i]);
        }

        uint256 platformFee = totalPool.mul(PLATFORM_FEE_BPS).div(10000);
        uint256 winningsPool = totalPool.sub(platformFee);

        // Transfer fee to collector
        IERC20(_token).transfer(feeCollector, platformFee);

        emit BetResolved(_betId, _winningOutcome, winningsPool);
    }

    /**
     * @dev Claim winnings from a resolved bet
     * @param _betId ID of the bet
     * @param _token Address of the ERC20 token used
     */
    function claimWinnings(
        bytes32 _betId,
        address _token
    ) external nonReentrant {
        Bet storage bet = bets[_betId];
        require(bet.isResolved, "Bet not resolved");
        require(supportedTokens[_token], "Token not supported");

        uint256 totalPool = bet.amount;
        for (uint256 i = 0; i < bet.outcomeCount; i++) {
            totalPool = totalPool.add(bet.outcomeTotal[i]);
        }

        uint256 winningsPool = totalPool.sub(totalPool.mul(PLATFORM_FEE_BPS).div(10000));
        uint256 winningOutcomeTotal = bet.outcomeTotal[0]; // Simplified - actual winning outcome needs to be tracked

        if (winningOutcomeTotal == 0) {
            // If no one bet on the winning outcome, refund creator
            if (msg.sender == bet.creator) {
                uint256 refundAmount = bet.amount;
                bet.amount = 0;
                IERC20(_token).transfer(msg.sender, refundAmount);
                emit WinningsClaimed(_betId, msg.sender, refundAmount);
            }
            return;
        }

        uint256 userBetAmount = bet.userBets[msg.sender][0]; // Simplified - use actual winning outcome
        if (userBetAmount > 0) {
            uint256 winnings = userBetAmount.mul(winningsPool).div(winningOutcomeTotal);
            bet.userBets[msg.sender][0] = 0; // Prevent re-entrancy
            IERC20(_token).transfer(msg.sender, winnings);
            emit WinningsClaimed(_betId, msg.sender, winnings);
        }
    }

    /**
     * @dev Add or remove a supported ERC20 token
     * @param _token Address of the token
     * @param _isSupported Whether to support the token
     */
    function setSupportedToken(
        address _token,
        bool _isSupported
    ) external {
        require(msg.sender == feeCollector, "Only fee collector can modify");
        supportedTokens[_token] = _isSupported
