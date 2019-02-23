import urllib3
import re
import const
import os
import json

class Crawl():
	def __init__(self, header):
		self.http = urllib3.PoolManager()
		self.header = header

	def get_page_content(self, url, formdata, re_pattern = None, handle_method = None):
		
		page = self.http.request('POST', url, fields = formdata)
		page = page.data.decode('utf8', 'ignore')
		# print(page)
		if re_pattern is None:
			return page
		else:
			ttt = re_pattern.findall(page)
			if handle_method is None:
				return ttt
			else:
				return handle_method(ttt)
		# except Exception as err:
		# 	print(err)
		# 	return None


	def save_page(self, url, filetitle, save_path,):
		html = self.http.request('GET', url, headers = self.header).data.decode('utf8', 'ignore')
		print(html)
		fout = open(os.path.join(save_path, '%s.html' % filetitle), 'w')
		print(html, file = fout)
		fout.close()

	def save_index(self, index_list, save_name):
		fout = open(save_name, 'w')
		for v in index_list:
			print(json.dumps(v, ensure_ascii = False), file = fout)
		fout.close()

	def read_list(self, filename):
		fin = open(filename, 'r')
		return [json.loads(line) for line in fin.readlines()]



def change(re_find):
	ans = []
	for v in re_find:
		ans.append({'url': v[0], 'title': v[1]})
	return ans


if __name__ == '__main__':
	crawl = Crawl(const.header)
	formdata = const.formdata

	'''
	page_list = []

	for i in range(96):
		if (i != 0):
			formdata['OldPageIndex'] = i - 1
		print(i)
		formdata['Pager.PageIndex'] = i
		tmp = crawl.get_page_content(const.index_url, formdata, re_pattern = const.index_pattern, handle_method = change)
		page_list += tmp
		# print(tmp)

	crawl.save_index(page_list, '../data/pkulaw/index.json')
	'''

	page_list = crawl.read_list('../data/pkulaw/index.json')

	for v in page_list:
		url = 'http://www.pkulaw.com' + v['url']
		print(url)
		crawl.save_page(url, v['title'], '../data/pkulaw/')




