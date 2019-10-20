import numpy as np
from sklearn.externals import joblib
from acpdrp import crawl_web_phosp
from acpdrp import hy_idx
from acpdrp import fac_cpx
from acpdrp import abe_cpx


############-*- Predict the IDRs -*-############
def equal_seq_meanscore(L):
	seq_score = np.zeros(shape=(len(L),len(L)+3))
	for i in range(len(L)):
		seq_score[i][i:i+4] = [L[i]]*4
	score_mean_s = []
	for j in range(seq_score.shape[1]):   
		if np.sum(seq_score[:,j]) != 0:
			score_mean = round(np.mean(list(filter(None,list(seq_score[:,j])))),4)
			score_mean_s.append(score_mean)
		elif  np.sum(seq_score[:,j]) == 0:
			score_mean_s.append(0)
	return score_mean_s

def Predict_result(Model_name,seq,threshold):
	clf = joblib.load(Model_name)
	y_predict_label = ""
	y_IDR_predict = []
	IDR_phy_score = crawl_web_phosp(seq)
	IDR_hy_num = hy_idx(seq)
	for L in range(len(seq)-4+1):
		IDR_WL = seq[L:L+4]
		IDR_WL_fac = fac_cpx(IDR_WL)
		IDR_WL_abe = abe_cpx(IDR_WL)
		IDR_WL_physcore = IDR_phy_score[L:L+4]
		IDR_WL_hy_num = IDR_hy_num[L:L+4]
		IDR_WL_fac.extend(IDR_WL_abe)
		IDR_WL_fac.extend(IDR_WL_physcore)
		IDR_WL_fac.extend(IDR_WL_hy_num)
		IDR_WL_faph = IDR_WL_fac
		IDR_WL_faph = [float(x) for x in IDR_WL_faph]
		IDR_WL_faph_arr = np.array(IDR_WL_faph).reshape(1,-1)
		y_IDR_predict_proba = clf.predict_proba(IDR_WL_faph_arr)
		y_IDR_predict.append([round(x[-1],2) for x in y_IDR_predict_proba][0])
	y_IDR_predict_mean = equal_seq_meanscore(y_IDR_predict)

	for i in range(len(y_IDR_predict_mean)):
		if y_IDR_predict_mean[i] < threshold:
			y_predict_label += '0'
		elif y_IDR_predict_mean[i] >= threshold:
			y_predict_label += '1'
	return y_IDR_predict_mean,y_predict_label



if __name__ == "__main__"
	seq = 'IMWRNAKRQSDRFYDEDVFINGEGLEPEQDTRGVDNAHMVTNHHALRSRDNIYEYRDSPSTKTLASKAHTDTTSLRSPSSLAMTQKSSSQASLKSGISLKETNGHLVKQSERAATPRSQQNGSIAKVASPPVEEKRLLQPLSSTPVTQLQAEPAKRVPTAASVSGSSRSTTPVPSARSTTTHTTTATLSSQPAAQPRRTHLVEGVPQTSVHHHHHH'
	_,y_predict_label = Predict_result('acpdrp_model.m',seq,0.95)
	print ("y_predict_label:",y_predict_label)