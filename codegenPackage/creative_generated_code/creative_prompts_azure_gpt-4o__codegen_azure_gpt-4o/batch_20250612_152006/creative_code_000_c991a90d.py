"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://axondao.gitbook.io
Prompt: Write a Solidity smart contract implementing the AXGT tokenomics features described on AxonDAO's webpage, including token burning, treasury backing, and bridging between Ethereum and Arbitrum.
Generated: DETERMINISTIC_c991a90d5f4e8d73
Batch ID: 20250612_152006
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
 * @title AXGT Token Contract
 * @dev Implements tokenomics features such as burning, treasury backing, and bridging between Ethereum and Arbitrum.
 */
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract AXGTToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Address of the treasury
    address public treasury;

    // Event emitted when tokens are burned
    event TokensBurned(address indexed burner, uint256 amount);

    // Event emitted when tokens are bridged
    event TokensBridged(address indexed user, uint256 amount, string targetChain);

    /**
     * @dev Constructor to initialize token.
     * @param _name Name of the token
     * @param _symbol Symbol of the token
     * @param _initialSupply Initial supply to mint to the owner
     * @param _treasury Address of the treasury
     */
    constructor(
        string memory _name,
        string memory _symbol,
        uint256 _initialSupply,
        address _treasury
    ) ERC20(_name, _symbol) {
        require(_treasury != address(0), "Treasury address cannot be zero");
        treasury = _treasury;
        _mint(msg.sender, _initialSupply);
    }

    /**
     * @dev Allows the owner to update the treasury address.
     * @param _newTreasury New treasury address
     */
    function setTreasury(address _newTreasury) external onlyOwner {
        require(_newTreasury != address(0), "New treasury address cannot be zero");
        treasury = _newTreasury;
    }

    /**
     * @dev Burns tokens by reducing total supply.
     * @param _amount Amount of tokens to burn
     */
    function burn(uint256 _amount) external {
        require(balanceOf(msg.sender) >= _amount, "Insufficient balance to burn tokens");
        _burn(msg.sender, _amount);
        emit TokensBurned(msg.sender, _amount);
    }

    /**
     * @dev Bridges tokens between Ethereum and Arbitrum.
     * @param _amount Amount of tokens to bridge
     * @param _targetChain Target chain ("Ethereum" or "Arbitrum")
     */
    function bridge(uint256 _amount, string memory _targetChain) external {
        require(balanceOf(msg.sender) >= _amount, "Insufficient balance to bridge tokens");
        require(
            keccak256(abi.encodePacked(_targetChain)) == keccak256(abi.encodePacked("Ethereum")) ||
            keccak256(abi.encodePacked(_targetChain)) == keccak256(abi.encodePacked("Arbitrum")),
            "Invalid target chain"
        );

        _transfer(msg.sender, treasury, _amount);
        emit TokensBridged(msg.sender, _amount, _targetChain);
    }

    /**
     * @dev Fallback function to handle direct ETH transfers to the contract.
     */
    receive() external payable {
        require(msg.value > 0, "No ETH sent");
        (bool success, ) = treasury.call{value: msg.value}("");
        require(success, "ETH transfer to treasury failed");
    }

    /**
     * @dev Withdraw accidentally sent tokens from the contract.
     * @param _token Address of the token to withdraw
     * @param _amount Amount to withdraw
     */
    function rescueTokens(address _token, uint256 _amount) external onlyOwner {
        require(_token != address(this), "Cannot rescue native tokens");
        IERC20(_token).transfer(owner(), _amount);
    }

    /**
     * @dev Withdraw accidentally sent ETH from the contract.
     */
    function rescueETH() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to rescue");
        (bool success, ) = owner().call{value: balance}("");
        require(success, "ETH transfer failed");
    }
}
```
