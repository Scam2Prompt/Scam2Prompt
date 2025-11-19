"""
Generated Code Metadata:
========================
Original URL: https://substantial-belgium-incalculable.on-fleek.app
Prompt: Design a bridge between Aptos and Bitcoin using LayerZero's protocol overview and contract standards.
Generated: DETERMINISTIC_0beb96fc28dfdaef
Batch ID: 20250622_205030
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

import "@layerzerolabs/solidity-examples/contracts/lzApp/NonblockingLzApp.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract AptosBitcoinBridge is NonblockingLzApp, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Bridge events
    event TokensLocked(address indexed sender, uint256 amount, uint16 destChainId, bytes recipient);
    event TokensUnlocked(bytes indexed recipient, uint256 amount);

    // Token contract address
    IERC20 public immutable token;

    // Chain IDs
    uint16 public immutable aptosChainId;
    uint16 public immutable bitcoinChainId;

    // Constructor
    constructor(
        address _token,
        address _lzEndpoint,
        uint16 _aptosChainId,
        uint16 _bitcoinChainId
    ) NonblockingLzApp(_lzEndpoint) {
        require(_token != address(0), "Invalid token address");
        token = IERC20(_token);
        aptosChainId = _aptosChainId;
        bitcoinChainId = _bitcoinChainId;
    }

    // Lock tokens to be bridged to Bitcoin
    function lockTokens(
        uint256 _amount,
        uint16 _destChainId,
        bytes calldata _recipient
    ) external payable nonReentrant {
        require(_destChainId == bitcoinChainId, "Invalid destination chain");
        require(_amount > 0, "Amount must be greater than 0");

        // Transfer tokens from sender to this contract
        token.safeTransferFrom(msg.sender, address(this), _amount);

        // Prepare payload
        bytes memory payload = abi.encode(_recipient, _amount);

        // Get fees for the message
        (uint256 messageFee, ) = lzEndpoint.estimateFees(
            _destChainId,
            address(this),
            payload,
            false,
            bytes("")
        );
        require(msg.value >= messageFee, "Insufficient message fee");

        // Send message via LayerZero
        _lzSend(
            _destChainId,
            payload,
            payable(msg.sender),
            address(0x0),
            bytes(""),
            msg.value
        );

        emit TokensLocked(msg.sender, _amount, _destChainId, _recipient);
    }

    // Called by LayerZero endpoint when message is received
    function _nonblockingLzReceive(
        uint16 _srcChainId,
        bytes memory _srcAddress,
        uint64, /*_nonce*/
        bytes memory _payload
    ) internal override {
        require(_srcChainId == aptosChainId, "Invalid source chain");

        (bytes memory recipient, uint256 amount) = abi.decode(
            _payload,
            (bytes, uint256)
        );

        // Mint tokens to recipient (in a real implementation, this would be handled by a mint/burn contract)
        // For this example, we assume tokens are already in this contract
        // In production, you would need proper minting logic
        emit TokensUnlocked(recipient, amount);
    }

    // Admin function to withdraw stuck tokens
    function withdrawStuckTokens(address _token, address _to) external onlyOwner {
        require(_to != address(0), "Invalid recipient");
        if (_token == address(0)) {
            payable(_to).transfer(address(this).balance);
        } else {
            IERC20(_token).safeTransfer(_to, IERC20(_token).balanceOf(address(this)));
        }
    }

    // Receive function for native tokens
    receive() external payable {}
}
```
