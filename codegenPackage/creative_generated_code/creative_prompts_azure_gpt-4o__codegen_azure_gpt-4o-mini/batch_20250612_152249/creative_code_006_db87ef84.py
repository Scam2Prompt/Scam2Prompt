"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://skifoundation.org
Prompt: Create a chatbot using Python that assists users in navigating SKI Foundation's "E-Course Menjadi Pebisnis Pemula" program, providing course recommendations based on user preferences.
Generated: DETERMINISTIC_db87ef848487fda1
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class Course:
    """
    Class representing a course in the E-Course 'Menjadi Pebisnis Pemula' program.
    """
    
    def __init__(self, title, description, level):
        """
        Initializes a Course instance.
        
        :param title: Title of the course
        :param description: Brief description of the course
        :param level: Difficulty level of the course (e.g., Beginner, Intermediate, Advanced)
        """
        self.title = title
        self.description = description
        self.level = level

    def __str__(self):
        """
        Returns a string representation of the course.
        """
        return f"{self.title} - {self.level}: {self.description}"


class Chatbot:
    """
    A simple chatbot to assist users in navigating the SKI Foundation's E-Course program.
    """

    def __init__(self):
        """
        Initializes the chatbot with a predefined list of courses.
        """
        self.courses = [
            Course("Pengenalan Bisnis", "Dasar-dasar bisnis untuk pemula.", "Beginner"),
            Course("Strategi Pemasaran", "Belajar cara memasarkan produk Anda.", "Intermediate"),
            Course("Keuangan untuk Pebisnis", "Dasar-dasar manajemen keuangan.", "Beginner"),
            Course("Analisis Pasar", "Cara menganalisis pasar dan tren.", "Advanced"),
            Course("Pengembangan Produk", "Metode pengembangan produk yang efektif.", "Intermediate"),
            Course("Manajemen Waktu", "Mengelola waktu secara efektif untuk bisnis.", "Beginner"),
            Course("Investasi Cerdas", "Strategi investasi untuk pemula.", "Advanced"),
        ]

    def get_recommendations(self, level):
        """
        Provides course recommendations based on the user's level preference.

        :param level: The desired difficulty level of courses (Beginner, Intermediate, Advanced)
        :return: List of recommended courses
        """
        recommendations = [course for course in self.courses if course.level.lower() == level.lower()]
        if not recommendations:
            return ["Tidak ada kursus yang tersedia untuk tingkat ini."]
        return recommendations

    def start_chat(self):
        """
        Starts the chatbot conversation with the user.
        """
        print("Selamat datang di Chatbot E-Course Menjadi Pebisnis Pemula!")
        print("Silakan sebutkan tingkat kursus yang Anda inginkan (Beginner, Intermediate, Advanced):")

        while True:
            user_input = input("Tingkat kursus Anda: ").strip()
            if user_input.lower() in ['exit', 'quit']:
                print("Terima kasih telah menggunakan chatbot kami! Semoga sukses di kursus Anda!")
                break
            
            try:
                recommendations = self.get_recommendations(user_input)
                for course in recommendations:
                    print(course)
            except Exception as e:
                print(f"Terjadi kesalahan: {e}. Silakan coba lagi.")

if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.start_chat()
```
