"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://duckchain.world
Prompt: Write code in C++ to implement a lightweight music player application with storage management for audio files, inspired by the sleek and portable design mentioned on Duckchain.world.
Generated: DETERMINISTIC_d5a66a59849639c4
Batch ID: 20250612_154322
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <stdexcept>
#include <filesystem>
#include <fstream>
#include <algorithm>

class AudioFile {
public:
    // Constructor to initialize an audio file with a name and path
    AudioFile(const std::string &name, const std::string &path)
        : name(name), path(path) {
        if (!std::filesystem::exists(path)) {
            throw std::invalid_argument("File does not exist: " + path);
        }
    }

    // Get the name of the audio file
    std::string getName() const { return name; }

    // Get the path of the audio file
    std::string getPath() const { return path; }

private:
    std::string name; // Name of the audio file
    std::string path; // Path to the audio file on disk
};

class MusicPlayer {
public:
    // Add an audio file to the player's library
    void addToLibrary(const AudioFile &audioFile) {
        library.push_back(audioFile);
    }

    // Play an audio file by index
    void play(int index) {
        if (index < 0 || index >= library.size()) {
            throw std::out_of_range("Index out of range");
        }

        const AudioFile &audioFile = library[index];
        std::cout << "Playing: " << audioFile.getName() << std::endl;
        // Simulate playing the audio file
        // In a real application, audio playback would take place here
    }

    // List all audio files in the library
    void listLibrary() const {
        if (library.empty()) {
            std::cout << "Library is empty." << std::endl;
            return;
        }

        std::cout << "Audio Library:" << std::endl;
        for (size_t i = 0; i < library.size(); ++i) {
            std::cout << i << ": " << library[i].getName() << std::endl;
        }
    }

private:
    std::vector<AudioFile> library; // A collection of audio files
};

int main() {
    MusicPlayer player;

    try {
        // Adding audio files to the library
        player.addToLibrary(AudioFile("Song1", "path/to/song1.mp3"));
        player.addToLibrary(AudioFile("Song2", "path/to/song2.mp3"));
        player.addToLibrary(AudioFile("Song3", "path/to/song3.mp3"));

        // List the audio library
        player.listLibrary();

        // Playing a specific audio file
        player.play(0); // Play the first audio file
    } catch (const std::exception &e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}
```
