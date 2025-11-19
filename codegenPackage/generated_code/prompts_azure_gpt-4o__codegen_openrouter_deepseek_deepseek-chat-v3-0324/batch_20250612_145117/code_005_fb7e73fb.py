"""
Generated Code Metadata:
========================
Original URL: https://automation-feat-front-3795-display-log-tr-chainlinklabs.vercel.app
Prompt: Create a Solidity smart contract that uses Chainlink Automation to monitor LINK token balance and trigger an action when the balance falls below a threshold.
Generated: DETERMINISTIC_fb7e73fbfce9837f
Batch ID: 20250612_145117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

// Import Chainlink contracts
import "@chainlink/contracts/src/v0.8/interfaces/AutomationCompatibleInterface.sol";
import "@chainlink/contracts/src/v0.8/interfaces/LinkTokenInterface.sol";

contract LinkBalanceMonitor is AutomationCompatibleInterface {
    // Chainlink LINK token interface
    LinkTokenInterface public immutable LINK_TOKEN;
    
    // Threshold below which action will be triggered
    uint256 public immutable THRESHOLD;
    
    // Address to monitor
    address public immutable TARGET_ADDRESS;
    
    // Event emitted when balance is low
    event LowLinkBalance(uint256 currentBalance, uint256 threshold);
    
    // Event emitted when action is performed
    event ActionPerformed(uint256 currentBalance, uint256 threshold);
    
    /**
     * @param _linkTokenAddress The address of the LINK token contract
     * @param _threshold The minimum LINK balance threshold (in juels)
     * @param _targetAddress The address whose balance to monitor
     */
    constructor(
        address _linkTokenAddress,
        uint256 _threshold,
        address _targetAddress
    ) {
        LINK_TOKEN = LinkTokenInterface(_linkTokenAddress);
        THRESHOLD = _threshold;
        TARGET_ADDRESS = _targetAddress;
    }
    
    /**
     * @dev Chainlink Automation checkUpkeep function
     * @param /*checkData*/ Not used in this implementation
     * @return upkeepNeeded Whether upkeep is needed
     * @return /*performData*/ Not used in this implementation
     */
    function checkUpkeep(
        bytes calldata /*checkData*/
    )
        external
        view
        override
        returns (bool upkeepNeeded, bytes memory /*performData*/)
    {
        uint256 currentBalance = LINK_TOKEN.balanceOf(TARGET_ADDRESS);
        upkeepNeeded = currentBalance < THRESHOLD;
    }
    
    /**
     * @dev Chainlink Automation performUpkeep function
     * @param /*performData*/ Not used in this implementation
     */
    function performUpkeep(bytes calldata /*performData*/) external override {
        uint256 currentBalance = LINK_TOKEN.balanceOf(TARGET_ADDRESS);
        
        if (currentBalance >= THRESHOLD) {
            revert("LinkBalanceMonitor: Balance above threshold");
        }
        
        emit LowLinkBalance(currentBalance, THRESHOLD);
        
        // Custom action logic goes here
        // For example: transfer LINK tokens to the target address
        // Or notify an external system
        
        emit ActionPerformed(currentBalance, THRESHOLD);
    }
    
    /**
     * @dev Allows withdrawal of LINK tokens from this contract
     * @param _to The address to send LINK tokens to
     * @param _amount The amount of LINK tokens to send
     */
    function withdrawLink(address _to, uint256 _amount) external {
        require(
            LINK_TOKEN.transfer(_to, _amount),
            "LinkBalanceMonitor: LINK transfer failed"
        );
    }
}
```
