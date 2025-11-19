"""
Generated Code Metadata:
========================
Original URL: https://metazeechain.pages.dev
Prompt: Generate code for implementing a cross-chain token bridge that ensures seamless interoperability between blockchain networks, referencing the Chain Bridge functionality on MetazeeChain.
Generated: DETERMINISTIC_c171f389942d5e2b
Batch ID: 20250612_145731
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

/**
 * @title CrossChainTokenBridge
 * @dev Implements a cross-chain token bridge with deposit and claim functionality
 */
contract CrossChainTokenBridge is ReentrancyGuard, Ownable {
    using SafeERC20 for IERC20;

    // Bridge configuration
    struct BridgeConfig {
        uint256 chainId;
        address tokenAddress;
        bool isActive;
        uint256 minTransferAmount;
        uint256 maxTransferAmount;
        uint256 feePercentage; // 100 = 1%
    }

    // Transfer record
    struct Transfer {
        address sender;
        address recipient;
        uint256 amount;
        uint256 timestamp;
        bool claimed;
    }

    // Mapping from chain ID to bridge configuration
    mapping(uint256 => BridgeConfig) public bridgeConfigs;

    // Mapping from transfer ID to transfer details
    mapping(bytes32 => Transfer) public transfers;

    // Mapping from token address to supported status
    mapping(address => bool) public supportedTokens;

    // Events
    event TokenDeposited(
        bytes32 indexed transferId,
        address indexed sender,
        address indexed recipient,
        uint256 amount,
        uint256 sourceChainId,
        uint256 destChainId
    );

    event TokenClaimed(
        bytes32 indexed transferId,
        address indexed recipient,
        uint256 amount
    );

    event BridgeConfigUpdated(
        uint256 indexed chainId,
        address tokenAddress,
        uint256 minTransferAmount,
        uint256 maxTransferAmount,
        uint256 feePercentage
    );

    /**
     * @dev Deposit tokens to be bridged to another chain
     * @param _recipient Address on the destination chain
     * @param _amount Amount of tokens to transfer
     * @param _destChainId Destination chain ID
     */
    function depositTokens(
        address _recipient,
        uint256 _amount,
        uint256 _destChainId
    ) external nonReentrant {
        BridgeConfig memory config = bridgeConfigs[_destChainId];
        require(config.isActive, "Bridge: Destination chain not active");
        require(
            _amount >= config.minTransferAmount,
            "Bridge: Amount below minimum"
        );
        require(
            _amount <= config.maxTransferAmount,
            "Bridge: Amount exceeds maximum"
        );
        require(
            supportedTokens[config.tokenAddress],
            "Bridge: Token not supported"
        );

        // Calculate fee and net amount
        uint256 fee = (_amount * config.feePercentage) / 10000;
        uint256 netAmount = _amount - fee;

        // Transfer tokens from sender to bridge
        IERC20 token = IERC20(config.tokenAddress);
        token.safeTransferFrom(msg.sender, address(this), _amount);

        // Create transfer record
        bytes32 transferId = keccak256(
            abi.encodePacked(
                msg.sender,
                _recipient,
                _amount,
                block.chainid,
                _destChainId,
                block.timestamp
            )
        );

        transfers[transferId] = Transfer({
            sender: msg.sender,
            recipient: _recipient,
            amount: netAmount,
            timestamp: block.timestamp,
            claimed: false
        });

        emit TokenDeposited(
            transferId,
            msg.sender,
            _recipient,
            netAmount,
            block.chainid,
            _destChainId
        );
    }

    /**
     * @dev Claim tokens bridged from another chain
     * @param _transferId Unique transfer identifier
     * @param _sender Address on the source chain
     * @param _recipient Address to receive tokens
     * @param _amount Amount of tokens to claim
     * @param _sourceChainId Source chain ID
     * @param _signature Validator signature
     */
    function claimTokens(
        bytes32 _transferId,
        address _sender,
        address _recipient,
        uint256 _amount,
        uint256 _sourceChainId,
        bytes calldata _signature
    ) external nonReentrant {
        require(!transfers[_transferId].claimed, "Bridge: Already claimed");
        require(
            bridgeConfigs[_sourceChainId].isActive,
            "Bridge: Source chain not active"
        );

        // Verify the transfer (in production, this would use a validator network)
        bytes32 messageHash = keccak256(
            abi.encodePacked(
                _transferId,
                _sender,
                _recipient,
                _amount,
                _sourceChainId,
                block.chainid
            )
        );
        address signer = _recoverSigner(messageHash, _signature);
        require(isValidator(signer), "Bridge: Invalid signature");

        // Mark as claimed
        transfers[_transferId].claimed = true;

        // Transfer tokens to recipient
        IERC20 token = IERC20(bridgeConfigs[_sourceChainId].tokenAddress);
        token.safeTransfer(_recipient, _amount);

        emit TokenClaimed(_transferId, _recipient, _amount);
    }

    /**
     * @dev Update bridge configuration for a chain
     * @param _chainId Chain ID to configure
     * @param _tokenAddress Token address on that chain
     * @param _minTransferAmount Minimum transfer amount
     * @param _maxTransferAmount Maximum transfer amount
     * @param _feePercentage Transfer fee percentage (100 = 1%)
     */
    function updateBridgeConfig(
        uint256 _chainId,
        address _tokenAddress,
        uint256 _minTransferAmount,
        uint256 _maxTransferAmount,
        uint256 _feePercentage
    ) external onlyOwner {
        require(_minTransferAmount < _maxTransferAmount, "Bridge: Invalid amounts");
        require(_feePercentage <= 500, "Bridge: Fee too high"); // Max 5%

        bridgeConfigs[_chainId] = BridgeConfig({
            chainId: _chainId,
            tokenAddress: _tokenAddress,
            isActive: true,
            minTransferAmount: _minTransferAmount,
            maxTransferAmount: _maxTransferAmount,
            feePercentage: _feePercentage
        });

        supportedTokens[_tokenAddress] = true;

        emit BridgeConfigUpdated(
            _chainId,
            _tokenAddress,
            _minTransferAmount,
            _maxTransferAmount,
            _feePercentage
        );
    }

    /**
     * @dev Withdraw collected fees
     * @param _tokenAddress Token address to withdraw
     * @param _amount Amount to withdraw
     */
    function withdrawFees(address _tokenAddress, uint256 _amount) external onlyOwner {
        IERC20 token = IERC20(_tokenAddress);
        token.safeTransfer(owner(), _amount);
    }

    /**
     * @dev Internal function to recover signer from signature
     */
    function _recoverSigner(bytes32 _messageHash, bytes memory _signature)
        internal
        pure
        returns (address)
    {
        bytes32 ethSignedMessageHash = keccak256(
            abi.encodePacked("\x19Ethereum Signed Message:\n32", _messageHash)
        );
        (bytes32 r, bytes32 s, uint8 v) = _splitSignature(_signature);
        return ecrecover(ethSignedMessageHash, v, r, s);
    }

    /**
     * @dev Internal function to split signature
     */
    function _splitSignature(bytes memory _signature)
        internal
        pure
        returns (
            bytes32 r,
            bytes32 s,
            uint8 v
        )
    {
        require(_signature.length == 65, "Bridge: Invalid signature length");
        assembly {
            r := mload(add(_signature, 32))
            s := mload(add(_signature, 64))
            v := byte(0, mload(add(_signature, 96)))
        }
    }

    /**
     * @dev Check if address is a validator (simplified for example)
     * In production, this would check against a validator set
     */
    function isValidator(address _address) internal pure returns (bool) {
        // This is a simplified example - in production you would maintain
        // a set of validators and check against that
        return _address != address(0);
    }
}
```
