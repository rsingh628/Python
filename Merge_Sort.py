def merge_Sort(array): 
    if len(array) >1: 
        mid = len(array)//2 #determining the mid of the array
        divide = array[:mid] # Dividing the array elements  
        split = array[mid:] # splitting the array into 2 halves 
  
        merge_Sort(divide) # first half of the sorting
        merge_Sort(split) # second half of the sorting
  
        i = j = k = 0
          
        # Copy data to temp arrayays divide[] and split[] 
        while i < len(divide) and j < len(split): 
            if divide[i] < split[j]: 
                array[k] = divide[i] 
                i+=1
            else: 
                array[k] = split[j] 
                j+=1
            k+=1
          
        # Checking if any element was left 
        while i < len(divide): 
            array[k] = divide[i] 
            i+=1
            k+=1
          
        while j < len(split): 
            array[k] = split[j] 
            j+=1
            k+=1
  
# Code to print the list 
def printdivideist(array): 
    for i in range(len(array)):         
        print(array[i],end=" ") 
    print() 
  
# driver code to test the above code 
if __name__ == '__main__': 
    array = [12, 2, 93, 65, 76, 27]  
    print ("Given arrayay is", end="\n")  
    printdivideist(array) 
    merge_Sort(array) 
    print("Sorted arrayay is: ", end="\n") 
    printdivideist(array)
