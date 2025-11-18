"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://token-pushdstore.pages.dev
Prompt: Write a Solidity contract to lock team tokens for 700 days and liquidity for 20 years, ensuring security and preventing rug pulls as outlined in Pushd's roadmap.
Generated: DETERMINISTIC_822d4137d7954aab
Batch ID: 20250612_150228
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
 * @title TokenLockContract
 * @dev A contract to lock team tokens for 700 days and liquidity for 20 years to ensure security.
 */
contract TokenLockContract {
    // The address of the token
    address public immutable tokenAddress;

    // Lock durations
    uint256 public constant TEAM_LOCK_DURATION = 700 days;
    uint256 public constant LIQUIDITY_LOCK_DURATION = 20 years;

    // Lock timestamps
    uint256 public immutable teamUnlockTime;
    uint256 public immutable liquidityUnlockTime;

    // The owner of the contract
    address public immutable owner;

    // Events
    event TokensLocked(address indexed sender, uint256 amount, string lockType);
    event TokensWithdrawn(address indexed recipient, uint256 amount, string lockType);

    /**
     * @dev Constructor sets the token address and initializes lock durations.
     * @param _tokenAddress The address of the token to be locked.
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Token address cannot be zero");
        tokenAddress = _tokenAddress;
        owner = msg.sender;

        // Set unlock timestamps
        teamUnlockTime = block.timestamp + TEAM_LOCK_DURATION;
        liquidityUnlockTime = block.timestamp + LIQUIDITY_LOCK_DURATION;
    }

    /**
     * @dev Modifier to restrict access to the contract's owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Modifier to ensure the tokens can only be withdrawn after the lock period.
     * @param lockType The type of lock ("team" or "liquidity").
     */
    modifier afterLockPeriod(string memory lockType) {
        if (keccak256(abi.encodePacked(lockType)) == keccak256(abi.encodePacked("team"))) {
            require(block.timestamp >= teamUnlockTime, "Team tokens are still locked");
        } else if (keccak256(abi.encodePacked(lockType)) == keccak256(abi.encodePacked("liquidity"))) {
            require(block.timestamp >= liquidityUnlockTime, "Liquidity tokens are still locked");
        } else {
            revert("Invalid lock type");
        }
        _;
    }

    /**
     * @dev Lock tokens into the contract.
     * @param amount The amount of tokens to be locked.
     * @param lockType The type of lock ("team" or "liquidity").
     */
    function lockTokens(uint256 amount, string memory lockType) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");

        if (keccak256(abi.encodePacked(lockType)) == keccak256(abi.encodePacked("team"))) {
            require(block.timestamp < teamUnlockTime, "Team lock period has ended");
        } else if (keccak256(abi.encodePacked(lockType)) == keccak256(abi.encodePacked("liquidity"))) {
            require(block.timestamp < liquidityUnlockTime, "Liquidity lock period has ended");
        } else {
            revert("Invalid lock type");
        }

        // Transfer tokens from the owner to the contract
        require(
            IERC20(tokenAddress).transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        emit TokensLocked(msg.sender, amount, lockType);
    }

    /**
     * @dev Withdraw locked tokens after the lock period has ended.
     * @param recipient The address to receive the withdrawn tokens.
     * @param amount The amount of tokens to withdraw.
     * @param lockType The type of lock ("team" or "liquidity").
     */
    function withdrawTokens(address recipient, uint256 amount, string memory lockType)
        external
        onlyOwner
        afterLockPeriod(lockType)
    {
        require(amount > 0, "Amount must be greater than zero");
        require(recipient != address(0), "Recipient address cannot be zero");

        // Transfer tokens from the contract to the recipient
        require(
            IERC20(tokenAddress).transfer(recipient, amount),
            "Token transfer failed"
        );

        emit TokensWithdrawn(recipient, amount, lockType);
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);

    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
