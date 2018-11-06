a. The idea is clear and properly formed. Null hypothesis is correctly documented in words. Currently, the alternate hypothesis and the mathematical representation of hypotheses are missing. I would encourage to add these two as it make the hypotheses easy to process and test.

b. Careful effort had been made to keep the samples size balanced which highlights the deligent way in which the data is processed and is appreciable. However, in the final data uneccessary field, 'gender' is present which could had been eliminated, and the field 'Birth Year' could had been converted to 'Age' and subsequently to age buckets '>25' or '<25'. These two changes would had made data more appropriate for the analysis.

c. A few minor mistakes were made while programming this code.
   a. package 'json' is imported uneccesarily. It is not used in the code thus, should not be imported
   b. package 'os' is imported twice.(Redundant)
   c. trying to check for missing environment variable 'PUIdata' twice(Again redundant). 
      Also, please add a line of code which will set the environment variable automatically if its not present.
   d. Please add comments to each new cell in jupyter to explain what is being done in the cell
      and delete all the empty cells after completing your program.
   I believe, if these mistakes are avoided in future the code will look good and easy to work with
   
d. The right statistical test for this analysis is - Z-test for unpaired data.
   Going through the flow chart presented in class slide:
   Step1: Do data come from the same or different populations?: Yes, infact it comes from same population i.e. Citibike riders
   Step2: Type of data?: Non-parametric as the distribution of samples are not normal
   Step3: Treatment variable?: 1, trip duration.
   Step4: Categories?: 2, >25 and <25
   Step5: Paired or Unpaired?: Unpaired, as sets of data arise from separate individuals.
   Step6: Sample Size?: We have atleast 30 data points for each group and our variable trip duration is continous
   Answer: Z-test for unpaired data