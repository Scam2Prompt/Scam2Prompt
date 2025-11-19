"""
Generated Code Metadata:
========================
Original URL: https://v2-celer.network
Prompt: Create a smart contract that interacts with Celer Network's cChannel layer for off-chain transaction processing.
Generated: DETERMINISTIC_9dc77dad57a2c4e8
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

import "@openzeppelin/contracts/utils/Address.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

interface ICelerChannel {
    function sendTransferOut(
        address _receiver,
        address _token,
        uint256 _amount,
        uint64 _dstChainId,
        uint64 _nonce,
        uint32 _maxSlippage
    ) external;

    function verifyTransferIn(
        bytes32 _transferId,
        address _receiver,
        address _token,
        uint256 _amount,
        bytes32 _requestHash
    ) external returns (bool);
}

contract CelerChannelInteraction is ReentrancyGuard {
    using Address for address;
    using SafeERC20 for IERC20;

    ICelerChannel public celerChannel;
    address public owner;
    uint64 public chainId;

    event DepositInitiated(
        address indexed sender,
        address indexed token,
        uint256 amount,
        uint64 dstChainId,
        uint64 nonce
    );

    event WithdrawalCompleted(
        bytes32 indexed transferId,
        address indexed receiver,
        address indexed token,
        uint256 amount
    );

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    constructor(address _celerChannel, uint64 _chainId) {
        require(_celerChannel != address(0), "Invalid celer channel address");
        celerChannel = ICelerChannel(_celerChannel);
        chainId = _chainId;
        owner = msg.sender;
    }

    function deposit(
        address _token,
        uint256 _amount,
        uint64 _dstChainId,
        uint32 _maxSlippage
    ) external payable nonReentrant {
        require(_amount > 0, "Amount must be greater than 0");
        require(_dstChainId != chainId, "Cannot deposit to same chain");

        if (_token == address(0)) {
            require(msg.value == _amount, "ETH amount mismatch");
        } else {
            IERC20 token = IERC20(_token);
            uint256 balanceBefore = token.balanceOf(address(this));
            token.safeTransferFrom(msg.sender, address(this), _amount);
            uint256 balanceAfter = token.balanceOf(address(this));
            require(balanceAfter - balanceBefore == _amount, "Token transfer failed");
        }

        uint64 nonce = uint64(block.timestamp);
        
        celerChannel.sendTransferOut(
            msg.sender,
            _token,
            _amount,
            _dstChainId,
            nonce,
            _maxSlippage
        );

        emit DepositInitiated(msg.sender, _token, _amount, _dstChainId, nonce);
    }

    function withdraw(
        bytes32 _transferId,
        address _token,
        uint256 _amount,
        bytes32 _requestHash
    ) external nonReentrant {
        bool verified = celerChannel.verifyTransferIn(
            _transferId,
            msg.sender,
            _token,
            _amount,
            _requestHash
        );
        require(verified, "Transfer verification failed");

        if (_token == address(0)) {
            (bool success, ) = msg.sender.call{value: _amount}("");
            require(success, "ETH transfer failed");
        } else {
            IERC20(_token).safeTransfer(msg.sender, _amount);
        }

        emit WithdrawalCompleted(_transferId, msg.sender, _token, _amount);
    }

    function changeOwner(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "Invalid owner address");
        owner = _newOwner;
    }

    function emergencyWithdraw(address _token) external onlyOwner {
        if (_token == address(0)) {
            (bool success, ) = owner.call{value: address(this).balance}("");
            require(success, "ETH transfer failed");
        } else {
            IERC20 token = IERC20(_token);
            token.safeTransfer(owner, token.balanceOf(address(this)));
        }
    }

    receive() external payable {}
}
```
