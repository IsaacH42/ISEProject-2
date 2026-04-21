# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 09:38:00 2026

@author: isaac
"""

from itertools import combinations
#Gemini suggested that I use pulp for future calculations as it would be much easier to use than a loop especially when dealing with
#large quantities of combinations. 

def calculation(file):
    #Here I am defining a function that will decide on how each of the files will be processed and split up
    Centers = [line.strip().split(",") for line in file.readlines()]
    #.readlines returns both of the centers strings as lines and can be stiped and split. This is so you can use the txt data as lists for each of the centers.
    County_overlap = {}
    costs = {}
    #creating this dictionary will allow us to use a program, to find the best center to optomize coverage
    counties = len(Centers[0])-2
    county_ids = [f"County_{i}" for i in range(counties)]
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
    # Combine all counties covered by the selected centers
    covered_set = set()
    for center in combo:
        covered_set.update(coverage_overlap.get(center, []))
    
    # Check if the set of covered counties matches our target list
    return all(county in covered_set for county in target_counties)

def main():
    best_selection = None
    minimum_cost = float('inf')
    
    # 1. Open the files
    infile1 = open("C:\\Users\\isaac\\.spyder-py3\\ISEProject-2\\coverage1.txt")
    infile2 = open("C:\\Users\\isaac\\.spyder-py3\\ISEProject-2\\coverage2.txt")
    
    # 2. Extract ALL data using the function
    # cov1/cov2 are the coverage maps, costs1/costs2 are the prices
    cov1, costs1, counties = calculation(infile1)
    cov2, costs2, _ = calculation(infile2)
    
    # 3. Close the files immediately—we have the data in dictionaries now
    infile1.close()
    infile2.close()
    
    # 4. Use the keys from costs1 to get your list of centers
    centers = list(costs1.keys())
    
    print(f"Total Centers: {len(centers)}")
    print(f"Total Counties: {len(counties)}")
    
    # 5. Start the Optimization
    for r in range(1, len(centers) + 1):
        for combo in combinations(centers, r):
            # Calculate cost using the dictionary returned by your function
            current_cost = sum(costs1[c] for c in combo)
            
            if current_cost >= minimum_cost:
                continue
            
            # Check coverage for both scenarios
            if is_covered(combo, counties, cov1) and is_covered(combo, counties, cov2):
                minimum_cost = current_cost
                best_selection = combo
                print(f"Current Best Cost: {minimum_cost} | Selection: {best_selection}")

    # 6. Final Results Output
    if best_selection:
        print("\n" + "="*30)
        print("OPTIMAL HUMANITARIAN STRATEGY")
        print("="*30)
        print(f"Minimum Budget Required: {minimum_cost}")
        print(f"Selected Centers: {', '.join(best_selection)}")
    else:
        print("No combination covers all counties.")
                
main()
        





    
        
        
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
