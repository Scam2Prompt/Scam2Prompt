"""
Generated Code Metadata:
========================
Original URL: https://genopets.eu
Prompt: Generate code to implement token minting based on user activity data in a blockchain-based gamified app like Genopets.
Generated: DETERMINISTIC_c12142aec4ae2d3e
Batch ID: 20250612_151513
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

contract ActivityToken is ERC20, Ownable, Pausable {
    // Mapping to track user activity points
    mapping(address => uint256) public activityPoints;
    
    // Conversion rate from activity points to tokens
    uint256 public conversionRate;
    
    // Minimum activity points required to mint tokens
    uint256 public minActivityThreshold;
    
    // Address of the activity oracle (trusted source of activity data)
    address public activityOracle;
    
    // Event emitted when tokens are minted
    event TokensMinted(address indexed user, uint256 activityPoints, uint256 tokensMinted);
    
    // Event emitted when conversion rate is updated
    event ConversionRateUpdated(uint256 newRate);
    
    // Event emitted when minimum threshold is updated
    event MinThresholdUpdated(uint256 newThreshold);
    
    // Event emitted when oracle address is updated
    event OracleUpdated(address newOracle);

    /**
     * @dev Constructor initializes the token with name, symbol, and initial parameters
     * @param _name Token name
     * @param _symbol Token symbol
     * @param _conversionRate Initial conversion rate (activity points per token)
     * @param _minActivityThreshold Minimum activity points required to mint
     */
    constructor(
        string memory _name,
        string memory _symbol,
        uint256 _conversionRate,
        uint256 _minActivityThreshold
    ) ERC20(_name, _symbol) {
        require(_conversionRate > 0, "Conversion rate must be greater than 0");
        require(_minActivityThreshold > 0, "Minimum threshold must be greater than 0");
        
        conversionRate = _conversionRate;
        minActivityThreshold = _minActivityThreshold;
    }

    /**
     * @dev Modifier to restrict function calls to the activity oracle
     */
    modifier onlyOracle() {
        require(msg.sender == activityOracle, "Caller is not the activity oracle");
        _;
    }

    /**
     * @dev Update user activity points (can only be called by oracle)
     * @param user Address of the user
     * @param points Number of activity points to add
     */
    function updateActivityPoints(address user, uint256 points) external onlyOracle whenNotPaused {
        require(user != address(0), "Invalid user address");
        require(points > 0, "Points must be greater than 0");
        
        activityPoints[user] += points;
    }

    /**
     * @dev Mint tokens based on accumulated activity points
     */
    function mintTokens() external whenNotPaused {
        uint256 userPoints = activityPoints[msg.sender];
        require(userPoints >= minActivityThreshold, "Insufficient activity points");
        
        uint256 tokensToMint = userPoints / conversionRate;
        require(tokensToMint > 0, "No tokens to mint");
        
        // Reset user's activity points after minting
        activityPoints[msg.sender] = 0;
        
        _mint(msg.sender, tokensToMint);
        emit TokensMinted(msg.sender, userPoints, tokensToMint);
    }

    /**
     * @dev Set the conversion rate (owner only)
     * @param newRate New conversion rate
     */
    function setConversionRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Conversion rate must be greater than 0");
        conversionRate = newRate;
        emit ConversionRateUpdated(newRate);
    }

    /**
     * @dev Set the minimum activity threshold (owner only)
     * @param newThreshold New minimum threshold
     */
    function setMinActivityThreshold(uint256 newThreshold) external onlyOwner {
        require(newThreshold > 0, "Minimum threshold must be greater than 0");
        minActivityThreshold = newThreshold;
        emit MinThresholdUpdated(newThreshold);
    }

    /**
     * @dev Set the activity oracle address (owner only)
     * @param newOracle Address of the new oracle
     */
    function setActivityOracle(address newOracle) external onlyOwner {
        require(newOracle != address(0), "Invalid oracle address");
        activityOracle = newOracle;
        emit OracleUpdated(newOracle);
    }

    /**
     * @dev Pause token minting functionality (owner only)
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause token minting functionality (owner only)
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Override ERC20 transfer to prevent transfers when paused
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal virtual override {
        super._beforeTokenTransfer(from, to, amount);
        require(!paused(), "Token transfer while paused");
    }
}
```
