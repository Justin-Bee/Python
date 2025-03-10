import pandas as pd
name = ""

while name != "exit":
    name = input("please enter a file name or type exit to quit")
    print(name)
    if name == "exit":
        break
    try:    
        df = pd.read_csv(name)
    except:
        print("file was not found") 
        break   
    print(df.columns)
    print(df.head())