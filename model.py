from sklearn.cluster import AgglomerativeClustering
from features import social_data_nums
from sklearn.model_selection import train_test_split
import scipy.cluster.hierarchy as sch
import matplotlib.pyplot as pt
from evaluation import evaluate_metrics

train, test = train_test_split(social_data_nums)

# silhouette_score where a high value indicates well-defined clusters.
# calinski_harabasz_score Higher values indicate better-defined clusters.
#  davies_bouldin_score A lower Davies-Bouldin Index is indicative of better clustering.

# silhouette_score for 6 clusters =>  0.4731587966832308
# calinski_harabasz_score for 6 clusters => 59.31580646293113
# davies_bouldin_score for 6 clusters => 0.7798346460341712


def fit_predict(data, n_clusters, name):
    clustering = AgglomerativeClustering(n_clusters=n_clusters, linkage="ward")
    Y_pred_train = clustering.fit_predict(data)
    evaluate_metrics(data, Y_pred_train, n_clusters)

    dendrogram = sch.dendrogram(sch.linkage(data, method="ward"))
    pt.savefig(f"dendrogram-test-{name}.png")


fit_predict(train, 6, name="train-12")
fit_predict(test, 6, name="test-12")
