import cv2
# Path of the input image
path = "./task/Flower.png"
# reading image (by default the flag is 1 if not specidied)
image = cv2.imread(path)
edges = cv2.Canny(image,200,300) # Canny Algorithm
cv2.imshow("Output",image)
cv2.imshow("Edges",edges)
# Wait until any key press (press any key to close the window)
cv2.waitKey()
# kill all the windows
cv2.destroyAllWindows()