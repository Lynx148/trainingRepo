
import numpy as np
np.set_printoptions(suppress=True)

from shutil import copyfile
import random
from importlib import reload


# from keras.utils import plot_model
from keras.utils.vis_utils import plot_model
import os
print(os.getcwd())
from game import Game, GameState
from agent import Agent
from memory import Memory
from model import Residual_CNN
from funcs import playMatches, playMatchesBetweenVersions

import loggers as lg

from settings import run_folder, run_archive_folder
import initialise
import pickle
env = Game()


from game import Game
from funcs import playMatchesBetweenVersions
import loggers as lg

env = Game()
playMatchesBetweenVersions(env, 2, 0, 8, 15, lg.logger_tourney, 0)