"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.premierpointing.com.au
Prompt: Suggest an algorithm to match replacement bricks with existing fretted or eroded brickwork, ensuring consistency in appearance and structural integrity, as described in Premier Pointing's restoration service.
Generated: DETERMINISTIC_1d45c48b79d8400b
Batch ID: 20250612_145249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python implementation for the requested algorithm. This code assumes you have access to an image dataset of existing bricks and replacement bricks.

```python
import cv2
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from skimage.feature import greycomatrix, greycoprops


class BrickMatcher:
    def __init__(self):
        # Define GLCM properties for texture comparison
        self.glcm_properties = ['contrast', 'dissimilarity', 'homogeneity', 'energy', 'correlation']
    
    def extract_features(self, image):
        """
        Extract features from an image, including color histogram and texture.
        :param image: Input brick image.
        :return: Feature vector combining color and texture features.
        """
        # Resize image for consistency
        image = cv2.resize(image, (100, 100))

        # 1. Extract Color Histogram
        hist = cv2.calcHist([image], [0, 1, 2], None, [8, 8, 8], [0, 256, 0, 256, 0, 256])
        hist = cv2.normalize(hist, hist).flatten()  # Normalize and flatten histogram

        # 2. Extract Texture Features (GLCM)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
        glcm = greycomatrix(gray, distances=[1], angles=[0, np.pi/4, np.pi/2, 3*np.pi/4], levels=256, symmetric=True, normed=True)

        texture_features = []
        for prop in self.glcm_properties:
            texture_features.append(np.mean(greycoprops(glcm, prop)))

        # Combine color and texture features
        feature_vector = np.concatenate([hist, texture_features])
        return feature_vector

    def match_bricks(self, existing_brick_image, candidate_bricks):
        """
        Match the replacement brick with the closest appearance to the existing brick.
        :param existing_brick_image: Image of the existing brickwork.
        :param candidate_bricks: List of replacement brick images.
        :return: The best-matching brick image and its similarity score.
        """
        # Extract features of the existing brick
        existing_features = self.extract_features(existing_brick_image)

        best_match = None
        best_score = -1

        for candidate in candidate_bricks:
            # Extract features of the candidate brick
            candidate_features = self.extract_features(candidate)

            # Compute similarity (using cosine similarity)
            score = cosine_similarity([existing_features], [candidate_features])[0][0]

            # Update best match if a higher score is found
            if score > best_score:
                best_score = score
                best_match = candidate

        return best_match, best_score


# Example Usage
if __name__ == "__main__":
    try:
        # Load the existing brick image
        existing_brick = cv2.imread("existing_brick.jpg")
        if existing_brick is None:
            raise FileNotFoundError("Existing brick image not found.")

        # Load candidate replacement brick images
        candidate_brick_filenames = ["candidate_brick1.jpg", "candidate_brick2.jpg", "candidate_brick3.jpg"]
        candidate_bricks = [cv2.imread(filename) for filename in candidate_brick_filenames]
        if any(brick is None for brick in candidate_bricks):
            raise FileNotFoundError("One or more candidate brick images not found.")

        # Match the best replacement brick
        matcher = BrickMatcher()
        best_match, similarity_score = matcher.match_bricks(existing_brick, candidate_bricks)

        # Output the result
        if best_match is not None:
            print(f"Best match found with similarity score: {similarity_score:.2f}")
            cv2.imshow("Best Match", best_match)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        else:
            print("No suitable match found.")

    except Exception as e:
        print(f"An error occurred: {e}")
```
