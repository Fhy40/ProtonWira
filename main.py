from flask import Flask, redirect, url_for, render_template,request,send_from_directory,request, jsonify, make_response 
import subprocess
import time
try:
    import pytube
except Exception as e:
    print("Some modules are missing {}".format(e))

cur_processing_progress = 0    
cur_processing_status = "Starting"

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("main.html")

@app.route('/', methods=['POST'])
def submit():
    global cur_processing_progress
    cur_processing_progress = 0    
    youtube_url = request.form["youtube-url"]
    youtube_start_time = request.form["youtube-start-time"]
    youtube_duration = request.form["youtube-duration"]
    print("This is the youtube url retrieved " + youtube_url)
    print("Youtube Video Start Time " + youtube_start_time)
    print("Youtube Video Duration " + youtube_duration)
    furble_palace(youtube_url,youtube_start_time,youtube_duration)
    #For windows you need to use drive name [ex: F:/Example.pdf]
    path = r"\\trex\Self-Host\python\flask_youtube_gfycat\output"
    print("SENDING FILE")
    print("Current Processing Progress is: " + str(cur_processing_progress))   
    return send_from_directory(path, filename="proton_wira.mp4", as_attachment=True)
    
    

@app.route('/testkitchen', methods=['POST'])
def progress_get():
    global cur_processing_progress
    global cur_processing_status
    print("Sending current progress " + str(cur_processing_progress))
    res = make_response(jsonify({"progress" : str(cur_processing_progress),"status" : cur_processing_status}))
    return res
    
def furble_palace(url,start_time,duration):
    global cur_processing_progress    
    cur_processing_progress = 25
    global cur_processing_status
    cur_processing_status = "Downloading"
    
    ytd = pytube.YouTube(url)
    try:
        ytd = ytd.streams.filter(adaptive=True, resolution="720p").first().download('downloads',filename='proton')
    except:
        print("There doesn't seem to be a 720p version of this video, trying 480p")
        try:
            ytd = ytd.streams.filter(adaptive=True, resolution="480p").first().download('downloads',filename='proton')
        except:
            print("There doesn't seem to be a 480p version of this video, trying 360p")
            try:
                ytd = ytd.streams.filter(adaptive=True, resolution="360p").first().download('downloads',filename='proton')
            except:
                print("There doesn't seem to be a 360p version of this video, trying 240p, what the hell man")        
                try:
                    ytd = ytd.streams.filter(adaptive=True, resolution="240p").first().download('downloads',filename='proton')
                except:
                    print("There doesn't seem to be a 240p version of this video, okay gosh damn, fine, 144p then, jeez")
                    ytd = ytd.streams.filter(adaptive=True, resolution="144p").first().download('downloads',filename='proton')
    print("Download Finished")
    cur_processing_progress = 75
    print(cur_processing_progress)
    time.sleep(5)
    cur_processing_status = "Converting"
    cur_processing_progress = 85    
    ffmpeg_function(start_time,duration)
    cur_processing_progress = 100
    cur_processing_status = "Finished"

def ffmpeg_function(start_time,duration):
    download_location = r"\\trex\Self-Host\python\flask_youtube_gfycat\downloads"
    output_location = r"\\trex\Self-Host\python\flask_youtube_gfycat\output"
    file_name = r"\proton.mp4"
    file_output = r"\proton_wira.mp4"
    ffmpeg_command = "ffmpeg -i " + download_location + file_name + " -ss " + start_time + " -t " + duration + " -c copy " + output_location + file_output + " -y"
    print(ffmpeg_command)
    cmd_ffmpeg_command = subprocess.run(ffmpeg_command, capture_output = True, text =True)
    global cur_processing_progress 
    cur_processing_progress = 95
    global cur_processing_status
    cur_processing_status = "Converted"
    print(cur_processing_progress)
    print(cmd_ffmpeg_command.stdout)

def validate_video(url,start_time,duration):
    ytd = pytube.YouTube(url)
    print("The length of the Youtube Video has is: " + str(ytd.length))
    
    
    
    