#from common.constants import CARDS_DEALINGS
from common.clairvoyance_constants import CARDS_DEALINGS
from games.clairvoyance import ClairvoyanceRootChanceGameState
from games.algorithms import ChanceSamplingCFR, VanillaCFR


root = ClairvoyanceRootChanceGameState(CARDS_DEALINGS)
chance_sampling_cfr = ChanceSamplingCFR(root)
chance_sampling_cfr.run(iterations = 10000)
chance_sampling_cfr.compute_nash_equilibrium()
print(chance_sampling_cfr.value_of_the_game())
print('NashEquil', chance_sampling_cfr.nash_equilibrium)
# read Nash-Equilibrum via chance_sampling_cfr.nash_equilibrium member
# try chance_sampling_cfr.value_of_the_game() function to get value of the game (-1/18)

# vanilla cfr
vanilla_cfr = VanillaCFR(root)
vanilla_cfr.run(iterations = 1000)
vanilla_cfr.compute_nash_equilibrium()
#print('Nash Equilibrium: ', vanilla_cfr.nash_equilibrium)
# read Nash-Equilibrum via vanilla_cfr.nash_equilibrium member
# try vanilla_cfr.value_of_the_game() function to get value of the game (-1/18)
