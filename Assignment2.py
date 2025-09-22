import numpy as np
import matplotlib.pyplot as plt

## assignment 2-1
states = ["S1", "S2", "S3", "S4", "S5", "S6"]

V = {s: 0 for s in states}
V['S1'] = 100
V['S6'] = 50

discount = 1.0

R = {s: 0 for s in states}

T = {
    'S2': {'S1': 0.5, 'S3': 0.5},
    'S3': {'S2': 0.5, 'S4': 0.5},
    'S4': {'S3': 0.5, 'S5': 0.5},
    'S5': {'S4': 0.5, 'S6': 0.5},
}

values_history = []
iterations = 0
while True:
    iterations += 1
    delta = 0
    old_V = V.copy()
    
    for s in ['S2', 'S3', 'S4', 'S5']:
        new_v = R[s] + discount * sum(T[s][s_prime] * old_V[s_prime] for s_prime in T[s])
        V[s] = new_v
        delta = max(delta, abs(old_V[s] - V[s]))

    values_history.append(V.copy())
    if iterations >= 100:
        break

for s, v in V.items():
    print(f"{s:<10}: {v:.4f}")

print("\n")

## assignment 2-2
Q = {}

for s in ['S2', 'S3', 'S4', 'S5']:
    Q[s] = {}
    s_int = int(s[1:])
    
    # left
    s_left = f'S{s_int - 1}'
    Q[s]['left'] = R[s] + discount * V[s_left]

    # right
    s_right = f'S{s_int + 1}'
    Q[s]['right'] = R[s] + discount * V[s_right]

for s, actions in Q.items():
    for action, q_val in actions.items():
        print(f"{s} -> {action:<5} => {q_val:.4f}")