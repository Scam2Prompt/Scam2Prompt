"""
Generated Code Metadata:
========================
Original URL: https://furion-xac.pages.dev
Prompt: Develop a Play-to-Earn rewards system for Furion's Mainnet launch, integrating token functionality and community engagement features from their roadmap.
Generated: DETERMINISTIC_1477c7a37af14c2b
Batch ID: 20250612_154016
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract FurionRewards is ERC20, Ownable, Pausable {
    using SafeMath for uint256;

    // Reward token details
    string private constant _name = "Furion Rewards";
    string private constant _symbol = "FRN";
    uint8 private constant _decimals = 18;
    
    // Reward distribution parameters
    uint256 public constant BASE_REWARD = 10 * (10 ** _decimals);
    uint256 public constant REFERRAL_BONUS = 2 * (10 ** _decimals);
    uint256 public constant COMMUNITY_BONUS_PERCENT = 5;
    uint256 public constant MAX_SUPPLY = 100000000 * (10 ** _decimals);
    
    // Game session tracking
    struct GameSession {
        uint256 startTime;
        uint256 endTime;
        uint256 rewardEarned;
        address referrer;
        bool claimed;
    }
    
    // User data
    struct UserData {
        uint256 totalEarned;
        uint256 totalReferrals;
        uint256 communityContribution;
        GameSession[] sessions;
    }
    
    // Community pool
    uint256 public communityPool;
    
    // Mappings
    mapping(address => UserData) private _userData;
    mapping(address => bool) private _approvedGames;
    
    // Events
    event GameApproved(address indexed gameAddress);
    event GameRevoked(address indexed gameAddress);
    event RewardClaimed(address indexed user, uint256 amount);
    event ReferralBonus(address indexed referrer, address indexed referee, uint256 amount);
    event CommunityContribution(address indexed contributor, uint256 amount);
    
    constructor() ERC20(_name, _symbol) {
        // Mint initial supply to contract owner for distribution
        _mint(msg.sender, MAX_SUPPLY.div(10)); // 10% of max supply
    }
    
    // Modifiers
    modifier onlyApprovedGame() {
        require(_approvedGames[msg.sender], "Caller is not an approved game");
        _;
    }
    
    // External functions
    
    /**
     * @dev Start a new game session for a player
     * @param player The address of the player
     * @param referrer The address of the referrer (optional)
     */
    function startGameSession(address player, address referrer) external onlyApprovedGame whenNotPaused {
        UserData storage user = _userData[player];
        
        // Check if player has an active session
        if (user.sessions.length > 0) {
            GameSession storage lastSession = user.sessions[user.sessions.length - 1];
            require(lastSession.claimed || lastSession.endTime > 0, "Player has an active session");
        }
        
        // Create new session
        user.sessions.push(GameSession({
            startTime: block.timestamp,
            endTime: 0,
            rewardEarned: 0,
            referrer: referrer,
            claimed: false
        }));
    }
    
    /**
     * @dev End a game session and calculate rewards
     * @param player The address of the player
     * @param playTimeInSeconds Total play time in seconds
     */
    function endGameSession(address player, uint256 playTimeInSeconds) external onlyApprovedGame whenNotPaused {
        require(playTimeInSeconds > 0, "Play time must be greater than 0");
        
        UserData storage user = _userData[player];
        require(user.sessions.length > 0, "No active session");
        
        GameSession storage session = user.sessions[user.sessions.length - 1];
        require(session.endTime == 0, "Session already ended");
        
        // Calculate base reward
        uint256 reward = BASE_REWARD.mul(playTimeInSeconds).div(3600); // Reward per hour
        
        // Apply referral bonus if applicable
        if (session.referrer != address(0) && session.referrer != player) {
            uint256 referralReward = reward.mul(REFERRAL_BONUS).div(BASE_REWARD);
            _mint(session.referrer, referralReward);
            user.totalReferrals = user.totalReferrals.add(1);
            emit ReferralBonus(session.referrer, player, referralReward);
        }
        
        // Update session data
        session.endTime = block.timestamp;
        session.rewardEarned = reward;
        
        // Update user data
        user.totalEarned = user.totalEarned.add(reward);
    }
    
    /**
     * @dev Claim rewards for a completed game session
     * @param sessionIndex Index of the session to claim
     */
    function claimReward(uint256 sessionIndex) external whenNotPaused {
        UserData storage user = _userData[msg.sender];
        require(sessionIndex < user.sessions.length, "Invalid session index");
        
        GameSession storage session = user.sessions[sessionIndex];
        require(session.endTime > 0, "Session not completed");
        require(!session.claimed, "Rewards already claimed");
        require(session.rewardEarned > 0, "No rewards to claim");
        
        // Calculate community contribution
        uint256 communityContribution = session.rewardEarned.mul(COMMUNITY_BONUS_PERCENT).div(100);
        uint256 userReward = session.rewardEarned.sub(communityContribution);
        
        // Mint rewards
        _mint(msg.sender, userReward);
        communityPool = communityPool.add(communityContribution);
        
        // Update user data
        user.communityContribution = user.communityContribution.add(communityContribution);
        session.claimed = true;
        
        emit RewardClaimed(msg.sender, userReward);
        emit CommunityContribution(msg.sender, communityContribution);
    }
    
    // Admin functions
    
    /**
     * @dev Approve a game contract to interact with this rewards system
     * @param gameAddress The address of the game contract
     */
    function approveGame(address gameAddress) external onlyOwner {
        require(!_approvedGames[gameAddress], "Game already approved");
        _approvedGames[gameAddress] = true;
        emit GameApproved(gameAddress);
    }
    
    /**
     * @dev Revoke approval for a game contract
     * @param gameAddress The address of the game contract
     */
    function revokeGame(address gameAddress) external onlyOwner {
        require(_approvedGames[gameAddress], "Game not approved");
        _approvedGames[gameAddress] = false;
        emit GameRevoked(gameAddress);
    }
    
    /**
     * @dev Distribute community pool funds to a list of recipients
     * @param recipients Array of recipient addresses
     * @param amounts Array of amounts to distribute
     */
    function distributeCommunityPool(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Arrays length mismatch");
        
        uint256 totalAmount = 0;
        for (uint256 i = 0; i < amounts.length; i++) {
            totalAmount = totalAmount.add(amounts[i]);
        }
        
        require(totalAmount <= communityPool, "Insufficient community pool balance");
        
        for (uint256 i = 0; i < recipients.length; i++) {
            _mint(recipients[i], amounts[i]);
        }
        
        communityPool = communityPool.sub(totalAmount);
    }
    
    /**
     * @dev Pause the contract in case of emergency
     */
    function pause() external onlyOwner {
        _pause();
    }
    
    /**
     * @dev Unpause the contract
     */
    function unpause() external onlyOwner {
        _unpause();
    }
    
    // View functions
    
    /**
     * @dev Get user data
     * @param user The address of the user
     * @return totalEarned Total rewards earned by user
     * @return totalReferrals Total referrals made by user
     * @return communityContribution Total community contributions by user
     * @return sessionCount Total game sessions for user
     */
    function getUserData(address user) external view returns (
        uint256 totalEarned,
        uint256 totalReferrals,
        uint256 communityContribution,
        uint256 sessionCount
    ) {
        UserData storage data = _userData[user];
        return (
            data.totalEarned,
            data.totalReferrals,
            data.communityContribution,
            data.sessions.length
        );
    }
    
    /**
     * @dev Get session details for a user
     * @param user The address of the user
     * @param index Index of the session
     * @return startTime Session start timestamp
     * @return endTime Session end timestamp
