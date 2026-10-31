
import random

# Step 1: Processing time of each job on each machine
times = [
    [4, 5, 3],
    [6, 2, 5],
    [3, 4, 2]
]

# Step 2: Initialize parameters
random.seed(7)

n = 10
pa = 0.25
iterations = 50
machines = 3
jobs = 3

# Step 3: Calculate fitness (makespan)
def fitness(nest):
    load = [0] * machines

    for j in range(jobs):
        m = nest[j]
        load[m] += times[j][m]

    return max(load)

# Step 4: Generate initial nests
nests = [
    [random.randint(0, 2) for _ in range(jobs)]
    for _ in range(n)
]

# Step 5: Display initial population
print("INITIAL POPULATION")
for i, nest in enumerate(nests):
    print("Nest", i + 1, ":", nest,
          "Fitness:", fitness(nest))

# Step 6: Find the best nest
best = min(nests, key=fitness).copy()

print("\nInitial Best Nest:", best)
print("Initial Best Fitness:", fitness(best))

# Step 7: Main Cuckoo Search loop
for iteration in range(iterations):

    # Select a random nest
    i = random.randint(0, n - 1)
    new = nests[i].copy()

    # Generate a new solution
    for _ in range(random.randint(1, 2)):
        job = random.randint(0, jobs - 1)
        new[job] = random.randint(0, machines - 1)

    # Select another random nest
    j = random.randint(0, n - 1)

    # Replace if the new solution is better
    if fitness(new) < fitness(nests[j]):
        nests[j] = new

    # Update the best solution
    current = min(nests, key=fitness)

    if fitness(current) < fitness(best):
        best = current.copy()

    # Abandon the worst nests
    nests.sort(key=fitness)

    for k in range(n - int(pa * n), n):
        nests[k] = [
            random.randint(0, machines - 1)
            for _ in range(jobs)
        ]

    # Preserve the best nest
    nests[0] = best.copy()

# Step 8: Display final result
print("\nFINAL BEST SOLUTION")

loads = [0] * machines

for j in range(jobs):
    m = best[j]
    time = times[j][m]
    loads[m] += time

    print("Job", j + 1, "-> Machine", m + 1,
          "(", time, "hours )")

print("\nMachine Workloads:")

for m in range(machines):
    print("Machine", m + 1, ":", loads[m], "hours")

print("\nMinimum Makespan:", fitness(best), "hours")

print("\nRESULT: Optimal Job Assignment Found")
