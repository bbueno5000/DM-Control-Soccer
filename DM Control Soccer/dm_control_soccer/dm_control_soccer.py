
"""
Interactive viewer for MuJoCo soccer environment.
"""
from dm_control import viewer
from dm_control.locomotion import soccer
import numpy

env = soccer.load(
    team_size=2,
    time_limit=10.0,
    disable_walker_contacts=False,
    enable_field_box=True,
    terminate_on_goal=False,
    walker_type=soccer.WalkerType.BOXHEAD)

action_specs = env.action_spec()

def random_policy(time_step):
    """
    Define a uniform random policy.
    """
    del time_step
    actions = []
    for action_spec in action_specs:
        action = numpy.random.uniform(
            action_spec.minimum,
            action_spec.maximum,
            size=action_spec.shape)
        actions.append(action)
    return actions
  
viewer.launch(env, random_policy)
