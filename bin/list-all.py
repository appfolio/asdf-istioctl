#!/usr/bin/env python3
from distutils.version import LooseVersion
from urllib import request
import os
import json

def get_releases():
  req = request.Request("https://api.github.com/repos/istio/istio/releases")

  github_token = os.getenv('GITHUB_API_TOKEN')
  if github_token:
    req.add_header('Authorization', f'token {github_token}')
    
  return json.load(request.urlopen(req))

def get_version_number(release):
  return release['tag_name']

releases = get_releases()
version_numbers = list(map(get_version_number, releases))
version_numbers.sort(key=LooseVersion)
space_seperated_versions = " ".join(version_numbers)

print(space_seperated_versions)
