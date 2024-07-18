import numpy as np
import cv2
import joints
import analyze_pose

welcomeMessage = "Welcome to the Form Analysis Tool. The following few questions will ask you about what your preferences are."

#ask for input choices
print(welcomeMessage)
print("")
#black background or video background
print("Question 1: Would you like to see just the pose skeleton or would you like to see it overlayed on the video?")
background_choice = input("Enter 1 for a black background or 2 for a video background: ")
if background_choice == 1:
    background_choice = "black"
elif background_choice == 2:
    background_choice = "video"
else:
    print("Invalid input. Please try again.")

input_video = input("Enter the name of the video file you would like to analyze. Ensure it is .mp4 format. Example: input_video.mp4 : ")


#def main():



#name 3 joints you are looking for
    # 1
    # 2
    # 3