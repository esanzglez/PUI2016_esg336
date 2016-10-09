(This is the review by xz694 for the Citibike project proposal by esg336.)

### 1. Idea:

"Idea: Our team was interested in seeing who was more prone to commute whether women or me using citibikes to go to their daily routines.For that purpouse we analyzed the commute hours of early morning (from 7-10) and evening (from 4 -7pm). Our level of significance is 0.05"

Comment: This statement seems to be a little confusing. The definition of "go to daily routines" is rather vague and does not completely justify the reason of choosing the specific time blocks (7-10 am and 4-7pm). People can commute for different routines at different hours. Sounds like it could be better if it's stated as typical rush hour commute...

### 2. Null and Alternative Hypotheses:
"Alternative hypothesis: female would be more likely to commute in the evening than their male counterparts
Null hypothesis: there would be no difference in the percentage of men and women commuting in the morning and evening"

Not sure why only evening commute is mentioned for the alternative hypothesis. Even if that's the case, the alternative hypothesis could be more quantitatively specific, like how it is stated in the null hypothesis, as in, mentioning the measure of interest is a percentage...
And if alternative hypothesis says "women is more likely to...", the null hypothesis should be saying not "no difference" but "equally likely or less likely to...(than men)"
Mathmatical expressions for each hypothesis should have been written too.

### 3. Data:
The data has the appropriate variables to answer the question. The time of the bike ride is of interest, and the Citibike data documents the travel time. Data is also properly pre-processed to extract the needed values. In the original data file, travel times, including date and time, are stored in one cell, and the group broke it down, so that they can pick out the bike rides that fall into the time periods of interest.

### 4. Test selected:
From what I understood, the proposed study wants to see that women are more likely to use Citibike in the evenings. To do that, presumably one will need to, for each gender, count the total number of rides (morning rides and evening rides together), count the rides that happen in the evenings, calculate the percentage, and then finally compare the percentages of the two genders.
Given these conditions, following the flowchart from the slides, I suggested the Pair Samples t-test. Reason being, the outcome is a ratio variable (percentage, and 0 could really mean 0), it studies group differences (between women and men), it is paired observation (women and men on the same days during weekdays), and finally, the number of groups is two.
