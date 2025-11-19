"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdcprinter.xyz
Prompt: How can I implement a smart contract that automatically distributes USDC rewards to holders of the $UPRINT token on Ethereum?
Generated: DETERMINISTIC_5d9d60dc4efdde99
Batch ID: 20250612_160319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title RewardDistributor
 * @dev A smart contract that automates the distribution of USDC rewards to holders of the $UPRINT token.
 */
contract RewardDistributor {
    // Address of the $UPRINT token contract
    address public uPrintToken;

    // Address of the USDC token contract
    address public usdcToken;

    // Event emitted when rewards are distributed
    event RewardsDistributed(uint256 totalRewards);

    // Modifier to check if the caller is the owner of the contract
    address public owner;

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the $UPRINT and USDC token addresses.
     * @param _uPrintToken Address of the $UPRINT token contract.
     * @param _usdcToken Address of the USDC token contract.
     */
    constructor(address _uPrintToken, address _usdcToken) {
        require(
            _uPrintToken != address(0) && _usdcToken != address(0),
            "Invalid token address"
        );
        uPrintToken = _uPrintToken;
        usdcToken = _usdcToken;
        owner = msg.sender;
    }

    /**
     * @dev Distributes USDC rewards to $UPRINT token holders proportionally to their holdings.
     * The rewards to be distributed should be sent to this contract beforehand.
     */
    function distributeRewards() external onlyOwner {
        // Interface for interacting with the $UPRINT token contract
        IERC20 uPrint = IERC20(uPrintToken);
        IERC20 usdc = IERC20(usdcToken);

        uint256 totalSupply = uPrint.totalSupply();
        require(totalSupply > 0, "No $UPRINT tokens exist");

        uint256 totalRewards = usdc.balanceOf(address(this));
        require(totalRewards > 0, "No USDC rewards available");

        // Iterate through all $UPRINT token holders to distribute rewards
        for (uint256 i = 0; i < totalSupply; i++) {
            address holder = uPrint.holderAt(i); // Hypothetical method to fetch token holders
            uint256 holderBalance = uPrint.balanceOf(holder);
            uint256 reward = (holderBalance * totalRewards) / totalSupply;

            // Transfer the reward to the holder
            require(
                usdc.transfer(holder, reward),
                "USDC transfer failed"
            );
        }

        emit RewardsDistributed(totalRewards);
    }

    /**
     * @dev Allows the owner to withdraw any leftover USDC from the contract.
     */
    function withdrawUSDC(uint256 amount) external onlyOwner {
        IERC20 usdc = IERC20(usdcToken);
        require(usdc.transfer(owner, amount), "Withdrawal failed");
    }
}

/**
 * @dev Interface for ERC20 tokens (USDC and $UPRINT).
 */
interface IERC20 {
    function totalSupply() external view returns (uint256);

    function balanceOf(address account) external view returns (uint256);

    function transfer(address recipient, uint256 amount)
        external
        returns (bool);

    // Hypothetical method to fetch token holders (not part of standard ERC20).
    function holderAt(uint256 index) external view returns (address);
}
```
