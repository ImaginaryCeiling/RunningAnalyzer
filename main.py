import numpy as np
import cv2
from analyze_pose import analyzePose
import sys

welcomeMessage = "Welcome to the Form Analysis Tool. The following few questions will ask you about what your preferences are."

#ask for input choices
print(welcomeMessage)
print("")

#black background or video background
print("Question 1: Would you like to see just the pose skeleton or would you like to see it overlayed on the video?")
background_choice = input("Enter black for a black background or video for a video background: ")
if background_choice == "black" or background_choice == "video":
    background = background_choice
else:
    print("Invalid input. Please try again.")
    sys.exit()
    


print("Question 2: What would you like the output video to be saved as?")
output_choice = input("Enter the name of the output video file you would like to save. Do not include .mp4 in your input. Example: output_video : ")

input_video = input("Enter the name of the video file you would like to analyze. Ensure it is .mp4 format. Example: input_video.mp4 : ")

analyzePose(input_video, output_choice, background)