from common.AT_constants import CARDS_DEALINGS
from games.AT import ATRootChanceGameState
from games.algorithms import ChanceSamplingCFR


root = ATRootChanceGameState(CARDS_DEALINGS)
chance_sampling_cfr = ChanceSamplingCFR(root)
chance_sampling_cfr.run(iterations = 10000)
chance_sampling_cfr.compute_nash_equilibrium()
print(chance_sampling_cfr.value_of_the_game())
print('NashEquil', chance_sampling_cfr.nash_equilibrium)