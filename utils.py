import numpy as np
import cv2
from joints import extract_joints
from analyze_pose import results

def extract_landmarks(a,b,c):
    try:
            landmarks = results.pose_landmarks.landmark
            joints = extract_joints(landmarks)

            if joints:
                # Get coordinates
                joint1 = joints.a
                joint2 = joints.b
                joint3 = joints.c

                # Calculate angle
                angle = calculate_angle(joint1, joint2, joint3)
                display_angle = True
                
                # Debugging prints
                print(f"Shoulder: {joint1}, Elbow: {joint2}, Wrist: {joint3}, Angle: {angle}")

    except Exception as e:
        print(f"Error: {e}")


def video_properties(cap):
    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

def calculate_angle(a, b, c):
    a = np.array(a)  # First
    b = np.array(b)  # Mid
    c = np.array(c)  # End
    
    radians = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1], a[0] - b[0])
    angle = np.abs(radians * 180.0 / np.pi)
    
    if angle > 180.0:
        angle = 360 - angle
        
    return int(angle)