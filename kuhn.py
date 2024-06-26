from common.constants import CARDS_DEALINGS
from games.kuhn import KuhnRootChanceGameState
from games.algorithms import ChanceSamplingCFR, VanillaCFR


root = KuhnRootChanceGameState(CARDS_DEALINGS)
chance_sampling_cfr = ChanceSamplingCFR(root)
chance_sampling_cfr.run(iterations = 10000)
chance_sampling_cfr.compute_nash_equilibrium()
print(chance_sampling_cfr.value_of_the_game())
print('NashEquil', chance_sampling_cfr.nash_equilibrium)