import time
import h5py
from dlgo.agent.predict import DeepLearningAgent, load_prediction_agent
from dlgo import agent
from dlgo import goboard_fast as goboard
from dlgo.utils import coords_from_point
from dlgo.utils import point_from_coords

board_size = 19
game_state = goboard.GameState.new_game(board_size)
# Replay the game up to this point.
# for move in content['moves']:
#	if move == 'pass':
#		next_move = goboard.Move.pass_turn()
#	elif move == 'resign':
#		next_move = goboard.Move.resign()
#	else:
#		next_move = goboard.Move.play(point_from_coords(move))
#		game_state = game_state.apply_move(next_move)

# bot_agent = bot_map[bot_name]
model_file = h5py.File("../agents/betago.hdf5", "r")
bot_agent = load_prediction_agent(model_file)

while True:
	bot_move = bot_agent.select_move(game_state)
	if bot_move.is_pass:
		bot_move_str = 'pass'
	elif bot_move.is_resign:
		bot_move_str = 'resign'
		print('resign')
		break
	else:
		bot_move_str = coords_from_point(bot_move.point)
		game_state = game_state.apply_move(goboard.Move.play(bot_move.point))
	print(bot_move_str)
	time.sleep(1)
