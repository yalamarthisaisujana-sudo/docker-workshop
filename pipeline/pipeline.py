import sys
import pandas as pd
print("aruguments", sys.argv)
month=int(sys.argv[1])
df = pd.DataFrame({"day":[1,2],"num_of_passengers":[3,4],"month":month})
df.to_parquet(f"output_{month}.parquet")
#df['month']= month
print(df.head())
#print(f'hello pipeline, month={month}')

