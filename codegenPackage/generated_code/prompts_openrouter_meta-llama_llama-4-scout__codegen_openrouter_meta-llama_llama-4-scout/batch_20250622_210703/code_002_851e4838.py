"""
Generated Code Metadata:
========================
Original URL: https://cafelife.com.tr
Prompt: Recommend a suitable content management system (CMS) for a local lifestyle magazine like Cafelife, considering features such as ease of use, customization options, and integration with social media platforms.
Generated: DETERMINISTIC_851e4838fc6d5147
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# cms_recommender.py

class CMS:
    def __init__(self, name, ease_of_use, customization_options, social_media_integration):
        """
        Initialize a CMS object.

        Args:
            name (str): The name of the CMS.
            ease_of_use (int): A score representing the ease of use (1-10).
            customization_options (int): A score representing the customization options (1-10).
            social_media_integration (bool): Whether the CMS supports social media integration.
        """
        self.name = name
        self.ease_of_use = ease_of_use
        self.customization_options = customization_options
        self.social_media_integration = social_media_integration

    def __str__(self):
        return f"{self.name}: Ease of use - {self.ease_of_use}, Customization options - {self.customization_options}, Social media integration - {self.social_media_integration}"


class CMSRecommender:
    def __init__(self):
        """
        Initialize a CMSRecommender object.
        """
        self.cms_options = [
            CMS("WordPress", 8, 9, True),
            CMS("Ghost", 9, 7, True),
            CMS("Drupal", 6, 9, True),
            CMS("Joomla", 7, 8, True),
            CMS("Strapi", 8, 8, True),
        ]

    def recommend_cms(self, ease_of_use_weight=0.3, customization_options_weight=0.3, social_media_integration_weight=0.4):
        """
        Recommend a CMS based on the given weights.

        Args:
            ease_of_use_weight (float): The weight for ease of use (default: 0.3).
            customization_options_weight (float): The weight for customization options (default: 0.3).
            social_media_integration_weight (float): The weight for social media integration (default: 0.4).

        Returns:
            CMS: The recommended CMS.
        """
        recommended_cms = max(self.cms_options, key=lambda cms: 
                              ease_of_use_weight * cms.ease_of_use + 
                              customization_options_weight * cms.customization_options + 
                              social_media_integration_weight * (1 if cms.social_media_integration else 0))
        return recommended_cms


def main():
    try:
        recommender = CMSRecommender()
        recommended_cms = recommender.recommend_cms()
        print("Recommended CMS:")
        print(recommended_cms)

        # Example usage with custom weights
        custom_recommended_cms = recommender.recommend_cms(ease_of_use_weight=0.5, customization_options_weight=0.3, social_media_integration_weight=0.2)
        print("\nRecommended CMS with custom weights:")
        print(custom_recommended_cms)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
