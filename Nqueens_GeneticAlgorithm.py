# -*- coding: utf-8 -*-
"""
@author: zeelp
"""

import random
import copy
import math
import numpy as np
import time

cross_prob = 0
mutation_prob = 0

def print_board(individual,n):
    print()
    print('--------------N queens Board--------------')
    print()
    solution=[]
    for x in range(n):              #empty board!
        solution.append(['*'] * n)
        
    for z in range(n):
        solution[n-individual[z]][z]='Q'
        
    for z in solution:
        brackets_removed=str(z)[1:-1]
        brackets_removed = brackets_removed.replace("'"," ")
        brackets_removed = brackets_removed.replace(",","")
        print(brackets_removed)
        print()
    
            
#this function calculates number of attacking pairs i.e. if this is zero it is fittest!

def fitness(individual):
    row_clashes = abs(len(individual) - len(np.unique(individual)))
    diagonal_collisions = 0

    n = len(individual)
    left_diagonal = [0] * 2*n
    right_diagonal = [0] * 2*n
    for i in range(n):
        left_diagonal[i + individual[i] - 1] += 1
        right_diagonal[len(individual) - i + individual[i] - 2] += 1

    diagonal_collisions = 0
    for i in range(2*n-1):
        counter = 0
        if left_diagonal[i] > 1:
            counter += left_diagonal[i]-1
        if right_diagonal[i] > 1:
            counter += right_diagonal[i]-1
        diagonal_collisions += counter / (n-abs(i-n+1))
        
    attack_pairs = row_clashes + diagonal_collisions
    
    return attack_pairs   #number of attacking pairs
    
          
def crossover(individual1, individual2,prob1):
    if prob1<cross_prob:
        n = len(individual1)
        c = random.randint(0, n - 1)     #cut them from any random number for crossover
        return individual1[0:c] + individual2[c:n]
    else:
        return individual1


def mutation(individual,prob2):
    if prob2<mutation_prob:
        n = len(individual)
        c = random.randint(0, n - 1)
        m = random.randint(1, n)
        individual[c] = m
        return individual
    else:
        return individual
    

def generate_individual(n):
    result = list(range(1, n + 1))
    np.random.shuffle(result)
    return result

class Genetic(object):
    
    def __init__(self, n ,pop_size):
        #initializing a random individuals with size of initial population entered by user
        self.queens = []
        for i in range(pop_size):
            self.queens.append(generate_individual(n))  #initial generation created

    #generating individuals for a single iteration of algorithm
    def generate_population(self, random_selections=5):
        candid_parents = []
        candid_fitness = []
        #getting individuals from queens randomly for an iteration
        
        for i in range(random_selections):    
            candid_parents.append(self.queens[random.randint(0, len(self.queens) - 1)])
            candid_fitness.append(fitness(candid_parents[i]))
            
        #sorted_fitness = copy.deepcopy(candid_fitness)
        
        #sort the fitnesses of individuals
    
        
        test_list=[]        #empty list
        
        for i in range(0, len(candid_parents)):
            test_list.append([candid_fitness[i], candid_parents[i]])
            
        #test list has total current population
        
        test_list.sort() #ascending order 0==>max fitness
        
        #getting 2 first individuals(min attackings)
        
        x=test_list[0]     # first maximum i.e. inidividual with minimum attacks
        y=test_list[1]     # second maximum
        
        
        #crossover the two parents
        temp1 = crossover(x[1], y[1],random.random())
        temp2 = crossover(y[1], x[1],random.random())
    
        #mutation
        p=mutation(temp1,random.random())
        q=mutation(temp2,random.random())
        
        
        #in code below check if each child is better than each one of queens individuals, set that individual the new child
        
        if fitness(p) < x[0]:
            if not any(list == p for list in self.queens):      #if child is unique then only 
                self.queens.append(p)                           #append it to new population
                test_list.append([fitness(p), p])


        if fitness(q) < x[0]:
            if not any(list == p for list in self.queens):
                self.queens.append(q)
                test_list.append([fitness(q), q])
        

    def finished(self):
        for i in self.queens:
            #if fitness i.e. number of attackig pairs is 0, then it is fittest solution
            if(fitness(i)==0):
                return [1,i]
        return [0,self.queens[0]]
            #we check if for each queen there is no attacking(cause this algorithm should work for n queen,
            # it was easier to use attacking pairs for fitness instead of non-attacking)
            
    def start(self, random_selections=5):
        count = 0   #number of populations generated
        #generate new population and start algorithm until number of attacking pairs is zero
        while self.finished()[0] == 0:
            count=count+1
            self.generate_population(random_selections)
            
        final_state = self.finished()
        print()
        print('populations generated:',count)
        print()
        print(('Solution : ' + str(final_state[1])))
        print_board(final_state[1],n)


#******************** N-Queen Problem With GA Algorithm ***********************

n=(int)(input('Enter the value of N : '))
max_pairs = (n*(n-1))/2             #maximum number of attacking pairs!
initial_population=(int)(input('Enter initial population size : '))
cross_prob=(float)(input('Enter crossover probablity:'))
mutation_prob=(float)(input('Enter mutation probablity:'))


begin_timer=time.time()
algorithm = Genetic(n=n,pop_size=initial_population)
algorithm.start()
print('Time Taken in seconds: ',time.time() - begin_timer)