
import random
import math

start = (0, 0)
goal = (10, 10)
obstacle = (5, 5)
radius = 2

particles = []

for i in range(10):
    particles.append({
        "x": [random.uniform(0, 10), random.uniform(0, 10)],
        "v": [0, 0],
        "best": None,
        "cost": float("inf")
    })

gbest = None
gbest_cost = float("inf")

def distance(a, b):
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

def cost(p):
    a = start
    b = p
    c = goal

    length = distance(a, b) + distance(b, c)

    # Check whether either path segment hits the obstacle
    for u, v in [(a, b), (b, c)]:
        dx = v[0] - u[0]
        dy = v[1] - u[1]
        denom = dx*dx + dy*dy

        t = 0
        if denom != 0:
            t = ((obstacle[0]-u[0])*dx +
                 (obstacle[1]-u[1])*dy) / denom
        t = max(0, min(1, t))

        nearest = (u[0]+t*dx, u[1]+t*dy)

        if distance(nearest, obstacle) < radius:
            length += 1000

    return length

for iteration in range(100):
    for p in particles:
        value = cost(p["x"])

        if value < p["cost"]:
            p["cost"] = value
            p["best"] = p["x"].copy()

        if value < gbest_cost:
            gbest_cost = value
            gbest = p["x"].copy()

    for p in particles:
        for j in range(2):
            r1 = random.random()
            r2 = random.random()

            p["v"][j] = (
                0.5 * p["v"][j]
                + 1.5 * r1 * (p["best"][j] - p["x"][j])
                + 1.5 * r2 * (gbest[j] - p["x"][j])
            )

            p["x"][j] += p["v"][j]
            p["x"][j] = max(0, min(10, p["x"][j]))

print("Start:", start)
print("Best waypoint:", gbest)
print("Goal:", goal)
print("Path cost:", round(gbest_cost, 2))
