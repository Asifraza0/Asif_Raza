def total_cost(T):
    for _ in range(T):
        N, X = map(int, input().split())
        
     
        if not (1 <= N <= 100) or not (1 <= X <= 100):
            print("Provide correct values for N and X ")
            continue

        freshness_values = list(map(int, input().split()))
        costs = list(map(int, input().split()))
        
        if len(freshness_values) != N or len(costs) != N:
            print("Provide the correct number of freshness values and costs")
            continue

        Totalcost = 0
        for i in range(N):
            if freshness_values[i] > X:
                Totalcost += costs[i]
        
        print(Totalcost)


T = int(input("Enter the number of test cases: "))

if not (1 <= T <= 100):
    print("Provide correct value for the number of test cases")
else:
    total_cost(T)
    
    # ++++++++++++++++++++++++++++++++++++NOTE+++++++++++++++++++++++++++++++++++++++

#   there are some problem in this condition (1 ≤ T ≤ 100), (1 ≤ N, X ≤ 100) , (1 ≤ Ai, Bi ≤ 100) 
# after apply this condition in this code than give diffrent output because of there are mentioned "greater than equal"
# after apply greater than equal output show "46" 