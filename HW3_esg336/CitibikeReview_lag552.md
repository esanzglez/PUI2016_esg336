#Peer Review of Citi Bike Assignment

##a. Verify that Null and alternative hypotheses are formulated correctly
First off, very interesting  idea! Regarding the hypothesis statements, I would suggest including more detail, and making sure
to state the "equal to or smaller" component in the null hypothesis and the "larger" component in the alternative hypothesis (instead
of just saying "no difference"). It would also be good to specify the time frame and the hypothesis in equation form. 

Additionally, I would be careful to distinguish if you're looking at the gender groups seperately or together - it was a little unclear, 
but what I got from reading your description was that you want to look at them seperately (i.e., in the female group, a higher 
percentage bike in the evening than in the morning, compared to a similar ratio in the male group). I feel this is an important 
distinction, simply because you could have a situation where there are a lot less women bikers overall which would skew the comparison 
if not normalized with a ratio of sorts. So I would suggest comparing the ratio of women biking in the evening over in the morning to
the ratio fo men biking in the evening over in the morning. My suggestions for these changes are below:

**H0:** In 2015, there was an equal or smaller ratio of female Citi Bike users commuting in the evening vs. the morning 
compared to their male counterparts, significance level = 0.05.

**H0 Equation:** (Evening Female Commuters/Morning Female Commuters) =< (Evening Male Commuters/Morning Male Commuters)

**Ha:** In 2015, a larger ratio of female Citi Bike users commuting in the evening vs. the morning compared to their male 
counterparts. 

**Ha Equation:** (Evening Female Commuters/Morning Female Commuters) > (Evening Male Commuters/Morning Male Commuters)

##b. Verify that the data supports the project

Really good job pulling out the correct variables (i.e., start times, gender, and creating the codes for morning, evening, or neither
and pulling out the correct times for those). I'm unsure, however, if "day of week" (Monday, Tuesday, etc) is needed, since this 
wasn't a componenet of your hypothesis. I thinkin your figures/the data you organized, you could have simplified it to just show 
morning and evening categories along the x-axis, and then the ratio value along the y-axis. I realize the ratio was my suggestion 
from above, so it's understandable that you guys did number of rides. Though I do think you have to be careful looking at raw numbers 
alone, since the numbers in each gender groupdiffer. But it looks like you tried to address this in the last normalized figure, so 
props for that! Regarding that last figure, I'm just a little confused because the label says "fraction" but the axis units are in 
the large numbers. I think if it's a fraction it should only span from 0 to 1 along the y-axis. But I think you had the right idea 
here to separate morning and eveningriders. Generally, I think you need to simplify the process and just look for the ratios of the 
two gender groups and compare those.

##c. Chose an appropriate test

I would suggest using a chi-square test to test this hypothesis. Chi-square tests compare only 1 independent variable (gender, here)
and 1 dependent variable (commute time). Also, the data type for both the independent and dependent variables are categorical, which
matches with your hypothesis (gender is the categorical IV; morning vs. evening commute time is the categorical DV). Also, chi-square 
tests compare observed to expected frequencies (expected being that the ratios named above are equal), so this fits with our hypothesis
comparing the ratios of the two genders regarding commute time.

*It might be tempting to use a t-test, since t-tests look at differences between only two groups of independent variables
(males and females, in this case) to test their effect on the dependent variable. However, a t-test's dependent variable is continuous,
not categorical, which does NOT fit in this case.*

