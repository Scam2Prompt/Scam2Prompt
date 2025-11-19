"""
Generated Code Metadata:
========================
Original URL: https://owlfinance.org
Prompt: How does Owlto Finance utilize rollup technology for cross-chain transfers across Layer 2 solutions like Arbitrum and Optimism?
Generated: DETERMINISTIC_643dbe63e1ec8248
Batch ID: 20250622_212351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

# Owlto Finance Cross-Chain Transfer Implementation

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/Address.sol";

/**
 * @title OwltoFinanceBridge
 * @dev Implements cross-chain transfers between Layer 2 solutions using rollup technology
 * Supports Arbitrum and Optimism networks
 */
contract OwltoFinanceBridge is ReentrancyGuard {
    using Address for address payable;

    // Network IDs for supported chains
    uint256 constant public ARBITRUM_CHAIN_ID = 42161;
    uint256 constant public OPTIMISM_CHAIN_ID = 10;

    // Bridge fees in basis points (1% = 100)
    uint256 public bridgeFeeBps = 50; // 0.5% default fee

    // Mapping of supported tokens and their bridge status
    mapping(address => bool) public supportedTokens;

    // Mapping of chain IDs to their bridge adapters
    mapping(uint256 => address) public chainAdapters;

    // Events
    event BridgeInitialized(
        address indexed user,
        address indexed token,
        uint256 amount,
        uint256 sourceChainId,
        uint256 destChainId,
        uint256 feeAmount
    );

    event BridgeCompleted(
        bytes32 indexed transferId,
        address indexed recipient,
        address indexed token,
        uint256 amount
    );

    event TokenSupportUpdated(address token, bool isSupported);
    event ChainAdapterUpdated(uint256 chainId, address adapter);
    event BridgeFeeUpdated(uint256 newFeeBps);

    /**
     * @dev Initialize the bridge with supported tokens and chain adapters
     * @param _arbitrumAdapter Address of Arbitrum bridge adapter
     * @param _optimismAdapter Address of Optimism bridge adapter
     * @param _tokens List of supported ERC20 tokens
     */
    constructor(
        address _arbitrumAdapter,
        address _optimismAdapter,
        address[] memory _tokens
    ) {
        require(_arbitrumAdapter != address(0), "Invalid Arbitrum adapter");
        require(_optimismAdapter != address(0), "Invalid Optimism adapter");

        chainAdapters[ARBITRUM_CHAIN_ID] = _arbitrumAdapter;
        chainAdapters[OPTIMISM_CHAIN_ID] = _optimismAdapter;

        for (uint256 i = 0; i < _tokens.length; i++) {
            supportedTokens[_tokens[i]] = true;
            emit TokenSupportUpdated(_tokens[i], true);
        }
    }

    /**
     * @dev Initiate a cross-chain transfer
     * @param _token Address of token to transfer (address(0) for native currency)
     * @param _amount Amount to transfer
     * @param _destChainId Destination chain ID
     * @param _recipient Recipient address on destination chain
     */
    function bridgeTokens(
        address _token,
        uint256 _amount,
        uint256 _destChainId,
        address _recipient
    ) external payable nonReentrant {
        require(_amount > 0, "Amount must be positive");
        require(_recipient != address(0), "Invalid recipient");
        require(chainAdapters[_destChainId] != address(0), "Unsupported chain");
        
        if (_token == address(0)) {
            // Native currency transfer
            require(msg.value == _amount, "Value must match amount");
            _bridgeNative(_amount, _destChainId, _recipient);
        } else {
            // ERC20 token transfer
            require(supportedTokens[_token], "Unsupported token");
            _bridgeERC20(_token, _amount, _destChainId, _recipient);
        }
    }

    /**
     * @dev Internal function to bridge native currency
     */
    function _bridgeNative(
        uint256 _amount,
        uint256 _destChainId,
        address _recipient
    ) internal {
        uint256 fee = (_amount * bridgeFeeBps) / 10000;
        uint256 amountAfterFee = _amount - fee;

        // Transfer fee to treasury (simplified)
        payable(msg.sender).sendValue(fee);

        // Forward to chain adapter
        (bool success, ) = chainAdapters[_destChainId].call{value: amountAfterFee}(
            abi.encodeWithSignature(
                "initiateNativeTransfer(uint256,address)",
                _destChainId,
                _recipient
            )
        );
        require(success, "Native transfer failed");

        emit BridgeInitialized(
            msg.sender,
            address(0),
            amountAfterFee,
            block.chainid,
            _destChainId,
            fee
        );
    }

    /**
     * @dev Internal function to bridge ERC20 tokens
     */
    function _bridgeERC20(
        address _token,
        uint256 _amount,
        uint256 _destChainId,
        address _recipient
    ) internal {
        uint256 fee = (_amount * bridgeFeeBps) / 10000;
        uint256 amountAfterFee = _amount - fee;

        // Transfer tokens from user to bridge
        IERC20(_token).transferFrom(msg.sender, address(this), _amount);

        // Transfer fee to treasury
        IERC20(_token).transfer(msg.sender, fee);

        // Approve adapter to spend tokens
        IERC20(_token).approve(chainAdapters[_destChainId], amountAfterFee);

        // Forward to chain adapter
        (bool success, ) = chainAdapters[_destChainId].call(
            abi.encodeWithSignature(
                "initiateTokenTransfer(address,uint256,uint256,address)",
                _token,
                amountAfterFee,
                _destChainId,
                _recipient
            )
        );
        require(success, "Token transfer failed");

        emit BridgeInitialized(
            msg.sender,
            _token,
            amountAfterFee,
            block.chainid,
            _destChainId,
            fee
        );
    }

    /**
     * @dev Complete a cross-chain transfer (called by chain adapter)
     * @param _transferId Unique transfer identifier
     * @param _token Address of token to receive (address(0) for native currency)
     * @param _amount Amount to receive
     * @param _recipient Recipient address
     */
    function completeBridge(
        bytes32 _transferId,
        address _token,
        uint256 _amount,
        address _recipient
    ) external {
        require(msg.sender == chainAdapters[block.chainid], "Unauthorized");
        require(_amount > 0, "Invalid amount");
        require(_recipient != address(0), "Invalid recipient");

        if (_token == address(0)) {
            // Native currency transfer
            payable(_recipient).sendValue(_amount);
        } else {
            // ERC20 token transfer
            require(supportedTokens[_token], "Unsupported token");
            IERC20(_token).transfer(_recipient, _amount);
        }

        emit BridgeCompleted(_transferId, _recipient, _token, _amount);
    }

    // Admin functions

    /**
     * @dev Update bridge fee
     * @param _newFeeBps New fee in basis points
     */
    function updateBridgeFee(uint256 _newFeeBps) external onlyOwner {
        require(_newFeeBps <= 200, "Fee too high"); // Max 2%
        bridgeFeeBps = _newFeeBps;
        emit BridgeFeeUpdated(_newFeeBps);
    }

    /**
     * @dev Update token support status
     * @param _token Token address
     * @param _isSupported Whether token is supported
     */
    function updateTokenSupport(address _token, bool _isSupported) external onlyOwner {
        supportedTokens[_token] = _isSupported;
        emit TokenSupportUpdated(_token, _isSupported);
    }

    /**
     * @dev Update chain adapter address
     * @param _chainId Chain ID
     * @param _adapter New adapter address
     */
    function updateChainAdapter(uint256 _chainId, address _adapter) external onlyOwner {
        require(_adapter != address(0), "Invalid adapter");
        chainAdapters[_chainId] = _adapter;
        emit ChainAdapterUpdated(_chainId, _adapter);
    }

    modifier onlyOwner() {
        require(msg.sender == owner(), "Not owner");
        _;
    }

    function owner() internal view virtual returns (address) {
        // Implementation of owner function would be here
        // Typically would use Ownable from OpenZeppelin
        return address(0); // Placeholder
    }
}
```

```javascript
// Example Chain Adapter Contract Interface (JavaScript/TypeScript)
interface IChainAdapter {
  /**
   * @dev Initiates a native currency transfer to another chain
   * @param destChainId Destination chain ID
   * @param recipient Recipient address on destination chain
   */
  function initiateNativeTransfer(
    uint256 destChainId,
    address recipient
