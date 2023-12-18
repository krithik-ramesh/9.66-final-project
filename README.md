# 9.66-final-project
final project for computational cognitive science, team members: Krithik, Maxi, Reina


## Overview

In this repository you will find code for the execution of the adapted PLoT with GPT for the Cluttr, Babi, E-share, and HOTPot QA.

There is also a small conceptual test using the bAbI dataset downloaded from Kaggle using GPT-3.5 and WebPPL demonstrating that for qa1_single-supporting-fact_test GPT-3.5 multiple times struggles to correct answer the simple deductive reasoning questions falsely claiming people's locations are unknown or there is not enough information to determine their location. However, the probabilistic program written in WebPPL successfully encodes the logical reasoning needed to correctly determine the location of the first person who's location GPT-3.5 claimed is unknown. This demonstrates proof of concept of offloading the cognitive burden of reasoning from LLMs to probabilistic programs.

## Datasets in this repository: 

In this repository you will find the csv fiels for the cluttr data, the text files for the Babi dataset (downloaded from the keras utils and processed), and the E-share dataset. the HotPot QA dataset was loaded from the hugging face dataset module. 


## Running and Replicating experiments: 

The OpenAI environemnt keys have been removed for security reasons, but replacing them with you own key will let you execute any code by simplifiying the python and specifying the appropriate csv file. There is a possibility that the executing GPT scripts might not work unless computer permission is granted to run subprocesses from python, I personally had a few issues with this execution and had to use sudo commands and change security privleges briefly. 

