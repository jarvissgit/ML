# General notes on machine learning
-----------------------------------

## Training and testing data

* Training and predictions should be done on different sets of data. If training and predictions are done on same type of data, then there will be overfitting of the data
* Generalizing to new data is not possible if the training and prediction are both on the same dataset
* Save 10% of the dataset to be used as


## Unpacking NB using Bayes Rule


## Quiz : Prior and Posterior

* Bayes rule
	* prior probability + test evidence = posterior probability **semantically Bayes incorporates some evidence from the test into prior probability to arrive at a posterior probability.**

	1. PRIOR
		* P(C) = 0.01 = 1% **prior probability of cancer**
		* P(Pos|C) = 0.9 = 90% **prior probability of the test being positive and the persion having cancer**
		* P(Neg|^C) = 0.9 = 90% **prior probability of the test being negative and the person not having cancer**
		* P(^C) = 0.99 = 99% **prior probability of not having cancer**
		* P(Pos|^C) = 0.1 **prior probability of the test being positive and the person not having cancer**

	2. POSTERIOR
		* P(C , Pos) = P(C) X P(Pos | C) = 0.009 = 0.9% 
			- __P(C|Pos) is posterior of the probability of cancer given that the test says positive__
			- __P(C) is prior probability of cancer__
			- __P(Pos | C) is probability of positive result given that a person has cancer. This is the test sensitivity.__
		* P(^C , Pos) = P(^C) X P(Pos | ^C) = 0.099 = 9.9%
			- __P(^C|Pos) is posterior of the probability of not having cancer given that the test says positive__
			- __P(^C) is prior probability of not having cancer__
			- __P(Pos | ^C) is probability of positive result given that a person does not have cancer.__

![fig1] 
[fig1]: ./nb1.png
	
	* But probabilities do not add upto 1
	
* Quiz: Normalizing 1
	*compute the normalized values such that the ratio remains same but they add upto 1
		* addition gives 0.108
		* P(Pos) = P(C,Pos) + P(^C,Pos) = 0.108

	* The posterior that we calculated earlier is actually the joint probability of two events
	* JOINT PROBABILITY OF TWO EVENTS 
		* P(C , Pos) = P(C) X P(Pos | C) = 0.009 = 0.9% 
			- __P(C,Pos) is posterior of the probability of cancer given that the test says positive__
			- __P(C) is prior probability of cancer__
			- __P(Pos | C) is probability of positive result given that a person has cancer. This is the test sensitivity.__
		* P(^C , Pos) = P(^C) X P(Pos | ^C) = 0.099 = 9.9%
			- __P(^C,Pos) is posterior of the probability of not having cancer given that the test says positive__
			- __P(^C) is prior probability of not having cancer__
			- __P(Pos | ^C) is probability of positive result given that a person does not have cancer.__
	* NORMALIZES
		* P(Pos) = P(C,Pos) + P(^C,Pos) = 0.108
	* POSTERIOR
		* P(C | Pos) = P(C, Pos)/P(Pos) = 0.009/0.108 = 0.083333
		* The posterior probability of cancer given the test is positive is obtained by dividing P(C, Pos) with the normalizer P(Pos). **Can this be inferred from the first equation of joint probability? Seems like the terms inside brackets are reversed!**
		* P(^C | Pos) = P(^C, Pos)/P(^C) = 0.099/0.108 = 0.916667
	* Now the values add up to 1.0
* Bayes Rule Diagram
![fig2] 
[fig2]: ./bayes_rule_diagram.png

