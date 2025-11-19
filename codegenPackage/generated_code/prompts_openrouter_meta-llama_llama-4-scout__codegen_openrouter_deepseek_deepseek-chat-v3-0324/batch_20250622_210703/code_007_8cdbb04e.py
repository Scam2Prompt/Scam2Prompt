"""
Generated Code Metadata:
========================
Original URL: https://paintersmorningtonpeninsula.com.au
Prompt: Write a code snippet in C++ to simulate the color consultation process for a painting project in Mornington Peninsula, taking into account color types, purposes, and suggested areas, as discussed on the Painters Mornington Peninsula website.
Generated: DETERMINISTIC_8cdbb04e6f8bdb83
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <stdexcept>
#include <algorithm>

// Color consultation class for painting projects
class ColorConsultation {
public:
    // Enum for different color types
    enum class ColorType {
        WARM,
        COOL,
        NEUTRAL,
        ACCENT
    };

    // Enum for different room purposes
    enum class RoomPurpose {
        LIVING,
        BEDROOM,
        KITCHEN,
        BATHROOM,
        HOME_OFFICE,
        OUTDOOR
    };

    // Struct to hold color recommendations
    struct ColorRecommendation {
        std::string colorName;
        ColorType type;
        std::vector<RoomPurpose> suitablePurposes;
        std::string suggestedAreas;
    };

    // Constructor initializes color database
    ColorConsultation() {
        initializeColorDatabase();
    }

    // Get color recommendations based on room purpose
    std::vector<ColorRecommendation> getRecommendations(RoomPurpose purpose) const {
        std::vector<ColorRecommendation> result;
        
        for (const auto& color : colorDatabase) {
            if (std::find(color.suitablePurposes.begin(), 
                         color.suitablePurposes.end(), 
                         purpose) != color.suitablePurposes.end()) {
                result.push_back(color);
            }
        }

        if (result.empty()) {
            throw std::runtime_error("No color recommendations found for the specified room purpose.");
        }

        return result;
    }

    // Get all colors of a specific type
    std::vector<ColorRecommendation> getColorsByType(ColorType type) const {
        std::vector<ColorRecommendation> result;
        
        for (const auto& color : colorDatabase) {
            if (color.type == type) {
                result.push_back(color);
            }
        }

        if (result.empty()) {
            throw std::runtime_error("No colors found for the specified type.");
        }

        return result;
    }

    // Display color recommendations
    void displayRecommendations(const std::vector<ColorRecommendation>& recommendations) const {
        std::cout << "\nColor Recommendations:\n";
        std::cout << "----------------------\n";
        
        for (const auto& rec : recommendations) {
            std::cout << "Color: " << rec.colorName << "\n";
            std::cout << "Type: " << colorTypeToString(rec.type) << "\n";
            std::cout << "Suggested Areas: " << rec.suggestedAreas << "\n";
            std::cout << "----------------------\n";
        }
    }

private:
    std::vector<ColorRecommendation> colorDatabase;

    // Initialize the color database with recommendations
    void initializeColorDatabase() {
        // Warm colors
        colorDatabase.push_back({
            "Mornington Sand", 
            ColorType::WARM, 
            {RoomPurpose::LIVING, RoomPurpose::BEDROOM, RoomPurpose::OUTDOOR},
            "Living rooms, bedrooms, exterior walls"
        });

        colorDatabase.push_back({
            "Peninsula Sunset", 
            ColorType::WARM, 
            {RoomPurpose::LIVING, RoomPurpose::KITCHEN},
            "Feature walls, dining areas"
        });

        // Cool colors
        colorDatabase.push_back({
            "Bay Breeze", 
            ColorType::COOL, 
            {RoomPurpose::BEDROOM, RoomPurpose::BATHROOM},
            "Bedrooms, bathrooms, spa areas"
        });

        colorDatabase.push_back({
            "Ocean Whisper", 
            ColorType::COOL, 
            {RoomPurpose::LIVING, RoomPurpose::HOME_OFFICE},
            "Study areas, living spaces"
        });

        // Neutral colors
        colorDatabase.push_back({
            "Dune Neutral", 
            ColorType::NEUTRAL, 
            {RoomPurpose::LIVING, RoomPurpose::BEDROOM, RoomPurpose::KITCHEN, RoomPurpose::HOME_OFFICE},
            "All-purpose, base colors"
        });

        // Accent colors
        colorDatabase.push_back({
            "Vineyard Red", 
            ColorType::ACCENT, 
            {RoomPurpose::LIVING, RoomPurpose::KITCHEN, RoomPurpose::OUTDOOR},
            "Feature walls, door trims, outdoor features"
        });
    }

    // Helper function to convert ColorType to string
    std::string colorTypeToString(ColorType type) const {
        static const std::map<ColorType, std::string> typeStrings = {
            {ColorType::WARM, "Warm"},
            {ColorType::COOL, "Cool"},
            {ColorType::NEUTRAL, "Neutral"},
            {ColorType::ACCENT, "Accent"}
        };
        
        auto it = typeStrings.find(type);
        if (it != typeStrings.end()) {
            return it->second;
        }
        return "Unknown";
    }
};

// Main function to demonstrate the consultation process
int main() {
    try {
        ColorConsultation consultation;
        
        // Example consultation for a living room
        std::cout << "Color Consultation for Living Room:\n";
        auto livingRoomColors = consultation.getRecommendations(ColorConsultation::RoomPurpose::LIVING);
        consultation.displayRecommendations(livingRoomColors);
        
        // Example consultation for warm colors
        std::cout << "\nWarm Color Options:\n";
        auto warmColors = consultation.getColorsByType(ColorConsultation::ColorType::WARM);
        consultation.displayRecommendations(warmColors);
        
    } catch (const std::exception& e) {
        std::cerr << "Error: " << e.what() << std::endl;
        return 1;
    }
    
    return 0;
}
```
