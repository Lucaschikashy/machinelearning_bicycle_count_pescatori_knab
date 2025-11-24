# Machine Learning Project: Dataset Overview
**Tommaso Pescatori, Luca Knab**

## Introduction
This document provides a brief overview of the dataset used for our machine learning project. The primary goal of this project is to predict bicycle rental demand at various counting stations at a certain time.

## Dataset Description
The core dataset includes the following main features:
* **Target Variable:** `bike_count`, which represents the bike count.
* **Identifiers:** `counter_id` to identify the specific bike counting station.
* **Location Data:** `latitude` and `longitude` for each counter, allowing for spatial analysis.
* **Time Information**

### Data Enrichment: Weather Data
To improve model performance, the core dataset will be enriched with an external weather dataset.

This weather dataset includes features such as:
* Temperature (`t`)
* Humidity (`u`)
* Wind speed (`ff`) and direction (`dd`)
* Precipitation (`rr`)
* Atmospheric pressure (`pmer`)

We hypothesize that weather conditions are a strong predictor of bicycle usage and integrating this data will significantly enhance our model's accuracy. The next steps will involve merging this weather data with the primary training data based on location and timestamp.
