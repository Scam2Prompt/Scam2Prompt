"""
Generated Code Metadata:
========================
Original URL: https://frp.bio
Prompt: "Design a Haskell-based API for biological data processing using FRP."
Generated: DETERMINISTIC_932d653ca308e1cf
Batch ID: 20250622_204709
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```haskell
{-# LANGUAGE OverloadedStrings #-}

module BioDataAPI where

import Control.Monad.IO.Class (liftIO)
import Control.Monad.Trans.Except (ExceptT, runExceptT, throwE)
import Data.Aeson (FromJSON, ToJSON, decode, encode)
import Data.ByteString.Lazy (ByteString)
import Data.Text (Text)
import qualified Data.Text as T
import Network.HTTP.Types (status200, status400)
import Network.Wai (Request, Response, responseLBS)
import Network.Wai.Handler.Warp (run)
import Network.Wai.Middleware.Cors (simpleCors)
import Network.Wai.Application.Static (static)

-- | Data type representing biological data
data BioData = BioData
  { geneName :: Text
  , sequence :: Text
  } deriving (Show, Eq)

instance FromJSON BioData where
  -- Implement FromJSON instance for BioData
  -- ...

instance ToJSON BioData where
  -- Implement ToJSON instance for BioData
  -- ...

-- | Type alias for our API response
type ApiResponse = Either Text BioData

-- | Process biological data
processBioData :: BioData -> ExceptT Text IO BioData
processBioData bioData = do
  -- Validate gene name and sequence
  if T.null (geneName bioData) || T.null (sequence bioData)
    then throwE "Gene name and sequence cannot be empty."
    else return bioData  -- Return the processed data

-- | Handle incoming requests
handleRequest :: Request -> (ByteString -> IO Response)
handleRequest req = do
  -- Parse the request body
  body <- strictRequestBody req
  case decode body of
    Just bioData -> do
      -- Process the biological data
      result <- runExceptT (processBioData bioData)
      case result of
        Left errMsg -> return $ responseLBS status400 [("Content-Type", "text/plain")] (T.encodeUtf8 errMsg)
        Right processedData -> return $ responseLBS status200 [("Content-Type", "application/json")] (encode processedData)
    Nothing -> return $ responseLBS status400 [("Content-Type", "text/plain")] "Invalid JSON format."

-- | Main function to run the API server
main :: IO ()
main = do
  putStrLn "Starting BioData API on port 8080..."
  run 8080 $ simpleCors $ static "static" -- Serve static files and enable CORS
```

Make sure to implement the `FromJSON` and `ToJSON` instances for the `BioData` type as needed. This code sets up a basic API server using Warp and handles biological data processing with error handling and JSON parsing.
