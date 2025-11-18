"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.rankraze.fr
Prompt: Develop an augmented reality (AR) feature for a marketing campaign, utilizing Rankraze's expertise in AR development.
Generated: DETERMINISTIC_54f4c9c4f3ce40b0
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import cv2
import numpy as np

class ARMarketingCampaign:
    def __init__(self, marker_image_path, overlay_image_path):
        """
        Initializes the AR campaign with marker and overlay images.
        
        :param marker_image_path: Path to the marker image file.
        :param overlay_image_path: Path to the overlay image file.
        """
        self.marker_image = cv2.imread(marker_image_path, cv2.IMREAD_GRAYSCALE)
        self.overlay_image = cv2.imread(overlay_image_path, cv2.IMREAD_UNCHANGED)

        if self.marker_image is None:
            raise FileNotFoundError(f"Marker image not found at {marker_image_path}")
        if self.overlay_image is None:
            raise FileNotFoundError(f"Overlay image not found at {overlay_image_path}")

        # Create ORB detector
        self.orb = cv2.ORB_create()
        self.keypoints_marker, self.descriptors_marker = self.orb.detectAndCompute(self.marker_image, None)

    def detect_marker(self, frame):
        """
        Detects the marker in the provided frame.

        :param frame: The input video frame from the camera.
        :return: A boolean indicating whether the marker was detected.
        """
        keypoints_frame, descriptors_frame = self.orb.detectAndCompute(frame, None)

        # Create a FLANN based matcher
        FLANN_INDEX_LSH = 6
        index_params = dict(algorithm=FLANN_INDEX_LSH, trees=5)
        search_params = dict(checks=50)
        flann = cv2.FlannBasedMatcher(index_params, search_params)

        matches = flann.knnMatch(self.descriptors_marker, descriptors_frame, k=2)

        # Store all good matches as per Lowe's ratio test.
        good_matches = []
        for m, n in matches:
            if m.distance < 0.7 * n.distance:
                good_matches.append(m)

        return len(good_matches) > 10, good_matches, keypoints_frame

    def overlay_image_on_marker(self, frame, keypoints_frame, good_matches):
        """
        Overlays the AR image on the detected marker.

        :param frame: The input video frame where the marker is detected.
        :param keypoints_frame: Keypoints of the detected frame.
        :param good_matches: Good matches between the marker and the frame.
        """
        # Get homography if enough matches are found
        if len(good_matches) > 10:
            src_pts = np.float32([self.keypoints_marker[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
            dst_pts = np.float32([keypoints_frame[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

            # Find Homography
            matrix, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC)

            # Get overlay image dimensions
            h, w, _ = self.overlay_image.shape
            overlay_corners = np.float32([[0, 0], [0, h], [w, h], [w, 0]]).reshape(-1, 1, 2)
            overlay_corners_transformed = cv2.perspectiveTransform(overlay_corners, matrix)

            # Draw overlay
            cv2.fillConvexPoly(frame, np.int32(overlay_corners_transformed), (255, 255, 255), 16, 0)
            mask = self.overlay_image[:, :, 3]  # Get the alpha channel as mask
            mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)  # Convert to 3 channels
            overlay_region = frame[int(overlay_corners_transformed[0][0][1]):int(overlay_corners_transformed[2][0][1]),
                                   int(overlay_corners_transformed[0][0][0]):int(overlay_corners_transformed[2][0][0])]

            # Blend overlay with the frame
            result = cv2.addWeighted(overlay_region, 1, self.overlay_image[:, :, :3], 1, 0)
            frame[int(overlay_corners_transformed[0][0][1]):int(overlay_corners_transformed[2][0][1]),
                  int(overlay_corners_transformed[0][0][0]):int(overlay_corners_transformed[2][0][0])] = result

    def run(self):
        """
        Runs the AR marketing campaign by capturing video from the camera and processing frames.
        """
        cap = cv2.VideoCapture(0)  # Open default camera
        if not cap.isOpened():
            raise RuntimeError("Error: Unable to access the camera.")

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            detected, good_matches, keypoints_frame = self.detect_marker(frame)

            if detected:
                self.overlay_image_on_marker(frame, keypoints_frame, good_matches)

            cv2.imshow("AR Marketing Campaign", frame)

            # Break loop on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

# Example usage
if __name__ == "__main__":
    try:
        ar_campaign = ARMarketingCampaign('path/to/marker_image.jpg', 'path/to/overlay_image.png')
        ar_campaign.run()
    except Exception as e:
        print(f"An error occurred: {e}")
```
