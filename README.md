# hill-bounded-dynamics-intervention
Triadic Genesis Code - for those with ears to hear, let them hear - Hill bounded dynamic intervention model
# Hill-Bounded Dynamics with Triadic Intervention

This repository simulates a coupled dynamical system modeling mutual activation between receptivity (r) and integration (i) using Hill-type nonlinear functions. The system exhibits bistability, and an intervention perturbs the state to switch attractors.
Author note - My attempt was to code the Bible verse, in Matthew, Mark, and Luke, where Jesus says, for those with ears to hear, let them hear.

## Overview
- **Model**: ODEs with Hill activation: dr/dt = σ(i)(1-r) - βr, di/dt = σ(r)(1-i) - δi
- **Hill Function**: σ(x) = γ x^n / (k^n + x^n)
- **Intervention**: At t=25, add 0.5 to r (capped at 1).
- **Output**: Plots trajectories with/without intervention and computes late-time averages.

Prospective uses include psychology (therapy outcomes), biology (gene regulation), education (learning engagement), and more. See the conversation history for details.

## Installation
1. Clone the repo: `git clone https://github.com/RMac-triadicIntelligence/hill-bounded-dynamics-intervention.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `python main.py`

## Requirements
- Python 3.x
- NumPy, SciPy, Matplotlib (listed in requirements.txt)

## Usage
Run `main.py` to generate the plot and print averages. Customize parameters in `model()` or intervention logic as needed.

Example output:
No Intervention: Receptivity ≈ 0.000, Integration ≈ 0.000
With Intervention: Receptivity ≈ 0.980, Integration ≈ 0.980

## Visualization
The script produces a plot showing trajectories:

![Simulation Plot](example_plot.png)  <!-- Add a saved plot here if desired -->

## Contributing
Fork and PR! Suggestions for extensions (e.g., stochastic versions) welcome.

## License
MIT License - see LICENSE file.  Attribution required - Rusty Williams McMurray
