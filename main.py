# from ssl import VerifyMode
from urllib import response
from flask import Flask, render_template,request,session,redirect,flash,url_for
from os import environ
from datetime import timedelta
import datetime
import isodate
import json, requests
import re
# logging
from dotenv import dotenv_values
with open('config.json','r') as c:
    params = json.load(c)["params"]
# yt_api = environ.get('yt_api')

# local_server=True
app = Flask(__name__)
def get_id(playlist_link):
    p = re.compile('^([\S]+list=)?([\w_-]+)[\S]*$')
    m = p.match(playlist_link)
    if m:
        return m.group(2)
    else:
        return 'invalid_playlist_link'
@app.route("/",methods=['GET','POST'])
def home():
    if(request.method=='POST'):
        link=request.form.get('link')
        # playlist_id = get_id(link)
        # replace with your api
        
        # replace with your playlist_id
        
        
        noOfVideos,avgLength,totalLength,at125,at150,at175,at200 = get_time(link)
        return render_template("ans.html",noOfVideos=noOfVideos,avgLength=avgLength,totalLength=totalLength,at125=at125,at150=at150,at175=at175,at200=at200)

    elif(request.method=='GET'):
        return render_template('index.html',params=params)

def get_time(link):
    # yt_api = params['API_KEY']
    # yt_api = environ.get('yt_api')
    a = dotenv_values('.env')
    yt_api = a['yt_api']
    playlist_id = get_id(link)
    URL1 = 'https://www.googleapis.com/youtube/v3/playlistItems?part=contentDetails&maxResults=50&fields=items/contentDetails/videoId,nextPageToken&key={}&playlistId={}&pageToken='.format(yt_api, playlist_id)
    URL2 = 'https://www.googleapis.com/youtube/v3/videos?&part=contentDetails&key={}&id={}&fields=items/contentDetails/duration'.format(yt_api, '{}')
    
    next_page = ''
    cnt = 0
    a = timedelta(0)

    while True:
        vid_list = [] 

        results = json.loads(requests.get(URL1 + next_page).text)
        
        for x in results['items']:
            vid_list.append(x['contentDetails']['videoId'])
            
        url_list = ','.join(vid_list)
        cnt += len(vid_list)

        op = json.loads(requests.get(URL2.format(url_list)).text)
        for x in op['items']:
            a += isodate.parse_duration(x['contentDetails']['duration'])

        if 'nextPageToken' in results:
            next_page = results['nextPageToken']
        else:
            noOfVideos = str(cnt) 
            avgLength = str(a/cnt) 
            totalLength = str(a)
            at125 = str(a/1.25) 
            at150 = str(a/1.5) 
            at175 = str(a/1.75) 
            at200 = str(a/2)
            break
    return noOfVideos,avgLength,totalLength,at125,at150,at175,at200
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
# app.run(debug=True,port=5001)

