import numpy as np
import matplotlib.pyplot as plt

states = ["Facebook", "Class_1", "Class_2", "Class_3", "Pub", "Pass", "Sleep"]

V = {s: 0 for s in states}
V["Pass"] = 10
V["Sleep"] = 0

discount = 0.85

R = {"Facebook": -1, "Class_1": -2, "Class_2": -2, "Class_3": -2, "Pub": 1, "Pass": 10, "Sleep": 0}

T = {
    "Facebook": {"Facebook": 0.9, "Class_1": 0.1},
    "Class_1": {"Facebook": 0.5, "Class_2": 0.5},
    "Class_2": {"Class_3": 0.8, "Sleep": 0.2},
    "Class_3": {"Pass": 0.6, "Pub": 0.4},
    "Pub": {"Class_1": 0.2, "Class_2": 0.4, "Class_3": 0.4},
}

values_history = []

iterations = 0
while True:
    iterations += 1
    delta = 0
    old_V = V.copy()
    for s in ["Facebook", "Class_1", "Class_2", "Class_3", "Pub"]:
        new_v = R[s] + discount * sum(T[s][s_prime] * old_V[s_prime] for s_prime in T[s])
        V[s] = new_v
        delta = max(delta, abs(old_V[s] - V[s]))

    values_history.append(V.copy())

    if iterations >= 100:
        break

for s, v in V.items():
    print(f"{s:<10}: {v:.4f}")

print("\n")
print(f"iter {iterations}")

Q = {}

for s in T.keys():
    Q[s] = {}
    for s_prime in T[s].keys():
        q_value = R[s] + discount * V[s_prime]
        Q[s][s_prime] = q_value

for s, actions in Q.items():
    for s_prime, q_val in actions.items():
        print(f"{s} -> {s_prime} => {q_val:.4f}")