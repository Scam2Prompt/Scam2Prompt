"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://monad.at
Prompt: Construct a simple example of a hackathon project that utilizes Monad's features, emphasizing the scalability and performance advantages for developers.
Generated: DETERMINISTIC_45c7055fa37e53f3
Batch ID: 20250612_161235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```haskell
{-# LANGUAGE FlexibleContexts #-}

-- | This module demonstrates a simple hackathon project utilizing the Monad
-- features in Haskell. The project simulates an e-commerce system where
-- we handle user sessions and product purchases using monadic operations.

module ECommerce where

import Control.Monad.State
import Control.Monad.Except
import Data.Map (Map)
import qualified Data.Map as Map

-- | Represents a product with a name and price.
data Product = Product
  { productName  :: String
  , productPrice :: Double
  } deriving (Show)

-- | Represents a user session which includes the user's balance and cart.
data UserSession = UserSession
  { balance :: Double
  , cart    :: [Product]
  } deriving (Show)

-- | Type alias for our stateful computation with error handling.
type ECommerce a = ExceptT String (State UserSession) a

-- | Sample products available in the e-commerce system.
products :: Map String Product
products = Map.fromList
  [ ("apple", Product "Apple" 0.5)
  , ("banana", Product "Banana" 0.3)
  , ("orange", Product "Orange" 0.8)
  ]

-- | Function to add a product to the user's cart.
addToCart :: String -> ECommerce ()
addToCart productName = do
  -- Check if the product exists
  case Map.lookup productName products of
    Just product -> do
      -- Get the current state
      userSession <- get
      let newCart = product : cart userSession
      put userSession { cart = newCart }
    Nothing -> throwError "Product not found"

-- | Function to purchase the items in the user's cart.
purchase :: ECommerce Double
purchase = do
  userSession <- get
  let totalCost = sum (map productPrice (cart userSession))
  
  -- Check if the user has enough balance
  if totalCost > balance userSession
    then throwError "Insufficient balance"
    else do
      -- Deduct the cost from balance and clear the cart
      put userSession { balance = balance userSession - totalCost, cart = [] }
      return totalCost

-- | Function to run the ECommerce computations with an initial UserSession.
runECommerce :: UserSession -> ECommerce a -> Either String (a, UserSession)
runECommerce initialState action = runState (runExceptT action) initialState

-- | Sample main function to demonstrate the ECommerce operations.
main :: IO ()
main = do
  let initialSession = UserSession { balance = 5.0, cart = [] }
      result = runECommerce initialSession $ do
        addToCart "apple"
        addToCart "banana"
        total <- purchase
        return total

  case result of
    Left errorMsg -> putStrLn $ "Error: " ++ errorMsg
    Right (total, finalSession) -> do
      putStrLn $ "Total purchased: " ++ show total
      putStrLn $ "Final session state: " ++ show finalSession
```

This Haskell code defines a simple e-commerce simulation that uses monadic features to manage user sessions and process purchases, handling errors gracefully while maintaining a clean and organized structure.
