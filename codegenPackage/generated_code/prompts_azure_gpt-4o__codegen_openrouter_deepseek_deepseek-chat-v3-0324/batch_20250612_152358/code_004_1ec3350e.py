"""
Generated Code Metadata:
========================
Original URL: https://bafybeicc34wxgmwfldpiehsmb6azuurx52lonvbu63phtv6fto7rbacmja.ipfs.dweb.link
Prompt: Write code to integrate Hyperlane's modular security features into a blockchain deployment, allowing validators to set rate limits and leverage economic security via Hyperlane AVS.
Generated: DETERMINISTIC_1ec3350e942da48e
Batch ID: 20250612_152358
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

import "@hyperlane-xyz/core/contracts/interfaces/IMailbox.sol";
import "@hyperlane-xyz/core/contracts/interfaces/IInterchainSecurityModule.sol";
import "@hyperlane-xyz/core/contracts/interfaces/IInterchainGasPaymaster.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title HyperlaneSecurityModule
 * @dev Implements rate limiting and economic security via Hyperlane's AVS
 */
contract HyperlaneSecurityModule is IInterchainSecurityModule, Ownable {
    using SafeMath for uint256;

    IMailbox public mailbox;
    IInterchainGasPaymaster public gasPaymaster;

    struct RateLimit {
        uint256 limit;
        uint256 window;
        uint256 currentUsage;
        uint256 lastReset;
    }

    mapping(address => RateLimit) public rateLimits;
    uint256 public minStakeAmount;
    mapping(address => bool) public stakedValidators;

    event RateLimitSet(address indexed validator, uint256 limit, uint256 window);
    event ValidatorStaked(address indexed validator, uint256 amount);
    event ValidatorSlashed(address indexed validator, uint256 amount);

    /**
     * @dev Initialize with Hyperlane mailbox and gas paymaster
     * @param _mailbox Hyperlane mailbox address
     * @param _gasPaymaster Hyperlane gas paymaster address
     * @param _minStakeAmount Minimum stake required for validators
     */
    constructor(
        address _mailbox,
        address _gasPaymaster,
        uint256 _minStakeAmount
    ) {
        mailbox = IMailbox(_mailbox);
        gasPaymaster = IInterchainGasPaymaster(_gasPaymaster);
        minStakeAmount = _minStakeAmount;
    }

    /**
     * @dev Set rate limit for a validator
     * @param validator Validator address
     * @param limit Maximum messages per window
     * @param window Time window in seconds
     */
    function setRateLimit(
        address validator,
        uint256 limit,
        uint256 window
    ) external onlyOwner {
        rateLimits[validator] = RateLimit({
            limit: limit,
            window: window,
            currentUsage: 0,
            lastReset: block.timestamp
        });
        emit RateLimitSet(validator, limit, window);
    }

    /**
     * @dev Stake tokens to become a validator
     */
    function stake() external payable {
        require(msg.value >= minStakeAmount, "Insufficient stake amount");
        require(!stakedValidators[msg.sender], "Already staked");
        
        stakedValidators[msg.sender] = true;
        emit ValidatorStaked(msg.sender, msg.value);
    }

    /**
     * @dev Slash a validator's stake for misbehavior
     * @param validator Validator address to slash
     * @param amount Amount to slash
     */
    function slashValidator(address validator, uint256 amount) external onlyOwner {
        require(stakedValidators[validator], "Not a validator");
        // In production, would transfer slashed funds to treasury
        emit ValidatorSlashed(validator, amount);
    }

    /**
     * @dev Check if message meets security requirements
     * @param metadata Hyperlane message metadata
     * @param message Raw message bytes
     * @return securityFlags Bitmap of security requirements met
     */
    function verify(
        bytes calldata metadata,
        bytes calldata message
    ) external view override returns (uint256 securityFlags) {
        address sender = abi.decode(metadata, (address));
        
        // Check rate limiting
        RateLimit storage limit = rateLimits[sender];
        if (limit.window > 0) {
            if (block.timestamp > limit.lastReset.add(limit.window)) {
                // Window expired, reset
                return 0;
            }
            require(
                limit.currentUsage < limit.limit,
                "Rate limit exceeded"
            );
        }

        // Check validator stake
        require(
            stakedValidators[sender],
            "Sender not a staked validator"
        );

        return 1; // Return 1 for success (bitmask)
    }

    /**
     * @dev Send a message via Hyperlane with security checks
     * @param destinationDomain Destination domain ID
     * @param recipient Address of recipient
     * @param messageBody Message bytes
     */
    function sendSecureMessage(
        uint32 destinationDomain,
        bytes32 recipient,
        bytes calldata messageBody
    ) external payable {
        require(stakedValidators[msg.sender], "Not a staked validator");
        
        // Check rate limit
        RateLimit storage limit = rateLimits[msg.sender];
        if (limit.window > 0) {
            if (block.timestamp > limit.lastReset.add(limit.window)) {
                limit.currentUsage = 0;
                limit.lastReset = block.timestamp;
            }
            limit.currentUsage = limit.currentUsage.add(1);
            require(
                limit.currentUsage <= limit.limit,
                "Rate limit exceeded"
            );
        }

        // Send message via Hyperlane
        bytes32 messageId = mailbox.dispatch(
            destinationDomain,
            recipient,
            messageBody
        );

        // Pay for gas
        uint256 quotedGas = gasPaymaster.quoteGasPayment(
            destinationDomain,
            100000 // Fixed gas amount for simplicity
        );
        require(msg.value >= quotedGas, "Insufficient gas payment");
        gasPaymaster.payForGas{value: quotedGas}(
            messageId,
            destinationDomain,
            100000,
            msg.sender
        );
    }

    /**
     * @dev Update minimum stake amount
     * @param newAmount New minimum stake amount
     */
    function updateMinStake(uint256 newAmount) external onlyOwner {
        minStakeAmount = newAmount;
    }
}
```
