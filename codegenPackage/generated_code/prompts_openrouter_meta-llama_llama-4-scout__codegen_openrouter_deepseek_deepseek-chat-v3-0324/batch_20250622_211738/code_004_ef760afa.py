"""
Generated Code Metadata:
========================
Original URL: https://tokenscreator-free-pro.pages.dev
Prompt: Create a step-by-step guide on how to create a token with a smart contract, including connecting to a wallet, transferring tokens to a liquidity pool, and listing on decentralized trading platforms.
Generated: DETERMINISTIC_ef760afa519b5645
Batch ID: 20250622_211738
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
import "@uniswap/v2-core/contracts/interfaces/IUniswapV2Factory.sol";
import "@uniswap/v2-periphery/contracts/interfaces/IUniswapV2Router02.sol";

/**
 * @title TokenContract
 * @dev ERC20 token with minting, burning, and Uniswap liquidity pool functionality
 */
contract TokenContract is ERC20, Ownable {
    IUniswapV2Router02 public uniswapRouter;
    address public uniswapPair;

    /**
     * @dev Constructor to initialize the token
     * @param name_ Name of the token
     * @param symbol_ Symbol of the token
     * @param initialSupply Initial token supply
     * @param routerAddress Address of Uniswap Router
     */
    constructor(
        string memory name_,
        string memory symbol_,
        uint256 initialSupply,
        address routerAddress
    ) ERC20(name_, symbol_) {
        _mint(msg.sender, initialSupply);
        uniswapRouter = IUniswapV2Router02(routerAddress);
    }

    /**
     * @dev Creates a Uniswap pair for the token
     */
    function createPair() external onlyOwner {
        require(uniswapPair == address(0), "Pair already exists");
        uniswapPair = IUniswapV2Factory(uniswapRouter.factory()).createPair(
            address(this),
            uniswapRouter.WETH()
        );
    }

    /**
     * @dev Adds liquidity to Uniswap pool
     * @param tokenAmount Amount of tokens to add
     * @param ethAmount Amount of ETH to add
     */
    function addLiquidity(uint256 tokenAmount, uint256 ethAmount) external onlyOwner {
        require(uniswapPair != address(0), "Pair not created");
        _approve(address(this), address(uniswapRouter), tokenAmount);
        
        uniswapRouter.addLiquidityETH{value: ethAmount}(
            address(this),
            tokenAmount,
            0,
            0,
            owner(),
            block.timestamp
        );
    }

    /**
     * @dev Mints new tokens
     * @param to Address to mint to
     * @param amount Amount to mint
     */
    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
    }

    /**
     * @dev Burns tokens
     * @param amount Amount to burn
     */
    function burn(uint256 amount) external {
        _burn(msg.sender, amount);
    }

    receive() external payable {}
}
```

```javascript
// Frontend interaction code (using ethers.js and web3-react)
import { ethers } from "ethers";
import { useWeb3React } from "@web3-react/core";
import { InjectedConnector } from "@web3-react/injected-connector";

// Token contract ABI (simplified)
const tokenABI = [
  // ERC20 standard functions
  "function balanceOf(address owner) view returns (uint256)",
  "function transfer(address to, uint256 value) returns (bool)",
  "function approve(address spender, uint256 value) returns (bool)",
  // Custom functions
  "function createPair()",
  "function addLiquidity(uint256 tokenAmount, uint256 ethAmount)",
  "function mint(address to, uint256 amount)",
];

// Wallet connection
const injected = new InjectedConnector({ supportedChainIds: [1, 3, 4, 5, 42] });

export const connectWallet = async () => {
  const { activate } = useWeb3React();
  try {
    await activate(injected);
  } catch (error) {
    console.error("Wallet connection error:", error);
  }
};

// Token operations
export const deployToken = async (
  name,
  symbol,
  initialSupply,
  routerAddress
) => {
  const { library, account } = useWeb3React();
  const signer = library.getSigner(account);
  
  const TokenFactory = new ethers.ContractFactory(
    tokenABI,
    tokenBytecode, // Should be replaced with actual compiled bytecode
    signer
  );

  try {
    const tokenContract = await TokenFactory.deploy(
      name,
      symbol,
      initialSupply,
      routerAddress
    );
    await tokenContract.deployed();
    return tokenContract.address;
  } catch (error) {
    console.error("Deployment error:", error);
    throw error;
  }
};

export const addLiquidity = async (tokenAddress, tokenAmount, ethAmount) => {
  const { library, account } = useWeb3React();
  const signer = library.getSigner(account);
  const tokenContract = new ethers.Contract(tokenAddress, tokenABI, signer);

  try {
    // Approve token transfer
    await tokenContract.approve(tokenAddress, tokenAmount);
    
    // Add liquidity
    const tx = await tokenContract.addLiquidity(tokenAmount, ethAmount, {
      value: ethers.utils.parseEther(ethAmount.toString()),
    });
    await tx.wait();
    return tx.hash;
  } catch (error) {
    console.error("Add liquidity error:", error);
    throw error;
  }
};

export const listOnDex = async (tokenAddress, routerAddress) => {
  const { library, account } = useWeb3React();
  const signer = library.getSigner(account);
  const tokenContract = new ethers.Contract(tokenAddress, tokenABI, signer);

  try {
    // Create pair
    await tokenContract.createPair();
    
    // Get pair address (would need Uniswap factory ABI)
    const factoryABI = ["function getPair(address, address) view returns (address)"];
    const factoryContract = new ethers.Contract(
      IUniswapV2Router02(routerAddress).factory(),
      factoryABI,
      signer
    );
    const pairAddress = await factoryContract.getPair(
      tokenAddress,
      IUniswapV2Router02(routerAddress).WETH()
    );
    return pairAddress;
  } catch (error) {
    console.error("Listing error:", error);
    throw error;
  }
};
```
