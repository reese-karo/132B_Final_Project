# 132B_Final_Project - Will Mahnke, Reese Karo
Exploring Game Theory problems with Linear Programming

## Setup
In this problem, we are exploring a game theory situation where we aim to maximize the value \( v \) subject to specific constraints. Suppose we have two players or generals, A and B, who can each choose to move North (N), East (E), or South (S). The constraints based on Player B's moves are as follows:

$$
\begin{align*}
\text{Player B Plays North: } & 3x_1 + 2x_2 - 2x_3 \geq v \\
\text{Player B Plays East: } & -x_1 + x_3 \geq v \\
\text{Player B Plays West: } & 2x_1 - 2x_2 + x_3 \geq v \\
\text{Such that: } & \sum_{i=1}^{3} x_i = 1 \\
& x, v \geq 0
\end{align*}
$$

Our goal is to...