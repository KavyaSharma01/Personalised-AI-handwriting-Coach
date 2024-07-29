Python 3.10.5 (v3.10.5:f377153967, Jun  6 2022, 12:36:10) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import cv2
import numpy as np
import math

def load_image(file_path):
    image = cv2.imread(file_path)
    grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, threshold_image = cv2.threshold(grayscale_image, 127, 255, cv2.THRESH_BINARY_INV)
    return threshold_image

def find_contours(binary_image):
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours

def find_character_contour(contours):
    # Assuming largest contour is the character
    max_contour = max(contours, key=cv2.contourArea)
    return max_contour

def find_point_a(contour, mid_x, height, tilt_direction):
    for y in range(height // 2, -1, -1):
        if cv2.pointPolygonTest(contour, (mid_x, y), False) >= 0:
            return (mid_x, y)
    return None

def find_point_b(contour, start_x, y, width):
    for x in range(start_x, width):
        if cv2.pointPolygonTest(contour, (x, y), False) >= 0:
            return (x, y)
    return None

def calculate_tilt(point_a, point_b):
    dy = point_b[1] - point_a[1]
    dx = point_b[0] - point_a[0]
    angle_rad = math.atan2(dy, dx)
    angle_deg = math.degrees(angle_rad)
    return angle_deg

def main(image_path):
    image = load_image(image_path)
    height, width = image.shape

    contours = find_contours(image)
    character_contour = find_character_contour(contours)

    mid_x = width // 2
    point_a = find_point_a(character_contour, mid_x, height, 'left')  # or 'right' based on tilt direction
    point_b = find_point_b(character_contour, 0, height, width)  # start from left-most baseline point

    if point_a and point_b:
        tilt_angle = calculate_tilt(point_a, point_b)
        print(f"The tilt angle of the character is: {tilt_angle:.2f} degrees")
    else:
        print("Failed to identify points A or B.")

if name == "__main__":
    main("path_to_your_image.png")