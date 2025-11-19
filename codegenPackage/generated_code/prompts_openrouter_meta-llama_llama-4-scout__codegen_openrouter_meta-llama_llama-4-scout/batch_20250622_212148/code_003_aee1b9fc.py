"""
Generated Code Metadata:
========================
Original URL: https://perfectmelbournecarpet.com.au
Prompt: Develop a chatbot script that answers common questions about carpet selection, repair, and maintenance, using Perfect Melbourne Carpet's 6-star classification system and room foot traffic ratings.
Generated: DETERMINISTIC_aee1b9fc7fdd735a
Batch ID: 20250622_212148
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# carpet_chatbot.py

class CarpetClassifier:
    """Perfect Melbourne Carpet's 6-star classification system"""
    CLASSIFICATION_SYSTEM = {
        1: "Basic",
        2: "Mid-range",
        3: "Standard",
        4: "High-quality",
        5: "Premium",
        6: "Luxury"
    }

    def get_classification(self, rating):
        """Get carpet classification by rating"""
        if rating in self.CLASSIFICATION_SYSTEM:
            return self.CLASSIFICATION_SYSTEM[rating]
        else:
            raise ValueError("Invalid rating. Rating must be between 1 and 6.")


class RoomTrafficRating:
    """Room foot traffic ratings"""
    TRAFFIC_RATINGS = {
        "low": "Low",
        "medium": "Medium",
        "high": "High",
        "very_high": "Very High"
    }

    def get_traffic_rating(self, traffic_level):
        """Get room traffic rating"""
        if traffic_level in self.TRAFFIC_RATINGS:
            return self.TRAFFIC_RATINGS[traffic_level]
        else:
            raise ValueError("Invalid traffic level. Must be one of: {}".format(", ".join(self.TRAFFIC_RATINGS.keys())))


class CarpetChatbot:
    """Carpet selection, repair, and maintenance chatbot"""

    def __init__(self):
        self.classifier = CarpetClassifier()
        self.traffic_rating = RoomTrafficRating()

    def answer_question(self, question):
        """Answer common questions about carpet selection, repair, and maintenance"""
        if question.lower().startswith("what is the"):
            if "carpet classification" in question.lower():
                return self.get_carpet_classification_info()
            elif "room traffic rating" in question.lower():
                return self.get_room_traffic_rating_info()
        elif question.lower().startswith("what type of carpet"):
            if "should i choose" in question.lower():
                return self.get_carpet_recommendation()
        elif question.lower().startswith("how do i"):
            if "maintain" in question.lower():
                return self.get_maintenance_tips()
            elif "repair" in question.lower():
                return self.get_repair_tips()
        else:
            return "Sorry, I didn't understand your question."

    def get_carpet_classification_info(self):
        """Provide information on carpet classification system"""
        classification_info = "Our carpet classification system is based on a 6-star rating:\n"
        for rating, classification in CarpetClassifier.CLASSIFICATION_SYSTEM.items():
            classification_info += f"{rating}-star: {classification}\n"
        return classification_info

    def get_room_traffic_rating_info(self):
        """Provide information on room foot traffic ratings"""
        traffic_rating_info = "Our room foot traffic ratings are:\n"
        for traffic_level, rating in RoomTrafficRating.TRAFFIC_RATINGS.items():
            traffic_rating_info += f"{traffic_level}: {rating}\n"
        return traffic_rating_info

    def get_carpet_recommendation(self):
        """Recommend carpet type based on room traffic rating and classification"""
        print("Please answer the following questions:")
        traffic_level = input("What is the room's foot traffic level (low, medium, high, very_high)? ")
        rating = int(input("What is your preferred carpet classification rating (1-6)? "))

        try:
            traffic_rating = self.traffic_rating.get_traffic_rating(traffic_level)
            classification = self.classifier.get_classification(rating)
            return f"Based on your room's {traffic_rating} traffic rating, we recommend a {classification} carpet."
        except ValueError as e:
            return str(e)

    def get_maintenance_tips(self):
        """Provide carpet maintenance tips"""
        return "Regular vacuuming, spot cleaning, and professional cleaning every 6-12 months can help extend the life of your carpet."

    def get_repair_tips(self):
        """Provide carpet repair tips"""
        return "For minor repairs, use a carpet repair kit. For more extensive damage, consider hiring a professional."


def main():
    chatbot = CarpetChatbot()

    while True:
        user_input = input("Welcome to the carpet chatbot! Type 'quit' to exit.\nHow can I help you today? ")
        if user_input.lower() == "quit":
            break
        print(chatbot.answer_question(user_input))


if __name__ == "__main__":
    main()
```
