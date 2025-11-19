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

```r
# music_recommender.R

# Import necessary libraries
library(tidyverse)
library(stringr)

# Define a function to load radio station data
load_radio_station_data <- function() {
  # Sample radio station data (replace with actual data source)
  radio_station_data <- data.frame(
    song = c("Song 1", "Song 2", "Song 3", "Song 4", "Song 5"),
    artist = c("Artist 1", "Artist 2", "Artist 3", "Artist 4", "Artist 5"),
    genre = c("Rock", "Pop", "Hip-Hop", "Electronic", "Rock")
  )
  
  return(radio_station_data)
}

# Define a function to create a music recommendation model
create_recommendation_model <- function(radio_station_data) {
  # Create a genre lookup table
  genres <- radio_station_data %>% 
    pull(genre) %>% 
    unique()
  
  # Create a simple recommendation model based on genre co-occurrence
  recommendation_model <- radio_station_data %>% 
    group_by(genre) %>% 
    summarise(count = n()) %>% 
    arrange(desc(count))
  
  return(list(genres = genres, model = recommendation_model))
}

# Define a function to generate music recommendations
generate_recommendations <- function(recommendation_model, target_genre, num_recommendations) {
  # Get the top songs for the target genre
  recommended_songs <- recommendation_model$model %>% 
    filter(genre == target_genre) %>% 
    arrange(desc(count)) %>% 
    head(num_recommendations)
  
  return(recommended_songs)
}

# Define a function to get similar genres
get_similar_genres <- function(recommendation_model, target_genre) {
  # Calculate genre similarity based on co-occurrence (simple implementation)
  genre_similarity <- recommendation_model$model %>% 
    group_by(genre) %>% 
    summarise(avg_count = mean(count)) %>% 
    arrange(desc(avg_count))
  
  # Get similar genres (genres with high average co-occurrence)
  similar_genres <- genre_similarity %>% 
    filter(genre != target_genre) %>% 
    head(3)
  
  return(similar_genres)
}

# Main function
main <- function() {
  # Load radio station data
  radio_station_data <- load_radio_station_data()
  
  # Create a music recommendation model
  recommendation_model <- create_recommendation_model(radio_station_data)
  
  # Generate music recommendations for a target genre
  target_genre <- "Rock"
  num_recommendations <- 3
  recommended_songs <- generate_recommendations(recommendation_model, target_genre, num_recommendations)
  print(paste("Recommended songs for", target_genre, ":"))
  print(recommended_songs)
  
  # Get similar genres for a target genre
  similar_genres <- get_similar_genres(recommendation_model, target_genre)
  print(paste("Similar genres to", target_genre, ":"))
  print(similar_genres)
}

# Run the main function
main()
```
