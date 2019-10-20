import re
import urllib
import numpy as np
from bs4 import BeautifulSoup


##########-*- get phosphorylation of protein sequence -*-##########
def crawl_web_phosp(seq_all):
	url = "http://www.dabi.temple.edu/disphos/pred/predict"
	headers = {
		"User-Agent": "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;",
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
		"Host": "www.dabi.temple.edu",
		"Origin": "http://www.dabi.temple.edu",
		"Referer": "http://www.dabi.temple.edu/disphos/",
		"Content-Type": "multipart/form-data; boundary=----WebKitFormBoundarykgdpT9IlfSthlGa3",
		"Accept-Encoding": "gzip, deflate",
		"DNT": "1"
	}
	formdata = {
		"seq": seq_all,
		"seqfile": "(binary)",
		"org": "0",
		"submit": "Predict"
	}
	data = urllib.parse.urlencode(formdata).encode('utf-8')
	request = urllib.request.Request(url, data=data)
	response = urllib.request.urlopen(request)
	html = response.read()
	soup = BeautifulSoup(html,features="html.parser")
	trs = soup.find_all("tr")

	pho_site_set = []
	pho_score_set = []
	for i in range(1,len(trs)):
		string_trs = trs[i]
		s = list(filter(None,re.split('<.{2,5}>',str(string_trs))))
		pho_site = int(s[0])
		pho_score = float(s[2])
		pho_site_set.append(pho_site)
		pho_score_set.append(pho_score)    
	seq = seq_all.split('\n')[-1]
	seq_score = np.zeros((len(seq),len(seq)))

	for i in range(len(pho_site_set)):
		phosite = pho_site_set[i]
		if phosite > len(seq)-4:
			seq_score[phosite-4-1:len(seq),phosite-1] = [pho_score_set[i]]*(len(seq)-phosite +5)
		elif phosite  <=4:
			seq_score[0:phosite+4,phosite-1] = [pho_score_set[i]]*(phosite+4)
		else:
			seq_score[phosite-4-1:phosite+4,phosite-1] = [pho_score_set[i]]*9

	score_mean_set = []
	for j in range(len(seq_score)):
		if np.sum(seq_score[j,]) != 0:
			score_mean = round(np.mean(list(filter(None,list(seq_score[j,])))),4)
			score_mean_set.append(score_mean)
		elif  np.sum(seq_score[j,]) == 0:
			score_mean_set.append(0)
	score = str(score_mean_set).strip('[]').split(',')
	return score
	

##########-*-get hydrophilic index of protein sequence-*-##########
def hy_idx(fasta_seq):
	ECS_dic = {'R':-2.5,'K':-1.5,'D':-0.90,'Q':-0.85,'N':-0.78,
			'E':-0.74,'H':-0.40,'S':-0.18,'T':-0.05,'P':0.12,
			'Y':0.26,'C':0.29,'G':0.48,'A':0.62,'M':0.64,
			'W':0.81,'L':1.1,'V':1.1,'F':1.2,'I':1.4,'U':0.006,'X':0.006}
	#U and X is the average of the 20 aa (accurate results=0.006000000000000017 )
	hy_num = []
	for i in range(len(fasta_seq)):
		seq_a = fasta_seq[i]
		hy_num_i = ECS_dic[seq_a]
		hy_num.append(hy_num_i)
	hy_num_lst = str(hy_num).strip('[]').split(',')
	return hy_num_lst
	
	
##########-*- get the fac_cpx of protein sequence -*-##########
def fac_cpx(w):
	keep_str = []
	for j in range(len(w)+1):
		for i in range(len(w)-j+1):
			keep_str.append(w[i:i+j])
	keep_str = list(filter(None,keep_str))
	keep_str_set = set(keep_str)
	keep_str_sorted = sorted(keep_str_set,key = lambda i:len(i),reverse=False)
	keep_num = []
	for i in range(1,len(w)+1):
		temporary_list =[]
		for j in range(len(keep_str_sorted)):
			if len(keep_str_sorted[j]) == i:
				temporary_list.append(keep_str_sorted[j])
		keep_num.append(temporary_list)
	fac_num = []
	for i in range(len(keep_num)):
		fac_num.append(len(keep_num[i]))
	return fac_num


##########-*- get abe_cpx of protein sequence -*-##########
def get_set_number(a):
	temporary_deposit  = []
	for i in range(len(a)):
		a[i] = sorted(a[i])
		a[i] = ''.join(a[i])
		temporary_deposit.append(a[i])
	temporary_deposit_set = set(temporary_deposit)
	temporary_deposit_set_length = len(temporary_deposit_set)
	return temporary_deposit_set_length

def abe_cpx(w):
	keep_str = []
	for j in range(len(w)+1):
		for i in range(len(w)-j+1):
			keep_str.append(w[i:i+j])
	keep_str = list(filter(None,keep_str))  #filter "" of all examples
	keep_str_set = set(keep_str)
	keep_str_set = sorted(keep_str_set,key = lambda i:len(i),reverse=False)
	list_num = []
	for i in range(1,len(w)+1):
		list_temporary =[]
		for j in range(len(keep_str_set)):
			if len(keep_str_set[j]) == i:
				list_temporary.append(keep_str_set[j])
		list_num.append(list_temporary)
	Abe_num = []
	for i in range(len(list_num)):
		Abe_num.append(get_set_number(list_num[i]))
	return Abe_num