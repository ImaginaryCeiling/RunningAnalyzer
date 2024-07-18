import cv2
import numpy as np
from joints import Joints, extract_joints
import mediapipe as mp
from utils import calculate_angle

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose



def analyzePose(input_video, output_location, background_choice):

    black_background = np.zeros(frame.shape, dtype=np.uint8)

    cap = cv2.VideoCapture(str(input_video)+'.mp4')

# Get video properties
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    # Define the codec and create VideoWriter object
    #output_location = string from function
    out = cv2.VideoWriter(str(output_location), cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))



# Setup mediapipe instance
    with mp_pose.Pose(min_detection_confidence=0.1, min_tracking_confidence=0.1) as pose:

        while cap.isOpened():
            ret, frame = cap.read()
            
            if not ret:
                print("Ignoring empty camera frame.")
                break

            # Recolor image to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            
            # Make detection
            results = pose.process(image)
            
            # Create a black background
            if background == "black":
                background = black_background
            elif background == "video":
                background = frame
            
            # Extract landmarks
            try:
                landmarks = results.pose_landmarks.landmark
                if landmarks:
                    # Make instance of joints
                    Joints = extract_joints(landmarks)
                    
                    # Get coordinates
                    right_shoulder = Joints.right_shoulder
                    right_elbow = Joints.right_elbow
                    right_wrist = Joints.right_wrist

                    # Calculate angle
                    angle = calculate_angle(right_shoulder, right_elbow, right_wrist)
                    cv2.putText(background, str(round(angle, 2)), 
                                (10,100), 
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (57, 255, 20), 2, cv2.LINE_AA
                                )
                    
                    # Debugging prints
                    print(f"Shoulder: {right_shoulder}, Elbow: {right_elbow}, Wrist: {right_wrist}, Angle: {angle}")

            except Exception as e:
                print(f"Error: {e}")
            
            # Render detections
            mp_drawing.draw_landmarks(background, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            # Write the frame to the video file
            out.write(background)

            cv2.imshow('Pose Skeleton', background)
            if cv2.waitKey(5) & 0xFF == 27:
                break

    cap.release()
    out.release()
    cv2.destroyAllWindows()