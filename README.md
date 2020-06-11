# ProtonWira
A Self Hosted Flask server that let's you easily convert Youtube videos into 10 - 20 second long clips to download and share


Requirements:
  *FFMPEG

Python Modules:
  *Flask
  *subprocess
  *pytube
  *pytube
  
 Javascript:
  *Jquery
 
 HTML & CSS:
  *Bootstrap
  
How it works?
The Youtube video is download to the download folder and then converted using FFMPEG to the output folder. Using Flask's send_from_directory
command, the video is sent to the user.