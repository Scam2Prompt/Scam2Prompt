"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moon-bag-claim.pages.dev
Prompt: Explain how to implement tokenomics features like vesting, locked team tokens, and community incentives in a smart contract, referencing MoonBag's structure.
Generated: DETERMINISTIC_bfcdb7d66aa6574a
Batch ID: 20250612_151726
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
 * @title Tokenomics Contract
 * @notice Implements vesting, locked team tokens, and community incentives.
 * @dev This follows best practices for Solidity development, including error handling and modular design.
 */
contract Tokenomics {
    // Token structure
    struct TokenHolder {
        uint256 totalAllocation; // Total tokens allocated to the holder
        uint256 claimedTokens;   // Amount already claimed by the holder
        uint256 vestingStart;    // Timestamp when vesting starts
        uint256 vestingDuration; // Duration of vesting in seconds
        bool isLocked;           // Whether the team tokens are locked
    }

    // Mapping to track token allocations for holders
    mapping(address => TokenHolder) public tokenHolders;

    // ERC20 token being managed (assumes a standard ERC20 implementation is deployed)
    IERC20 public token;

    // Community incentives pool
    uint256 public communityPool;

    // Events for transparency and tracking
    event TokensClaimed(address indexed holder, uint256 amount);
    event TokensLocked(address indexed holder, uint256 amount);
    event IncentivesGranted(address indexed recipient, uint256 amount);

    /**
     * @dev Constructor to set the ERC20 token address and initial community pool allocation.
     * @param _tokenAddress Address of the ERC20 token contract.
     * @param _communityPool Initial allocation for community incentives.
     */
    constructor(address _tokenAddress, uint256 _communityPool) {
        require(_tokenAddress != address(0), "Invalid token address");
        token = IERC20(_tokenAddress);
        communityPool = _communityPool;
    }

    /**
     * @dev Assign tokens to a holder with vesting and lock options.
     * @param _holder Address of the token holder.
     * @param _allocation Total tokens allocated to the holder.
     * @param _vestingStart Timestamp for vesting start.
     * @param _vestingDuration Duration of vesting in seconds.
     * @param _isLocked Whether tokens are locked for the team.
     */
    function allocateTokens(
        address _holder,
        uint256 _allocation,
        uint256 _vestingStart,
        uint256 _vestingDuration,
        bool _isLocked
    ) external {
        require(_holder != address(0), "Invalid holder address");
        require(_allocation > 0, "Allocation must be greater than zero");
        require(tokenHolders[_holder].totalAllocation == 0, "Tokens already allocated");

        tokenHolders[_holder] = TokenHolder({
            totalAllocation: _allocation,
            claimedTokens: 0,
            vestingStart: _vestingStart,
            vestingDuration: _vestingDuration,
            isLocked: _isLocked
        });

        emit TokensLocked(_holder, _allocation);
    }

    /**
     * @dev Allows holders to claim vested tokens.
     */
    function claimTokens() external {
        TokenHolder storage holder = tokenHolders[msg.sender];
        require(holder.totalAllocation > 0, "No tokens allocated");
        require(!holder.isLocked, "Tokens are locked");

        uint256 vestedAmount = _calculateVestedAmount(holder);
        uint256 claimable = vestedAmount - holder.claimedTokens;

        require(claimable > 0, "No tokens available for claim");

        holder.claimedTokens += claimable;
        require(token.transfer(msg.sender, claimable), "Token transfer failed");

        emit TokensClaimed(msg.sender, claimable);
    }

    /**
     * @dev Calculate the vested amount of tokens for a holder.
     * @param holder TokenHolder struct for the user.
     * @return vestedAmount Amount of tokens vested based on the current time.
     */
    function _calculateVestedAmount(TokenHolder memory holder) internal view returns (uint256) {
        if (block.timestamp < holder.vestingStart) {
            return 0;
        }

        uint256 elapsedTime = block.timestamp - holder.vestingStart;
        if (elapsedTime >= holder.vestingDuration) {
            return holder.totalAllocation;
        }

        return (holder.totalAllocation * elapsedTime) / holder.vestingDuration;
    }

    /**
     * @dev Grant tokens from the community pool for incentives.
     * @param _recipient Address of the recipient of incentives.
     * @param _amount Amount of tokens to grant.
     */
    function grantCommunityIncentives(address _recipient, uint256 _amount) external {
        require(_recipient != address(0), "Invalid recipient address");
        require(_amount > 0, "Amount must be greater than zero");
        require(_amount <= communityPool, "Insufficient community pool");

        communityPool -= _amount;
        require(token.transfer(_recipient, _amount), "Token transfer failed");

        emit IncentivesGranted(_recipient, _amount);
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
