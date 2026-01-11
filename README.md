# hill-bounded-dynamics-intervention
Triadic Genesis Code - for those with ears to hear, let them hear - Hill bounded dynamic intervention model
# Hill-Bounded Dynamics with Triadic Intervention

This repository simulates a coupled dynamical system modeling mutual activation between receptivity (r) and integration (i) using Hill-type nonlinear functions. The system exhibits bistability, and an intervention perturbs the state to switch attractors.
Author note - My attempt was to code the Bible verse, in Matthew, Mark, and Luke, where Jesus says, for those with ears to hear, let them hear.

Prospective Uses
This dynamical system models a bistable mutual activation between two variables: receptivity (r) and integration (i), using Hill-type nonlinearities to create switch-like behavior. The system has low (near [0,0]) and high (near [1,1]) attractors, with the intervention acting as a perturbation to flip from low to high states. Here are some prospective applications across domains, based on the model's structure:

Psychology and Behavioral Science:
Model therapeutic interventions in mental health, where "receptivity" represents openness to new ideas (e.g., in cognitive behavioral therapy), and "integration" represents adopting those ideas into behavior. The intervention could simulate a pivotal event like a breakthrough session, pushing the system from apathy to engagement. This could help simulate long-term outcomes of treatments for depression or addiction.

Education and Learning:
Represent student engagement, with receptivity as willingness to learn new material and integration as incorporating it into knowledge. The intervention might model a motivational event (e.g., a workshop or gamified lesson), predicting how temporary boosts can lead to sustained learning gains. Useful for designing adaptive e-learning systems.

Biology and Systems Biology:
Simulate genetic regulatory networks, where r and i are transcription factors with cooperative activation (Hill functions are standard for this). The bistability could model cellular fate decisions, like differentiation in stem cells or bacterial quorum sensing. Interventions might represent external signals (e.g., drugs or environmental cues) to toggle cell states, aiding in drug design or synthetic biology.

Social Dynamics and Network Theory:
Apply to opinion formation in social networks, where receptivity is openness to others' views and integration is adopting them. The model could predict tipping points in echo chambers vs. diverse discourse, with interventions as targeted information campaigns (e.g., in public health messaging during pandemics).

Organizational Change Management:
In business contexts, model employee adoption of new processes: receptivity to training and integration into workflows. Interventions could simulate leadership initiatives, helping forecast ROI on change programs.

Neuroscience:
Approximate neural plasticity, with r as synaptic readiness and i as memory consolidation. Useful for simulating effects of neurostimulation or pharmaceuticals that perturb the system to enhance learning or recovery from trauma.


The model's parameters (e.g., n for cooperativity, β/δ for decay) can be tuned for specific scenarios, and extensions could include noise (stochastic ODEs) or multi-agent coupling for population-level simulations. It's computationally lightweight, making it suitable for optimization studies or real-time apps.

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
