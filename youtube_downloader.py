from __future__ import unicode_literals
import youtube_dl
import sys

class colors:
    reset='\033[0m'
    red='\033[31m'
    green='\033[32m'
    orange='\033[33m'
    blue='\033[34m'

print colors.green + """
__   __          _         _          
\ \ / /__  _   _| |_ _   _| |__   ___ 
 \ V / _ \| | | | __| | | | '_ \ / _ \
  | | (_) | |_| | |_| |_| | |_) |  __/
  |_|\___/ \__,_|\__|\__,_|_.__/ \___|
                                      
     _                     _                 _           
  __| | _____      ___ __ | | ___   __ _  __| | ___ _ __ 
 / _` |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
| (_| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   
 \__,_|\___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   
                                                         

""" + "\n\t\t" + colors.blue + "author: " + colors.orange + "r4pt3r" + "\n" + colors.reset


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

with open(sys.argv[1], "r") as ins:
	array = []
	for line in ins:
		array.append(line)
for i in array:
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
	    ydl.download([i])
