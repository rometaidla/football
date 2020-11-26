
from gfootball.env import football_action_set
from gfootball.env import player_base

import memory_based

class Player(player_base.PlayerBase):
  """Lazy player not moving at all."""

  def __init__(self, player_config, env_config):
    player_base.PlayerBase.__init__(self, player_config)

  def take_action(self, observations):
    return memory_based.agent(observations)
