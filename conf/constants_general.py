from .constants_mine import *
# [GENERAL]
PYTHON_PATH = PYTHON_PATH_MINE
EMA_WINDOW = 10
VERBOSE = False

# [MQTT]
MQTT_SERVER = "192.168.0.10"
MQTT_SERVER_FOR_RIP = "192.168.0.12"
MQTT_PORT = 1883
MQTT_TOPIC_EPISODE_DETAIL = "Episode_Detail"
MQTT_TOPIC_SUCCESS_DONE = "Success_Done"
MQTT_TOPIC_FAIL_DONE = "Fail_Done"
MQTT_TOPIC_TRANSFER_ACK = "Transfer_Ack"
MQTT_TOPIC_UPDATE_ACK = "Update_Ack"
MQTT_TOPIC_ACK = "Ack"

# MQTT Topic for RIP
MQTT_PUB_TO_SERVO_POWER = 'motor_power'
MQTT_PUB_RESET = 'reset'
MQTT_SUB_FROM_SERVO = 'servo_info'
MQTT_SUB_MOTOR_LIMIT = 'motor_limit_info'
MQTT_SUB_RESET_COMPLETE = 'reset_complete'

# [WORKER]
NUM_WORKERS = 2

# [TRANSFER]
SOFT_TRANSFER = False
SOFT_TRANSFER_TAU = 0.3

# [TARGET_UPDATE]
SOFT_TARGET_UPDATE = False
SOFT_TARGET_UPDATE_TAU = 0.3

# [MLP_DEEP_LEARNING_MODEL]
HIDDEN_1_SIZE = 128
HIDDEN_2_SIZE = 128
HIDDEN_3_SIZE = 128

# [CNN_DEEP_LEARNING_MODEL]
CNN_INPUT_WIDTH = 10
CNN_INPUT_HEIGHT = 10

# [OPTIMIZATION]
MAX_EPISODES = 1000
GAMMA = 0.98 # discount factor

# [MODE]
MODE_SYNCHRONIZATION = True
MODE_GRADIENTS_UPDATE = True        # Distributed
MODE_PARAMETERS_TRANSFER = True     # Transfer
MODE_DEEP_LEARNING_MODEL = "MLP"    # "CNN" or "MLP"
