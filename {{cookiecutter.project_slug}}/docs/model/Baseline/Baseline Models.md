# Baseline Model Report

Through building the baseline model, we have a quick assessment of the feasibility of the machine learning task. In order to do so, as soon as the feature set is availabe, a simple model is developed to evaluate the task and provide an orientation for the next steps.


## Analytic Approach

+ Target Variable:

	| Name | Type | Description |
	| ---:| ---: | ---: |
	| Y | Quantitative/Qualitative | Business understanding |

+ Input Variables:

	| Name | Type | Description |
	| ---:| ---: | ---: |
	| X1 | Quantitative/Qualitative | Business understanding |

+ Data Science Pipeline:

	| Description | Value |
	|  ---: | ---: |
	| Train Split | 70% |
	| Validation Split | 15% |
	| Test Split | 15% |


## Model Description

+ Model

	+ Strategy: Machine Learning | Deep Learning

	+ Framework: scikit-learn

	+ Model class: RandomForestClassifier

	+ Hyper-Parameters:

		| Name | Value |
		|  ---: | ---: |
		| n_estimators | 100 |
		| max_depth | 5 |
		| random_state | 99 |


## Results (Model Performance)

[Regression]

| MAE | MSE | RMSE | R<sup>2</sup> | RMLSE | MAPE |
|  ---: | ---: |  ---: | ---: |  ---: | ---: |
|  ### | ### |  ### | ### |  ### | ### |

Histogram (true x predicted), QQ-Plot, Residual Plot, true x predicted


[Classification]

| Accuracy | Recall | Precision | F1-Score | AUC-ROC | KS |
|  ---: | ---: |  ---: | ---: |  ---: | ---: |
|  ### | ### |  ### | ### |  ### | ### |

ROC, Precision-Recall, CAP Plot, KS-Plot


## Model Understanding

+ Feature Importance:

+ Insights:


Shapley Plots


## Conclusion and Discussions for Next Steps

+ Conclusion on Feasibility Assessment of the Machine Learning Task:

+ Feature Engineering analysis:

+ Possible additional data sources to help at the task: