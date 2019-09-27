from nose.tools import assert_true
import requests
from constants import NAME_URL,JOKE_URL

def test_name_response():
  response = requests.get(url = NAME_URL)
  assert_true(response.ok)

def test_joke_response():
  response = requests.get(url = JOKE_URL)
  assert_true(response.ok)
