# youtube-downloader-python
Python script to download the youtube videos to mp3 by reading a text file containing multiple links

# How to use
First you have to install all requirements by 
~~~~
    chmod +x install.sh
    sudo ./install.sh
~~~~
Now you requirements are installed 
Make a text file in the same directory and put links you have to be downloaded by newline for example you can check test.txt make one like that including the links you needed.
~~~~
    python youtube_downloader.py <your text file name here>
~~~~
example in my case:
~~~~
    python youtube_downloader.py test.txt
~~~~
Youtube links mp3 file would be downloaded to the same directory.
