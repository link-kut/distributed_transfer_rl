import gym

from rl_main.conf.names import EnvironmentName
from rl_main.environments.environment import Environment

"""
    FrozenLake-v0 environment

    The agent controls the movement of a character in a grid world. 
    
    Some tiles of the grid are walkable, and others lead to the agent falling into the water. 
    
    Additionally, the movement direction of the agent is uncertain and only partially depends on the chosen direction. 
    
    The agent is rewarded for finding a walkable path to a goal tile.

    The surface is described using a grid like the following:

    SFFF       (S: starting point, safe)
    FHFH       (F: frozen surface, safe)
    FFFH       (H: hole, fall to your doom)
    HFFG       (G: goal, where the frisbee is located)


    The episode ends when you reach the goal or fall in a hole. 

    the ice is slippery, so you won't always move in the direction you intend.
        
    You receive a reward of 1 if you reach the goal, and zero otherwise.
    
    https://gym.openai.com/envs/FrozenLake-v0/
"""


class FrozenLake_v0(Environment):
    def __init__(self):
        self.env = gym.make(EnvironmentName.FROZENLAKE_V0.value, is_slippery=False)
        super(FrozenLake_v0, self).__init__()
        self.action_shape = self.get_action_shape()
        self.state_shape = self.get_state_shape()

        self.continuous = False
        self.WIN_AND_LEARN_FINISH_SCORE = 1.0
        self.WIN_AND_LEARN_FINISH_CONTINUOUS_EPISODES = 25

    def get_n_states(self):
        n_states = self.env.observation_space.n
        return n_states

    def get_n_actions(self):
        n_actions = self.env.action_space.n
        return n_actions

    def get_state_shape(self):
        return 1,

    def get_action_shape(self):
        action_shape = (self.env.action_space.n, )
        return action_shape

    def get_action_space(self):
        return self.env.action_space

    @property
    def action_meanings(self):
        action_meanings = ["LEFT", "DOWN", "RIGHT", "UP"]
        return action_meanings

    def reset(self):
        state = self.env.reset()
        return state

    def step(self, action):
        if "torch" in str(type(action)):
            action = int(action.item())

        next_state, reward, done, info = self.env.step(action)

        adjusted_reward = reward

        return next_state, reward, adjusted_reward, done, info

    def render(self):
        self.env.render()

    def close(self):
        self.env.close()


if __name__ == "__main__":
    env = FrozenLake_v0()

    for i_episode in range(10):
        state = env.reset()
        env.render()
        step = 0
        while True:
            print("\nstep: {0}".format(step))
            action = env.action_space.sample()
            next_state, reward, adjusted_reward, done, info = env.step(action)
            print(state, action, next_state, reward, adjusted_reward, done)
            env.render()
            step += 1
            if done:
                print('End game! Reward: ', reward)
                print('You won :)\n') if reward > 0 else print('You lost :(\n')
                break
            state = next_state

