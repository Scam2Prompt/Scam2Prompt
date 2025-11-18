"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://beefy.pages.dev
Prompt: Develop a smart contract that interacts with Beefy Finance to automatically reinvest earnings into a vault.
Generated: DETERMINISTIC_9c7b7ded0da36e93
Batch ID: 20250612_150342
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
 * @title AutoCompounder
 * @dev A smart contract that interacts with the Beefy Finance protocol to automatically reinvest earnings into a vault.
 * This contract assumes existing vault contracts on Beefy Finance.
 */

interface IBeefyVault {
    function deposit(uint256 _amount) external;
    function withdraw(uint256 _amount) external;
    function balanceOf(address _account) external view returns (uint256);
    function getPricePerFullShare() external view returns (uint256);
    function earn() external;
}

interface IERC20 {
    function approve(address _spender, uint256 _amount) external returns (bool);
    function transfer(address _to, uint256 _amount) external returns (bool);
    function transferFrom(address _from, address _to, uint256 _amount) external returns (bool);
    function balanceOf(address _account) external view returns (uint256);
}

contract AutoCompounder {
    // State variables
    address public owner; // Owner of the contract
    IBeefyVault public beefyVault; // Beefy Finance vault instance
    IERC20 public rewardToken; // Reward token used in the vault

    /**
     * @dev Emitted when earnings are reinvested.
     */
    event Reinvest(address indexed user, uint256 amount);

    /**
     * @dev Emitted when ownership changes.
     */
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    modifier onlyOwner() {
        require(msg.sender == owner, "AutoCompounder: Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with vault and token addresses.
     * @param _beefyVault Address of the Beefy Vault.
     * @param _rewardToken Address of the reward token used by the vault.
     */
    constructor(address _beefyVault, address _rewardToken) {
        require(_beefyVault != address(0), "AutoCompounder: Vault address cannot be zero");
        require(_rewardToken != address(0), "AutoCompounder: Reward token address cannot be zero");

        owner = msg.sender;
        beefyVault = IBeefyVault(_beefyVault);
        rewardToken = IERC20(_rewardToken);
    }

    /**
     * @dev Transfers ownership of the contract to a new address.
     * @param _newOwner Address of the new owner.
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "AutoCompounder: New owner address cannot be zero");
        emit OwnershipTransferred(owner, _newOwner);
        owner = _newOwner;
    }

    /**
     * @dev Deposits rewards back into the Beefy Vault to reinvest earnings.
     */
    function reinvest() external onlyOwner {
        uint256 rewardBalance = rewardToken.balanceOf(address(this));
        require(rewardBalance > 0, "AutoCompounder: No rewards to reinvest");

        // Approve the vault to spend the reward tokens
        rewardToken.approve(address(beefyVault), rewardBalance);

        // Deposit the reward tokens back into the vault
        beefyVault.deposit(rewardBalance);

        emit Reinvest(msg.sender, rewardBalance);
    }

    /**
     * @dev Emergency withdraw function to rescue tokens from the contract.
     * @param _token Address of the token to be rescued.
     * @param _to Address to send the tokens to.
     * @param _amount Amount of tokens to rescue.
     */
    function emergencyWithdraw(address _token, address _to, uint256 _amount) external onlyOwner {
        require(_to != address(0), "AutoCompounder: Recipient address cannot be zero");
        IERC20(_token).transfer(_to, _amount);
    }
}
```
