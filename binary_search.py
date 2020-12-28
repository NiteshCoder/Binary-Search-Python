#Searching algorithm:
#Binary Searching

#Binary Search Works on Sorted Data Only Otherwise it will give wrong output unexpected.
def sort_data(data):
	data.sort()
	pass
	
#Actual Logic of binary Searching
def binary_search(data,search):
	
	#Membership operator cheks searched element actually present or not.
	if search in data:
		low = 0	#For base Index
		high = len(data) - 1 #For last index
		mid = 0 #Middle index
		
		#Loop working till last element.
		while(low<=high):
			mid = (low + high) // 2 #It will decide where is mid point.

			#If Middle element is greater then search then it will go for searching only left side.
			if data[mid] > search: 
				high = mid - 1
				
			#If Middle element is greater then search then it will go for searching only right side.
			elif data[mid] < search:
				low = mid + 1
			else:
				return mid
	else:
		print("Sorry Search is not available in Data")
		
		

#Start execution from here		
if __name__ =="__main__":
	data = []	#Data
	size = int(input("How many data you want to enter : ")) #Size of List (How many element going to store.

	#Loop for scanning values from user.
	for i in range(0,size):
		temp = int(input(f"Enter Element { i+1 } : "))
		data.append(temp)

	#Scanning element from user to search.
	search = int(input("Which element you want to search : "))
	sort_data(data)
	print(f"Sorted Data : \n {data}")
	print(f"Searching for ................ {search}")
	
	answer = binary_search(data,search) #Function return Index.
	print(f"Element is Success Fully searched\nIndex Of Element : { answer }\n")
	
	
	