from sklearn.cluster import AgglomerativeClustering
from features import social_data_nums
from sklearn.model_selection import train_test_split
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as pt

train, test = train_test_split(social_data_nums)

clustering = AgglomerativeClustering(n_clusters=5, linkage="ward")


Y_pred_train = clustering.fit_predict(train)
Y_pred_test = clustering.fit_predict(test)

dendrogram = sch.dendrogram(sch.linkage(train[:, :], method="ward"))
pt.savefig("dendrogram-test.png")
