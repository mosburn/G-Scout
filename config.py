import os.path
import argparse
from oauth2client.service_account import ServiceAccountCredentials
from oauth2client.client import GoogleCredentials
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage
from oauth2client import tools

CLIENT_ID = '206629590950-6o7fig55aupliolgt6o10obpnagdf4pd.apps.googleusercontent.com'
CLIENT_SECRET = 'qgRgh8NA4Y8Qlqn7r7ulrKXV'#not actually a secret
flow = OAuth2WebServerFlow(client_id=CLIENT_ID,
                           client_secret=CLIENT_SECRET,
                           scope='https://www.googleapis.com/auth/cloud-platform')

storage = Storage('creds.data')
parser = argparse.ArgumentParser(parents=[tools.argparser])
flags = parser.parse_args(args=[])

if os.path.isfile('keyfile.json'):
	creds = GoogleCredentials.get_application_default()
else:
	creds = tools.run_flow(flow, storage, flags)
	
storage.put(creds)