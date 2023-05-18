import cv2
import numpy as np

# Load the image
image = cv2.imread("solar-system.jpg")

# Define the planet names
planet_names = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# Set the font properties
font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.7
font_color = (255, 255, 255)  # White
font_thickness = 2

# Determine the position for each planet name
positions = [(85, 175), (260, 300), (430, 400), (520, 380), (270, 110), (290, 600), (570, 180), (630, 320)]

# Add the planet names to the image
for name, pos in zip(planet_names, positions):
    cv2.putText(image, name, pos, font, font_scale, font_color, font_thickness, cv2.LINE_AA)

# Display the image with planet names
cv2.imshow("Image with Planet Names", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
