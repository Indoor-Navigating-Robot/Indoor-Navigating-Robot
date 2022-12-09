# Indoor-Navigating-Robot
 * Parse_Data_and_Build_Model.ipynb: A Jupyter notebook which loads the collected data, does some preprocessing, and then builds the ML model that was deployed on the Robot.
 * a_star_search.py: A Python file representing the A* search algorithm which can be used to generate checkpoints
 * getMacs.py: A Python file which sifts through all the data collected and pulls out the Mac addresses (I needed a list to put inside dataframe.py)
 * dataframe.py: Python file that compiles all the files created during data collection into a single CSV which can be read in as a Pandas dataframe.
 * collected_rssi.csv: The data that was collected after being compiled into a CSV file
 * saved_model.pb: The saved Keras model that was used.
 * deployable.ipynb: The Jupyter Notebook that was actually deployed on the robot
 * 545-2x.mp4: A video taken from my smartphone of the robot in action
