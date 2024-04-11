'''Remember to edit those fields , or else good luck'''

import requests
import json
import base64
from datetime import date
from datetime import datetime

# Set up the authentication credentials
username = 'your username'                                    # Edit it
password = 'your github password'                             # Edit it
repository_name = 'repo name'                                 # This too
file_path = 'file path in the following repo'                 # This also
commit_message = 'commit message'                             # This too

# Create a new file or update an existing one
url = f'https://api.github.com/repos/{username}/{repository_name}/contents/{file_path}'
headers = {
    'Accept': 'application/vnd.github+json',
    'Authorization': f'token {password}'
}
response = requests.get(url, headers=headers)

# getting current date and time 
curDateTime = date.today()
dt = datetime.now()

if response.status_code == 200:
    # File exists, read and update it
    sha = response.json()['sha']
    content = base64.b64decode(response.json()['content']).decode()
    content += f'Stuff you want to commit in that file'             #main thing is here 'your content'
    content_encoded = base64.b64encode(content.encode()).decode()
    data = {
        'message': commit_message,
        'content': content_encoded,
        'sha': sha
    }
    response = requests.put(url, headers=headers, data=json.dumps(data))
else:
    # File doesn't exist, create it
    content = f'{curDateTime}: your file content'
    content_encoded = base64.b64encode(content.encode()).decode()
    data = {
        'message': commit_message,
        'content': content_encoded
    }
    response = requests.put(url, headers=headers, data=json.dumps(data))

if response.status_code == 200:
    print('File committed successfully')
else:
    print(f'Failed to commit file: {response.text}')
