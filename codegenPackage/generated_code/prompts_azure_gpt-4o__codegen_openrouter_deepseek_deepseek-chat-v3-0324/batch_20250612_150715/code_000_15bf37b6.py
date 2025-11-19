"""
Generated Code Metadata:
========================
Original URL: https://moxie.social
Prompt: Write a smart contract using the Moxie Protocol to create a Fan Token for a Farcaster channel, including programmatic rewards for followers' actions.
Generated: DETERMINISTIC_15bf37b6c864aa17
Batch ID: 20250612_150715
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

interface IMoxieProtocol {
    function registerToken(address tokenAddress, string memory tokenName) external;
}

contract FanToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Moxie Protocol address
    address public moxieProtocolAddress;
    
    // Channel owner address (Farcaster channel)
    address public channelOwner;
    
    // Reward parameters
    uint256 public constant BASE_REWARD = 10 * 10 ** 18; // 10 tokens
    uint256 public constant LIKE_REWARD = 5 * 10 ** 18;  // 5 tokens
    uint256 public constant RECAST_REWARD = 7 * 10 ** 18; // 7 tokens
    uint256 public constant COMMENT_REWARD = 3 * 10 ** 18; // 3 tokens
    
    // Mapping to track claimed rewards per action per user
    mapping(address => mapping(bytes32 => bool)) public claimedRewards;
    
    // Events
    event RewardClaimed(address indexed user, bytes32 actionId, uint256 amount);
    event TokensMinted(address indexed to, uint256 amount);
    event TokensBurned(address indexed from, uint256 amount);
    
    constructor(
        string memory _name,
        string memory _symbol,
        address _moxieProtocolAddress,
        address _channelOwner,
        uint256 _initialSupply
    ) ERC20(_name, _symbol) {
        require(_moxieProtocolAddress != address(0), "Invalid Moxie Protocol address");
        require(_channelOwner != address(0), "Invalid channel owner address");
        
        moxieProtocolAddress = _moxieProtocolAddress;
        channelOwner = _channelOwner;
        
        // Mint initial supply to channel owner
        _mint(_channelOwner, _initialSupply);
        
        // Register token with Moxie Protocol
        IMoxieProtocol(moxieProtocolAddress).registerToken(address(this), _name);
    }
    
    /**
     * @dev Claim reward for a specific action
     * @param actionId Unique identifier for the action (e.g., cast hash)
     * @param actionType Type of action (0: follow, 1: like, 2: recast, 3: comment)
     */
    function claimReward(bytes32 actionId, uint8 actionType) external {
        require(!claimedRewards[msg.sender][actionId], "Reward already claimed");
        
        uint256 rewardAmount;
        
        if (actionType == 0) {
            rewardAmount = BASE_REWARD;
        } else if (actionType == 1) {
            rewardAmount = LIKE_REWARD;
        } else if (actionType == 2) {
            rewardAmount = RECAST_REWARD;
        } else if (actionType == 3) {
            rewardAmount = COMMENT_REWARD;
        } else {
            revert("Invalid action type");
        }
        
        claimedRewards[msg.sender][actionId] = true;
        _mint(msg.sender, rewardAmount);
        
        emit RewardClaimed(msg.sender, actionId, rewardAmount);
    }
    
    /**
     * @dev Mint new tokens (only owner)
     * @param to Address to mint tokens to
     * @param amount Amount to mint
     */
    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
        emit TokensMinted(to, amount);
    }
    
    /**
     * @dev Burn tokens (only owner)
     * @param from Address to burn tokens from
     * @param amount Amount to burn
     */
    function burn(address from, uint256 amount) external onlyOwner {
        _burn(from, amount);
        emit TokensBurned(from, amount);
    }
    
    /**
     * @dev Update Moxie Protocol address (only owner)
     * @param newAddress New Moxie Protocol address
     */
    function updateMoxieProtocolAddress(address newAddress) external onlyOwner {
        require(newAddress != address(0), "Invalid address");
        moxieProtocolAddress = newAddress;
    }
    
    /**
     * @dev Transfer ownership of the channel (only owner)
     * @param newOwner New channel owner address
     */
    function transferChannelOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid address");
        channelOwner = newOwner;
    }
}
```
