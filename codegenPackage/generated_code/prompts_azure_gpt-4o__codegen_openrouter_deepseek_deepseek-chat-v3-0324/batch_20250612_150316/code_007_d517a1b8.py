"""
Generated Code Metadata:
========================
Original URL: https://bibbydivs.com
Prompt: Develop a Solidity smart contract that implements a mechanism for redistributing exit fees to all token holders proportionally, as described on BibbyDivs.com.
Generated: DETERMINISTIC_d517a1b833662c40
Batch ID: 20250612_150316
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract BibbyDivsToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Exit fee percentage (e.g., 500 for 5%)
    uint256 public exitFeePercentage;
    
    // Total fees collected
    uint256 public totalFeesCollected;
    
    // Total shares for fee distribution
    uint256 public totalShares;
    
    // Mapping to track shares per address
    mapping(address => uint256) private _shares;
    
    // Mapping to track claimed fees per address
    mapping(address => uint256) private _claimedFees;
    
    // Events
    event ExitFeeCollected(address indexed from, uint256 amount);
    event FeesDistributed(address indexed to, uint256 amount);
    event ExitFeePercentageUpdated(uint256 newPercentage);

    constructor(
        string memory name,
        string memory symbol,
        uint256 initialSupply,
        uint256 _exitFeePercentage
    ) ERC20(name, symbol) {
        _mint(msg.sender, initialSupply);
        exitFeePercentage = _exitFeePercentage;
        totalShares = initialSupply;
        _shares[msg.sender] = initialSupply;
    }

    /**
     * @dev Overrides transfer function to collect exit fees
     */
    function transfer(address recipient, uint256 amount) public override returns (bool) {
        uint256 fee = amount.mul(exitFeePercentage).div(10000);
        uint256 amountAfterFee = amount.sub(fee);
        
        // Collect fee
        if (fee > 0) {
            totalFeesCollected = totalFeesCollected.add(fee);
            emit ExitFeeCollected(msg.sender, fee);
        }
        
        // Update shares
        _updateShares(msg.sender, recipient, amountAfterFee);
        
        // Perform transfer
        super.transfer(recipient, amountAfterFee);
        return true;
    }

    /**
     * @dev Overrides transferFrom function to collect exit fees
     */
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) public override returns (bool) {
        uint256 fee = amount.mul(exitFeePercentage).div(10000);
        uint256 amountAfterFee = amount.sub(fee);
        
        // Collect fee
        if (fee > 0) {
            totalFeesCollected = totalFeesCollected.add(fee);
            emit ExitFeeCollected(sender, fee);
        }
        
        // Update shares
        _updateShares(sender, recipient, amountAfterFee);
        
        // Perform transfer
        super.transferFrom(sender, recipient, amountAfterFee);
        return true;
    }

    /**
     * @dev Updates shares when tokens are transferred
     */
    function _updateShares(address sender, address recipient, uint256 amount) private {
        if (sender != address(0)) {
            _shares[sender] = _shares[sender].sub(amount);
        }
        if (recipient != address(0)) {
            _shares[recipient] = _shares[recipient].add(amount);
        }
    }

    /**
     * @dev Calculates unclaimed fees for an address
     */
    function calculateUnclaimedFees(address account) public view returns (uint256) {
        if (totalShares == 0) return 0;
        uint256 totalClaimable = totalFeesCollected.mul(_shares[account]).div(totalShares);
        return totalClaimable.sub(_claimedFees[account]);
    }

    /**
     * @dev Claims accumulated fees
     */
    function claimFees() public {
        uint256 unclaimed = calculateUnclaimedFees(msg.sender);
        require(unclaimed > 0, "No fees to claim");
        
        _claimedFees[msg.sender] = _claimedFees[msg.sender].add(unclaimed);
        _mint(msg.sender, unclaimed);
        
        emit FeesDistributed(msg.sender, unclaimed);
    }

    /**
     * @dev Updates exit fee percentage (owner only)
     */
    function setExitFeePercentage(uint256 newPercentage) public onlyOwner {
        require(newPercentage <= 1000, "Fee cannot exceed 10%");
        exitFeePercentage = newPercentage;
        emit ExitFeePercentageUpdated(newPercentage);
    }

    /**
     * @dev Gets the current shares for an address
     */
    function sharesOf(address account) public view returns (uint256) {
        return _shares[account];
    }

    /**
     * @dev Gets the claimed fees for an address
     */
    function claimedFeesOf(address account) public view returns (uint256) {
        return _claimedFees[account];
    }
}
```
