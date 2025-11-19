"""
Generated Code Metadata:
========================
Original URL: https://as-media.rs
Prompt: Design a simple music recommendation system in R, using the genres and playlists featured on Radio S.
Generated: DETERMINISTIC_47d661d9b2a53168
Batch ID: 20250622_205117
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```R
# Music Recommendation System for Radio S

# Load required libraries
library(dplyr)
library(tidyr)
library(recommenderlab)

# Set seed for reproducibility
set.seed(42)

# Sample data - genres and playlists featured on Radio S
genres <- c("Pop", "Rock", "Hip Hop", "Electronic", "Jazz", "Classical", "R&B", "Country", "Reggae", "Metal")
users <- paste0("user", 1:100)

# Create a synthetic user-item matrix (ratings from 1-5)
create_synthetic_data <- function(users, genres, num_samples = 1000) {
  data <- data.frame(
    user = sample(users, num_samples, replace = TRUE),
    genre = sample(genres, num_samples, replace = TRUE),
    rating = sample(1:5, num_samples, replace = TRUE)
  )
  
  # Convert to wide format (user-item matrix)
  data_wide <- data %>%
    group_by(user, genre) %>%
    summarise(rating = mean(rating), .groups = 'drop') %>%
    spread(key = genre, value = rating, fill = 0)
  
  return(as.matrix(data_wide[,-1]))
}

# Generate synthetic data
ratings_matrix <- create_synthetic_data(users, genres)

# Convert to realRatingMatrix for recommenderlab
ratings <- as(ratings_matrix, "realRatingMatrix")

# Create evaluation scheme
eval_scheme <- evaluationScheme(ratings, method = "split", train = 0.8, given = 2, goodRating = 4)

# Train different recommendation models
models <- list(
  "Random" = "RANDOM",
  "Popular" = "POPULAR",
  "User-Based CF" = "UBCF",
  "Item-Based CF" = "IBCF"
)

# Evaluate models
results <- evaluate(eval_scheme, models, type = "ratings")

# Compare model performance
avg_results <- avg(results)
print(avg_results)

# Select best model (UBCF in this case)
recommender <- Recommender(getData(eval_scheme, "train"), "UBCF")

# Function to get recommendations for a user
get_recommendations <- function(user_id, n = 3) {
  # Check if user exists in the system
  if (!user_id %in% users) {
    stop("User not found in the system")
  }
  
  # Get user ratings
  user_ratings <- ratings[user_id, ]
  
  # Predict recommendations
  pred <- predict(recommender, user_ratings, n = n)
  
  # Convert to list
  rec_list <- as(pred, "list")
  
  # Return recommendations
  return(rec_list[[1]])
}

# Example usage
# user10_recommendations <- get_recommendations("user10")
# print(user10_recommendations)

# Function to get similar users
get_similar_users <- function(user_id, n = 3) {
  # Check if user exists in the system
  if (!user_id %in% users) {
    stop("User not found in the system")
  }
  
  # Calculate similarity
  similarity <- similarity(ratings, method = "cosine")
  
  # Get similarity scores for the user
  user_sim <- as.matrix(similarity)[user_id, ]
  
  # Sort and get top n similar users (excluding self)
  similar_users <- names(sort(user_sim, decreasing = TRUE)[2:(n+1)])
  
  return(similar_users)
}

# Example usage
# similar_to_user10 <- get_similar_users("user10")
# print(similar_to_user10)

# Function to recommend based on genre
recommend_by_genre <- function(genre, n = 5) {
  # Check if genre exists
  if (!genre %in% genres) {
    stop("Genre not found in our database")
  }
  
  # Get top rated items for the genre
  genre_ratings <- colMeans(ratings_matrix[, genre, drop = FALSE])
  
  # Get similar genres
  genre_sim <- similarity(t(ratings_matrix), method = "cosine")
  similar_genres <- names(sort(genre_sim[genre, ], decreasing = TRUE)[2:(n+1)])
  
  return(list(
    top_rated = genre_ratings,
    similar_genres = similar_genres
  ))
}

# Example usage
# pop_recommendations <- recommend_by_genre("Pop")
# print(pop_recommendations)
```
