import cv2

image = cv2.imread('hill.jpg')

imagename='detection'
rectangle_coordinates = (100, 50, 200, 150)

rectangle_coordinates1 = (150, 100, 200, 150)

x, y, w, h = rectangle_coordinates
x1, y1, w1,h1 = rectangle_coordinates1

cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.rectangle(image, (x1, y1), (x1 + w1, y1 + h1), (0, 255, 0), 2)



text = "Votre texte ici"
cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
cv2.putText(image, text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
cv2.imwrite('hills.jpg',image)
cv2.imshow(imagename, image)
cv2.waitKey(0)
cv2.destroyAllWindows()
