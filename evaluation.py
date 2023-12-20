from sklearn.metrics import (
    silhouette_score,
    calinski_harabasz_score,
    davies_bouldin_score,
)


def evaluate_metrics(features, labels_pred, n_clusters):
    silhouette_value = silhouette_score(features, labels_pred)
    calinski_value = calinski_harabasz_score(features, labels_pred)
    davies_bouldin_value = davies_bouldin_score(features, labels_pred)
    print(f"silhouette_score for {n_clusters} clusters =>  {silhouette_value}")
    print(f"calinski_harabasz_score for {n_clusters} clusters => {calinski_value}")
    print(f"davies_bouldin_score for {n_clusters} clusters => {davies_bouldin_value}")
    return (silhouette_value, calinski_value, davies_bouldin_value)
