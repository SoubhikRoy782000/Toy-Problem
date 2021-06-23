# Toy-Problem
To implement a toy problem

Problem Statement –

A person has 3000 bananas and a camel. The person wants to transport the maximum number 
of bananas to a destination which is 1000 KMs away, using only the camel as a mode of 
transportation. The camel cannot carry more than 1000 bananas at a time and eats a banana every 
km it travels.

Algorithm –

STEP 1 – Take the input of number of bananas at starting, total distance to cover and the 
maximum load capacity of the camel.
STEP 2 – There would be one or more than one checkpoint. We are breaking each section of the 
checkpoint in the sections of length one.
STEP 3 – Here transportation is done in 1-km steps. As in the problem statement discussed 
above, camel walks with 1000 bananas for 1 km left 998 bananas there and consume 2. In the 
last round, the camel will consume only one banana.
STEP 4 – At each subsequent km, we are subtracting the number of bananas lost in travelling 
each km from the total number of bananas. 
STEP 5 – To calculate the total bananas left after 1 km we use another variable start. 
