import urllib3

class crawl():
	def __init__(self, header, ):
		self.http = urllib3.PoolManager()
		self.header = header