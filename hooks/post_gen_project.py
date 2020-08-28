import os
import requests
import json
import subprocess

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)

def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))

if __name__ == '__main__':
    data = json.loads('{"name":"{{cookiecutter.project_slug}}","description":"{{cookiecutter.project_description|e}}"}')
    data = json.dumps(data)
    r = requests.post('https://api.github.com/orgs/{{cookiecutter.github_organization}}/repos',
                    data = data,
                    headers={'Authorization': 'token {{cookiecutter.github_token}}'}
                    )
    if r.status_code != 201:
        print('ERROR: unable to create a new GitHub repository!')
    else:
        print('INFO: GitHub repository successfully created.')

        # on initialise le dépôt GitHub
        subprocess.call(['git', 'init'])
        # on commit
        subprocess.call(['git', 'add', '*'])
        subprocess.call(['git', 'commit', '-m', '"first commit"'])
        # on push
        subprocess.call(['git', 'remote', 'add', 'origin', 'git@github.com:{{cookiecutter.github_organization}}/{{cookiecutter.project_slug}}.git'])
        subprocess.call(['git', 'push', '-u', 'origin', 'master'])
