import cv2

image = cv2.imread('hill.jpg')

image_name='detection'
image_modif='modify/'+imagename+'modif.jpg'

rectangle_coordinates = (100, 50, 200, 150)


x, y, w, h = rectangle_coordinates

cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)


detection = "Votre texte ici"
police=cv2.FONT_HERSHEY_SIMPLEX
scale=0.5
cv2.putText(image, detection, (x, y - 10), police, scale, (255, 0, 0),2 )

cv2.imwrite(image_modif,image)

cv2.imshow(image_name, image)

cv2.waitKey(0)
cv2.destroyAllWindows()
