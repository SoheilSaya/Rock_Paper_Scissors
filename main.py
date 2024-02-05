
import time
t0=time.time()

print('t0',time.time()-t0)
t0=time.time()
import cv2
from tkinter import PhotoImage
import tkinter as tk
import re
import numpy as np
import requests
import os
import random
import threading
import pyaudio
import vlc

import argparse
import queue
import sys
import sounddevice as sd
import urllib.parse




timeout_seconds = 10

print('t1',time.time()-t0)
t0=time.time()

from cvzone.HandTrackingModule import HandDetector
print('t100',time.time()-t0)
t0=time.time()
# Constants for gestures
ROCK = 0
PAPER = 1
SCISSORS = 2

# Gesture names
global gesture_names
gesture_names = ["سنگ", "کاغذ", "قیچی"]

print('t10',time.time()-t0)
t0=time.time()

def tts(question,answer,static_answer):
    if not answer:
        update_face("")
        update_text('عدم ارتباط با سرور')
        root.update()
        print("API request failed; no answer; check your internet connection.")
        time.sleep(1)
        return ''
    print('static_answer:',static_answer)
    print('check_file_exists:',check_file_exists(f'voices/{question}.mp3'))
    if not check_file_exists(f'voices/{question}.mp3') or not static_answer:
        print('newwwwwwwwwwwwwwww')
        save_audio_from_url(answer,f'voices/{question}.mp3')
        print('created')
    simpleVlcFile(question)
    print(question)
    print(answer)
    print('___________________________')
print('t11',time.time()-t0)
t0=time.time()
def vlcfile(question,detected_word): 
    # update_face("resources/15.png")
    # root.update()
    update_face("")  # Hide the image
    update_text(detected_word)
    root.update()
    player = vlc.MediaPlayer(f"voices/{question}.mp3")
    print('vlc local play')

    player.play()
    counter=0
    faced=False
    while player.get_state() != vlc.State.Ended:
        if counter>4 and not faced:
            update_face("resources/13.png")
            root.update()
            faced=True
        print('delay')
        time.sleep(0.1)
        counter+=1
    player.release()
print('t12',time.time()-t0)
t0=time.time()
def vlctts(text,detected_word):
    # update_face("resources/15.png")
    # root.update()
    t0=time.time()
    update_face("")  # Hide the image
    update_text(detected_word)
    root.update()
    url=str(f'api.farsireader.com/ArianaCloudService/ReadTextGET?APIKey=4JN129JCAF20A6S&Text={text}&Speaker=Male1&Format=mp3')
    url2=urllib.parse.quote(url)    
    player = vlc.MediaPlayer("https://"+url2)
    player.play()
    counter=0
    faced=False
    while player.get_state() != vlc.State.Ended:
        if counter>4 and not faced:
            update_face("resources/13.png")
            root.update()
            faced=True
        print('delay')
        time.sleep(0.1)

    player.release()

print('t2',time.time()-t0)
t0=time.time()

class EmptyContentError(Exception):
  pass 
def simpleVlcFile(question): 
  global isSpeaking
  isSpeaking = True

  # Encode the filename
  encoded_question = urllib.parse.quote(question)  
  print('en',encoded_question)
      
  decoded_question = urllib.parse.unquote(encoded_question)
  print('de',decoded_question)
      
  file_path = f"voices/{decoded_question}.mp3"
  print(file_path)
  player = vlc.MediaPlayer(file_path)
  print('vlc local play')
  player.play()

  while player.get_state() != vlc.State.Ended:
      print('delay')
      time.sleep(0.1)

  player.release()
  isSpeaking = False

  # Decode the filename back to its original form
  decoded_question = urllib.parse.unquote(encoded_question)
  print(f"Original Filename: {decoded_question}")
      
    
def save_audio_from_url(text: str, file_name: str):
  tts_url = f'https://api.farsireader.com/ArianaCloudService/ReadTextGET?APIKey=4JN129JCAF20A6S&Text={text}&Speaker=Male1&Format=mp3'
  try:
      response = requests.get(tts_url, timeout=timeout_seconds)
      response.raise_for_status()
      if not response.content:
          raise EmptyContentError("شارژ")
      with open(file_name, 'wb') as file:
          file.write(response.content)
  except requests.exceptions.RequestException as e:
      update_face("")
      update_text('عدم ارتباط با سرور')
      root.update()
      print("Ariana API request failed; check your internet connection.")
      time.sleep(1)
  except EmptyContentError as e:
      update_face("")
      update_text('شارژ')
      root.update()
      print("فایل خالی فایل خالی فایل خالی")
      time.sleep(1)
# Function to determine the winner
def determine_winner(machine_gesture, player_gesture):
    # Rules: Rock beats scissors, scissors beats paper, paper beats rock
    if machine_gesture == player_gesture:
        return "مساوی شدیم"
    elif (machine_gesture == ROCK and player_gesture == SCISSORS) or \
         (machine_gesture == SCISSORS and player_gesture == PAPER) or \
         (machine_gesture == PAPER and player_gesture == ROCK):
        return "حافظ برد"
    else:
        return "حافظ باخت"
def check_file_exists(file_name: str):
  base_directory = os.getcwd()
  file_path = os.path.join(base_directory, file_name)
  return os.path.exists(file_path)

print('t3',time.time()-t0)
t0=time.time()


# Initialize video capture
cap = cv2.VideoCapture(0)
print('t30',time.time()-t0)
t0=time.time()
cap.set(3, 640)
cap.set(4, 360)
print('t31',time.time()-t0)
t0=time.time()
# Initialize hand detector
detector = HandDetector(detectionCon=0.6, maxHands=1)


print('t4',time.time()-t0)
t0=time.time()
# Main game loop





import threading
import cv2
import time


image_path = "dependencies/help.png"  # Replace with the path to your image
image = cv2.imread(image_path)

# Display the image
cv2.imshow("Image", image)
cv2.moveWindow("Image", 0, 0)
cv2.waitKey(1000)  # Wait for 3 seconds (3000 milliseconds)
cv2.destroyAllWindows()



# Global variables
webcam_image = None
game_running = True
def show_gesture_image(image_path, gesture_name, duration_ms=4000):
    gesture_image = cv2.imread(image_path)

    # Resize the gesture image to fit next to the video feed
    gesture_image = cv2.resize(gesture_image, (300, 300))

    # Create a blank canvas to display both video feed and gesture image
    display_image = np.zeros((480, 640 + 300, 3), dtype=np.uint8)  # Adjusted the height to match webcam image height

    # Insert the webcam feed into the display image
    display_image[:480, :640] = webcam_image  # Adjusted the height to match webcam image height

    # Insert the gesture image next to the webcam feed
    display_image[:300, 640:] = gesture_image

    # Add text indicating the detected gesture
    cv2.putText(display_image, gesture_name, (720, 350), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    # Display the combined image
    cv2.imshow("Webcam Feed with Gesture", display_image)
    cv2.waitKey(duration_ms)  # Wait for the specified duration in milliseconds
    cv2.destroyAllWindows()  # Close the window after the specified duration

# Function to continuously capture frames from the webcam feed
player_gesture=None
def capture_webcam_feed():
    global webcam_image, game_running,hands,player_gesture,gesture_names,machine_gesture

    cap = cv2.VideoCapture(0)

    while game_running:
        ret, frame = cap.read()
        if ret:
            webcam_image = frame.copy()
            hands, img = detector.findHands(webcam_image)
            if player_gesture is None:
                cv2.imshow("Webcam Feed", img)
            else:
                #show the image of the hand gesture next to the video feed
           # Display the appropriate gesture image next to the webcam feed
                if machine_gesture == ROCK:
                    show_gesture_image("dependencies/rock.png", "Rock")
                    machine_gesture = None
                elif machine_gesture == PAPER:
                    show_gesture_image("dependencies/paper.png", "Paper")
                    machine_gesture = None
                elif machine_gesture == SCISSORS:
                    show_gesture_image("dependencies/scissors.png", "Scissors")
                    machine_gesture = None

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Function to simulate the Rock-Paper-Scissors game logic
def rps_game():
    print('rps')
    global webcam_image, game_running,hands,player_gesture,gesture_names,machine_gesture
    
    while game_running:
        print('rps')
        player_gesture = None
        # Your Rock-Paper-Scissors game logic here
        # Display timer
        for timer in range(3, 0, -1):
            if timer==3:
              tts('سنگ',f'سنگ',True)
            if timer==2:
              tts('کاغذ',f'کاغذ',True)
            if timer==1:
              tts('قیچی',f'قیچی',True)
            # Clear the frame
        
            # img_copy = img.copy()
            # cv2.putText(img_copy, str(timer), (int(img_copy.shape[1] / 2) - 25, int(img_copy.shape[0] / 2) + 25),
            #             cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 0), 3)
        
            cv2.waitKey(10)
            #tts(سنگ,f'سنگ',True)
            # Clear the frame again after each iteration
        
        #_, img = cap.read()
    
       # img_copy = img.copy()

        # Show the camera feed
        #cv2.imshow("Smart Camera", img)

        # Fetch and display the image

        # Update the display immediately
        #cv2.waitKey(1)
        # Generate a random gesture for the machine
        
        
        
        
        if webcam_image is not None:
            machine_gesture = random.randint(0, 2)

            if hands:
                hand = hands[0]  # Assuming there's only one hand detected
                fingers = detector.fingersUp(hand)

                # Determine player's gesture based on the number of fingers up
                if fingers[0] == 0 and fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 0 and fingers[4] == 0:
                    player_gesture = SCISSORS
                elif fingers[0] == 0 and fingers[1] == 0 and fingers[2] == 0 and fingers[3] == 0 and fingers[4] == 0:
                    player_gesture = ROCK
                elif fingers[0] == 1 and fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 1:
                    player_gesture = PAPER
                else:
                    player_gesture = None


                if player_gesture is not None:
                    result = determine_winner(machine_gesture, player_gesture)
                    print("حافظ:", gesture_names[machine_gesture])
                    tts(f'حافظ {gesture_names[machine_gesture]}',f'حافظ {gesture_names[machine_gesture]} آورد',True)
                    print("کاربر:", gesture_names[player_gesture])
                    tts(f'کاربر {gesture_names[player_gesture]}',f'کاربر {gesture_names[player_gesture]} آورد',True)
                    print(result,'\n_____________________________')
                    tts(result,f'{result}',True)
                else:
                    tts("چیزی ندیدم","چیزی ندیدم",True)
            else:
                tts("چیزی ندیدم","چیزی ندیدم",True)


            if cv2.waitKey(1) == ord("q"):
                break
        
            print("Image captured and processed for RPS game.")
            webcam_image = None  # Reset the webcam image after processing

        # Simulate the game delay
        time.sleep(0.5)  # Adjust the timing as needed

# Start the threads
# Start the threads
def start_webcam():
    capture_webcam_feed()

def start_rps_game():
    rps_game()

# Create threads for each function
webcam_thread = threading.Thread(target=start_webcam)
rps_thread = threading.Thread(target=start_rps_game)

# Start the webcam thread first
webcam_thread.start()

# Allow some time for the webcam thread to initialize
time.sleep(5)

# Start the Rock-Paper-Scissors logic thread
rps_thread.start()

# Wait for both threads to finish
webcam_thread.join()
rps_thread.join()







cap.release()
cv2.destroyAllWindows()
