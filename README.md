# Graph-SLAM
# Landmark Detection & Robot Tracking (SLAM)
## Accomplished as a required project for Udacity Computer Vision Nanodegree 

## Project Overview
[N.B All the codes are in Jupyter notebook.] 

In this project, I implemented SLAM (Simultaneous Localization and Mapping) for a 
2 dimensional world! The task asks to combine Robot sensor measurements and 
movement to create a map of an environment from only sensor and motion data gathered by 
a Robot, over time. SLAM gives a way to track the location of a Robot in the world 
in real-time and identify the locations of landmarks such as buildings, trees, rocks, 
and other world features. To be noted, this is an active area of research in the fields of robotics 
and autonomous systems. 

*Below is an example of a 2D Robot world with landmarks (purple x's) and the Robot (a red 'o') located and found using *only* sensor and motion data collected by that Robot. This is just one example for a 50x50 grid world.*

<p align="center">
  <img src="./images/robot_world.png" width=50% height=50% />
</p>

The project can be broken up into three Python notebooks; the first two are for exploration 
of provided code, and a review of SLAM architectures.

__Notebook 1__ : Robot Moving and Sensing

__Notebook 2__ : Omega and Xi, Constraints 

__Notebook 3__ : Landmark Detection and Tracking 


### Local Environment Instructions

1. Clone the repository, and navigate to the downloaded folder. This may take a minute or less to clone.
```
git clone https://github.com/prudhvirajstark/Graph-SLAM.git
cd visual_slam
```

2. Create (and activate) a new environment named `cv-nd` with all the required packages, 
run the 'create_and_set_environment.bat' file. If prompted to proceed with the install `(Proceed [y]/n)` type y.
```shell
create_and_set_environment.bat
proceeed with [y]

### Environemnt
The bat file will create a conda environment using python 3.6 with the required pip and conda packages
specified in the requirement files in /requirements subdirectory.

```

2. Open the directory of notebooks, run the 'run_notebook.bat' file. This file will activate the `cv-nd` conda environment
and open the notebook in the browser. Open the notebooks and follow the instructions.
```shell
run_notebook.bat
```
