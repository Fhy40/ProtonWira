# ProtonWira
A Self Hosted Flask server that let's you easily convert Youtube videos into 10 - 20 second long clips to download and share


### 1. Requirements:
- Windows
  - FFMPEG
- Python Modules
  - Flask
  - subprocess
  - pytube
- Javascript
  - JQuery
- HTML & CSS
  - Bootstrap
  
### How it works?
The Flask server hosts the webpage that acts as an interface. The user pastes a youtube url and specifies the start time and duration of the the GIF/MP4. The flask server downloads said youtube video and cuts it using ffmpeg to a specified length. That file is sent back to the user as an attachment.

### How to use?
Well, that's something I'm going to have to work on. I think everything should work if you download all the files and install the requirements but I haven't tested it on another computer yet. But if you think you've got all the requirments sorted then simply start the Flask server and navigate to the webpage.
