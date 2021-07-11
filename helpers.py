from robot_class import Robot
from math import *
import random
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# --------
# this helper function displays the world that a Robot is in
# it assumes the world is a square grid of some given size
# and that landmarks is a list of landmark positions(an optional argument)
def display_world(world_size, position, landmarks=None):
    # using seaborn, set background grid to gray
    sns.set_style("dark")

    # Plot grid of values
    world_grid = np.zeros((world_size + 1, world_size + 1))

    # Set minor axes in between the labels
    ax = plt.gca()
    cols = world_size + 1
    rows = world_size + 1

    ax.set_xticks([x for x in range(1, cols)], minor=True)
    ax.set_yticks([y for y in range(1, rows)], minor=True)

    # Plot grid on minor axes in gray (width = 1)
    plt.grid(which='minor', ls='-', lw=1, color='white')

    # Plot grid on major axes in larger width
    plt.grid(which='major', ls='-', lw=2, color='white')

    # Create an 'o' character that represents the Robot
    # ha = horizontal alignment, va = vertical
    ax.text(position[0], position[1], 'o', ha='center', va='center', color='r', fontsize=30)

    # Draw landmarks if they exists
    if (landmarks is not None):
        # loop through all path indices and draw a dot (unless it's at the car's location)
        for pos in landmarks:
            if (pos != position):
                ax.text(pos[0], pos[1], 'x', ha='center', va='center', color='purple', fontsize=20)

    # Display final result


# --------
# this routine makes the Robot data
# the data is a list of measurements and movements: [measurements, [dx, dy]]
# collected over a specified number of time steps, N
#
def make_data(N, num_landmarks, world_size, measurement_range, motion_noise, measurement_noise, distance, visualize=False):
    complete = False
    robot_instance = None
    data = list()

    while not complete:
        data = []

        # make Robot and landmarks
        robot_instance = Robot(world_size, measurement_range, motion_noise, measurement_noise)
        print('Robot x: {}, y: {}'.format(robot_instance.x, robot_instance.y))
        robot_instance.make_landmarks(num_landmarks)
        seen = [False for row in range(num_landmarks)]

        # guess an initial motion
        orientation = random.random() * 2.0 * pi
        dx = cos(orientation) * distance
        dy = sin(orientation) * distance

        for k in range(N - 1):

            # collect sensor measurements in a list, Z
            Z = robot_instance.sense()

            # check off all landmarks that were observed 
            for i in range(len(Z)):
                seen[Z[i][0]] = True

            # move
            while not robot_instance.move(dx, dy):
                # if we'd be leaving the Robot world, pick instead a new direction
                orientation = random.random() * 2.0 * pi
                dx = cos(orientation) * distance
                dy = sin(orientation) * distance

            if visualize:
                display_world(int(world_size), [robot_instance.x, robot_instance.y], robot_instance.landmarks)
                plt.arrow(robot_instance.x, robot_instance.y, dx, dy, color='k', head_width=1)
            # collect/memorize all sensor and motion data
            data.append([Z, [dx, dy]])

        # we are done when all landmarks were observed; otherwise re-run
        complete = (sum(seen) == num_landmarks)

    print(' ')
    print('Landmarks: ', robot_instance.landmarks)
    print(robot_instance)

    return data


def get_poses_landmarks(mu, N, num_landmarks):
    # a helper function that creates a list of poses and of landmarks for ease of printing
    # this only works for the suggested constraint architecture of interlaced x,y poses
    # create a list of poses
    poses = []
    for i in range(N):
        poses.append((mu[2*i].item(), mu[2*i+1].item()))

    # create a list of landmarks
    landmarks = []
    for i in range(num_landmarks):
        landmarks.append((mu[2*(N+i)].item(), mu[2*(N+i)+1].item()))

    # return completed lists
    return poses, landmarks


def print_all(poses, landmarks):
    print('\n')
    print('Estimated Poses:')
    for i in range(len(poses)):
        print('['+', '.join('%.3f'%p for p in poses[i])+']')
    print('\n')
    print('Estimated Landmarks:')
    for i in range(len(landmarks)):
        print('['+', '.join('%.3f'%l for l in landmarks[i])+']')
