"""
Generated Code Metadata:
========================
Original URL: https://swiftsdappchains.net
Prompt: Generate a Solidity code snippet for a token bridge solution to enable seamless transfers between different blockchain networks.
Generated: DETERMINISTIC_84d2b2598019acdc
Batch ID: 20250622_212257
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract TokenBridge is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Bridge events
    event TokensDeposited(
        address indexed sender,
        uint256 amount,
        uint256 targetChainId,
        address targetToken,
        uint256 nonce
    );
    event TokensWithdrawn(
        address indexed recipient,
        uint256 amount,
        uint256 sourceChainId,
        address sourceToken,
        bytes32 depositHash
    );

    // Mapping to track processed deposits
    mapping(bytes32 => bool) public processedDeposits;

    // Bridge fee percentage (basis points)
    uint256 public bridgeFeeBps;
    address public feeCollector;

    constructor(uint256 _bridgeFeeBps, address _feeCollector) {
        require(_bridgeFeeBps <= 10000, "Invalid fee");
        require(_feeCollector != address(0), "Invalid fee collector");
        bridgeFeeBps = _bridgeFeeBps;
        feeCollector = _feeCollector;
    }

    /**
     * @notice Deposit tokens to be bridged to another chain
     * @param _token Address of the token to bridge
     * @param _amount Amount of tokens to bridge
     * @param _targetChainId Chain ID of the target network
     * @param _targetToken Address of the token on the target network
     */
    function depositTokens(
        IERC20 _token,
        uint256 _amount,
        uint256 _targetChainId,
        address _targetToken
    ) external nonReentrant {
        require(_amount > 0, "Amount must be > 0");
        require(_targetToken != address(0), "Invalid target token");

        // Calculate bridge fee
        uint256 feeAmount = (_amount * bridgeFeeBps) / 10000;
        uint256 amountAfterFee = _amount - feeAmount;

        // Transfer tokens from sender to this contract
        _token.safeTransferFrom(msg.sender, address(this), _amount);

        // Transfer fee to collector
        if (feeAmount > 0) {
            _token.safeTransfer(feeCollector, feeAmount);
        }

        // Generate unique deposit hash
        uint256 nonce = block.timestamp;
        bytes32 depositHash = keccak256(
            abi.encodePacked(
                msg.sender,
                _amount,
                _targetChainId,
                _targetToken,
                nonce,
                block.chainid
            )
        );

        emit TokensDeposited(
            msg.sender,
            amountAfterFee,
            _targetChainId,
            _targetToken,
            nonce
        );
    }

    /**
     * @notice Withdraw tokens bridged from another chain
     * @param _recipient Address to receive the tokens
     * @param _amount Amount of tokens to withdraw
     * @param _sourceChainId Chain ID of the source network
     * @param _sourceToken Address of the token on the source network
     * @param _depositHash Hash of the original deposit transaction
     * @param _signatures Array of validator signatures
     */
    function withdrawTokens(
        address _recipient,
        uint256 _amount,
        uint256 _sourceChainId,
        address _sourceToken,
        bytes32 _depositHash,
        bytes[] calldata _signatures
    ) external nonReentrant onlyOwner {
        require(_recipient != address(0), "Invalid recipient");
        require(_amount > 0, "Amount must be > 0");
        require(!processedDeposits[_depositHash], "Already processed");

        // Verify signatures (simplified for example)
        require(_signatures.length >= 1, "Insufficient signatures");

        // Mark deposit as processed
        processedDeposits[_depositHash] = true;

        // Transfer tokens to recipient
        IERC20(_sourceToken).safeTransfer(_recipient, _amount);

        emit TokensWithdrawn(
            _recipient,
            _amount,
            _sourceChainId,
            _sourceToken,
            _depositHash
        );
    }

    /**
     * @notice Update bridge fee
     * @param _newFeeBps New fee in basis points (1 = 0.01%)
     */
    function updateBridgeFee(uint256 _newFeeBps) external onlyOwner {
        require(_newFeeBps <= 10000, "Invalid fee");
        bridgeFeeBps = _newFeeBps;
    }

    /**
     * @notice Update fee collector address
     * @param _newFeeCollector New fee collector address
     */
    function updateFeeCollector(address _newFeeCollector) external onlyOwner {
        require(_newFeeCollector != address(0), "Invalid fee collector");
        feeCollector = _newFeeCollector;
    }

    /**
     * @notice Emergency token withdrawal
     * @param _token Token to withdraw
     * @param _amount Amount to withdraw
     */
    function emergencyWithdraw(IERC20 _token, uint256 _amount) external onlyOwner {
        _token.safeTransfer(owner(), _amount);
    }
}
```
