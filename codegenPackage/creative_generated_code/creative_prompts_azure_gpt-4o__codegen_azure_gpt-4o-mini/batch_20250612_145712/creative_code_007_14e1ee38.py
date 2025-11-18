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

/**
 * Represents a movie with its title, language, and release year.
 */
class Movie {
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

/**
 * Manages a collection of movies and provides search functionality.
 */
class MovieLibrary {
    private List<Movie> movies;

    public MovieLibrary() {
        this.movies = new ArrayList<>();
    }

    /**
     * Adds a movie to the library.
     * 
     * @param movie The movie to be added.
     */
    public void addMovie(Movie movie) {
        if (movie != null) {
            movies.add(movie);
        } else {
            throw new IllegalArgumentException("Cannot add null movie.");
        }
    }

    /**
     * Searches for movies by specific language and release era.
     * 
     * @param language The language to filter by.
     * @param startYear The start year of the era.
     * @param endYear The end year of the era.
     * @return A list of movies that match the search criteria.
     */
    public List<Movie> searchMovies(String language, int startYear, int endYear) {
        if (language == null || startYear < 0 || endYear < startYear) {
            throw new IllegalArgumentException("Invalid search parameters.");
        }

        return movies.stream()
                .filter(movie -> movie.getLanguage().equalsIgnoreCase(language) &&
                                movie.getReleaseYear() >= startYear &&
                                movie.getReleaseYear() <= endYear)
                .collect(Collectors.toList());
    }
}

/**
 * Main class to demonstrate the functionality of the MovieLibrary.
 */
public class MovieBox {
    public static void main(String[] args) {
        try {
            MovieLibrary library = new MovieLibrary();

            // Sample movies for demonstration
            library.addMovie(new Movie("Inception", "English", 2010));
            library.addMovie(new Movie("Amélie", "French", 2001));
            library.addMovie(new Movie("Parasite", "Korean", 2019));
            library.addMovie(new Movie("Crouching Tiger, Hidden Dragon", "Chinese", 2000));
            library.addMovie(new Movie("La La Land", "English", 2016));

            // Search for movies in English between 2000 and 2020
            List<Movie> foundMovies = library.searchMovies("English", 2000, 2020);
            System.out.println("Found Movies:");
            for (Movie movie : foundMovies) {
                System.out.println(movie.getTitle() + " (" + movie.getReleaseYear() + ")");
            }
        } catch (IllegalArgumentException e) {
            System.err.println("Error: " + e.getMessage());
        } catch (Exception e) {
            System.err.println("An unexpected error occurred: " + e.getMessage());
        }
    }
}
```
