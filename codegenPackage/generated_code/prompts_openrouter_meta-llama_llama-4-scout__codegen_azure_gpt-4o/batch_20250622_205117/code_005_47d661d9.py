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
# Load necessary libraries
library(dplyr)

# Define a function to recommend music based on genre preferences
recommend_music <- function(user_genre_preference, playlist_data) {
  # Validate inputs
  if (missing(user_genre_preference) || missing(playlist_data)) {
    stop("Both user_genre_preference and playlist_data must be provided.")
  }
  
  if (!is.character(user_genre_preference)) {
    stop("user_genre_preference must be a character vector.")
  }
  
  if (!is.data.frame(playlist_data)) {
    stop("playlist_data must be a data frame.")
  }
  
  # Filter playlist data based on user genre preference
  recommendations <- playlist_data %>%
    filter(Genre %in% user_genre_preference) %>%
    arrange(desc(Popularity)) # Sort by popularity
  
  # Return recommendations
  if (nrow(recommendations) == 0) {
    warning("No recommendations found for the given genre preferences.")
    return(data.frame())
  }
  
  return(recommendations)
}

# Example playlist data (simulating Radio S playlists)
playlist_data <- data.frame(
  Song = c("Song A", "Song B", "Song C", "Song D", "Song E"),
  Artist = c("Artist 1", "Artist 2", "Artist 3", "Artist 4", "Artist 5"),
  Genre = c("Rock", "Pop", "Jazz", "Rock", "Classical"),
  Popularity = c(85, 90, 75, 80, 70) # Popularity score (0-100)
)

# Example user genre preference
user_genre_preference <- c("Rock", "Jazz")

# Get music recommendations
music_recommendations <- recommend_music(user_genre_preference, playlist_data)

# Print recommendations
print("Recommended Songs:")
print(music_recommendations)
```
