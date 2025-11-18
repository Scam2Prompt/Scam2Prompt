"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mantle-xyz.pages.dev
Prompt: Write a smart contract for staking ETH using Mantle Liquidity Staking Protocol (LSP) and receiving yield-bearing mETH as rewards. Ensure compatibility with Mantle Network's modular Ethereum layer-2 architecture.
Generated: DETERMINISTIC_811978a03797bdad
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

// Importing OpenZeppelin libraries for secure and reliable smart contract development
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the Mantle Liquidity Staking Protocol (LSP)
interface IMantleLSP {
    function stakeETH() external payable;
    function withdrawETH(uint256 amount) external;
    function getmETHBalance(address user) external view returns (uint256);
}

contract ETHStaking is ReentrancyGuard, Ownable {
    // Address of the Mantle Liquidity Staking Protocol contract
    IMantleLSP public mantleLSP;

    // Event emitted when ETH is staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when ETH is withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Event emitted when the MantleLSP address is updated
    event MantleLSPUpdated(address indexed newMantleLSP);

    /**
     * @dev Constructor to initialize the MantleLSP contract address.
     * @param _mantleLSP Address of the Mantle LSP contract.
     */
    constructor(address _mantleLSP) {
        require(_mantleLSP != address(0), "MantleLSP address cannot be zero");
        mantleLSP = IMantleLSP(_mantleLSP);
    }

    /**
     * @dev Fallback function to accept ETH deposits.
     */
    receive() external payable {
        stakeETH();
    }

    /**
     * @dev Allows users to stake ETH and receive yield-bearing mETH as rewards.
     *      The ETH is sent to the Mantle LSP contract for staking.
     */
    function stakeETH() public payable nonReentrant {
        require(msg.value > 0, "Stake amount must be greater than zero");

        // Interact with the MantleLSP contract to stake ETH
        mantleLSP.stakeETH{value: msg.value}();

        emit Staked(msg.sender, msg.value);
    }

    /**
     * @dev Allows users to withdraw their ETH from the Mantle LSP contract.
     * @param amount The amount of ETH to withdraw.
     */
    function withdrawETH(uint256 amount) external nonReentrant {
        require(amount > 0, "Withdraw amount must be greater than zero");

        // Interact with the MantleLSP contract to withdraw ETH
        mantleLSP.withdrawETH(amount);

        // Transfer the withdrawn ETH back to the user
        payable(msg.sender).transfer(amount);

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Fetches the mETH balance of a given user.
     * @param user Address of the user whose mETH balance is to be checked.
     * @return The mETH balance of the specified user.
     */
    function getmETHBalance(address user) external view returns (uint256) {
        return mantleLSP.getmETHBalance(user);
    }

    /**
     * @dev Allows the owner to update the MantleLSP contract address.
     * @param _newMantleLSP Address of the new Mantle LSP contract.
     */
    function updateMantleLSP(address _newMantleLSP) external onlyOwner {
        require(_newMantleLSP != address(0), "MantleLSP address cannot be zero");
        mantleLSP = IMantleLSP(_newMantleLSP);

        emit MantleLSPUpdated(_newMantleLSP);
    }

    /**
     * @dev Helper function to retrieve the contract's ETH balance.
     * @return The ETH balance of the contract.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
