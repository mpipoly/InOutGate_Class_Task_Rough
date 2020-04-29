```python
# This will be the only package I will need to use for this demonstration
import numpy as np
```


```python
#The following is a breakdown of two functions used in my tassk script
```


```python
# The purpose of this function is to take an integer number, in this case the number of trials
# and create an out put of that input

num_trials=4 # integer (could be of any size: 8, 2, 23 etc..)

print(type(num_trials))
print(isinstance(num_trials, int))

def make_ITI(num_trials):
    if isinstance(num_trials, int) == True:    
        ITI=np.random.choice([1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]) # numpy randomly grabs a value
        # ITI refers to a "jitter" to prevent anticipatory effects
        # The random value between 1-2 seconds is returned
        return ITI
    else:
        print('Error: Input of Jitter is not integer')

# Here we shall show a good output

Good_Output = make_ITI(1) # here we assign good output to the variable "Good_Output"
print(Good_Output)
print(type(num_trials)) # As we can see this is because num_trials is an integer
print(isinstance(num_trials, int)) # When we check we see it is True
```

    <class 'int'>
    True
    1.1



```python
# Following the above cases, we will now show bad output
num_trials = '4' # When it is a string

bad_output = make_ITI(num_trials) # We try running it in the function

print(type(num_trials)) # We see it is class string
print(isinstance(num_trials, int)) # We see it does not pass our test of 'Integer?'
bad_output # An we print to see our variable is the error
```

    Error: Input of Jitter is not integer
    <class 'str'>
    False



```python
# This function is set up to take a list of elements of any type, and capture their frequency
# For my taks I need an even distribution of cue type trials

List_to_use = ['6','8','2','8','6','8','8','2','8','8','6','2','8','6','8''2','2','2','6'] # This is good output format

def getDuplicatesWithCount(listOfElems=''):
    ''' Get frequency count of duplicate elements in the given list '''
    # The if statement below makes sure the fed in variable is list type
    if isinstance(listOfElems, list) == True:
        dictOfElems = dict() # Create empty dicionary for trial type frequency organization
        # Iterate over each element in list
        for elem in listOfElems:
            # Interates through the list of elements, our case string types
            if elem in dictOfElems:
                # if the given string does exist, it increments the value by 1 (how it counts)
                dictOfElems[elem] += 1
            else:
                # if the given string type does not exist, it inputs with a dictionary key value of 1
                dictOfElems[elem] = 1
        # Filter key-value pairs in dictionary. Keep pairs whose value is greater than 1 i.e. only duplicate elements from list.
        dictOfElems = { key:value for key, value in dictOfElems.items() if value > 1}
        # Returns a dict of duplicate elements and their frequency count
        return dictOfElems
    else:
        # If the fed in variable is not list type, below error
        print('Error: did not feed in a list')

        
# Each element is filtered and incrementally added into dictionary bins
# These bins reveal the counts, so you can check if your trials are even uneven
getDuplicatesWithCount(List_to_use)
```




    {'6': 5, '8': 7, '2': 5}




```python
# Here is example of bad input
Not_a_list = 4 # This is a single integer and not a list
getDuplicatesWithCount(Not_a_list) # The function took this call and failed the if statement printing error message
```

    Error: did not feed in a list

