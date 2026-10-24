

import random
import turtle

random.seed(7)

# Distance matrix
distance = [
    [0, 2, 4, 0],
    [2, 0, 1, 5],
    [4, 1, 0, 2],
    [0, 5, 2, 0]
]

# Initial pheromone values
pheromone = [
    [0, 1, 1, 0],
    [1, 0, 1, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 0]
]

iterations = 30
ants = 10
evaporation = 0.9

best_route = []
best_cost = float("inf")

# Ant Colony Optimization
for iteration in range(iterations):

    routes = []

    for ant in range(ants):
        route = [0]
        current = 0

        while current != 3:
            choices = []

            for j in range(4):
                if distance[current][j] > 0 and j not in route:
                    choices.append(j)

            if len(choices) == 0:
                break

            weights = []

            for j in choices:
                weight = pheromone[current][j] / distance[current][j]
                weights.append(weight)

            next_node = random.choices(
                choices, weights=weights, k=1
            )[0]

            route.append(next_node)
            current = next_node

        if route[-1] == 3:
            cost = 0

            for i in range(len(route) - 1):
                cost += distance[route[i]][route[i + 1]]

            routes.append((route, cost))

            if cost < best_cost:
                best_cost = cost
                best_route = route[:]

    # Evaporate pheromones
    for i in range(4):
        for j in range(4):
            pheromone[i][j] *= evaporation

    # Deposit pheromones on successful routes
    for route, cost in routes:
        deposit = 1 / cost

        for i in range(len(route) - 1):
            a = route[i]
            b = route[i + 1]

            pheromone[a][b] += deposit
            pheromone[b][a] += deposit

# Display result in terminal
print("Best route:", best_route)
print("Minimum cost:", best_cost)
print("\nFinal pheromone values:")

for i in range(4):
    for j in range(i + 1, 4):
        if distance[i][j] > 0:
            print(
                i, "-", j,
                "Cost:", distance[i][j],
                "Pheromone:", round(pheromone[i][j], 2)
            )

# Draw network using Turtle
screen = turtle.Screen()
screen.title("ACO Network Routing with Pheromone Values")
screen.setup(width=800, height=600)

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()
pen.pensize(2)

# Node positions
positions = {
    0: (-250, 100),
    1: (0, 150),
    2: (0, -100),
    3: (250, 50)
}

# Draw all connections
for i in range(4):
    for j in range(i + 1, 4):
        if distance[i][j] > 0:
            pen.penup()
            pen.goto(positions[i])
            pen.pendown()
            pen.color("gray")
            pen.pensize(2)
            pen.goto(positions[j])

# Highlight the best route in red
for i in range(len(best_route) - 1):
    a = best_route[i]
    b = best_route[i + 1]

    pen.penup()
    pen.goto(positions[a])
    pen.pendown()
    pen.color("red")
    pen.pensize(4)
    pen.goto(positions[b])

# Display cost and pheromone values on every edge
for i in range(4):
    for j in range(i + 1, 4):
        if distance[i][j] > 0:
            x = (positions[i][0] + positions[j][0]) / 2
            y = (positions[i][1] + positions[j][1]) / 2

            pen.penup()
            pen.goto(x, y + 12)
            pen.color("black")
            pen.write(
                "C:" + str(distance[i][j]),
                align="center",
                font=("Arial", 10, "bold")
            )

            pen.goto(x, y - 5)
            pen.write(
                "P:" + format(pheromone[i][j], ".2f"),
                align="center",
                font=("Arial", 9, "normal")
            )

# Draw nodes
for node in positions:
    pen.penup()
    pen.goto(positions[node])
    pen.dot(35, "blue")
    pen.goto(positions[node][0], positions[node][1] - 8)
    pen.color("white")
    pen.write(
        str(node),
        align="center",
        font=("Arial", 12, "bold")
    )

# Display best route and cost
pen.penup()
pen.goto(-300, -220)
pen.color("red")
pen.write(
    "Best Route: " + str(best_route),
    font=("Arial", 13, "bold")
)

pen.goto(-300, -250)
pen.write(
    "Minimum Cost: " + str(best_cost),
    font=("Arial", 13, "bold")
)

pen.goto(-300, -280)
pen.color("black")
pen.write(
    "C = Connection Cost     P = Final Pheromone Value",
    font=("Arial", 10, "normal")
)

turtle.done()
