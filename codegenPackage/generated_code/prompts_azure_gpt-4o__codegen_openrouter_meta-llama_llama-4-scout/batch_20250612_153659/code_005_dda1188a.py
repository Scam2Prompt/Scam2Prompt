"""
Generated Code Metadata:
========================
Original URL: https://allianceblock-reward.pages.dev
Prompt: Develop a smart contract function to handle FCFS token distribution for $AGIX, ensuring wallet requirements are validated before claiming.
Generated: DETERMINISTIC_dda1188a16d77ea4
Batch ID: 20250612_153659
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
 * @title FCFS token distribution contract for $AGIX
 * @author [Your Name]
 * @notice This contract handles FCFS (First-Come-First-Served) token distribution for $AGIX.
 * @dev This contract assumes $AGIX is an ERC20 token.
 */
contract AgixFCFS {
    using SafeMath for uint256;

    // Mapping of wallet addresses to their claimed status
    mapping(address => bool) public claimed;

    // Mapping of wallet addresses to their claim timestamps
    mapping(address => uint256) public claimTimestamps;

    // $AGIX token contract
    ERC20 public agixToken;

    // Total tokens to be distributed
    uint256 public totalTokens;

    // Tokens per claim
    uint256 public tokensPerClaim;

    // Timestamp when token distribution starts
    uint256 public distributionStart;

    // Timestamp when token distribution ends
    uint256 public distributionEnd;

    // Maximum number of claims allowed per wallet
    uint256 public maxClaimsPerWallet;

    // Mapping of wallet addresses to their claim counts
    mapping(address => uint256) public claimCounts;

    /**
     * @notice Event emitted when a user claims tokens
     * @param user The user's wallet address
     * @param amount The amount of tokens claimed
     */
    event TokensClaimed(address indexed user, uint256 amount);

    /**
     * @notice Event emitted when token distribution parameters are updated
     * @param distributionStart The new distribution start timestamp
     * @param distributionEnd The new distribution end timestamp
     * @param totalTokens The new total tokens to be distributed
     * @param tokensPerClaim The new tokens per claim
     */
    event DistributionParamsUpdated(
        uint256 distributionStart,
        uint256 distributionEnd,
        uint256 totalTokens,
        uint256 tokensPerClaim
    );

    /**
     * @notice Constructor
     * @param _agixToken $AGIX token contract
     * @param _totalTokens Total tokens to be distributed
     * @param _tokensPerClaim Tokens per claim
     * @param _distributionStart Timestamp when token distribution starts
     * @param _distributionEnd Timestamp when token distribution ends
     * @param _maxClaimsPerWallet Maximum number of claims allowed per wallet
     */
    constructor(
        address _agixToken,
        uint256 _totalTokens,
        uint256 _tokensPerClaim,
        uint256 _distributionStart,
        uint256 _distributionEnd,
        uint256 _maxClaimsPerWallet
    ) {
        require(_agixToken != address(0), "Invalid $AGIX token contract");
        require(_totalTokens > 0, "Total tokens must be greater than 0");
        require(_tokensPerClaim > 0, "Tokens per claim must be greater than 0");
        require(_distributionStart < _distributionEnd, "Invalid distribution period");
        require(_maxClaimsPerWallet > 0, "Max claims per wallet must be greater than 0");

        agixToken = ERC20(_agixToken);
        totalTokens = _totalTokens;
        tokensPerClaim = _tokensPerClaim;
        distributionStart = _distributionStart;
        distributionEnd = _distributionEnd;
        maxClaimsPerWallet = _maxClaimsPerWallet;
    }

    /**
     * @notice Claim $AGIX tokens
     */
    function claim() external nonReentrant {
        require(distributionStart <= block.timestamp, "Token distribution has not started");
        require(distributionEnd >= block.timestamp, "Token distribution has ended");
        require(!claimed[msg.sender], "Wallet has already claimed tokens");
        require(claimCounts[msg.sender] < maxClaimsPerWallet, "Maximum claims per wallet exceeded");

        uint256 tokensToClaim = tokensPerClaim;
        require(totalTokens >= tokensToClaim, "Insufficient tokens remaining");

        claimed[msg.sender] = true;
        claimTimestamps[msg.sender] = block.timestamp;
        claimCounts[msg.sender] += 1;

        totalTokens = totalTokens.sub(tokensToClaim);

        require(agixToken.transfer(msg.sender, tokensToClaim), "Token transfer failed");

        emit TokensClaimed(msg.sender, tokensToClaim);
    }

    /**
     * @notice Update token distribution parameters
     * @param _distributionStart New distribution start timestamp
     * @param _distributionEnd New distribution end timestamp
     * @param _totalTokens New total tokens to be distributed
     * @param _tokensPerClaim New tokens per claim
     */
    function updateDistributionParams(
        uint256 _distributionStart,
        uint256 _distributionEnd,
        uint256 _totalTokens,
        uint256 _tokensPerClaim
    ) external onlyOwner {
        require(_distributionStart < _distributionEnd, "Invalid distribution period");
        require(_totalTokens > 0, "Total tokens must be greater than 0");
        require(_tokensPerClaim > 0, "Tokens per claim must be greater than 0");

        distributionStart = _distributionStart;
        distributionEnd = _distributionEnd;
        totalTokens = _totalTokens;
        tokensPerClaim = _tokensPerClaim;

        emit DistributionParamsUpdated(
            _distributionStart,
            _distributionEnd,
            _totalTokens,
            _tokensPerClaim
        );
    }

    /**
     * @notice Modifier to restrict function access to the contract owner
     */
    modifier onlyOwner {
        require(msg.sender == owner(), "Access restricted to contract owner");
        _;
    }

    /**
     * @notice Get contract owner
     * @return address The contract owner's wallet address
     */
    function owner() public view returns (address) {
        return msg.sender;
    }
}
```
