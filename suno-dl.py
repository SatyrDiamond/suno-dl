import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument("input")
args = parser.parse_args()

if args.input.startswith('https://suno.com/song/'):
	suuid = args.input.split('https://suno.com/song/')[1]
	mp3link = requests.get('https://cdn1.suno.ai/'+suuid+'.mp3')
	file = open(suuid+'.mp3', 'wb')
	file.write(mp3link.content)