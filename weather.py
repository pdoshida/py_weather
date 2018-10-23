#!/usr/bin/env python
# coding: utf-8

import requests
import json

def get_weather():
	url = 'http://weather.livedoor.com/forecast/webservice/json/v1'
	payload = {'city': '130010'} # tokyo
	data = requests.get(url, params = payload).json()

	print(data['title'])
	for weather in data['forecasts']:
		print(weather['dateLabel'] + ':' + weather['telop'])

	return

if __name__ == '__main__':

	get_weather()
