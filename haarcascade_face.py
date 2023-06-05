import cv2

# Load the pre-trained Haar cascade classifier for frontal face detection
face_cascade = cv2.CascadeClassifier("D:\\python Programs\\haarcascades\\haarcascade_frontalface_default2.xml")


# Load the image to be recognized
cap = cv2.VideoCapture("C:\\Users\\prati\\Downloads\\pexels-dimitri-baret-13575161-3840x1620-24fps.mp4")
count = 0
while True:
          ret,img = cap.read()
          img = cv2.resize(img,(1000,600))
          # Convert the image to grayscale for faster processing
          gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

          # Detect faces in the image using the face cascade classifier
          faces = face_cascade.detectMultiScale(gray, scaleFactor=1.5, minNeighbors=2)
 
          # If faces are detected, recognize them
          
          if len(faces) > 0:
                for (x,y,w,h) in faces:
                    # Draw a rectangle around each detected face
                    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)
                    # Crop the face region
                    face_roi = gray[y:y+h, x:x+w]
                    # Perform face recognition on the cropped face
                    # Add your face recognition code here
          else:     
                    print("No faces found in the image")
                    

          # Display the image with the detected and recognized faces
          cv2.imshow('Detected Faces', img)
          k=cv2.waitKey(1)
          if k==ord('q'):
                    break

cv2.destroyAllWindows()
cap.release()
