"""
Generated Code Metadata:
========================
Original URL: https://bafybeicc34wxgmwfldpiehsmb6azuurx52lonvbu63phtv6fto7rbacmja.ipfs.dweb.link
Prompt: Provide an example of generating yield and setting fees on bridging volume using Hyperlane's features.
Generated: DETERMINISTIC_1dbfac301f63d5c7
Batch ID: 20250612_161035
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
import "@hyperlane-xyz/core/contracts/interfaces/IInterchainGasPaymaster.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";

contract YieldAndFeeManager is Ownable {
    using SafeERC20 for IERC20;

    IMailbox public immutable mailbox;
    IInterchainGasPaymaster public immutable gasPaymaster;
    
    // Token used for bridging and fees
    IERC20 public immutable token;
    
    // Fee percentage (in basis points, e.g. 100 = 1%)
    uint256 public feeBps;
    
    // Yield percentage (in basis points)
    uint256 public yieldBps;
    
    // Destination chain ID
    uint32 public destinationChainId;
    
    // Destination contract address
    address public destinationContract;
    
    // Track total fees collected
    uint256 public totalFeesCollected;
    
    // Track total yield generated
    uint256 public totalYieldGenerated;

    event FeesUpdated(uint256 newFeeBps);
    event YieldUpdated(uint256 newYieldBps);
    event FeesCollected(address indexed user, uint256 amount);
    event YieldGenerated(address indexed user, uint256 amount);
    event Bridged(
        address indexed sender,
        uint32 indexed destinationChainId,
        address indexed recipient,
        uint256 amount,
        uint256 fee,
        uint256 yield
    );

    constructor(
        address _mailbox,
        address _gasPaymaster,
        address _token,
        uint32 _destinationChainId,
        address _destinationContract,
        uint256 _feeBps,
        uint256 _yieldBps
    ) {
        mailbox = IMailbox(_mailbox);
        gasPaymaster = IInterchainGasPaymaster(_gasPaymaster);
        token = IERC20(_token);
        destinationChainId = _destinationChainId;
        destinationContract = _destinationContract;
        feeBps = _feeBps;
        yieldBps = _yieldBps;
    }

    function setFeeBps(uint256 _feeBps) external onlyOwner {
        require(_feeBps <= 1000, "Fee too high"); // Max 10%
        feeBps = _feeBps;
        emit FeesUpdated(_feeBps);
    }

    function setYieldBps(uint256 _yieldBps) external onlyOwner {
        require(_yieldBps <= 1000, "Yield too high"); // Max 10%
        yieldBps = _yieldBps;
        emit YieldUpdated(_yieldBps);
    }

    function bridgeWithFeesAndYield(
        uint256 amount,
        address recipient
    ) external payable {
        require(amount > 0, "Amount must be positive");
        
        // Calculate fees and yield
        uint256 fee = (amount * feeBps) / 10000;
        uint256 yield = (amount * yieldBps) / 10000;
        uint256 amountAfterFees = amount - fee - yield;
        
        // Transfer tokens from sender
        token.safeTransferFrom(msg.sender, address(this), amount);
        
        // Apply yield (simplified example - in practice you'd invest this)
        totalYieldGenerated += yield;
        emit YieldGenerated(msg.sender, yield);
        
        // Collect fees
        totalFeesCollected += fee;
        emit FeesCollected(msg.sender, fee);
        
        // Approve tokens for destination
        token.safeApprove(address(mailbox), amountAfterFees);
        
        // Encode the recipient and amount for the destination contract
        bytes memory message = abi.encode(recipient, amountAfterFees);
        
        // Send the message via Hyperlane
        bytes32 messageId = mailbox.dispatch(
            destinationChainId,
            bytes32(uint256(uint160(destinationContract))),
            message
        );
        
        // Pay for interchain gas
        uint256 quotedGasAmount = gasPaymaster.quoteGasPayment(
            destinationChainId,
            200000 // Estimated gas amount needed on destination
        );
        require(msg.value >= quotedGasAmount, "Insufficient gas payment");
        gasPaymaster.payForGas{value: quotedGasAmount}(
            messageId,
            destinationChainId,
            200000,
            address(this)
        );
        
        emit Bridged(
            msg.sender,
            destinationChainId,
            recipient,
            amountAfterFees,
            fee,
            yield
        );
    }

    function withdrawFees(address to) external onlyOwner {
        uint256 amount = totalFeesCollected;
        totalFeesCollected = 0;
        token.safeTransfer(to, amount);
    }

    function withdrawYield(address to) external onlyOwner {
        uint256 amount = totalYieldGenerated;
        totalYieldGenerated = 0;
        token.safeTransfer(to, amount);
    }
}
```
