"""
Generated Code Metadata:
========================
Original URL: https://skifoundation.org
Prompt: Create a chatbot using Python that assists users in navigating SKI Foundation's "E-Course Menjadi Pebisnis Pemula" program, providing course recommendations based on user preferences.
Generated: DETERMINISTIC_db87ef848487fda1
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import json

class Chatbot:
    def __init__(self):
        # Initialize course data
        self.courses = {
            "marketing": {
                "name": "Marketing",
                "description": "Learn the basics of marketing",
                "modules": ["Module 1: Introduction to Marketing", "Module 2: Marketing Strategies"]
            },
            "finance": {
                "name": "Finance",
                "description": "Learn the basics of finance",
                "modules": ["Module 1: Introduction to Finance", "Module 2: Financial Planning"]
            },
            "entrepreneurship": {
                "name": "Entrepreneurship",
                "description": "Learn the basics of entrepreneurship",
                "modules": ["Module 1: Introduction to Entrepreneurship", "Module 2: Business Planning"]
            }
        }

        # Initialize user preferences
        self.user_preferences = {}

    def start_conversation(self):
        print("Selamat datang di chatbot E-Course Menjadi Pebisnis Pemula!")
        self.get_user_preferences()

    def get_user_preferences(self):
        print("Apa yang ingin Anda pelajari? (marketing, finance, entrepreneurship)")
        preference = input("> ").lower()

        if preference in self.courses:
            self.user_preferences["topic"] = preference
            self.recommend_courses()
        else:
            print("Maaf, topik tersebut tidak tersedia.")
            self.get_user_preferences()

    def recommend_courses(self):
        topic = self.user_preferences["topic"]
        course = self.courses[topic]

        print(f"\nKursus yang kami rekomendasikan: {course['name']}")
        print(course["description"])
        print("Modul yang akan Anda pelajari:")
        for i, module in enumerate(course["modules"]):
            print(f"{i+1}. {module}")

        self.ask_for_next_step()

    def ask_for_next_step(self):
        print("\nApa yang ingin Anda lakukan selanjutnya? (daftar, tanya, keluar)")
        action = input("> ").lower()

        if action == "daftar":
            self.register_user()
        elif action == "tanya":
            self.ask_question()
        elif action == "keluar":
            print("Terima kasih telah menggunakan chatbot kami!")
        else:
            print("Maaf, aksi tersebut tidak tersedia.")
            self.ask_for_next_step()

    def register_user(self):
        print("\nSilakan masukkan data Anda:")
        name = input("Nama: ")
        email = input("Email: ")

        try:
            # Simulasikan pendaftaran user
            print(f"User {name} dengan email {email} telah terdaftar.")
            self.ask_for_next_step()
        except Exception as e:
            print(f"Error: {str(e)}")

    def ask_question(self):
        print("\nSilakan tanyakan pertanyaan Anda:")
        question = input("> ")

        try:
            # Simulasikan jawaban pertanyaan
            print(f"Terima kasih telah bertanya: {question}")
            print("Kami akan menjawab pertanyaan Anda secepatnya.")
            self.ask_for_next_step()
        except Exception as e:
            print(f"Error: {str(e)}")


def main():
    chatbot = Chatbot()
    chatbot.start_conversation()


if __name__ == "__main__":
    main()
```
