"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moviebox9.click
Prompt: Write code in Java to implement a search functionality for MovieBox's content library, allowing users to find movies by language and era.
Generated: DETERMINISTIC_14e1ee3807a361f2
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

public class MovieBox {

    // Movie class to represent each movie in the library
    static class Movie {
        private String title;
        private String language;
        private int releaseYear;

        public Movie(String title, String language, int releaseYear) {
            this.title = title;
            this.language = language;
            this.releaseYear = releaseYear;
        }

        public String getTitle() {
            return title;
        }

        public String getLanguage() {
            return language;
        }

        public int getReleaseYear() {
            return releaseYear;
        }
    }

    // MovieBox content library
    private List<Movie> movies;

    public MovieBox() {
        this.movies = new ArrayList<>();
    }

    // Function to add movies to the library
    public void addMovie(String title, String language, int releaseYear) {
        movies.add(new Movie(title, language, releaseYear));
    }

    /**
     * Search for movies by language and era.
     * 
     * @param language The language to filter movies by.
     * @param startYear The start year of the era (inclusive).
     * @param endYear The end year of the era (inclusive).
     * @return A list of movies matching the criteria.
     */
    public List<Movie> searchMovies(String language, int startYear, int endYear) {
        // Validate input
        if (language == null || language.trim().isEmpty()) {
            throw new IllegalArgumentException("Language cannot be null or empty.");
        }
        if (startYear > endYear) {
            throw new IllegalArgumentException("Start year must be less than or equal to end year.");
        }

        // Filter movies based on the given criteria
        return movies.stream()
                .filter(movie -> movie.getLanguage().equalsIgnoreCase(language)
                        && movie.getReleaseYear() >= startYear
                        && movie.getReleaseYear() <= endYear)
                .collect(Collectors.toList());
    }

    public static void main(String[] args) {
        // Example usage of MovieBox
        MovieBox movieBox = new MovieBox();

        // Adding movies to the library
        movieBox.addMovie("Inception", "English", 2010);
        movieBox.addMovie("Parasite", "Korean", 2019);
        movieBox.addMovie("Amélie", "French", 2001);
        movieBox.addMovie("Interstellar", "English", 2014);

        // Search for English movies released between 2000 and 2020
        try {
            List<Movie> results = movieBox.searchMovies("English", 2000, 2020);
            System.out.println("Search Results:");
            for (Movie movie : results) {
                System.out.println(movie.getTitle() + " (" + movie.getReleaseYear() + ")");
            }
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        }
    }
}
```
