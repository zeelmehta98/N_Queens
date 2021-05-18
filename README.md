# N_Queens
Classic N Queens problem is solved using Genetic Algorithm.
Using Brute force algorithm for N-queens results in O(N^N) time complexity.
By using Brute force technique for N-queens results in O(2^N) time complexity.
Above mentioned techniques result in exponential time complexity. 
To improve that and have a good solution in limited time, we use Genetic Algorithm.

Genetic Algorithm (GA) is a search-based optimization technique based on the principles of Genetics and Natural Selection. 
It is frequently used to find optimal or near-optimal solutions to difficult problems which otherwise would take a lifetime to solve.
Here, we will solve classic N-Queen’s problem using Genetic algorithm.

Population: Initial population size must be optimum, as large population size may lead for genetic algorithm to take more time 
whereas less population size may not lead to good mating pools

Crossover:  Here, parents are selected and off springs are produced, using them. 
This is used for exploitation of the Search space. Here, crossover probability is entered by user. This probability is generally kept high.

Mutation: Here, a random change in chromosome to make a new solution is known as mutation. 
This is used for exploration of the Search space. This probability is generally kept less, as High mutation probability leads to random search.
