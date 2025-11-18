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
#include <fstream>
#include <stdexcept>
#include <map>

class AudioFile {
public:
    // Constructor to initialize audio file details
    AudioFile(const std::string& name, const std::string& path, double sizeMB)
        : fileName(name), filePath(path), fileSizeMB(sizeMB) {}

    // Getters for file details
    std::string getFileName() const { return fileName; }
    std::string getFilePath() const { return filePath; }
    double getFileSizeMB() const { return fileSizeMB; }

private:
    std::string fileName; // Name of the audio file
    std::string filePath; // Path where the audio file is stored
    double fileSizeMB;    // Size of the audio file in MB
};

class MusicPlayer {
public:
    // Adds a new audio file to the library
    void addAudioFile(const AudioFile& file) {
        audioLibrary[file.getFileName()] = file;
        totalStorageUsedMB += file.getFileSizeMB();
    }

    // Removes an audio file from the library
    void removeAudioFile(const std::string& fileName) {
        auto it = audioLibrary.find(fileName);
        if (it != audioLibrary.end()) {
            totalStorageUsedMB -= it->second.getFileSizeMB();
            audioLibrary.erase(it);
            std::cout << "Audio file '" << fileName << "' removed.\n";
        } else {
            std::cerr << "Error: File not found in library.\n";
        }
    }

    // Plays an audio file (simulated via output to console)
    void playAudioFile(const std::string& fileName) {
        auto it = audioLibrary.find(fileName);
        if (it != audioLibrary.end()) {
            std::cout << "Playing: " << it->second.getFileName() << " from " 
                      << it->second.getFilePath() << "\n";
        } else {
            std::cerr << "Error: File not found in library.\n";
        }
    }

    // Lists all audio files in the library
    void listAudioFiles() const {
        if (audioLibrary.empty()) {
            std::cout << "Audio library is empty.\n";
            return;
        }

        std::cout << "Audio Library:\n";
        for (const auto& [name, file] : audioLibrary) {
            std::cout << "- " << name << " (Size: " << file.getFileSizeMB() << " MB)\n";
        }
    }

    // Displays total storage currently used
    void displayStorageUsage() const {
        std::cout << "Total storage used: " << totalStorageUsedMB << " MB\n";
    }

private:
    std::map<std::string, AudioFile> audioLibrary;   // Library of audio files
    double totalStorageUsedMB = 0.0;                 // Total storage used by audio files
};

int main() {
    try {
        MusicPlayer player;

        // Adding audio files to the library
        player.addAudioFile(AudioFile("Track1", "/music/track1.mp3", 5.0));
        player.addAudioFile(AudioFile("Track2", "/music/track2.mp3", 3.5));

        // Listing audio files
        player.listAudioFiles();

        // Playing an audio file
        player.playAudioFile("Track1");

        // Displaying storage usage
        player.displayStorageUsage();

        // Removing an audio file
        player.removeAudioFile("Track2");

        // Listing audio files again
        player.listAudioFiles();

        // Displaying storage usage again
        player.displayStorageUsage();

    } catch (const std::exception& e) {
        std::cerr << "An error occurred: " << e.what() << '\n';
    }

    return 0;
}
```
