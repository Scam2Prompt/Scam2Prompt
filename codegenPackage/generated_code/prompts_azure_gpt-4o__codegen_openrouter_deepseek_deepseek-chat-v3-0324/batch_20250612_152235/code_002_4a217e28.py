"""
Generated Code Metadata:
========================
Original URL: https://bafybeibasskry2ovpgydqzwiw46ea2lmyxe4fqb6jekaixqidxb6cvjn3m.ipfs.dweb.link
Prompt: Generate code to integrate EigenLayer's scalability features with Polymer's Ethereum interoperability hub.
Generated: DETERMINISTIC_4a217e2879e15f98
Batch ID: 20250612_152235
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

interface IEigenLayer {
    function depositIntoStrategy(address strategy, IERC20 token, uint256 amount) external;
    function withdrawFromStrategy(address strategy, IERC20 token, uint256 amount) external;
    function getStrategyShares(address user, address strategy) external view returns (uint256);
}

interface IPolymerHub {
    function sendCrossChainMessage(
        uint256 destinationChainId,
        bytes calldata recipient,
        bytes calldata data
    ) external payable;
    function receiveCrossChainMessage(
        bytes calldata sender,
        uint256 sourceChainId,
        bytes calldata data
    ) external;
}

contract EigenPolymerIntegration is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    IEigenLayer public immutable eigenLayer;
    IPolymerHub public immutable polymerHub;
    address public strategy;
    IERC20 public token;

    // Mapping to track cross-chain operations
    mapping(bytes32 => bool) public processedMessages;

    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event CrossChainDepositInitiated(
        address indexed user,
        uint256 destinationChainId,
        uint256 amount
    );
    event CrossChainWithdrawalInitiated(
        address indexed user,
        uint256 destinationChainId,
        uint256 amount
    );
    event CrossChainDepositCompleted(
        address indexed user,
        uint256 sourceChainId,
        uint256 amount
    );
    event CrossChainWithdrawalCompleted(
        address indexed user,
        uint256 sourceChainId,
        uint256 amount
    );

    constructor(
        address _eigenLayer,
        address _polymerHub,
        address _strategy,
        address _token
    ) {
        require(_eigenLayer != address(0), "Invalid EigenLayer address");
        require(_polymerHub != address(0), "Invalid PolymerHub address");
        require(_strategy != address(0), "Invalid strategy address");
        require(_token != address(0), "Invalid token address");

        eigenLayer = IEigenLayer(_eigenLayer);
        polymerHub = IPolymerHub(_polymerHub);
        strategy = _strategy;
        token = IERC20(_token);
    }

    /**
     * @dev Deposit tokens into EigenLayer strategy
     * @param amount Amount of tokens to deposit
     */
    function deposit(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        token.safeTransferFrom(msg.sender, address(this), amount);
        token.safeApprove(address(eigenLayer), amount);
        eigenLayer.depositIntoStrategy(strategy, token, amount);
        
        emit Deposited(msg.sender, amount);
    }

    /**
     * @dev Withdraw tokens from EigenLayer strategy
     * @param amount Amount of tokens to withdraw
     */
    function withdraw(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        uint256 userShares = eigenLayer.getStrategyShares(msg.sender, strategy);
        require(userShares >= amount, "Insufficient shares");
        
        eigenLayer.withdrawFromStrategy(strategy, token, amount);
        token.safeTransfer(msg.sender, amount);
        
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Initiate cross-chain deposit to another chain
     * @param destinationChainId ID of the destination chain
     * @param amount Amount of tokens to deposit on destination chain
     */
    function initiateCrossChainDeposit(
        uint256 destinationChainId,
        uint256 amount
    ) external payable nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        uint256 userShares = eigenLayer.getStrategyShares(msg.sender, strategy);
        require(userShares >= amount, "Insufficient shares");

        // Lock shares on source chain
        eigenLayer.withdrawFromStrategy(strategy, token, amount);
        
        // Prepare message data
        bytes memory data = abi.encode(msg.sender, amount);
        
        // Send cross-chain message via Polymer Hub
        polymerHub.sendCrossChainMessage{value: msg.value}(
            destinationChainId,
            abi.encodePacked(address(this)),
            data
        );
        
        emit CrossChainDepositInitiated(msg.sender, destinationChainId, amount);
    }

    /**
     * @dev Complete cross-chain deposit from another chain
     * @param sender Address of the sender on the source chain
     * @param sourceChainId ID of the source chain
     * @param data Encoded data containing (user, amount)
     */
    function receiveCrossChainMessage(
        bytes calldata sender,
        uint256 sourceChainId,
        bytes calldata data
    ) external {
        require(msg.sender == address(polymerHub), "Only PolymerHub can call");
        
        (address user, uint256 amount) = abi.decode(data, (address, uint256));
        require(amount > 0, "Invalid amount");
        
        // Generate unique message hash to prevent replay
        bytes32 messageHash = keccak256(abi.encodePacked(sender, sourceChainId, data));
        require(!processedMessages[messageHash], "Message already processed");
        processedMessages[messageHash] = true;
        
        // Deposit tokens into EigenLayer on destination chain
        token.safeApprove(address(eigenLayer), amount);
        eigenLayer.depositIntoStrategy(strategy, token, amount);
        
        emit CrossChainDepositCompleted(user, sourceChainId, amount);
    }

    /**
     * @dev Initiate cross-chain withdrawal to another chain
     * @param destinationChainId ID of the destination chain
     * @param amount Amount of tokens to withdraw on destination chain
     */
    function initiateCrossChainWithdrawal(
        uint256 destinationChainId,
        uint256 amount
    ) external payable nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        // Prepare message data
        bytes memory data = abi.encode(msg.sender, amount);
        
        // Send cross-chain message via Polymer Hub
        polymerHub.sendCrossChainMessage{value: msg.value}(
            destinationChainId,
            abi.encodePacked(address(this)),
            data
        );
        
        emit CrossChainWithdrawalInitiated(msg.sender, destinationChainId, amount);
    }

    /**
     * @dev Complete cross-chain withdrawal from another chain
     * @param sender Address of the sender on the source chain
     * @param sourceChainId ID of the source chain
     * @param data Encoded data containing (user, amount)
     */
    function completeCrossChainWithdrawal(
        bytes calldata sender,
        uint256 sourceChainId,
        bytes calldata data
    ) external {
        require(msg.sender == address(polymerHub), "Only PolymerHub can call");
        
        (address user, uint256 amount) = abi.decode(data, (address, uint256));
        require(amount > 0, "Invalid amount");
        
        // Generate unique message hash to prevent replay
        bytes32 messageHash = keccak256(abi.encodePacked(sender, sourceChainId, data));
        require(!processedMessages[messageHash], "Message already processed");
        processedMessages[messageHash] = true;
        
        // Withdraw tokens from EigenLayer and send to user
        eigenLayer.withdrawFromStrategy(strategy, token, amount);
        token.safeTransfer(user, amount);
        
        emit CrossChainWithdrawalCompleted(user, sourceChainId, amount);
    }

    /**
     * @dev Update the strategy address (only owner)
     * @param newStrategy New strategy address
     */
    function updateStrategy(address newStrategy) external onlyOwner {
        require(newStrategy != address(0), "Invalid strategy address");
        strategy = newStrategy;
    }

    /**
     * @dev Emergency withdraw tokens (only owner)
     * @param _token Token address to withdraw
     * @param amount Amount to withdraw
     */
    function emergencyWithdraw(address _token, uint256 amount) external onlyOwner {
        IERC20(_token).safeTransfer(owner(), amount);
    }
}
```
