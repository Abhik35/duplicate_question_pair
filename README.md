# duplicate_question_pair
Quora and Stack Exchange are knowledge-sharing platforms where people can ask questions in the hopes of attracting high-quality answers. Often, questions that people submit have previously been asked. Companies like Quora can improve user experience by identifying these duplicate entries. This would enable users to find questions that have already been answered and prevent community members from answering the same question multiple times.
Consider the following pair of questions:
1.Is talent nurture or nature?
2.Are people talented by birth or can it be developed?
These are duplicates; they are worded differently, but they have the same intent. This blog post focuses on solving the problem of duplicate question identification.


## SOLUTION
Suppose we have a fairly large data set of question-pairs that has been labeled (by humans) as “duplicate” or “not duplicate.” We could then use natural language processing (NLP) techniques to extract the difference in meaning or intent of each question-pair, use machine learning (ML) to learn from the human-labeled data, and predict whether a new pair of questions is duplicate or not.
This post explores a few of these NLP and ML techniques, like text pre-processing, embedding, logistic regression, gradient-boosted machine, and neural networks. The general approach of the solution is outlined in this high-level diagram:
![1_EYrwCbBDUAbx5dKPjJIIIg](https://user-images.githubusercontent.com/90651409/158041484-c6d49713-4537-483f-96d9-dbcd01e3bd72.png)


## DATA
The data, from Kaggle (Quora Question Pairs), contains a human-labeled training set and a test set. Each record in the training set represents a pair of questions and a binary label indicating whether it’s a duplicate or not.



here you can see my project
## https://duplicate-question-pair-soura.herokuapp.com/
