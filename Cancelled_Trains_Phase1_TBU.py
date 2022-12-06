import math
import random
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import statistics
import sys
import os
import pandas as pd
import tweepy
from tweepy import OAuthHandler

# Phase 1 of NJ Transit System Grader.
# This phase is a simple algorithm that reads tweets of cancelled
# NJ Transit Trains from a file named "Cancelled_NJT_Trains_10_24_2022.txt."
# Lines Focused: Morris & Essex (M & E) with Gladstone Branch,
# North Jersey Coast Line (NJCL), Northeast Corridor Line (NEC), and Raritan Valley Line (RVL).
# All trains in file are listed as cancelled.
# This program is responsible for detecting the string "cancelled" and then assigning a grade
# between A-C, and F if a certain number of trains has been added to a list that we call "Cancellations and Delays"


# Grading:
# A = No Trains or Only 1 Train Cancelled
# A- = 2 Trains Cancelled
# B+ = 3 Trains Cancelled
# B = 4 Trains Cancelled
# B- = 5 Trains Cancelled
# C+ = 6 to 10 Trains Cancelled
# C = 11 to 15 Trains Cancelled
# F = 16 or More Trains Cancelled

with open("Cancelled_Delayed_NJT_Trains_11_9_2022.txt", "r") as tweet_list:
    read_cancelled_NJT_train_tweets = tweet_list.read().splitlines()

detected_conditions = "cancelled"
alternative_detected_conditions = "canceled"
cancellation_tweets = []
cancelled_trains = 0
delayed_trains = 0
cancellation_or_delay_tweets = 0

# line_number_in_cancelled_tweets = 1
print("\n")


for line in read_cancelled_NJT_train_tweets:
    print(line)

    # cancelled_trains = 0
    # detected_string = "cancelled"

    if (line.find(detected_conditions) != -1) or (line.find(alternative_detected_conditions) != -1):
        print("Either", detected_conditions, "or", alternative_detected_conditions,
              "detected. "
              "This Train has been added to the Cancelled Trains List.")
        # print("Line Numbers Detected: ", line_number_in_cancelled_tweets)
        # line_number_in_cancelled_tweets += 1
        cancellation_tweets.append(line)
        cancelled_trains += 1
        # print("\n")

    cancellation_or_delay_tweets += 1

print("\n\nTotal Cancellation/Delay Tweets: ", cancellation_or_delay_tweets, "\n")

print("\n\nCancellation Tweets: ")
print(cancellation_tweets, "\n\n")
print("Cancelled Train Count for November 9th, 2022:", cancelled_trains)
# print("\n")

grade_received = ''

# Define Grades

while cancelled_trains >= 0:

    if (cancelled_trains == 0) or (cancelled_trains == 1):
        grade_received = 'A'
        # print("Grade Received:", grade_received)
        break
    elif cancelled_trains == 2:
        grade_received = 'A-'
        # print("Grade Received:", grade_received)
        break
    elif cancelled_trains == 3:
        grade_received = 'B+'
        # print("Grade Received:", grade_received)
        break
    elif cancelled_trains == 4:
        grade_received = 'B'
        # print("Grade Received:", grade_received)
        break
    elif cancelled_trains == 5:
        grade_received = 'B-'
        # print("Grade Received:", grade_received)
        break
    elif (cancelled_trains >= 6) and (cancelled_trains <= 7):
        grade_received = 'C+'
        # print("Grade Received:", grade_received)
        break
    elif (cancelled_trains >= 8) and (cancelled_trains <= 9):
        grade_received = 'C'
        # print("Grade Received:", grade_received)
        break
    elif cancelled_trains >= 10:  # or, else
        grade_received = 'F'
        # print("Grade Received:", grade_received)
        break

print("Grade Received:", grade_received, "\n")


consumer_key = 'CHANGE-WITH-YOUR-CONSUMER-KEY'
consumer_secret = 'CHANGE-WITH-YOUR-CONSUMER-SECRET'
access_token = 'CHANGE-WITH-YOUR-ACCESS-TOKEN'
access_token_secret = 'CHANGE-WITH-YOUR-ACCESS-SECRET'
tweets_per_queue = 100
max_Tweets = 1000000


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# Get User object:
