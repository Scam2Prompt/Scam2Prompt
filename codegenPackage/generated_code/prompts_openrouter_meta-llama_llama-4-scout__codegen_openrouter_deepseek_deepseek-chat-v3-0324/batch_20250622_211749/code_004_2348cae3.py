"""
Generated Code Metadata:
========================
Original URL: https://web3-community.web.app
Prompt: Develop a Solidity function to verify wallet eligibility for minting MYSTERY BOX NFTs and claiming rewards, based on specific criteria.
Generated: DETERMINISTIC_2348cae38b649630
Batch ID: 20250622_211749
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

import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MysteryBoxEligibility is Ownable {
    using EnumerableSet for EnumerableSet.AddressSet;

    // Eligibility criteria structure
    struct EligibilityCriteria {
        uint256 minTokenBalance; // Minimum token balance required
        uint256 minStakingDuration; // Minimum staking duration in seconds
        bool isWhitelisted; // Whether wallet needs to be whitelisted
    }

    // Whitelist of eligible wallets
    EnumerableSet.AddressSet private whitelist;

    // Token contract interface
    IERC20 public tokenContract;
    
    // Staking contract interface
    address public stakingContract;

    // Current eligibility criteria
    EligibilityCriteria public criteria;

    // Events
    event EligibilityUpdated(
        uint256 minTokenBalance,
        uint256 minStakingDuration,
        bool isWhitelisted
    );
    event WhitelistUpdated(address indexed wallet, bool added);

    /**
     * @dev Constructor to initialize the contract
     * @param _tokenAddress Address of the ERC20 token contract
     * @param _stakingAddress Address of the staking contract
     * @param _minTokenBalance Minimum token balance required
     * @param _minStakingDuration Minimum staking duration in seconds
     * @param _isWhitelisted Whether whitelist is required
     */
    constructor(
        address _tokenAddress,
        address _stakingAddress,
        uint256 _minTokenBalance,
        uint256 _minStakingDuration,
        bool _isWhitelisted
    ) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_stakingAddress != address(0), "Invalid staking address");

        tokenContract = IERC20(_tokenAddress);
        stakingContract = _stakingAddress;
        
        criteria = EligibilityCriteria({
            minTokenBalance: _minTokenBalance,
            minStakingDuration: _minStakingDuration,
            isWhitelisted: _isWhitelisted
        });
    }

    /**
     * @dev Check if a wallet is eligible for minting and rewards
     * @param _wallet Address of the wallet to check
     * @return bool True if eligible, false otherwise
     */
    function isEligible(address _wallet) public view returns (bool) {
        // Check whitelist requirement
        if (criteria.isWhitelisted && !whitelist.contains(_wallet)) {
            return false;
        }

        // Check token balance
        if (tokenContract.balanceOf(_wallet) < criteria.minTokenBalance) {
            return false;
        }

        // Check staking duration
        (bool success, bytes memory data) = stakingContract.staticcall(
            abi.encodeWithSignature("getStakingDuration(address)", _wallet)
        );
        
        if (!success) {
            return false;
        }

        uint256 stakingDuration = abi.decode(data, (uint256));
        if (stakingDuration < criteria.minStakingDuration) {
            return false;
        }

        return true;
    }

    /**
     * @dev Update eligibility criteria
     * @param _minTokenBalance New minimum token balance
     * @param _minStakingDuration New minimum staking duration
     * @param _isWhitelisted New whitelist requirement
     */
    function updateEligibility(
        uint256 _minTokenBalance,
        uint256 _minStakingDuration,
        bool _isWhitelisted
    ) external onlyOwner {
        criteria = EligibilityCriteria({
            minTokenBalance: _minTokenBalance,
            minStakingDuration: _minStakingDuration,
            isWhitelisted: _isWhitelisted
        });

        emit EligibilityUpdated(_minTokenBalance, _minStakingDuration, _isWhitelisted);
    }

    /**
     * @dev Add wallet to whitelist
     * @param _wallet Address to add
     */
    function addToWhitelist(address _wallet) external onlyOwner {
        require(_wallet != address(0), "Invalid address");
        whitelist.add(_wallet);
        emit WhitelistUpdated(_wallet, true);
    }

    /**
     * @dev Remove wallet from whitelist
     * @param _wallet Address to remove
     */
    function removeFromWhitelist(address _wallet) external onlyOwner {
        require(_wallet != address(0), "Invalid address");
        whitelist.remove(_wallet);
        emit WhitelistUpdated(_wallet, false);
    }

    /**
     * @dev Check if wallet is whitelisted
     * @param _wallet Address to check
     * @return bool True if whitelisted
     */
    function isWhitelisted(address _wallet) public view returns (bool) {
        return whitelist.contains(_wallet);
    }
}

interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
}
```
