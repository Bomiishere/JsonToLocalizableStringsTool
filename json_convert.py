import xlrd
import re

import datetime
from enum import Enum
import json

### Setup ###
project_directory = '/Users/bomichen/Developer/iOS_CaiLiFang/orange'
source_directory = '/Users/bomichen/Developer/Backend_CaiLiFang.Locale.Resx/Json/ios'

# define reading files by Enum
class Languages(Enum):
	Base = 'base'
	English = 'en'
	Simplified_Chinese = 'zh-Hans'
	Vietnamese = 'vi'

	def describe(self):
		return self.name, self.value

	@classmethod
	def source_directory(cls, language: "Language" = None):
		return source_directory

	def fileName(self):
		val = self.value
		if val == 'base':
			return 'ios.zh-CN.json'
		if val == 'en':
			return 'ios.en-US.json'
		if val == 'zh-Hans':
			return 'ios.zh-CN.json'
		if val == 'vi':
			return 'ios.vi-VN.json'

		return ''

	def sub_directory(self):
		val = self.value
		if val == 'base':
			return '/Base.lproj'
		if val == 'en':
			return '/en.lproj'
		if val == 'zh-Hans':
			return '/zh-Hans.lproj'
		if val == 'vi':
			return '/vi.lproj'

		return ''

### Data Process ###
print('\n=== START PROCESS ===')
for language in Languages:
	
	file_directory = Languages.source_directory() + '/' + language.fileName()
	target_directory = project_directory + language.sub_directory() + '/Localizable.strings'

	print('%s to Localizable.strings' % language.fileName())
	print('from: %s' % file_directory)
	print('to: %s' % target_directory)

	#output header
	### Output Header ###
	header_1_export_file_name = 'Localizable' + '-' + language.value + '.strings'
	header_2_from_where = 'from Backend_CaiLiFang.Locale.Resx' 
	header_3_created_by = 'auto generated'
	header_4_create_date = datetime.datetime.now().strftime('%Y/%-m/%-d')
	header_5_create_year = datetime.datetime.now().strftime('%Y')
	header_6_copyright = 'JohnsonTechInc.'
	output = '//\n//  %s\n//  %s\n//\n//  created by %s on %s.\n//  Copyright © %s %s All rights reserved.\n//\n\n' % (header_1_export_file_name, header_2_from_where, header_3_created_by, header_4_create_date, header_5_create_year, header_6_copyright)

	# parse file

	with open(file_directory) as jsonfile:
		data = jsonfile.read()
	
	jsonObject = json.loads(data)
	keys = list(jsonObject)

	row = -1
	for key in jsonObject:

		row = row + 1 # count row at begin

		value = jsonObject[key]

		export_line = '%s = \"%s\";' % (key, value)

		# detect key splited string 1st, 2nd match, if true add notes
		if row + 1 < len(jsonObject):
			next_key = keys[row+1]

		cur_split_key_results = key.split('.', 3) # split key to results
		next_split_key_results = next_key.split('.', 3) # split next_key to results

		if len(cur_split_key_results) < 3: # output condition: less than three phrases
			last_match_str = ''
			output = output + '\n' + export_line + '\n'
			continue

		cur_phrases = ''
		next_pharses = ''

		count = 0
		for r in cur_split_key_results: # get current first 2 pharses
			if count > 1: # read first 2
				break
			cur_phrases = cur_phrases + r
			count = count + 1
		
		if cur_phrases == last_match_str: # if match with last matched string, output & continue(skip)
			output = output + export_line + '\n' # output condition: matched
			continue
		else: # if not, clear last matched string
			last_match_str = ''

		count = 0
		for r in next_split_key_results: # get next first 2 pharses
			if count > 1: # read first 2
				break
			next_pharses = next_pharses + r
			count = count + 1

		if cur_phrases == next_pharses: # current & next matched, add notes
			export_line = '//%s\n' % (cur_phrases) + export_line
			last_match_str = cur_phrases

		output = output + '\n' + export_line + '\n'

	### Output File ###
	text_file = open(target_directory, "w")
	text_file.write(output)
	text_file.close()
	print('done\n')

print('=== COMPLETE ===')







