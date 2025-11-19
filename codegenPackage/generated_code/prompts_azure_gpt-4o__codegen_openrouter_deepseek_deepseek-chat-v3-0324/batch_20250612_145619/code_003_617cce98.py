"""
Generated Code Metadata:
========================
Original URL: https://tonfor.com
Prompt: Create a smart contract that integrates with The Open Network Blockchain (TON) to manage fees in TON or issued tokens for liquidity pools, as described on the TonFOR platform.
Generated: DETERMINISTIC_617cce981e529c28
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```typescript
// SPDX-License-Identifier: MIT
pragma ton-solidity >= 0.57.0;

import "@broxus/contracts/contracts/libraries/MsgFlag.sol";

/**
 * @title FeeManager
 * @dev Smart contract for managing fees in TON or issued tokens for liquidity pools
 */
contract FeeManager {
    uint16 constant FEE_PRECISION = 10000; // 1 = 0.01%
    uint16 public protocolFee; // Protocol fee percentage (in basis points)
    address public protocolFeeReceiver; // Address to receive protocol fees
    address public owner; // Contract owner

    // Token address => Fee percentage
    mapping(address => uint16) public tokenFees;
    // Token address => Fee receiver address
    mapping(address => address) public tokenFeeReceivers;

    // Events
    event FeeUpdated(address indexed token, uint16 newFee);
    event FeeReceiverUpdated(address indexed token, address newReceiver);
    event ProtocolFeeUpdated(uint16 newFee);
    event ProtocolFeeReceiverUpdated(address newReceiver);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);
    event FeesCollected(address indexed token, uint128 amount, address indexed receiver);

    modifier onlyOwner() {
        require(msg.sender == owner, 100, "Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor
     * @param _protocolFee Initial protocol fee (in basis points)
     * @param _protocolFeeReceiver Address to receive protocol fees
     * @param _owner Contract owner address
     */
    constructor(uint16 _protocolFee, address _protocolFeeReceiver, address _owner) public {
        require(_protocolFee <= FEE_PRECISION, 101, "Fee exceeds maximum");
        protocolFee = _protocolFee;
        protocolFeeReceiver = _protocolFeeReceiver;
        owner = _owner;
    }

    /**
     * @dev Set fee for a specific token
     * @param token Token address
     * @param fee Fee percentage (in basis points)
     */
    function setTokenFee(address token, uint16 fee) external onlyOwner {
        require(fee <= FEE_PRECISION, 101, "Fee exceeds maximum");
        tokenFees[token] = fee;
        emit FeeUpdated(token, fee);
    }

    /**
     * @dev Set fee receiver for a specific token
     * @param token Token address
     * @param receiver Address to receive fees for this token
     */
    function setTokenFeeReceiver(address token, address receiver) external onlyOwner {
        tokenFeeReceivers[token] = receiver;
        emit FeeReceiverUpdated(token, receiver);
    }

    /**
     * @dev Update protocol fee
     * @param newFee New protocol fee percentage (in basis points)
     */
    function setProtocolFee(uint16 newFee) external onlyOwner {
        require(newFee <= FEE_PRECISION, 101, "Fee exceeds maximum");
        protocolFee = newFee;
        emit ProtocolFeeUpdated(newFee);
    }

    /**
     * @dev Update protocol fee receiver
     * @param newReceiver New protocol fee receiver address
     */
    function setProtocolFeeReceiver(address newReceiver) external onlyOwner {
        protocolFeeReceiver = newReceiver;
        emit ProtocolFeeReceiverUpdated(newReceiver);
    }

    /**
     * @dev Transfer ownership of the contract
     * @param newOwner Address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), 102, "New owner cannot be zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Collect fees for a token
     * @param token Token address (address(0) for TON)
     * @param amount Amount to collect
     */
    function collectFees(address token, uint128 amount) external {
        uint16 fee = token == address(0) ? protocolFee : tokenFees[token];
        address receiver = token == address(0) ? protocolFeeReceiver : tokenFeeReceivers[token];

        require(fee > 0, 103, "Fee not set for this token");
        require(receiver != address(0), 104, "Fee receiver not set for this token");

        uint128 feeAmount = (amount * fee) / FEE_PRECISION;
        
        if (token == address(0)) {
            // Transfer TON
            receiver.transfer(feeAmount, false, MsgFlag.ALL_NOT_RESERVED);
        } else {
            // Transfer token
            TvmCell payload = tvm.encodeBody(ITokenWallet(token).transfer, receiver, feeAmount);
            token.transfer({value: 0, flag: MsgFlag.ALL_NOT_RESERVED, body: payload});
        }

        emit FeesCollected(token, feeAmount, receiver);
    }

    /**
     * @dev Fallback function to receive plain TON transfers
     */
    receive() external pure {}
}

/**
 * @dev Minimal token wallet interface for token transfers
 */
interface ITokenWallet {
    function transfer(address dest, uint128 tokens) external;
}
```
