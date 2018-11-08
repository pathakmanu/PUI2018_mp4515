# Idea
ok but ou should say why this is interesting and why you would think that

# Null hypothesis

Consitent with the idea/question

# Formula
Missing!  Please write the formula corresponding to your H0 and Ha which you will go and test

# Data

why did you retain the Gender? it is not part of the data features relevant to you. 
Instead you are not finished with the processing: you need to convert birth year to age, split the data into 2 groups, >25 and <25, and take the means (and standard deviations)


# Test

this is a difference between means of samples, so the t test would work. however the distributions are not Gaussian. the t-test assumes Gaussianity and your distributions are not Gaussian. a non parametric test for difference of means is the Mann-Whitney U test (https://www.healthknowledge.org.uk/public-health-textbook/research-methods/1b-statistical-methods/parametric-nonparametric-tests) since the samples is large, the t-test may be ok

here is a list of assumptions the t-test makes https://www.investopedia.com/ask/answers/073115/what-assumptions-are-made-when-conducting-ttest.asp
