import sys
import json
import Secretkey as config
try:import requests
except:from urllib import request as requests
try:print(str(requests.post("https://www.google.com/recaptcha/api/siteverify",data={"secret":config.secretGoogleApiKey,"response":sys.argv[1]}).text).split(",")[0].split(": ")[1]=="true")
except:print("None")
