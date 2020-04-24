INPUT_TIMESTEPS = 8
TIMESTEP_PLANES = 9
PLANE_WIDTH = 20
PLANE_HEIGHT = 7
USED_LAYOUT="smallClassic.lay"


REPLAY_MEMORY_SIZE=1000
MIN_REPLAY_MEMORY_SIZE=512
MINIBATCH_SIZE=128
DISCOUNT = 0.8
UPDATE_TARGET_EVERY=1

LEARNING_RATE=1e-4
DECAY=0
MOMENTUM=0.9

GAME_MOVE_LIMIT=600
FOOD_REWARD=10
CAPSULE_REWARD=30
WIN_REWARD=1000
KILL_REWARD=500

DIE_PENALTY=-200
TIME_PENALTY =-1
RUN_GRAPHICS=True
EPSILON=0
EPSILON_DECREASE=.001
EPSILON_FLOOR=0
NUM_RANDOM_GAMES=0
