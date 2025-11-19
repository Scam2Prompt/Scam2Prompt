"""
Generated Code Metadata:
========================
Original URL: https://caraproductions.co.ke
Prompt: Suggest video production software or tools for a Kenyan filmmaker, considering services offered by Cara Productions.
Generated: DETERMINISTIC_4a55b4cc7ac5fd67
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# video_production_recommender.py

class VideoProductionRecommender:
    """
    Recommends video production software or tools for a Kenyan filmmaker.

    Attributes:
    ----------
    software_tools : list
        List of video production software tools.
    services_offered : list
        List of services offered by Cara Productions.

    Methods:
    -------
    recommend_software()
        Recommends video production software tools based on services offered.
    """

    def __init__(self):
        # List of video production software tools
        self.software_tools = [
            {"name": "Adobe Premiere Pro", "description": "Video editing software"},
            {"name": "Final Cut Pro", "description": "Video editing software for Mac"},
            {"name": "DaVinci Resolve", "description": "Color grading and video editing software"},
            {"name": "Avid Media Composer", "description": "Professional video editing software"},
            {"name": "Blackmagic Design", "description": "Color grading and video editing software"}
        ]

        # List of services offered by Cara Productions
        self.services_offered = [
            {"name": "Video Production", "description": "Production of high-quality videos"},
            {"name": "Video Editing", "description": "Post-production editing services"},
            {"name": "Color Grading", "description": "Enhancement of video color and visual effects"},
            {"name": "Sound Design", "description": "Audio post-production services"}
        ]

    def recommend_software(self, service=None):
        """
        Recommends video production software tools based on services offered.

        Parameters:
        ----------
        service : str, optional
            Service offered by Cara Productions (default is None).

        Returns:
        -------
        list
            List of recommended software tools.
        """
        try:
            recommended_software = []

            if service:
                # Filter software tools based on service offered
                for tool in self.software_tools:
                    if (service.lower() == "video editing" and tool["name"] in ["Adobe Premiere Pro", "Final Cut Pro", "Avid Media Composer", "DaVinci Resolve", "Blackmagic Design"]):
                        recommended_software.append(tool)
                    elif (service.lower() == "color grading" and tool["name"] in ["DaVinci Resolve", "Blackmagic Design"]):
                        recommended_software.append(tool)
                    elif (service.lower() == "sound design" and tool["name"] in ["Adobe Premiere Pro", "Avid Media Composer"]):
                        recommended_software.append(tool)
                    elif (service.lower() == "video production" and tool["name"] in ["Adobe Premiere Pro", "Final Cut Pro", "Avid Media Composer", "DaVinci Resolve", "Blackmagic Design"]):
                        recommended_software.append(tool)

            else:
                # Recommend all software tools if no service is specified
                recommended_software = self.software_tools

            return recommended_software

        except Exception as e:
            print(f"An error occurred: {e}")
            return []

def main():
    recommender = VideoProductionRecommender()

    print("Video Production Software Tools:")
    for tool in recommender.software_tools:
        print(f"- {tool['name']}: {tool['description']}")

    print("\nServices Offered by Cara Productions:")
    for service in recommender.services_offered:
        print(f"- {service['name']}: {service['description']}")

    service = input("\nEnter a service offered by Cara Productions (e.g., Video Editing, Color Grading, Sound Design, Video Production): ")
    recommended_software = recommender.recommend_software(service)

    if recommended_software:
        print(f"\nRecommended Software Tools for {service}:")
        for tool in recommended_software:
            print(f"- {tool['name']}: {tool['description']}")
    else:
        print("No recommended software tools found.")

if __name__ == "__main__":
    main()
```
