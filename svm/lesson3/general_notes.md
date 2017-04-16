# CODING UP SVM
* Naive Bayes classification accuracy was 88.4%
* SVM is giving 92%

# NONLINEAR SVM
* SVM can do really complicated shapes by nonlinear SVM

# QUIZ: PRACTICE MAKING A NEW FEATURE
* |x| will work to separate all the points into two separate sets

# KERNEL TRICK
* There are functions that take a low dimensional feature space and map them to a high dimensional space

X<sub>1</sub>Y ---> X<sub>1</sub>1X<sub>2</sub>X<sub>3</sub>X<sub>4</sub>X<sub>5</sub>

1. a not separable feature space is mapped to higher dimension.
2. a separation solution is found in the higher feature space
3. then the separation solution is mapped back to lower feature space the separation solution found
4. The separation boundary in the lower feature space is non-linear

# QUIZ: KERNEL AND GAMMA

SVM parameters:
	1. kernel
	2. C - controls tradeoff between smooth decision boundary and classifying training points correctly
	3. gamma - 

# SVM C parameter

1. An intricate boundary will classify the points correctly but may not generalize as much as a straight boundary.
2. Larger the value of C, more intricate will be the boundary of classification.
3. The artistry of machine learning lies in figuring out whether a smooth decision boundary or intricate one will work for a particular problem.

# SVM gamma parameter

1. Defines how far the influence of a single training example reaches
2. low values - far reach, high values - close reach
3. With a low value of gamma, even the far points decide where the decision boundary will be formed. However, with a high value of gamma, only the nearer points decide where the decision boundary will be formed.

# OVERFITTING

1. Overfitting can be controlled by controlling the algorithm parameters
2. C, gamma and kernel parameters can control the overfitting.
3. The artistry of machine learning is in tuning these parameters to avoid overfitting.
4. There are techniques to detect overfitting.

# PROS AND CONS OF SVM

1. SVM's work very well in complicated domains where there is a clear margin of separation.

CONS
1. They don't work very well in large datasets because training time happens to be cube of the dataset size.
2. They do not work when there is lots and lots of noise. So when the classes are overlapping so that we have to count independent evidence, SVM does not work well. In such scenarios, Naive Bayes classifier will work better.
3. The choice depends on the dataset and features that are available.

* A big dataset with lots and lots of features will be slow in SVM and prone to overfitting to some of the noise in the data.
