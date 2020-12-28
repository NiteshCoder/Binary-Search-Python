# Binary-Searching-Python-Code


# Note :
Binary Search Only works with Sorted Data.

# Explation :

# Here is Sorted data:
10 20 30 40 50 60

Search For 20 Okie.

# Step 1 : Find Mid data
         Index of 10  + Index of 60
         ----------------------------
                       2
        - You will get 30.
        
# Step 2: So Now mid data is 30 but our search data is 20 .
        - So You can see 20 is left side of 30.
        - So now we just short it out.
           
#          LEFT SIDE  |  MID  |  RIGHT SIDE
            10  20       30       40 50 60
          
          
# Hence this algo now only Search element in Left Side Without Wasting time in right Side.
          
