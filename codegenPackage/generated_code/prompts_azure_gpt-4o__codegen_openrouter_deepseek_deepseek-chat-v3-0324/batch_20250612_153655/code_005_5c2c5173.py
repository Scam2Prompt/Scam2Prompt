"""
Generated Code Metadata:
========================
Original URL: https://v2-celer.network
Prompt: Develop a decentralized application (DApp) using Celer Network's cOS framework to enable micropayments with zero off-chain transaction fees.
Generated: DETERMINISTIC_5c2c51735a36fad8
Batch ID: 20250612_153655
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@celer-network/contracts/message/interfaces/IMessageBus.sol";
import "@celer-network/contracts/message/libraries/MessageSenderLib.sol";

contract MicropaymentDApp is Ownable {
    IMessageBus public messageBus;
    address public receiverContract;
    uint64 public chainId;
    
    // Mapping to track pending payments
    mapping(bytes32 => bool) public pendingPayments;
    
    // Events
    event PaymentInitiated(
        address indexed sender,
        address indexed receiver,
        uint256 amount,
        address token,
        bytes32 paymentId
    );
    
    event PaymentCompleted(
        bytes32 indexed paymentId,
        address indexed receiver,
        uint256 amount,
        address token
    );
    
    event PaymentFailed(
        bytes32 indexed paymentId,
        string reason
    );
    
    constructor(
        address _messageBus,
        address _receiverContract,
        uint64 _chainId
    ) {
        messageBus = IMessageBus(_messageBus);
        receiverContract = _receiverContract;
        chainId = _chainId;
    }
    
    /**
     * @dev Initialize a micropayment
     * @param _receiver Address of the receiver
     * @param _amount Amount to send
     * @param _token Token address (address(0) for native token)
     * @param _paymentId Unique payment identifier
     */
    function initiatePayment(
        address _receiver,
        uint256 _amount,
        address _token,
        bytes32 _paymentId
    ) external payable {
        require(!pendingPayments[_paymentId], "Payment ID already exists");
        
        if (_token == address(0)) {
            require(msg.value == _amount, "Incorrect native token amount");
        } else {
            IERC20 token = IERC20(_token);
            require(
                token.transferFrom(msg.sender, address(this), _amount),
                "Token transfer failed"
            );
        }
        
        pendingPayments[_paymentId] = true;
        
        emit PaymentInitiated(
            msg.sender,
            _receiver,
            _amount,
            _token,
            _paymentId
        );
        
        _sendMessage(_receiver, _amount, _token, _paymentId);
    }
    
    /**
     * @dev Internal function to send message via cOS
     */
    function _sendMessage(
        address _receiver,
        uint256 _amount,
        address _token,
        bytes32 _paymentId
    ) internal {
        bytes memory message = abi.encode(
            _receiver,
            _amount,
            _token,
            _paymentId
        );
        
        uint256 fee = messageBus.fee();
        
        MessageSenderLib.sendMessage(
            receiverContract,
            chainId,
            message,
            MessageSenderLib.PaymentType.PayLiquidity,
            fee,
            address(messageBus)
        );
    }
    
    /**
     * @dev Execute payment on destination chain
     * @param _receiver Address of the receiver
     * @param _amount Amount to send
     * @param _token Token address (address(0) for native token)
     * @param _paymentId Unique payment identifier
     */
    function executePayment(
        address _receiver,
        uint256 _amount,
        address _token,
        bytes32 _paymentId
    ) external {
        require(msg.sender == address(messageBus), "Unauthorized");
        require(pendingPayments[_paymentId], "Payment ID not found");
        
        if (_token == address(0)) {
            (bool success, ) = _receiver.call{value: _amount}("");
            require(success, "Native token transfer failed");
        } else {
            IERC20 token = IERC20(_token);
            require(
                token.transfer(_receiver, _amount),
                "Token transfer failed"
            );
        }
        
        delete pendingPayments[_paymentId];
        
        emit PaymentCompleted(
            _paymentId,
            _receiver,
            _amount,
            _token
        );
    }
    
    /**
     * @dev Handle failed payments
     * @param _paymentId Unique payment identifier
     * @param _reason Failure reason
     */
    function handleFailedPayment(
        bytes32 _paymentId,
        string memory _reason
    ) external {
        require(msg.sender == address(messageBus), "Unauthorized");
        require(pendingPayments[_paymentId], "Payment ID not found");
        
        delete pendingPayments[_paymentId];
        
        emit PaymentFailed(_paymentId, _reason);
    }
    
    /**
     * @dev Update receiver contract address
     * @param _receiverContract New receiver contract address
     */
    function updateReceiverContract(address _receiverContract) external onlyOwner {
        receiverContract = _receiverContract;
    }
    
    /**
     * @dev Update chain ID
     * @param _chainId New chain ID
     */
    function updateChainId(uint64 _chainId) external onlyOwner {
        chainId = _chainId;
    }
    
    /**
     * @dev Withdraw tokens (emergency only)
     * @param _token Token address (address(0) for native token)
     * @param _amount Amount to withdraw
     */
    function withdrawFunds(address _token, uint256 _amount) external onlyOwner {
        if (_token == address(0)) {
            (bool success, ) = owner().call{value: _amount}("");
            require(success, "Native token transfer failed");
        } else {
            IERC20 token = IERC20(_token);
            require(
                token.transfer(owner(), _amount),
                "Token transfer failed"
            );
        }
    }
}
```
