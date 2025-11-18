"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-neiroeth.pages.dev
Prompt: Write a Solidity contract that allows users to claim Neiro tokens during specific time windows, such as the New Moon, with restrictions on claim amounts per wallet.
Generated: DETERMINISTIC_51fab8951ea55b92
Batch ID: 20250612_151343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title NeiroTokenClaimer
 * @dev Allows users to claim Neiro tokens during specific time windows (e.g., New Moon period) with restrictions on claim amounts per wallet.
 */
contract NeiroTokenClaimer {
    // Address of the Neiro token contract
    address public tokenAddress;

    // Mapping to track claimed amounts for each wallet
    mapping(address => uint256) public claimedAmounts;

    // Maximum claimable amount per wallet
    uint256 public maxClaimAmount;

    // Claim time window (start and end timestamps)
    uint256 public claimStartTime;
    uint256 public claimEndTime;

    // Event emitted when a claim is made
    event TokensClaimed(address indexed user, uint256 amount);

    // Modifier to ensure the function is called during the claim window
    modifier onlyDuringClaimWindow() {
        require(
            block.timestamp >= claimStartTime && block.timestamp <= claimEndTime,
            "Claim period is not active"
        );
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _tokenAddress Address of the Neiro token contract.
     * @param _maxClaimAmount Maximum claimable amount per wallet.
     * @param _claimStartTime Start timestamp of the claim period.
     * @param _claimEndTime End timestamp of the claim period.
     */
    constructor(
        address _tokenAddress,
        uint256 _maxClaimAmount,
        uint256 _claimStartTime,
        uint256 _claimEndTime
    ) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_claimStartTime < _claimEndTime, "Invalid claim period");

        tokenAddress = _tokenAddress;
        maxClaimAmount = _maxClaimAmount;
        claimStartTime = _claimStartTime;
        claimEndTime = _claimEndTime;
    }

    /**
     * @dev Allows users to claim Neiro tokens.
     * @param _amount Amount of tokens to claim.
     */
    function claimTokens(uint256 _amount) external onlyDuringClaimWindow {
        require(_amount > 0, "Claim amount must be greater than zero");
        require(
            claimedAmounts[msg.sender] + _amount <= maxClaimAmount,
            "Claim amount exceeds the maximum limit"
        );

        // Update the claimed amount for the caller
        claimedAmounts[msg.sender] += _amount;

        // Transfer tokens to the caller
        bool success = IERC20(tokenAddress).transfer(msg.sender, _amount);
        require(success, "Token transfer failed");

        emit TokensClaimed(msg.sender, _amount);
    }

    /**
     * @dev Interface for the ERC20 token contract.
     */
    interface IERC20 {
        function transfer(address recipient, uint256 amount)
            external
            returns (bool);
    }
}
```
