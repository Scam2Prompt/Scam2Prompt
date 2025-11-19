"""
Generated Code Metadata:
========================
Original URL: https://dwinity.pages.dev
Prompt: Create a Solidity smart contract template that aligns with Dwinity's requirements for deploying a digital twin and claiming $DWIN tokens.
Generated: DETERMINISTIC_12a4f1c5f4b5a702
Batch ID: 20250612_150130
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title DigitalTwinManager
 * @dev Manages digital twin creation and DWIN token claims
 */
contract DigitalTwinManager is Ownable, ReentrancyGuard {
    IERC20 public dwinToken;
    
    // Digital twin structure
    struct DigitalTwin {
        address owner;
        string metadataURI;
        uint256 creationTime;
        bool isActive;
    }

    // Mapping from twin ID to DigitalTwin
    mapping(uint256 => DigitalTwin) public digitalTwins;
    
    // Mapping to track claimed tokens per address
    mapping(address => uint256) public claimedTokens;
    
    // Reward amount per twin creation
    uint256 public rewardAmount;
    
    // Total twins created
    uint256 public totalTwins;
    
    // Events
    event TwinCreated(uint256 indexed twinId, address indexed owner, string metadataURI);
    event TokensClaimed(address indexed recipient, uint256 amount);
    event RewardAmountUpdated(uint256 newAmount);
    
    /**
     * @dev Constructor
     * @param _dwinTokenAddress Address of DWIN ERC20 token
     * @param _initialRewardAmount Initial reward amount for twin creation
     */
    constructor(address _dwinTokenAddress, uint256 _initialRewardAmount) {
        require(_dwinTokenAddress != address(0), "Invalid token address");
        dwinToken = IERC20(_dwinTokenAddress);
        rewardAmount = _initialRewardAmount;
    }
    
    /**
     * @dev Create a new digital twin
     * @param metadataURI URI pointing to twin metadata
     * @return twinId The ID of the newly created twin
     */
    function createTwin(string memory metadataURI) external returns (uint256 twinId) {
        require(bytes(metadataURI).length > 0, "Metadata URI cannot be empty");
        
        twinId = totalTwins++;
        digitalTwins[twinId] = DigitalTwin({
            owner: msg.sender,
            metadataURI: metadataURI,
            creationTime: block.timestamp,
            isActive: true
        });
        
        emit TwinCreated(twinId, msg.sender, metadataURI);
        return twinId;
    }
    
    /**
     * @dev Claim DWIN tokens for created twins
     */
    function claimTokens() external nonReentrant {
        uint256 claimableAmount = getClaimableAmount(msg.sender);
        require(claimableAmount > 0, "No tokens to claim");
        
        claimedTokens[msg.sender] += claimableAmount;
        
        require(
            dwinToken.transfer(msg.sender, claimableAmount),
            "Token transfer failed"
        );
        
        emit TokensClaimed(msg.sender, claimableAmount);
    }
    
    /**
     * @dev Get claimable token amount for an address
     * @param user Address to check
     * @return amount Claimable token amount
     */
    function getClaimableAmount(address user) public view returns (uint256 amount) {
        uint256 twinCount;
        for (uint256 i = 0; i < totalTwins; i++) {
            if (digitalTwins[i].owner == user && digitalTwins[i].isActive) {
                twinCount++;
            }
        }
        return (twinCount * rewardAmount) - claimedTokens[user];
    }
    
    /**
     * @dev Update reward amount (owner only)
     * @param newAmount New reward amount per twin
     */
    function setRewardAmount(uint256 newAmount) external onlyOwner {
        require(newAmount > 0, "Amount must be positive");
        rewardAmount = newAmount;
        emit RewardAmountUpdated(newAmount);
    }
    
    /**
     * @dev Withdraw remaining DWIN tokens (owner only)
     * @param amount Amount to withdraw
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(
            dwinToken.transfer(owner(), amount),
            "Token transfer failed"
        );
    }
    
    /**
     * @dev Toggle twin active status (owner only)
     * @param twinId ID of the twin to toggle
     */
    function toggleTwinStatus(uint256 twinId) external onlyOwner {
        require(twinId < totalTwins, "Invalid twin ID");
        digitalTwins[twinId].isActive = !digitalTwins[twinId].isActive;
    }
}
```
