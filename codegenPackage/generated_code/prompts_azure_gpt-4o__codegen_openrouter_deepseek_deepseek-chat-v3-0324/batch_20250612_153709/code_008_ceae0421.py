"""
Generated Code Metadata:
========================
Original URL: https://bluwhales.pages.dev
Prompt: Create a decentralized application (dApp) that allows users to claim their wallet profiles and earn tokens for engaging with on-chain messages, inspired by Bluwhale's wallet outreach system.
Generated: DETERMINISTIC_ceae042135d88902
Batch ID: 20250612_153709
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract WalletProfile is Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    
    // Token contract interface
    IERC20 public rewardToken;
    
    // Profile structure
    struct Profile {
        string username;
        string bio;
        uint256 points;
        uint256 lastClaimTimestamp;
        bool exists;
    }
    
    // Message structure
    struct Message {
        address sender;
        string content;
        uint256 timestamp;
        uint256 rewardAmount;
    }
    
    // Mappings
    mapping(address => Profile) public profiles;
    mapping(address => Message[]) public sentMessages;
    mapping(address => Message[]) public receivedMessages;
    mapping(address => mapping(address => bool)) public hasInteracted;
    
    // Counters
    Counters.Counter private _profileCount;
    Counters.Counter private _messageCount;
    
    // Constants
    uint256 public constant CLAIM_COOLDOWN = 1 days;
    uint256 public constant BASE_REWARD = 10 ether; // Assuming 18 decimals
    uint256 public constant INTERACTION_BONUS = 5 ether;
    
    // Events
    event ProfileCreated(address indexed wallet, string username);
    event ProfileUpdated(address indexed wallet, string newBio);
    event MessageSent(address indexed from, address indexed to, string content, uint256 reward);
    event TokensClaimed(address indexed wallet, uint256 amount);
    
    constructor(address _tokenAddress) {
        rewardToken = IERC20(_tokenAddress);
    }
    
    /**
     * @dev Create or update a wallet profile
     * @param _username Desired username
     * @param _bio Profile biography
     */
    function createOrUpdateProfile(string memory _username, string memory _bio) external {
        require(bytes(_username).length > 0, "Username cannot be empty");
        
        if (!profiles[msg.sender].exists) {
            _profileCount.increment();
            profiles[msg.sender] = Profile({
                username: _username,
                bio: _bio,
                points: 0,
                lastClaimTimestamp: 0,
                exists: true
            });
            emit ProfileCreated(msg.sender, _username);
        } else {
            profiles[msg.sender].bio = _bio;
            emit ProfileUpdated(msg.sender, _bio);
        }
    }
    
    /**
     * @dev Send a message to another wallet
     * @param _to Recipient wallet address
     * @param _content Message content
     */
    function sendMessage(address _to, string memory _content) external nonReentrant {
        require(profiles[msg.sender].exists, "Sender must have a profile");
        require(profiles[_to].exists, "Recipient must have a profile");
        require(bytes(_content).length > 0, "Message cannot be empty");
        
        uint256 rewardAmount = BASE_REWARD;
        
        // Check if this is first interaction between these wallets
        if (!hasInteracted[msg.sender][_to]) {
            rewardAmount += INTERACTION_BONUS;
            hasInteracted[msg.sender][_to] = true;
        }
        
        // Create message
        Message memory newMessage = Message({
            sender: msg.sender,
            content: _content,
            timestamp: block.timestamp,
            rewardAmount: rewardAmount
        });
        
        // Add to both sender and recipient
        sentMessages[msg.sender].push(newMessage);
        receivedMessages[_to].push(newMessage);
        _messageCount.increment();
        
        // Update points
        profiles[msg.sender].points += rewardAmount;
        profiles[_to].points += rewardAmount;
        
        emit MessageSent(msg.sender, _to, _content, rewardAmount);
    }
    
    /**
     * @dev Claim earned tokens
     */
    function claimTokens() external nonReentrant {
        require(profiles[msg.sender].exists, "No profile exists");
        require(
            block.timestamp >= profiles[msg.sender].lastClaimTimestamp + CLAIM_COOLDOWN,
            "Claim cooldown not passed"
        );
        
        uint256 claimableAmount = profiles[msg.sender].points;
        require(claimableAmount > 0, "No tokens to claim");
        
        // Reset points and update timestamp
        profiles[msg.sender].points = 0;
        profiles[msg.sender].lastClaimTimestamp = block.timestamp;
        
        // Transfer tokens
        require(
            rewardToken.transfer(msg.sender, claimableAmount),
            "Token transfer failed"
        );
        
        emit TokensClaimed(msg.sender, claimableAmount);
    }
    
    /**
     * @dev Get profile count
     * @return uint256 Total profile count
     */
    function getProfileCount() external view returns (uint256) {
        return _profileCount.current();
    }
    
    /**
     * @dev Get message count
     * @return uint256 Total message count
     */
    function getMessageCount() external view returns (uint256) {
        return _messageCount.current();
    }
    
    /**
     * @dev Get sent messages for a wallet
     * @param _wallet Wallet address
     * @return Message[] Array of sent messages
     */
    function getSentMessages(address _wallet) external view returns (Message[] memory) {
        return sentMessages[_wallet];
    }
    
    /**
     * @dev Get received messages for a wallet
     * @param _wallet Wallet address
     * @return Message[] Array of received messages
     */
    function getReceivedMessages(address _wallet) external view returns (Message[] memory) {
        return receivedMessages[_wallet];
    }
    
    /**
     * @dev Withdraw tokens from contract (owner only)
     * @param _amount Amount to withdraw
     */
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(
            rewardToken.transfer(owner(), _amount),
            "Token transfer failed"
        );
    }
}
```
