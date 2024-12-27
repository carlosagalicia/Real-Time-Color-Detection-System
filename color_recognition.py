import cv2
import numpy as np

# Set window resolution
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Color recognition limits (HSV format)
red_lower = np.array([158, 87, 0], np.uint8)
red_upper = np.array([180, 255, 255], np.uint8)

green_lower = np.array([68, 87, 0], np.uint8)
green_upper = np.array([81, 255, 255], np.uint8)

orange_lower = np.array([0, 87, 111], np.uint8)
orange_upper = np.array([18, 255, 255], np.uint8)

blue_lower = np.array([90, 0, 88], np.uint8)
blue_upper = np.array([120, 255, 255], np.uint8)

yellow_lower = np.array([30, 47, 116], np.uint8)
yellow_upper = np.array([37, 184, 255], np.uint8)

white_lower = np.array([0, 0, 182], np.uint8)
white_upper = np.array([180, 96, 255], np.uint8)


# Detect objects in the image and analyze their colors and area
def get_contours(img, img_contour):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        # Calculate area
        area = cv2.contourArea(cnt)

        # Minimum area to be considered
        area_min = cv2.getTrackbarPos("Area", "HSV")

        # If the area is large enough...
        if area > area_min:

            # Calculate perimeter and centroid coordinates
            perimeter = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*perimeter, True)
            x, y, width, height = cv2.boundingRect(approx)
            center_x = x + (width * .5)
            center_y = y + (height * .5)

            # Read HSV values from the central pixel
            pixel_center = img_Hsv[int(center_y), int(center_x)]
            print(pixel_center)
            h = pixel_center[0]
            s = pixel_center[1]
            v = pixel_center[2]

            color = "UNKNOWN"

            # Red detection
            if (red_lower[0] <= h <= red_upper[0]) and (red_lower[1] <= s <= red_upper[1]) and (red_lower[2] <= v <= red_upper[2]):
                color = "RED"

            # Green detection
            if green_lower[0] <= h <= green_upper[0] and green_lower[1] <= s <= green_upper[1] and green_lower[2] <= v <= green_upper[2]:
                color = "GREEN"

            # Orange detection
            if orange_lower[0] <= h <= orange_upper[0] and orange_lower[1] <= s <= orange_upper[1] and orange_lower[2] <= v <= orange_upper[2]:
                color = "ORANGE"

            # Blue detection
            if blue_lower[0] <= h <= blue_upper[0] and blue_lower[1] <= s <= blue_upper[1] and blue_lower[2] <= v <= blue_upper[2]:
                color = "BLUE"

            # Yellow detection
            if yellow_lower[0] <= h <= yellow_upper[0] and yellow_lower[1] <= s <= yellow_upper[1] and yellow_lower[2] <= v <= yellow_upper[2]:
                color = "YELLOW"

            # White detection
            """if white_lower[0] <= h <= white_upper[0] and white_lower[1] <= s <= white_upper[1] and white_lower[2] <= v <= white_upper[2]:
                color = "WHITE"
            """

            if color != "UNKNOWN":
                # Draw the contour
                cv2.drawContours(img_contour, cnt, -1, (255, 0, 255), 3)
                draw_contour(img_contour, center_x, center_y, x, y, width, height, area, color)


# Draw contours and lines
def draw_contour(img_contour, center_x, center_y, x, y, width, height, area, color):
    # Vertical line
    cv2.rectangle(img_contour, (int(center_x), y), (int(center_x), y + height), (0, 0, 255), 1)

    # Horizontal line
    cv2.rectangle(img_contour, (x, int(center_y)), (x + width, int(center_y)), (0, 0, 255), 1)

    # Centroid
    cv2.rectangle(img_contour, (int(center_x), int(center_y)), (int(center_x), int(center_y)), (255, 0, 0), 2)

    # Container
    cv2.rectangle(img_contour, (x, y), (x + width, y + height), (0, 255, 0), 5)

    # Area text
    cv2.putText(img_contour, "Area: " + str(int(area)), (x, y - 20), cv2.FONT_HERSHEY_COMPLEX, 0.3,
                (255, 0, 0), 1)

    # Color text
    cv2.putText(img_contour, color, (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.3,
                (255, 0, 0), 1)


# Color parameters window
cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 400, 400)
cv2.createTrackbar("HUE min", "HSV", 0, 179, lambda x: None)
cv2.createTrackbar("HUE max", "HSV", 179, 179, lambda x: None)
cv2.createTrackbar("SAT min", "HSV", 0, 255, lambda x: None)
cv2.createTrackbar("SAT max", "HSV", 255, 255, lambda x: None)
cv2.createTrackbar("VALUE min", "HSV", 0, 255, lambda x: None)
cv2.createTrackbar("VALUE max", "HSV", 255, 255, lambda x: None)

# Threshold parameters
cv2.createTrackbar("Threshold1", "HSV", 0, 255, lambda x: None)
cv2.createTrackbar("Threshold2", "HSV", 47, 255, lambda x: None)

# Area parameters
cv2.createTrackbar("Area", "HSV", 1800, 30000, lambda x: None)


while cv2.waitKey(1) & 0xFF != ord('q'):
    # Get parameter values
    h_min = cv2.getTrackbarPos("HUE min", "HSV")
    h_max = cv2.getTrackbarPos("HUE max", "HSV")
    s_min = cv2.getTrackbarPos("SAT min", "HSV")
    s_max = cv2.getTrackbarPos("SAT max", "HSV")
    v_min = cv2.getTrackbarPos("VALUE min", "HSV")
    v_max = cv2.getTrackbarPos("VALUE max", "HSV")
    threshold1 = cv2.getTrackbarPos("Threshold1", "HSV")
    threshold2 = cv2.getTrackbarPos("Threshold2", "HSV")

    # Create image filter windows (blur, gray, HSV, canny)
    success, img = cap.read()
    img_contour = img.copy()
    img_Hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    img_Blur = cv2.GaussianBlur(img, (9, 9), 1)
    img_Gray = cv2.cvtColor(img_Blur, cv2.COLOR_BGR2GRAY)
    img_Canny = cv2.Canny(img_Gray, threshold1, threshold2)
    kernel = np.ones((7, 7))
    img_Dil = cv2.dilate(img_Canny, kernel, iterations=1)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    get_contours(img_Dil, img_contour)

    # Display image filter windows
    cv2.imshow("Canny", img_Dil)
    cv2.imshow("Contour", img_contour)

cap.release()
cv2.destroyAllWindows()
