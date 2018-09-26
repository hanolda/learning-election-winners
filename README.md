# Learning election winners

## Project goal 

The goal is to understand and apply the versatile and powerful machine learning techniques by investigating learnability of linear ranking of the alternatives in pairwise election. Preference voting (aggregation) methods are used in computational social choice, computational learning theory and real world collective decisions, for instance election systems as one of the characteristics by which electoral systems can be evaluated.
Research questions that will be hold:
 - How can we use machine learning techniques to learn winners of elections for Dodgson, Kemeny and Borda voting model?
-  Which proportion of possible "data points" is sufficient for good classification?
- What is the best factorized representation?




## Project background / Motivation
The focus of the project is to study the machine learning techniques in basic mechanisms of judgment aggregation voting. This approach is multidisciplinary and combines data aggregation and mining, computer modeling and multiagent systems application to investigate social choice mechanisms of voting protocols and voting as preference aggregation estimation. Preferably the output of the Master thesis will be presented in the article on the conference.

## Methodology
The primary techniques to be mastered are learnability of voting rules by investigating machine learning methods. With its different configurations, the set of agents have preferences over a set of alternatives. Taking preferences of all agents (so called profile), the mechanism outputs a social preference over the set of alternatives or output a single winner. Winer prediction will be performed based on different scoring rules, i.e.: 
- Kemeny voting (chooses the ranking which is closest to the individual rankings based on the total number of pairwise switches.)
- Borda voting (which assigns  n-1 points to a top ranked choice, n-2 points to second ranked choice, down to 0 points for a bottom ranked alternative. Finally, ranks alternatives of n candidates according to total number of points.)
- Dodgson voting (which elects Condorcet winner by making swaps of adja-cent candidates. The winner is the candidate that needs the minimum number of swaps).

Calculations are performed in Python using related scientific libraries/toolboxes, like Scikit-learn, NumPy, SciPy and Pandas.
