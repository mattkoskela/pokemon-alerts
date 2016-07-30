Pokemon Alerts
==============

## Overview

Pokemon Alerts is a Command Line Interface that uses the pokevision.com API to send you alerts (SMS) when a Pokemon shows upnearby.

## Installation

I'll uplload this to pypi later.  In the meatime, download this repo and run the following command in the root of the repo:

    pip install .

## Usage

Once pokemon-alerts is installed, the most basic usage is to run this in your terminal:

    pokemon-alerts --latitude 34.016641 --longitude -118.495146

To change the time interval, use the --time flag (defaults to 5 minutes, minimum is 1 minute)

    pokemon-alerts --latitude 34.016641 --longitude -118.495146 --time 5

To change the search radius, use the --distance flag (defaults to 100 meters)

    pokemon-alerts --latitude 34.016641 --longitude -118.495146 --time 5 --distance 250

To ignore certain Pokemon, include a csv of ids in the --ignore flag (no spaces)

    pokemon-alerts --latitude 34.016641 --longitude -118.495146 --time --distance 250 --ignore 16,41

To only look for certain Pokemon, include a csv of ids in the --include flag (no spaces)

    pokemon-alerts --latitude 34.016641 --longitude -118.495146 --time --distance 250 --include 16,41

To receive SMS alerts when this script finds a Pokemon, you must have your own Twilio Account. Use the --twilio flag, and the script will prompt you for your phone number, Twilio phone number, Twilio SID and Twilio Auth Token.

    pokemon-alerts --latitude 34.016641 --longitude -118.495146 --time --distance 250 --ignore 16,41 --twilio


## TODO:

* Unit Tests
* Slack Notification Support
* Email Notification Support
* Submit to Pypi
