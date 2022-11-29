import pandas as pd
import math
ud = pd.read_excel("input_octant_longest_subsequence.xlsx")                   # read the input file
ud.head()
ud.loc[0,"U_Average"] = ud["U"].mean()                                        #Creating average for coloumns U,V,W 
ud.loc[0,"V_Average"] = ud["V"].mean()
ud.loc[0,"W_Average"] = ud["W"].mean()
ud["U1"] = ud["U"]-ud["U"].mean()                                            # Creating new columns for U1,V2,W3 
ud["V2"] = ud["V"]-ud["V"].mean()
ud["W3"] = ud["W"]- ud["W"].mean()

ud.loc[((ud.U1 > 0) & (ud.V2 > 0) & (ud.W3 >0)), "Octant"] = "+1" 
ud.loc[((ud.U1 > 0) &(ud.V2 > 0) & (ud.W3 <0)), "Octant" ] = "-1"
ud.loc[((ud.U1 < 0) &(ud.V2 > 0) & (ud.W3 >0)), "Octant" ] = "+2"
ud.loc[((ud.U1 < 0) &(ud.V2 > 0) & (ud.W3 <0)), "Octant" ] = "-2"           # assigning integers for each octant and creating octant column, 
ud.loc[((ud.U1 < 0) &(ud.V2 < 0) & (ud.W3 >0)), "Octant" ] = "+3"
ud.loc[((ud.U1 < 0) &(ud.V2 < 0) & (ud.W3 <0)), "Octant" ] = "-3"
ud.loc[((ud.U1 > 0) &(ud.V2 < 0) & (ud.W3 >0)), "Octant" ] = "+4"
ud.loc[((ud.U1 > 0) &(ud.V2 < 0) & (ud.W3 <0)), "Octant" ] = "-4"     

#octants are created

ud.loc[0," "]=" "
ud.loc[0,"  "]="  "
ud.loc[0,"Count"]="+1"
ud.loc[1,"Count"]="-1"
ud.loc[2,"Count"]="+2"                                                     # creating a column Count for (+1,-1,+2,-2,+3,-3,+4,-4) 
ud.loc[3,"Count"]="-2"
ud.loc[4,"Count"]="+3"
ud.loc[5,"Count"]="-3"
ud.loc[6,"Count"]="+4"
ud.loc[7,"Count"]="-4"




a=[]  # for counting sequence (+1,+1 -1,-1 ........ +4,+4 -4,-4) creating a array a .
for i in range(9) : 
   a.append(0)    # in a a[]array  inserting all elements to 0's  
b=[]   # for storing maximum length of each subsequence for (+1,+1 -1,-1 ........ +4,+4 -4,-4) creating b array 
for i in range(9) : 
   b.append(0)     #in a b[]array  inserting all elements to 0's
c=[]    # for maximum length of each subsequence for (+1,+1 -1,-1 ........ +4,+4 -4,-4) creating c array for storing count 
for i in range(9) : 
   c.append(0)  #in a c[]array  inserting all elements to 0's 
mod=29744
for i in range(mod) :
   a[int(ud["Octant"][i])+4]=a[int(ud["Octant"][i])+4]+1 # in a c[]array  incrementing count 
   if a[int(ud["Octant"][i])+4] != a[int(ud["Octant"][i+1])+4]:
      if(a[int(ud["Octant"][i])+4]>b[int(ud["Octant"][i])+4]):
        b[int(ud["Octant"][i])+4]=max(a[int(ud["Octant"][i])+4],b[int(ud["Octant"][i])+4])#  for each subsequence finding max length 
        c[int(ud["Octant"][i])+4]=1 
        a[int(ud["Octant"][i])+4] =0
      else :
        if(a[int(ud["Octant"][i])+4]==b[int(ud["Octant"][i])+4]):
           c[int(ud["Octant"][i])+4] += 1 # for each subsequence of maximum length incrementing count .
           a[int(ud["Octant"][i])+4] =0
        if (a[int(ud["Octant"][i])+4]<b[int(ud["Octant"][i])+4]):
            a[int(ud["Octant"][i])+4] =0
ud.loc[0,"Longest Subsequence Length"] = b[5]           # storing the  maximum length of subsequence +1 in b[5]
ud.loc[1,"Longest Subsequence Length"] = b[3]           # storing the maximum length of subsequence -1 in b[3]
ud.loc[2,"Longest Subsequence Length"] = b[6]           # storing the maximum length of subsequence +2 in b[6]
ud.loc[3,"Longest Subsequence Length"] = b[2]           # storing the maximum length of subsequence -2 in b[2]
ud.loc[4,"Longest Subsequence Length"] = b[7]           # storing the maximum length of subsequence +3 in b[7]
ud.loc[5,"Longest Subsequence Length"] = b[1]           # storing the maximum length of subsequence -3 in b[2]
ud.loc[6,"Longest Subsequence Length"] = b[8]           # storing the maximum length of subsequence +4 in b[8]
ud.loc[7,"Longest Subsequence Length"] = b[0]           # storing the maximum length of subsequence -4 in b[0]
                           
ud.loc[0,"count"] = c[5]                                # storing the count of maximum length of subsequence +1 in c[5]
ud.loc[1,"count"] = c[3]                                # storing the count of maximum length of subsequence -1 in c[3]
ud.loc[2,"count"] = c[6]                                # storing the count of maximum length of subsequence +2 in c[6]   
ud.loc[3,"count"] = c[2]                                # storing the count of maximum length of subsequence -2 in c[2]     
ud.loc[4,"count"] = c[7]                                # storing the count of maximum length of subsequence +3 in c[7]   
ud.loc[5,"count"] = c[1]                                # storing the count of maximum length of subsequence +2 in c[1]   
ud.loc[6,"count"] = c[8]                                # storing the count of maximum length of subsequence +2 in c[8]   
ud.loc[7,"count"] = c[0]                                # storing the count of maximum length of subsequence +2 in c[0]   
ud.to_excel("output_octant_longest_subsequence.xlsx",index=False)

    ``