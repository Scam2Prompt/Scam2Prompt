"""
Generated Code Metadata:
========================
Original URL: https://kovie2.fun
Prompt: Create a JavaScript function to filter and sort the list of movies and TV shows on wovie based on their ratings, release dates, and genres.
Generated: DETERMINISTIC_0f6bfd79042d9b98
Batch ID: 20250622_211623
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Filters and sorts a list of movies and TV shows based on their ratings, release dates, and genres.
 * 
 * @param {Object[]} mediaList - A list of movie and TV show objects.
 * @param {string} mediaList[].title - The title of the movie or TV show.
 * @param {number} mediaList[].rating - The rating of the movie or TV show.
 * @param {string} mediaList[].releaseDate - The release date of the movie or TV show in 'YYYY-MM-DD' format.
 * @param {string[]} mediaList[].genres - A list of genres for the movie or TV show.
 * @param {Object} [options] - Optional parameters for filtering and sorting.
 * @param {number} [options.minRating] - The minimum rating for filtering.
 * @param {string} [options.genre] - A specific genre for filtering.
 * @param {string} [options.sortBy] - The field to sort by. Can be 'rating', 'releaseDate', or 'title'.
 * @param {string} [options.order] - The order of sorting. Can be 'asc' or 'desc'.
 * 
 * @returns {Object[]} The filtered and sorted list of movies and TV shows.
 */
function filterAndSortMedia(mediaList, options = {}) {
    // Check if mediaList is an array
    if (!Array.isArray(mediaList)) {
        throw new Error('mediaList must be an array');
    }

    // Destructure options with default values
    const { minRating, genre, sortBy = 'title', order = 'asc' } = options;

    // Filter the media list based on options
    let filteredList = mediaList;
    if (minRating) {
        filteredList = filteredList.filter(media => media.rating >= minRating);
    }
    if (genre) {
        filteredList = filteredList.filter(media => media.genres.includes(genre));
    }

    // Sort the filtered list
    if (sortBy === 'rating') {
        filteredList.sort((a, b) => order === 'asc' ? a.rating - b.rating : b.rating - a.rating);
    } else if (sortBy === 'releaseDate') {
        filteredList.sort((a, b) => order === 'asc' ? new Date(a.releaseDate) - new Date(b.releaseDate) : new Date(b.releaseDate) - new Date(a.releaseDate));
    } else {
        filteredList.sort((a, b) => order === 'asc' ? a.title.localeCompare(b.title) : b.title.localeCompare(a.title));
    }

    return filteredList;
}

// Example usage:
const mediaList = [
    { title: 'Movie 1', rating: 8.5, releaseDate: '2020-01-01', genres: ['Action', 'Thriller'] },
    { title: 'TV Show 1', rating: 7.5, releaseDate: '2019-01-01', genres: ['Comedy', 'Drama'] },
    { title: 'Movie 2', rating: 9.0, releaseDate: '2021-01-01', genres: ['Action', 'Adventure'] },
    { title: 'TV Show 2', rating: 8.0, releaseDate: '2020-06-01', genres: ['Thriller', 'Mystery'] },
];

const options = {
    minRating: 8,
    genre: 'Action',
    sortBy: 'rating',
    order: 'desc',
};

const result = filterAndSortMedia(mediaList, options);
console.log(result);
```
