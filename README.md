# 2D - Pathing Search Agent

## Abstract
This report describes the implementation and evaluation of a search-based agent for a dynamically changing 2D environment. The agent is designed to navigate through moving hazards while collecting coins and aiming for a designated goal. The core algorithms utilized are A* search and Breadth-First Search (BFS), each serving specific roles within the dynamic context of the game.

## 1. Introduction
The game presents a dynamic environment where an agent must avoid moving cars, collect coins, and reach a goal. The complexity arises from the changing positions of the cars, which can potentially block the agent's planned path. This scenario requires an agent that can adapt its pathfinding in real-time to optimize both survival and objective completion.

## 2. Algorithm Description
### 2.1 A* Search
The A* search algorithm is utilized for its efficiency in pathfinding with goals. It incorporates a heuristic that estimates the cost from the current node to the goal, improving pathfinding efficiency by prioritizing promising paths. Additionally, the agent reduces step costs when a coin is collected along the path, incentivizing coin collection.

### 2.2 Breadth-First Search (BFS)
BFS is employed to ensure the shortest path to nearby coins, avoiding the goal unless no coins are accessible within a two-move radius. This strategy guarantees that the agent collects maximum coins in its vicinity before proceeding to the goal, balancing between the dual objectives effectively.

## 3. Implementation
The agent's implementation involves managing its state between two primary modes: collecting coins ('coin' state) and navigating towards the goal ('goal' state). The state transitions based on the proximity of coins:
- **Coin State:** The agent performs BFS to find the shortest path to the nearest coin.
- **Goal State:** The agent switches to A* search directed towards the goal when no nearby coins are detectable.

## 4. Challenges
Initial iterations focused primarily on goal attainment, which neglected potential coin collections that could enhance overall scores. The revised strategy introduced dual states to balance goal orientation with coin collection, substantially improving the agent's utility in varied scenarios.

## 5. Future Work
Further development can include more sophisticated heuristic adjustments to better handle densely populated hazard areas and to integrate learning mechanisms that adapt to the agent's success and failure patterns, potentially using reinforcement learning.

## 6. Conclusion
The Search Agent illustrates the effective application of hybrid search strategies in a complex, dynamic environment. The agent's ability to adapt its behavior based on the game state underscores the potential of integrating classical pathfinding algorithms with game-specific heuristics.

## Appendices
### A. Installation and Running Instructions
- Required software: Python 3, Pygame
- Command to run the simulation: `python agent_A.py`
