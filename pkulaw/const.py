import re

index_url = 'http://www.pkulaw.com/case/search/RecordSearch'
index_pattern = re.compile(r'<a target="_blank" flink="true" href="(/pfnl/.*?)">(.*?)</a>')

page_url = ''

header = {
	
	'Access-Control-Allow-Headers': 'Content-Type',
	'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
	'Access-Control-Allow-Origin': '*',
	'Cache-Control': 'private',
	'Connection': 'keep-alive',
	'Content-Encoding': 'gzip',
	# # 'Content-Length': 7856,
	'Content-Type': 'text/html; charset=utf-8',
	# 'Date': 'Thu, 06 Dec 2018 02:22:43 GMT',
	'Server': 'nginx',
	'Vary': 'Accept-Encoding',
	'X-AspNet-Version': 0,
	'X-AspNetMvc-Version': '5.2',
	'X-Powered-By': 'WAF/2.0',
	'X-Powered-By-Defense': 'from pon-wyxm-tel-qs-qssec-kd55',
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
	'Accept-Encoding': 'gzip, deflate',
	'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
	'Cache-Control': 'no-cache',
	'Connection': 'keep-alive',
	'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
	# 'Cookie': 'gr_user_id=afa488b2-e6ae-4626-8849-777822d58234; pkulaw_v6_sessionid=ijweaabhiscnfidp4q05jjst; safedog-flow-item=A13060350CF9C2345DB82E8CA8833C26; Hm_lvt_8266968662c086f34b2a3e2ae9014bf8=1542277305,1544062751; gr_session_id_81eec0d0f0be2df1=b7222c7b-6622-4c42-a321-fe0f2130f509; gr_session_id_81eec0d0f0be2df1_b7222c7b-6622-4c42-a321-fe0f2130f509=true; xCloseNew=Fri Dec 07 2018 10:19:17 GMT+0800 (ä¸­å½æ åæ¶é´); Hm_lpvt_8266968662c086f34b2a3e2ae9014bf8=1544062941',
	'Cookie': 'gr_user_id=afa488b2-e6ae-4626-8849-777822d58234; safedog-flow-item=A13060350CF9C2345DB82E8CA8833C26; pkulaw_v6_sessionid=0qrdeepzervfdudvyfhv2gow; Hm_lvt_8266968662c086f34b2a3e2ae9014bf8=1542277305,1544062751,1544087669; Hm_lpvt_8266968662c086f34b2a3e2ae9014bf8=1544108804; gr_session_id_81eec0d0f0be2df1=5c009977-49ae-4174-90d3-5a5a3b45d9bb; gr_session_id_81eec0d0f0be2df1_5c009977-49ae-4174-90d3-5a5a3b45d9bb=true',
	'Host': 'www.pkulaw.com',
	'Origin': 'http://www.pkulaw.com',
	'Pragma': 'no-cache',
	'Referer': 'http://www.pkulaw.com/case/',
	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
	'X-Requested-With': 'XMLHttpRequest'
}

formdata = {
	'Menu': 'case',
	'Keywords': '',
	'SearchKeywordType': 'Title',
	'MatchType': 'Exact',
	'RangeType': 'Piece',
	'Library': 'pfnl',
	'ClassFlag': 'pfnl',
	'GroupLibraries': '',
	'QueryOnClick': False,
	'AfterSearch': False,
	'pdfStr': '',
	'pdfTitle': '',
	'IsAdv': False,
	'ClassCodeKey': ',04,,',
	'GroupByIndex': 0,
	'OrderByIndex': 0,
	'ShowType': 'Default',
	'GroupValue': '04',
	'FilterItems.CourtGrade': '',
	'FilterItems.TrialStep': '',
	'FilterItems.DocumentAttr': '',
	'FilterItems.TrialStepCount': '',
	'TitleKeywords': '',
	'FullTextKeywords': '',
	'Pager.PageIndex': 1,
	'Pager.PageSize': 10,
	'QueryBase64Request': '',
	'VerifyCodeResult': '',
	'isEng': 'chinese',
	'OldPageIndex': 0,
	'X-Requested-With': 'XMLHttpRequest'
}

