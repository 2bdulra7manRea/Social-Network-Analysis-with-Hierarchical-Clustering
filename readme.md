# Social Network Analysis with Hierarchical Clustering

## Overview

This project focuses on Social Network Analysis (SNA) using Hierarchical Clustering. The dataset used includes information about individuals' interests, names, and social platform usage. The analysis involves feature engineering, including encoding categorical data, and visualizing the results using a dendrogram.

## Dataset

The dataset consists of the following columns:

- **interest:** Interests of individuals.
- **name:** Names of individuals.
- **social_platform:** Social media platforms used by individuals.

## Feature Engineering

To prepare the data for analysis, feature engineering was performed. This included encoding categorical data, specifically the "social_platform" column. Encoding transforms categorical variables into numerical format, making them suitable for clustering algorithms.

## Hierarchical Clustering

Hierarchical Clustering was chosen as the primary clustering algorithm for this Social Network Analysis. The algorithm groups similar individuals into clusters, forming a tree-like structure known as a dendrogram. The dendrogram visually represents the hierarchy of clusters and allows for the identification of distinct social network communities.

## Dendrogram Visualization

The dendrogram was generated using the hierarchical clustering results. Each leaf of the dendrogram represents an individual, and the branches indicate the merging of clusters. The height at which branches merge provides insights into the similarity between clusters.

### Dendrogram Example:

![Dendrogram](/dendrogram-test.png)

In the dendrogram, observe how individuals with similar interests or social platform usage are grouped together. The structure of the dendrogram can reveal patterns and communities within the social network.

## Evaluation Metrics

The clustering results were evaluated using the following metrics:

- **Silhouette Score:** 0.4732

  - A higher silhouette score indicates well-defined clusters.

- **Calinski-Harabasz Score:** 59.32

  - Higher values indicate better-defined clusters.

- **Davies-Bouldin Score:** 0.7798

  - A lower Davies-Bouldin Index is indicative of better clustering.

## Usage

To replicate or extend this analysis, follow these steps:

1. **Dataset:** Ensure you have a similar dataset with columns for interests, names, and social platform usage.
2. **Feature Engineering:** Encode categorical data, if applicable, using suitable encoding techniques.
3. **Hierarchical Clustering:** Apply hierarchical clustering algorithms to identify clusters within the dataset.
4. **Dendrogram Visualization:** Use visualization tools to create a dendrogram that illustrates the hierarchy of clusters.

## Dependencies

- Python 3.x
- Libraries: NumPy, Pandas, Scikit-learn, Matplotlib, scipy

## Acknowledgments

This project is inspired by the field of Social Network Analysis and hierarchical clustering techniques.
