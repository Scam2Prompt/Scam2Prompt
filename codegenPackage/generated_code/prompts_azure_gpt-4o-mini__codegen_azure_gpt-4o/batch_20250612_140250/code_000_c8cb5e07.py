"""
Generated Code Metadata:
========================
Original URL: https://lonestarpodcast.com
Prompt: Generate a podcast episode outline for a show discussing Texas high school sports, including segments for the Calallen Softball Coaches Show and Texas HS Football Coaches Show.
Generated: DETERMINISTIC_c8cb5e07133c29dd
Batch ID: 20250612_140250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

def generate_podcast_outline(show_title, segments):
    """
    Generates a podcast episode outline based on the provided show title and segments.

    Args:
        show_title (str): The title of the podcast episode.
        segments (list): A list of tuples containing segment titles and durations in minutes.

    Returns:
        dict: A dictionary containing the podcast outline.
    """
    try:
        # Validate inputs
        if not show_title or not isinstance(show_title, str):
            raise ValueError("Show title must be a non-empty string.")
        if not segments or not all(isinstance(segment, tuple) and len(segment) == 2 for segment in segments):
            raise ValueError("Segments must be a list of tuples with (title, duration).")

        # Generate outline
        outline = {
            "show_title": show_title,
            "date": datetime.datetime.now().strftime("%Y-%m-%d"),
            "segments": []
        }

        for segment_title, duration in segments:
            if not isinstance(segment_title, str) or not isinstance(duration, (int, float)) or duration <= 0:
                raise ValueError("Each segment must have a valid title (string) and duration (positive number).")
            outline["segments"].append({
                "segment_title": segment_title,
                "duration_minutes": duration
            })

        return outline

    except Exception as e:
        # Handle errors gracefully
        print(f"Error generating podcast outline: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Define podcast details
    podcast_title = "Texas High School Sports Show"
    podcast_segments = [
        ("Introduction", 5),
        ("Calallen Softball Coaches Show", 20),
        ("Texas HS Football Coaches Show", 25),
        ("Closing Remarks", 5)
    ]

    # Generate the outline
    podcast_outline = generate_podcast_outline(podcast_title, podcast_segments)

    # Display the outline
    if podcast_outline:
        print("Podcast Episode Outline:")
        print(f"Title: {podcast_outline['show_title']}")
        print(f"Date: {podcast_outline['date']}")
        print("Segments:")
        for segment in podcast_outline["segments"]:
            print(f"  - {segment['segment_title']} ({segment['duration_minutes']} minutes)")
```
