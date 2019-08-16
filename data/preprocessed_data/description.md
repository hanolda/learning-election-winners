Create 5 representations:
############################
## Representation 1: score factorisation

This factorised representation transforms original list of ranks into Borda count dataset, such that the \textbf{feature is set of the candidates $C$} and the \textbf{value of the feature} is \textbf{Borda score}\footnote{ Depending on the position of the candidate in each rank $n$, Borda rule assigns $n-1$ points to a top ranked choice, $n-2$ points to second ranked choice, down to $0$ points for a bottom ranked alternative.}of the feature. The profile from Example~\ref{ex:running} is given in Table~\ref{tab:rep1} and Figure~ \ref{fig:Representation1}.

The shape of the new representation is:$$(\# profiles, \# candidates).$$ Here, the shape of the Spotify model is: $(361, 20)$ and the generated model: $(12360, 20)$.

The main drawback of this factorisation is lack of reduction in time consumption during training phase and minor in memory (data) compression. Another disadvantage of this transformation  is forced anonymity, namely lost information e.g. about who voted for whom. From the other side, the main advantage of this approach is that the original profiles don’t have to be the same size in order to transform dataset to this feature representation. Moreover, once learned new representation of the data, predictive model might be used for winner prediction of any new set of candidates. 
Finally, we fund this representation much more informative for further processing in terms of improved accuracy of supervised algorithms (we will discuss it in next chapter).

############################
# Representation 2: occurrence factorisation

The \textbf{features} in this representation are \textbf{the set of candidates together with the position at which each candidate can be ranked}. In the other words, this transformation consist of counting the occurrence of each candidate at each position of the ranking, such that the features are the combinations of the candidates at each rank position. The value of the feature is the number of votes for the candidate appearing at featured position, so \textbf{the value of the feature is the number of times the candidate occurs in the particular position in the profile}. For example, if the set of candidates has four candidates we obtain 16 features, one for each position in which each candidate can be ranked.  The shape of the new representation is: $$( \# profiles, |C|\cdot|C|).$$ Thus, for given  $N = 20$  candidates  and length of each vote (ranking) equal to $20$ positions, we obtain $400$ features. Here, shape of the Spotify model is: $(361, 400)$ and of the generated model: $(12360, 400)$.

The main drawback of this transformation is that we loose the information about the sequence of individual preference. On the other hand, we gain more information about hall profile complex dependencies. This presentation of given data leads to great reduction in time consumption, in particular in Kemeny winner prediction models. Moreover, learning this data transformation also improve the accuracy of supervised algorithms in comparison to making "most frequent" predictions or random predictions of Kemeny winners.

############################
## Representation 3: ocumullative ccurrence factorisation

This representation of data consist of making pairwise comparison of the candidates and scoring by $1$ whenever there is agreement and $0$ in case of disagreement for each individual preferance order. Here, we obtain the \textbf{features} again from the set of candidates, but we now consider one \textbf{feature} to be a\textbf{ unique pair of candidates}. The value of feature $ab$ is 1 if $a \succ_1 b$ and 0 otherwise. 
For given $N=20$ candidates there is $380$ possible pair combination (without repetition, with order). Profile is composed of $V=25$ ranks. By marging the dataset, $9500$ features were obtained, given $380$ combination for $25$ ranks. 
The shape of the   representation is: $$( \# profiles, \binom{|C|}{2} \cdot |V|).$$ Here, the shape of the Spotify model is: $(361, 9500)$ and the generated model: $(12360, 9500)$.
The reason to create this representation arose from how distanced-based Kemeny rule determines the winner. This explicit transformation had a chance to help supervised algorithms for rank aggregation to learn the indispensable correlation when predicting Kemeny and Dodgson winner. By application of principal component analysis (PCA) techniques it was possible to distinguish the most vital components, and so maximise the entropy of the information\footnote{Surprisingly, PCA  didn't led to the improvement of the accuracy of supervised algorithms.}.

############################
## Representation 4: pairwise cumulative score
Here, the set of features is the set of unique pairs of candidates. The value of the feature is the number of voters that prefer the first candidate to the second. 
The profile from Example~\ref{ex:running} is given in Table~\ref{tab:rep4} and Figure~ \ref{fig:Representation4} .
For given $N=20$ candidates we have  $380$ possible combination (without repetition, with order).The shape of the representation is: $$( \# profiles, \binom{|C|}{2}).$$Here, shape of the Spotify model is: $(361, 380)$ and the generated model: $(12360, 380)$.


Similarly to the Representation 3, this transformation also implies the reduction in time complexity. However, it doesn't led to increase in the accuracy of the algorithms, but stays on similar level as making "most frequent" predictions or random predictions for Kemeny winners. 

############################
Representation 5: weighted sum

The feature is the set of the voters $V$ an the value of the feature is the weighted sum of voter's rank. The profile from Example \ref{ex:running} is given in Table \ref{tab:rep5}.
The shape of the new representation is: $$(\#profiles, \#voters).$$
Here, the shape of the Spotify model is: $(361, 25)$ and the generated model: $(12360, 25)$.

