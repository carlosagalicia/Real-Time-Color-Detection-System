import cv2
import numpy as np

# Establecer medidas/resolution de ventanas
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Rangos minimos y maximos de color
# Lower and upper color recognition limits
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


# Detecta los objectos en la imagen y analiza sus colores y área
def getcontours(img, imgcountour):
    contours, hierachy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:

        # Calcula el area
        area = cv2.contourArea(cnt)

        # Area minima para ser considerada
        areamin = cv2.getTrackbarPos("Area", "HSV")

        # Si el area es lo suficientemente grande...
        if area > areamin:
            # Dibuja el contorno
            cv2.drawContours(imgcountour, cnt, -1, (255, 0, 255), 3)

            # Calcula su perimetro y coordenadas del centroide
            perimeter = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*perimeter, True)
            x, y, width, height = cv2.boundingRect(approx)
            halfx = x + (width * .5)
            halfy = y + (height * .5)

            # Leer valores hsv del pixel central
            pixel_center = imgHsv[int(halfy), int(halfx)]
            print(pixel_center)
            h = pixel_center[0]
            s = pixel_center[1]
            v = pixel_center[2]

            color = "UNKNOWN"

            # Deteccion de rojos
            if (red_lower[0] <= h <= red_upper[0]) and (red_lower[1] <= s <= red_upper[1]) and (red_lower[2] <= v <= red_upper[2]):
                color = "RED"

            # Deteccion de verdes
            if green_lower[0] <= h <= green_upper[0] and green_lower[1] <= s <= green_upper[1] and green_lower[2] <= v <= green_upper[2]:
                color = "GREEN"

            # Deteccion de naranja
            if orange_lower[0] <= h <= orange_upper[0] and orange_lower[1] <= s <= orange_upper[1] and orange_lower[2] <= v <= orange_upper[2]:
                color = "ORANGE"

            # Deteccion de azules
            if blue_lower[0] <= h <= blue_upper[0] and blue_lower[1] <= s <= blue_upper[1] and blue_lower[2] <= v <= blue_upper[2]:
                color = "BLUE"

            # Deteccion de amarillos
            if yellow_lower[0] <= h <= yellow_upper[0] and yellow_lower[1] <= s <= yellow_upper[1] and yellow_lower[2] <= v <= yellow_upper[2]:
                color = "YELLOW"

            # Deteccion de blancos
            """if white_lower[0] <= h <= white_upper[0] and white_lower[1] <= s <= white_upper[1] and white_lower[2] <= v <= white_upper[2]:
                color = "WHITE"
            """

            if color != "UNKNOWN":
                drawcontour(imgcountour, halfx, halfy, x, y, width, height, area, color)


# Dibujar contornos y lineas
def drawcontour(imgcountour, halfx, halfy, x, y, width, height, area, color):

    # Linea vertical
    cv2.rectangle(imgcountour, (int(halfx), y), (int(halfx), y + height), (0, 0, 255), 1)

    # Linea horizontal
    cv2.rectangle(imgcountour, (x, int(halfy)), (x + width, int(halfy)), (0, 0, 255), 1)

    # Centroide
    cv2.rectangle(imgcountour, (int(halfx), int(halfy)), (int(halfx), int(halfy)), (255, 0, 0), 2)

    # Contenedor
    cv2.rectangle(imgcountour, (x, y), (x + width, y + height), (0, 255, 0), 5)

    # Texto de area
    cv2.putText(imgcountour, "Area: " + str(int(area)), (x, y - 20), cv2.FONT_HERSHEY_COMPLEX, 0.3,
                (255, 0, 0), 1)

    # Texto de color
    cv2.putText(imgcountour, color, (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.3,
                (255, 0, 0), 1)


# Parametros de color
cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 400, 400)
cv2.createTrackbar("HUE min", "HSV", 0, 179, lambda x: None)
cv2.createTrackbar("HUE max", "HSV", 179, 179, lambda x: None)
cv2.createTrackbar("SAT min", "HSV", 0, 255, lambda x: None)
cv2.createTrackbar("SAT max", "HSV", 255, 255, lambda x: None)
cv2.createTrackbar("VALUE min", "HSV", 0, 255, lambda x: None)
cv2.createTrackbar("VALUE max", "HSV", 255, 255, lambda x: None)

# Parametros de tono
cv2.createTrackbar("Treshold1", "HSV", 0, 255, lambda x: None)
cv2.createTrackbar("Treshold2", "HSV", 47, 255, lambda x: None)

# Parametros de área
cv2.createTrackbar("Area", "HSV", 1800, 30000, lambda x: None)


while cv2.waitKey(1) & 0xFF != ord('q'):

    # Tomar datos de parametros
    h_min = cv2.getTrackbarPos("HUE min", "HSV")
    h_max = cv2.getTrackbarPos("HUE max", "HSV")
    s_min = cv2.getTrackbarPos("SAT min", "HSV")
    s_max = cv2.getTrackbarPos("SAT max", "HSV")
    v_min = cv2.getTrackbarPos("VALUE min", "HSV")
    v_max = cv2.getTrackbarPos("VALUE max", "HSV")
    threshold1 = cv2.getTrackbarPos("Treshold1", "HSV")
    threshold2 = cv2.getTrackbarPos("Treshold2", "HSV")

    # Crear ventanas de filtro de imagen (borroso, gris, HSV, canny)
    success, img = cap.read()
    imgcontour = img.copy()
    imgHsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    imgBlur = cv2.GaussianBlur(img, (9, 9), 1)
    imgGray = cv2.cvtColor(imgBlur, cv2.COLOR_BGR2GRAY)
    imgCanny = cv2.Canny(imgGray, threshold1, threshold2)
    kernel = np.ones((7, 7))
    imgDil = cv2.dilate(imgCanny, kernel, iterations=1)

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    getcontours(imgDil, imgcontour)

    # Desplegar ventanas con filtros de imagen
    cv2.imshow("Canny", imgDil)
    cv2.imshow("Contour", imgcontour)

cap.release()
cv2.destroyAllWindows()
