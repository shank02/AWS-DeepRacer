def reward_function(params):
    #input parameters
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    abs_steering = abs(params['steering_angle'])
    progress = params['progress']
    all_wheels_on_track = params['all_wheels_on_track']
    steps = params['steps']

    #performance bonus
    if progress >= 100:
        performance_reward = 1.0
    else:
        performance_reward = progress / 100.0

    # reward for closer to the center line
    marker_1 = 0.15 * track_width
    marker_2 = 0.3 * track_width
    marker_3 = 0.45 * track_width

    if distance_from_center <= marker_1:
        center_reward = 1.0
    elif distance_from_center <= marker_2:
        center_reward = 0.5
    elif distance_from_center <= marker_3:
        center_reward = 0.1
    else:
        center_reward = 1e-3

    #excessive steering
    ABS_STEERING_THRESHOLD = 20

    if abs_steering > ABS_STEERING_THRESHOLD:
        steering_penalty = 0.5
    else:
        steering_penalty = 0.0

    #off-track 
    if not all_wheels_on_track:
        off_track_penalty = 3.0
    else:
        off_track_penalty = 0.0

    #total reward
    reward = performance_reward + center_reward - steering_penalty - off_track_penalty

    #range
    reward = max(1e-3, min(1.0, reward))

    return float(reward)
