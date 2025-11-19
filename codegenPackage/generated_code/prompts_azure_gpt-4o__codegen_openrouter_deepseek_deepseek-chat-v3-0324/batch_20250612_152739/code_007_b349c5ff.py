"""
Generated Code Metadata:
========================
Original URL: https://sugarkingdomodyssey.web.app
Prompt: Provide an example of a smart contract function to handle token distribution rounds with a fixed total supply, similar to the $10,000,000 $SKO distribution.
Generated: DETERMINISTIC_b349c5ff36743797
Batch ID: 20250612_152739
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

contract TokenDistribution is ERC20, Ownable {
    using SafeMath for uint256;

    // Distribution round structure
    struct DistributionRound {
        string name;
        uint256 startTime;
        uint256 endTime;
        uint256 totalAllocation;
        uint256 claimedAmount;
        uint256 tokensPerEther;
        bool isActive;
    }

    // Total supply of tokens (10,000,000 in this case)
    uint256 public constant TOTAL_SUPPLY = 10_000_000 * 10**18;
    
    // Mapping of distribution rounds
    mapping(uint256 => DistributionRound) public distributionRounds;
    uint256 public currentRoundId;
    
    // Track user claims per round
    mapping(address => mapping(uint256 => uint256)) public userClaims;

    // Events
    event RoundAdded(uint256 roundId, string name, uint256 totalAllocation);
    event RoundUpdated(uint256 roundId);
    event TokensClaimed(address indexed user, uint256 roundId, uint256 amount);

    constructor() ERC20("SKO Token", "SKO") {
        _mint(address(this), TOTAL_SUPPLY);
    }

    /**
     * @dev Add a new distribution round
     * @param name Round name
     * @param startTime Round start timestamp
     * @param endTime Round end timestamp
     * @param totalAllocation Tokens allocated for this round
     * @param tokensPerEther Conversion rate for ETH contributions
     */
    function addDistributionRound(
        string memory name,
        uint256 startTime,
        uint256 endTime,
        uint256 totalAllocation,
        uint256 tokensPerEther
    ) external onlyOwner {
        require(startTime < endTime, "Invalid time range");
        require(totalAllocation > 0, "Allocation must be positive");
        
        currentRoundId++;
        distributionRounds[currentRoundId] = DistributionRound({
            name: name,
            startTime: startTime,
            endTime: endTime,
            totalAllocation: totalAllocation,
            claimedAmount: 0,
            tokensPerEther: tokensPerEther,
            isActive: true
        });

        emit RoundAdded(currentRoundId, name, totalAllocation);
    }

    /**
     * @dev Update an existing distribution round
     * @param roundId ID of the round to update
     * @param startTime New start time (0 to keep current)
     * @param endTime New end time (0 to keep current)
     * @param tokensPerEther New conversion rate (0 to keep current)
     * @param isActive New active status
     */
    function updateDistributionRound(
        uint256 roundId,
        uint256 startTime,
        uint256 endTime,
        uint256 tokensPerEther,
        bool isActive
    ) external onlyOwner {
        require(roundId <= currentRoundId && roundId > 0, "Invalid round ID");
        DistributionRound storage round = distributionRounds[roundId];

        if (startTime > 0) {
            require(startTime < round.endTime, "Start time must be before end time");
            round.startTime = startTime;
        }
        
        if (endTime > 0) {
            require(round.startTime < endTime, "End time must be after start time");
            round.endTime = endTime;
        }
        
        if (tokensPerEther > 0) {
            round.tokensPerEther = tokensPerEther;
        }
        
        round.isActive = isActive;
        
        emit RoundUpdated(roundId);
    }

    /**
     * @dev Claim tokens from active distribution round
     * @param roundId ID of the round to claim from
     * @param ethAmount Amount of ETH contributed
     */
    function claimTokens(uint256 roundId, uint256 ethAmount) external payable {
        require(roundId <= currentRoundId && roundId > 0, "Invalid round ID");
        DistributionRound storage round = distributionRounds[roundId];
        
        require(round.isActive, "Round not active");
        require(block.timestamp >= round.startTime, "Round not started");
        require(block.timestamp <= round.endTime, "Round ended");
        require(msg.value == ethAmount, "ETH amount mismatch");
        
        uint256 tokenAmount = ethAmount.mul(round.tokensPerEther);
        require(tokenAmount > 0, "No tokens to claim");
        
        uint256 remainingAllocation = round.totalAllocation.sub(round.claimedAmount);
        require(tokenAmount <= remainingAllocation, "Exceeds round allocation");
        
        round.claimedAmount = round.claimedAmount.add(tokenAmount);
        userClaims[msg.sender][roundId] = userClaims[msg.sender][roundId].add(tokenAmount);
        
        _transfer(address(this), msg.sender, tokenAmount);
        
        emit TokensClaimed(msg.sender, roundId, tokenAmount);
    }

    /**
     * @dev Withdraw ETH collected during distribution
     */
    function withdrawETH() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Recover any ERC20 tokens accidentally sent to this contract
     * @param tokenAddress Address of the token contract
     * @param tokenAmount Amount of tokens to recover
     */
    function recoverERC20(address tokenAddress, uint256 tokenAmount) external onlyOwner {
        require(tokenAddress != address(this), "Cannot recover distribution tokens");
        IERC20(tokenAddress).transfer(owner(), tokenAmount);
    }
}
```
