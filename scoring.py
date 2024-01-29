print(" choice format")
print("1.leaderboard")
print("2.knockout")
print("3.leaderboard/knockout")
print("4.league/knockout")

while True:
    choice = input("Enter choice(1/2/3/4): ")
    
    if choice in ('1', '2', '3', '4'):
        if choice == '1':
            
            import pandas as pd

            df = pd.read_excel(r"C:\Users\freet\OneDrive\Desktop\athletic.xlsx")

            print (df)
    


# sorting
            df = df.sort_values(['event', 'Score'], ascending=[1,0])

            print (df)

# changing order of columns
            #df = df.reindex(['Name','event','Score'], axis=1)

            

        elif choice == '2':
            
            u = input("Enter the first team name ")
            x = input("Enter the first team score: ")
            z = input("Enter the second team name ")
            y = input("Enter the second team score: ")
            # if a is b: - Compares id's, and can cause inconsistencies. Use == instead.
            if x > y:
                print ("winner\n" + u )
            else:
                print ("winner\n" + z )
              
        elif choice == '3':
            
            import pandas as pd

            df = pd.read_excel(r"C:\Users\freet\OneDrive\Desktop\athletic.xlsx")

            print (df)
    
# sorting
            df = df.sort_values(['event', 'Score'], ascending=[1,0])

            print (df)

            
            u = input("Enter the first team name ")
            x = input("Enter the first team score: ")
            z = input("Enter the second team name ")
            y = input("Enter the second team score: ")
            # if a is b: - Compares id's, and can cause inconsistencies. Use == instead.
            if x > y:
                print ("winner\n" + u )
            else:
                print ("winner\n" + z )
                
                
                
       # elif choice == '4':
            
                