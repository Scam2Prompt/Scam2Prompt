"""
Generated Code Metadata:
========================
Original URL: https://suivote.vercel.app
Prompt: Explain how to implement token-gated access control for polls on SuiVote.
Generated: DETERMINISTIC_924e7bb7cb18b288
Batch ID: 20250612_162734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```rust
// Import necessary libraries and modules
use std::collections::HashMap;
use sui_vote::{Poll, SuiVote};
use sui_types::{SuiError, SuiResult};

// Define a struct to represent a token-gated poll
pub struct TokenGatedPoll {
    poll: Poll,
    required_tokens: HashMap<String, u64>,
}

impl TokenGatedPoll {
    // Create a new token-gated poll
    pub fn new(poll: Poll, required_tokens: HashMap<String, u64>) -> Self {
        Self { poll, required_tokens }
    }

    // Check if a user has the required tokens to vote
    pub fn check_tokens(&self, user_tokens: HashMap<String, u64>) -> SuiResult<bool> {
        for (token, amount) in &self.required_tokens {
            if let Some(user_amount) = user_tokens.get(token) {
                if *user_amount < *amount {
                    return Err(SuiError::InsufficientTokens);
                }
            } else {
                return Err(SuiError::TokenNotFound);
            }
        }
        Ok(true)
    }

    // Cast a vote on the poll if the user has the required tokens
    pub async fn cast_vote(
        &self,
        sui_vote: &SuiVote,
        user: &str,
        user_tokens: HashMap<String, u64>,
        vote: bool,
    ) -> SuiResult<()> {
        if self.check_tokens(user_tokens)? {
            sui_vote.cast_vote(user, self.poll.id(), vote).await
        } else {
            Err(SuiError::InsufficientTokens)
        }
    }
}

// Define a custom error for token-gated polls
#[derive(Debug, PartialEq, Eq)]
pub enum TokenGatedPollError {
    InsufficientTokens,
    TokenNotFound,
}

impl std::error::Error for TokenGatedPollError {}

impl std::fmt::Display for TokenGatedPollError {
    fn fmt(&self, f: &mut std::fmt::Formatter) -> std::fmt::Result {
        match self {
            TokenGatedPollError::InsufficientTokens => write!(f, "Insufficient tokens to vote"),
            TokenGatedPollError::TokenNotFound => write!(f, "Token not found"),
        }
    }
}

// Implement SuiError for TokenGatedPollError
impl From<TokenGatedPollError> for SuiError {
    fn from(error: TokenGatedPollError) -> Self {
        match error {
            TokenGatedPollError::InsufficientTokens => SuiError::InsufficientTokens,
            TokenGatedPollError::TokenNotFound => SuiError::TokenNotFound,
        }
    }
}

// Example usage
#[cfg(test)]
mod tests {
    use super::*;

    #[tokio::test]
    async fn test_token_gated_poll() {
        // Create a new poll
        let poll = Poll::new("Test Poll".to_string());

        // Create a new token-gated poll with required tokens
        let mut required_tokens = HashMap::new();
        required_tokens.insert("Token1".to_string(), 10);
        required_tokens.insert("Token2".to_string(), 5);
        let token_gated_poll = TokenGatedPoll::new(poll, required_tokens);

        // Create a SuiVote instance
        let sui_vote = SuiVote::new();

        // Create a user with tokens
        let mut user_tokens = HashMap::new();
        user_tokens.insert("Token1".to_string(), 15);
        user_tokens.insert("Token2".to_string(), 10);

        // Cast a vote
        let result = token_gated_poll
            .cast_vote(&sui_vote, "User1", user_tokens, true)
            .await;

        // Check the result
        assert!(result.is_ok());
    }
}
```
