"""
Generated Code Metadata:
========================
Original URL: https://launchlawinc.com
Prompt: Write code to implement a "Why Choose Us?" section for a DIY legal services website, highlighting unique selling points similar to Launch Law's approach.
Generated: DETERMINISTIC_1a90167a0d0c5e08
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# why_choose_us.py

class WhyChooseUsSection:
    def __init__(self, unique_selling_points):
        """
        Initialize the WhyChooseUsSection class.

        Args:
            unique_selling_points (list): A list of dictionaries containing information about the unique selling points.
        """
        self.unique_selling_points = unique_selling_points

    def render_section(self):
        """
        Render the "Why Choose Us?" section.

        Returns:
            str: The HTML content of the section.
        """
        try:
            section_content = ""
            section_content += "<section id='why-choose-us'>"
            section_content += "<h2>Why Choose Us?</h2>"
            section_content += "<div class='grid-container'>"

            for point in self.unique_selling_points:
                section_content += self.render_point(point)

            section_content += "</div>"
            section_content += "</section>"
            return section_content
        except Exception as e:
            # Log the error and return an error message
            print(f"Error rendering 'Why Choose Us?' section: {str(e)}")
            return "<p>Error rendering section.</p>"

    def render_point(self, point):
        """
        Render a single unique selling point.

        Args:
            point (dict): A dictionary containing information about the unique selling point.

        Returns:
            str: The HTML content of the point.
        """
        try:
            required_keys = ["title", "description", "icon"]
            if not all(key in point for key in required_keys):
                raise ValueError("Point dictionary is missing required keys")

            point_content = ""
            point_content += "<div class='grid-item'>"
            point_content += f"<i class='{point['icon']}'></i>"
            point_content += f"<h3>{point['title']}</h3>"
            point_content += f"<p>{point['description']}</p>"
            point_content += "</div>"
            return point_content
        except Exception as e:
            # Log the error and return an error message
            print(f"Error rendering unique selling point: {str(e)}")
            return "<p>Error rendering point.</p>"


def main():
    unique_selling_points = [
        {
            "title": "Expert Guidance",
            "description": "Get step-by-step guidance on the legal process",
            "icon": "fas fa-gavel"
        },
        {
            "title": "Affordable",
            "description": "Our services are affordable and transparent",
            "icon": "fas fa-dollar-sign"
        },
        {
            "title": "User-Friendly",
            "description": "Our platform is easy to use and navigate",
            "icon": "fas fa-smile"
        }
    ]

    section = WhyChooseUsSection(unique_selling_points)
    print(section.render_section())


if __name__ == "__main__":
    main()
```
