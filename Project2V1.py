# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 09:38:00 2026

@author: isaac
"""

from itertools import combinations
#This was the combination tool that was recomended to be used and this is how Gemini sugested that I call the library.

def calculation(file):
    #Here I am defining a function that will decide on how each of the files will be processed and split up
    Centers = [line.strip().split(",") for line in file.readlines()]
    #.readlines returns both of the centers strings as lines and can be stiped and split. This is so you can use the txt data as lists for each of the centers.
    County_overlap = {}
    #The idea is to create dictionaries for the county overlap and the costs associated with the centers 
    costs = {}
    #creating this dictionary will allow us to use a program, to find the best center to optomize coverage
    counties = len(Centers[0])-2
    #This gives us a numerical range of how long/many counties there are that will allow us to calculate for the coverage.
    #This is important for the dictionaries being set up because they need to have values that the counties are assigned to.
    county_ids = [f"County_{i}" for i in range(counties)]
    #the county_ids variable is a dictionary with the values and keys for the counties. It gives them a name to be recalled at a later time. 
    for row in Centers:
        #This starts deconstructing each of the lines in the data set.
        center_name = row[0]
        costs[center_name] = float(row[1])
        #This defines the name for the center that will be added to the dictionary
        covered_for_this_center = []
        for i, val in enumerate(row[2:]):
            if val.strip() == '1':
                # Map the index to our generated County ID
                covered_for_this_center.append(county_ids[i])
        
        County_overlap[center_name] = covered_for_this_center
        #Gemini suggested that I used this line iteration to collect centers for the dictionary
        #I also have an offset starting at 2 so that it excludes the name of the center along with the price
        #This creates the dictionary by assigning the keys and the values
    return County_overlap, costs, county_ids
    # This finishes the function and outpus the counties and the map of counties that will be used later in determining the optimal configuration.
    
def is_covered(combo, target_counties, coverage_overlap):
    #This is a new function that allows us to figure out if the counties are being covered 
    covered_set = set()
    #This defines an empty set that can be added to to find the coverage.
    for center in combo:
        covered_set.update(coverage_overlap.get(center, []))
    #This creates a loop to use the coverage_overlap dictionary to pull the target_counties from it.
    return all(county in covered_set for county in target_counties)
    #This returns a list of all of the counties that are covered by a center. This allows us to eventually call this back out when we are testing combinations.
def main():
    best_selection = None
    minimum_cost = float('inf')
    #'inf' means infinity. for the top two variables they are just creating them without adding anything into them for the meantime.
    
    infile1 = open("C:\\Users\\isaac\\.spyder-py3\\ISEProject-2\\coverage1.txt")
    infile2 = open("C:\\Users\\isaac\\.spyder-py3\\ISEProject-2\\coverage2.txt")
    #These are the direct filepaths to both of the data txt files.
    cov1, costs1, counties = calculation(infile1)
    cov2, costs2, _ = calculation(infile2)
    # cov1/cov2 are the coverage maps, costs1/costs2 are the prices that we have been able to pull from the file using the calculation function.
    infile1.close()
    infile2.close()
    #It is just good common practice to close the file at this point since we won't be interacting with the file anymore.
    
    centers = list(costs1.keys())
    #This gives us the number of centers there are in both of the files
    
    for r in range(1, len(centers) + 1):
        #This defines the first parameter for the combinations
        for combo in combinations(centers, r):
            #This defines the itertools combination tool to generate all of the combinations that will be tested
            current_cost = sum(costs1[c] for c in combo)
            # We can now calculate costs for each of the combination in each combination that covers every county.
            if current_cost >= minimum_cost:
                continue
            #This is just validation to make sure that if the value is less than the previous before being allowed to be tested with the other coverage.
            if is_covered(combo, counties, cov1) and is_covered(combo, counties, cov2):
                #This is so we can import another function and test which one is the cheapest plan
                minimum_cost = current_cost
                best_selection = combo
                #These are variables we are defining to find the lowest cost and best selection for the centers.


    print("Best Coverage plan")
    print(f"Minimum Budget Required: {minimum_cost}")
    print(f"Selected Centers: {', '.join(best_selection)}")                
main()
        





    
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
