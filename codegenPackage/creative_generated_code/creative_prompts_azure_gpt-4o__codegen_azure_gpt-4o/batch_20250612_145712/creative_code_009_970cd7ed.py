"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moviebox9.click
Prompt: Provide an example of how to use MovieBox's offline viewing feature in a React Native app for users with limited internet access.
Generated: DETERMINISTIC_970cd7ed7edadad1
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary modules from React Native and third-party libraries
import React, { useState, useEffect } from 'react';
import { View, Text, Button, FlatList, StyleSheet, Alert } from 'react-native';
import * as FileSystem from 'expo-file-system'; // File handling in React Native
import { Video } from 'expo-av'; // For video playback

// Replace with your actual MovieBox SDK import
import MovieBox from 'moviebox-sdk'; 

const OfflineViewing = () => {
  const [movies, setMovies] = useState([]);
  const [offlineMovies, setOfflineMovies] = useState([]);
  const [downloading, setDownloading] = useState(false);

  // Fetch available movies from MovieBox on component mount
  useEffect(() => {
    async function fetchMovies() {
      try {
        const response = await MovieBox.getMovies(); // Fetch movie list from MovieBox
        setMovies(response);
      } catch (error) {
        console.error("Error fetching movies:", error);
        Alert.alert("Error", "Failed to fetch movies. Please try again later.");
      }
    }

    fetchMovies();
  }, []);

  // Function to download a movie for offline viewing
  const downloadMovie = async (movie) => {
    try {
      setDownloading(true);
      const fileUri = `${FileSystem.documentDirectory}${movie.id}.mp4`; // Define file path
      const download = FileSystem.createDownloadResumable(
        movie.downloadUrl, 
        fileUri
      );

      const { uri } = await download.downloadAsync(); // Start the download
      setOfflineMovies((prev) => [...prev, { ...movie, uri }]); // Add downloaded movie to offline list
      Alert.alert("Success", `${movie.title} downloaded for offline viewing.`);
    } catch (error) {
      console.error("Error downloading movie:", error);
      Alert.alert("Error", "Failed to download movie. Please try again.");
    } finally {
      setDownloading(false);
    }
  };

  // Function to render a movie item
  const renderMovie = ({ item }) => (
    <View style={styles.movieItem}>
      <Text style={styles.movieTitle}>{item.title}</Text>
      <Button
        title="Download for Offline"
        onPress={() => downloadMovie(item)}
        disabled={downloading || offlineMovies.some((m) => m.id === item.id)}
      />
    </View>
  );

  // Function to render an offline movie item
  const renderOfflineMovie = ({ item }) => (
    <View style={styles.movieItem}>
      <Text style={styles.movieTitle}>{item.title}</Text>
      <Video
        source={{ uri: item.uri }}
        style={styles.video}
        useNativeControls
        resizeMode="contain"
        shouldPlay={false}
      />
    </View>
  );

  return (
    <View style={styles.container}>
      <Text style={styles.header}>Available Movies</Text>
      <FlatList
        data={movies}
        renderItem={renderMovie}
        keyExtractor={(item) => item.id.toString()}
      />
      <Text style={styles.header}>Offline Movies</Text>
      <FlatList
        data={offlineMovies}
        renderItem={renderOfflineMovie}
        keyExtractor={(item) => item.id.toString()}
      />
    </View>
  );
};

// Styles for the component
const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    backgroundColor: "#fff",
  },
  header: {
    fontSize: 20,
    fontWeight: "bold",
    marginBottom: 10,
  },
  movieItem: {
    marginBottom: 15,
    padding: 10,
    borderWidth: 1,
    borderColor: "#ccc",
    borderRadius: 5,
  },
  movieTitle: {
    fontSize: 16,
    fontWeight: "bold",
    marginBottom: 5,
  },
  video: {
    width: "100%",
    height: 200,
    marginTop: 10,
  },
});

// Export the component for use in the app
export default OfflineViewing;
```
